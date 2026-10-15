"""Busca en el catálogo todos los mapas de un lugar y genera una galería.

Uso:
  python scripts/buscar_lugar.py "Turquía"                 # todos los siglos
  python scripts/buscar_lugar.py "Turquía" --desde 1400 --hasta 1800
  python scripts/buscar_lugar.py "Turquía" --siglo 16

El lugar se amplía con catalogo/alias_es.json (p. ej. Turquía -> Turkey, Anatolia, Asia Minor,
Ottoman Empire...). Coincide con los lugares deducidos de las categorías de Commons y, como
respaldo, con el título del archivo.
Salida: tabla en pantalla + salidas/busquedas/<lugar>.html (galería con miniaturas y enlaces)
        + salidas/busquedas/<lugar>.json
"""
import argparse
import gzip
import html
import json
import re
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent


def norm(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", t).strip()


def terminos(lugar):
    alias = json.loads((RAIZ / "catalogo/alias_es.json").read_text(encoding="utf-8"))
    alias = {norm(k): v for k, v in alias.items() if not k.startswith("_")}
    entrada = alias.get(norm(lugar), {})
    lista = [lugar] + entrada.get("terminos", [])
    return sorted({norm(x) for x in lista}), entrada.get("pais")


def zona(pais):
    """Geometría del país actual (visor/datos/actual.geojson) para buscar por coordenadas."""
    if not pais:
        return None
    from shapely.geometry import shape
    from shapely.ops import unary_union
    datos = json.loads((RAIZ / "visor/datos/actual.geojson").read_text(encoding="utf-8"))
    g = [shape(f["geometry"]) for f in datos["features"] if norm(f["properties"].get("nombre") or "") == norm(pais)]
    return unary_union(g) if g else None


def por_coordenadas(r, z):
    """Coincide si la cobertura del mapa cubre una parte relevante del país y no es un mapamundi."""
    b = r.get("bbox")
    if not z or not b or None in b:
        return False
    from shapely.geometry import box
    o, s_, e, n = b
    if e - o > 120 or n - s_ > 80:
        return False
    caja = box(min(o, e), min(s_, n), max(o, e), max(s_, n))
    if caja.area == 0:
        return z.contains(caja.centroid)
    inter = caja.intersection(z).area
    return inter / caja.area >= 0.15 or inter / z.area >= 0.3


def coincide(r, ts, z=None):
    if por_coordenadas(r, z):
        return "coordenadas"
    lugares = [norm(x) for x in r.get("lugares", [])]
    for t in ts:
        patron = re.compile(r"\b" + re.escape(t) + r"\b")
        if any(patron.search(l) for l in lugares):
            return "categoría"
    titulo = norm(r["t"])
    for t in ts:
        if re.search(r"\b" + re.escape(t) + r"\b", titulo):
            return "título"
    return None


def resolver_paises(lugar):
    """Convierte la consulta en códigos ISO3 usando los mismos nombres que el clasificador
    (nombres actuales en 25+ idiomas y nombres históricos)."""
    sys.path.insert(0, str(RAIZ / "scripts"))
    import comprender
    paises, _, _, _, terminos, _ = comprender.cargar_paises()
    q = norm(lugar)
    isos = {iso for iso, _ in terminos.get(q, set())}
    if not isos:
        isos = {iso for iso, d in paises.items() if norm(d["nombre_es"] or "") == q}
    return sorted(isos), paises


def resolver_regiones(lugar):
    """Provincias/estados/regiones (Natural Earth admin-1) cuyo nombre coincide con la consulta."""
    datos = json.loads((RAIZ / "catalogo/geo/regiones.geojson").read_text(encoding="utf-8"))
    q = norm(lugar)
    res = {}
    for f in datos["features"]:
        p = f["properties"]
        nombres = [p.get("nombre"), p.get("nombre_es")] + (p.get("alternativos") or [])
        if any(n and norm(n) == q for n in nombres):
            res[p["id"]] = p["pais"]
    return res


def desde_biblioteca(isos, a, regiones=None):
    res = []
    for iso in isos:
        ruta = RAIZ / "catalogo/biblioteca/paises" / f"{iso}.jsonl.gz"
        if not ruta.exists():
            continue
        with gzip.open(ruta, "rt", encoding="utf-8") as f:
            for linea in f:
                r = json.loads(linea)
                anio = r.get("anio")
                if a.desde and (not anio or anio < a.desde):
                    continue
                if a.hasta and (not anio or anio > a.hasta):
                    continue
                if a.siglo and a.siglo not in (r.get("siglos") or []):
                    continue
                if a.tipo and norm(a.tipo) not in norm(r.get("tipo") or ""):
                    continue
                if (r.get("relevancia") or 0) < a.relevancia:
                    continue
                if regiones and not (set(r.get("regiones") or []) & set(regiones)):
                    continue
                r["coincidencia"] = r.get("via")
                res.append(r)
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("lugar")
    ap.add_argument("--desde", type=int)
    ap.add_argument("--hasta", type=int)
    ap.add_argument("--siglo", type=int)
    ap.add_argument("--max", type=int, default=2000)
    ap.add_argument("--tipo", help="portulano, carta náutica, ptolemaico, mapamundi, plano urbano, topográfico…")
    ap.add_argument("--relevancia", type=float, default=0.0,
                    help="mínimo (1 = el mapa nombra el país; 0,3 = el país ocupa al menos el 30 %% del mapa)")
    a = ap.parse_args()
    isos, _ = resolver_paises(a.lugar)
    regs = resolver_regiones(a.lugar)
    # Si la consulta es una provincia/región del mismo país (p. ej. "Antioquia"), se busca la región.
    if regs and isos and set(regs.values()) <= set(isos):
        isos = []
    if isos and (RAIZ / "catalogo/biblioteca/paises").exists():
        ts = isos
        res = desde_biblioteca(isos, a)
    elif regs:
        ts = [f"región {rid} ({pais})" for rid, pais in regs.items()]
        res = desde_biblioteca(sorted(set(regs.values())), a, regiones=list(regs))
    else:
        # Región que no es un país (p. ej. "Mediterráneo", "Ptolomeo"): búsqueda por texto en el índice.
        fragmentos = sorted((RAIZ / "catalogo/indice").glob("mapas-*.jsonl.gz"))
        if not fragmentos:
            sys.exit("No hay índice: ejecuta el flujo 'Catálogo' o scripts/indexar_catalogo.py")
        ts, pais = terminos(a.lugar)
        z = zona(pais)
        res = []
        for frag in fragmentos:
            with gzip.open(frag, "rt", encoding="utf-8") as f:
                for linea in f:
                    r = json.loads(linea)
                    como = coincide(r, ts, z)
                    if not como:
                        continue
                    anio = r.get("anio")
                    if a.desde and (not anio or anio < a.desde):
                        continue
                    if a.hasta and (not anio or anio > a.hasta):
                        continue
                    if a.siglo and a.siglo not in r.get("siglos", []):
                        continue
                    r["coincidencia"] = como
                    res.append(r)
    res.sort(key=lambda r: (r.get("anio") or 9999, r["t"]))
    print(f"«{a.lugar}» -> {ts}: {len(res)} mapas")
    for r in res[:60]:
        print(f"  {r.get('anio') or '¿?':>5}  {(r.get('t') or '')[:70]}  [{r.get('tipo', '')}; {r.get('fuente', 'commons')}; por {r['coincidencia']}]")
    if len(res) > 60:
        print(f"  … y {len(res) - 60} más (ver la galería)")

    destino = RAIZ / "salidas/busquedas"
    destino.mkdir(parents=True, exist_ok=True)
    nombre = re.sub(r"[^a-z0-9]+", "-", norm(a.lugar)).strip("-")
    (destino / f"{nombre}.json").write_text(json.dumps(res[: a.max], ensure_ascii=False, indent=1), encoding="utf-8")
    tarjetas = []
    for r in res[: a.max]:
        pagina = r.get("url") or "https://commons.wikimedia.org/wiki/File:" + r["t"].replace(" ", "_")
        tarjetas.append(
            f'<figure><a href="{html.escape(pagina)}" target="_blank" rel="noopener">'
            f'<img loading="lazy" src="{html.escape(r.get("th") or "")}" alt=""></a>'
            f'<figcaption><b>{r.get("anio") or "¿?"}</b> · {html.escape(r["t"][:90])}<br>'
            f'<small>{html.escape((r.get("autor") or "")[:60])} · {html.escape(r["lic"])} · '
            f'{html.escape(r.get("fuente", "commons"))} · por {r["coincidencia"]}</small></figcaption></figure>')
    (destino / f"{nombre}.html").write_text(f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>Mapas de {html.escape(a.lugar)}</title>
<style>body{{margin:0;padding:16px;background:#1b2a33;color:#efe6d2;font-family:Georgia,serif}}
h1{{color:#d9a441;font-size:22px}}main{{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:14px}}
figure{{margin:0;background:#22323c;border-radius:8px;overflow:hidden}}img{{width:100%;height:180px;object-fit:cover;display:block;background:#333}}
figcaption{{padding:8px;font-size:13px;line-height:1.35}}small{{opacity:.75}}</style></head><body>
<h1>Mapas de {html.escape(a.lugar)} · {len(res)} resultados</h1>
<p>Términos: {html.escape(", ".join(ts))}. Fuentes: Wikimedia Commons, bibliotecas de OpenGeoMetadata, Library of Congress, Internet Archive y Europeana; solo licencias libres (sin NC/ND). Orden cronológico.</p>
<main>{"".join(tarjetas)}</main></body></html>""", encoding="utf-8")
    print(f"Galería: salidas/busquedas/{nombre}.html")


if __name__ == "__main__":
    main()
