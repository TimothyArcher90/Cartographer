"""Catálogo masivo de mapas antiguos libres de Wikimedia Commons.

Recorre el árbol de categorías a partir de las raíces de catalogo/config.json, apunta para cada
archivo de imagen: título, enlace, miniatura, tamaño, licencia, autor, fecha, año estimado,
categorías y LUGARES (deducidos de las categorías "maps of <lugar>"), y descarta licencias
que no permiten uso comercial (NC/ND).

Se ejecuta en GitHub Actions. Es reanudable: guarda el estado en catalogo/estado.json.gz y
para al agotar el tiempo (--minutos). Cada ejecución continúa donde se quedó la anterior.
Salida: catalogo/commons/parte-XXXX.jsonl.gz (un mapa por línea).
"""
import argparse
import gzip
import json
import re
import time
import urllib.parse
import urllib.request
from collections import deque
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
API = "https://commons.wikimedia.org/w/api.php"
UA = "Cartographer/1.0 (https://github.com/TimothyArcher90/Cartographer; catalogo de mapas libres)"
DIR = RAIZ / "catalogo"
ESTADO = DIR / "estado.json.gz"
POR_PARTE = 20000

RE_LUGAR = re.compile(r"maps? (?:of|showing) (?:the )?(.+?)(?: in the \d+.*| by .*| from .*)?$", re.I)
RE_SIGLO = re.compile(r"(\d{1,2})(?:st|nd|rd|th)[- ]century", re.I)
RE_ANIO = re.compile(r"(?<!\d)(1[0-9]{3}|[5-9][0-9]{2})(?!\d)")
ARTEFACTOS = re.compile(r"(?i)date QS:.*$")


def api(**p):
    p.update(format="json", formatversion="2", maxlag="5")
    url = API + "?" + urllib.parse.urlencode(p)
    for intento in range(6):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=90) as r:
                d = json.load(r)
            if d.get("error", {}).get("code") == "maxlag":
                time.sleep(5)
                continue
            return d
        except Exception:
            time.sleep(min(60, 2 ** intento))
    return {}


def limpiar(html, n=300):
    t = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", html or "")).strip()
    return ARTEFACTOS.sub("", t)[:n]


def lugar_de(cat):
    nombre = cat.split(":", 1)[-1]
    m = RE_LUGAR.search(nombre)
    return m.group(1).strip() if m else None


def siglo_de(cat):
    m = RE_SIGLO.search(cat)
    return int(m.group(1)) if m else None


def permite(lic):
    l = (lic or "").lower()
    if not l:
        return False
    if re.search(r"\bnc\b|non-?commercial|\bnd\b|no ?deriv", l):
        return False
    return True


def anio_de(fecha, titulo):
    for texto in (fecha or "", titulo or ""):
        m = RE_ANIO.search(texto)
        if m:
            return int(m.group(1))
    return None


def cargar_estado(raices, profundidad):
    if ESTADO.exists():
        return json.loads(gzip.decompress(ESTADO.read_bytes()))
    return {"cola": [[r, 0, [], []] for r in raices], "vistas_cat": [], "vistos": 0,
            "parte": 0, "en_parte": 0, "profundidad": profundidad, "terminado": False,
            "descartados_licencia": 0}


def guardar_estado(e):
    DIR.mkdir(exist_ok=True)
    ESTADO.write_bytes(gzip.compress(json.dumps(e).encode()))


def procesar(item, e_prof, seguir, excluir, vistas, fin):
    """Procesa una categoría: subcategorías nuevas y registros de sus archivos.
    Devuelve (subcats, registros, descartados, completa)."""
    cat, prof, lugares, siglos = item
    l, s = lugar_de(cat), siglo_de(cat)
    lugares = sorted(set(lugares + ([l] if l else [])))[:12]
    siglos = sorted(set(siglos + ([s] if s else [])))
    subcats, registros, descartados = [], [], 0
    if prof < e_prof:
        cont = {}
        while True:
            r = api(action="query", list="categorymembers", cmtitle=cat, cmtype="subcat", cmlimit="500", **cont)
            for m in r.get("query", {}).get("categorymembers", []):
                t = m["title"]
                if t not in vistas and seguir.search(t) and not any(x.search(t) for x in excluir):
                    subcats.append([t, prof + 1, lugares, siglos])
            if "continue" not in r:
                break
            cont = r["continue"]
    cont = {}
    while True:
        r = api(action="query", generator="categorymembers", gcmtitle=cat, gcmtype="file",
                gcmlimit="50", prop="imageinfo", iiprop="url|size|mime|extmetadata",
                iiurlwidth="640", iiextmetadatafilter="LicenseShortName|Artist|DateTimeOriginal|ObjectName",
                **cont)
        for p in r.get("query", {}).get("pages", []):
            ii = (p.get("imageinfo") or [{}])[0]
            if not ii or not str(ii.get("mime", "")).startswith("image/"):
                continue
            m = ii.get("extmetadata", {})
            lic = limpiar(m.get("LicenseShortName", {}).get("value"), 60)
            if not permite(lic):
                descartados += 1
                continue
            fecha = limpiar(m.get("DateTimeOriginal", {}).get("value"), 80)
            titulo = p["title"]
            registros.append({
                "t": titulo[5:], "pid": p.get("pageid"), "w": ii.get("width"), "h": ii.get("height"),
                "th": ii.get("thumburl"), "lic": lic, "autor": limpiar(m.get("Artist", {}).get("value"), 120),
                "fecha": fecha, "anio": anio_de(fecha, titulo), "siglos": siglos, "lugares": lugares,
                "cat": cat[9:],
            })
        if "continue" not in r:
            return subcats, registros, descartados, True
        if time.time() > fin:
            # Sin tiempo a mitad de categoría: se repite en la próxima tanda (duplicados fuera por pid).
            return subcats, registros, descartados, False
        cont = r["continue"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--minutos", type=float, default=300)
    ap.add_argument("--hilos", type=int, default=6)
    a = ap.parse_args()
    cfg = json.loads((DIR / "config.json").read_text(encoding="utf-8"))
    e = cargar_estado(cfg["raices"], cfg["profundidad"])
    excluir = [re.compile(x, re.I) for x in cfg.get("excluir_categorias", [])]
    seguir = re.compile(cfg["seguir_si"], re.I)
    vistas = set(e["vistas_cat"])
    cola = deque(e["cola"])
    fin = time.time() + a.minutos * 60
    (DIR / "commons").mkdir(parents=True, exist_ok=True)
    salida = gzip.open(DIR / "commons" / f"parte-{e['parte']:04d}.jsonl.gz", "at", encoding="utf-8")

    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=a.hilos) as pool:
        while cola and time.time() < fin:
            lote = []
            while cola and len(lote) < a.hilos:
                item = cola.popleft()
                if item[0] in vistas:
                    continue
                vistas.add(item[0])
                lote.append(item)
            resultados = list(pool.map(lambda it: (it, procesar(it, e["profundidad"], seguir, excluir, vistas, fin)), lote))
            for item, (subcats, registros, descartados, completa) in resultados:
                cola.extend(x for x in subcats if x[0] not in vistas)
                e["descartados_licencia"] += descartados
                for reg in registros:
                    salida.write(json.dumps(reg, ensure_ascii=False) + "\n")
                    e["vistos"] += 1
                    e["en_parte"] += 1
                    if e["en_parte"] >= POR_PARTE:
                        salida.close()
                        e["parte"] += 1
                        e["en_parte"] = 0
                        salida = gzip.open(DIR / "commons" / f"parte-{e['parte']:04d}.jsonl.gz", "at", encoding="utf-8")
                if not completa:
                    vistas.discard(item[0])
                    cola.appendleft(item)

    salida.close()
    e["cola"] = list(cola)
    e["vistas_cat"] = sorted(vistas)
    e["terminado"] = not cola
    guardar_estado(e)
    print(f"Registros: {e['vistos']} · categorías vistas: {len(vistas)} · en cola: {len(cola)} · "
          f"descartados por licencia: {e['descartados_licencia']} · terminado: {e['terminado']}")


if __name__ == "__main__":
    main()
