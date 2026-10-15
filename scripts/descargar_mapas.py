"""Descarga desde Wikimedia Commons la imagen de cada mapa con ficha y registra su licencia oficial.

Se ejecuta en GitHub Actions (tiene acceso a internet). Solo biblioteca estándar.
Para cada mapas/<id>/ficha.json que tenga "commons_archivo" (p. ej. "File:Nombre.jpg"):
  1. Consulta la API de Commons y guarda en la ficha, literal, la licencia, autor, fecha y crédito.
  2. Si la licencia permite uso comercial (dominio público, CC0, CC BY, CC BY-SA), descarga la imagen
     (ancho "descarga_ancho", por defecto 4000 px) como original.jpg y marca licencia_verificada=true.
  3. Si no lo permite, no descarga y deja licencia_verificada=false.
"""
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
API = "https://commons.wikimedia.org/w/api.php"
UA = "Cartographer/1.0 (https://github.com/TimothyArcher90/Cartographer)"


def pedir(url):
    for intento in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=120) as r:
                return r.read()
        except Exception:
            time.sleep(2 ** intento)
    raise RuntimeError(url)


def limpiar(html):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", html or "")).strip()


def permite_uso_comercial(licencia):
    l = licencia.lower()
    if "nc" in re.split(r"[\s\-]", l) or "non-commercial" in l or "noncommercial" in l or "-nd" in l:
        return False
    return any(x in l for x in ("public domain", "pd", "cc0", "cc by", "cc-by"))


def main():
    for ruta in sorted((RAIZ / "mapas").glob("*/ficha.json")):
        f = json.loads(ruta.read_text(encoding="utf-8"))
        archivo = f.get("commons_archivo")
        if not archivo:
            continue
        ancho = f.get("descarga_ancho", 4000)
        q = urllib.parse.urlencode(dict(action="query", titles=archivo, prop="imageinfo",
                                        iiprop="url|size|extmetadata|sha1", iiurlwidth=ancho,
                                        format="json", formatversion="2"))
        pagina = json.loads(pedir(f"{API}?{q}"))["query"]["pages"][0]
        if "imageinfo" not in pagina:
            print(f"{ruta.parent.name}: {archivo} no existe en Commons")
            f["licencia_verificada"] = False
            f["commons_error"] = "archivo no encontrado"
        else:
            ii = pagina["imageinfo"][0]
            m = ii.get("extmetadata", {})
            v = lambda k: limpiar(m.get(k, {}).get("value"))
            f["commons"] = {
                "pagina": ii["descriptionurl"], "url_original": ii["url"],
                "ancho_original": ii["width"], "alto_original": ii["height"], "sha1": ii.get("sha1"),
                "licencia": v("LicenseShortName"), "licencia_url": v("LicenseUrl"),
                "uso": v("UsageTerms"), "autor": v("Artist"), "fecha": v("DateTimeOriginal"),
                "credito": v("Credit")[:500], "consultado": time.strftime("%Y-%m-%d"),
            }
            f["url"] = ii["descriptionurl"]
            f["licencia"] = v("LicenseShortName")
            f["licencia_verificada"] = permite_uso_comercial(v("LicenseShortName"))
            destino = ruta.parent / f.get("imagen_original", "original.jpg")
            if f["licencia_verificada"] and not destino.exists():
                url = ii.get("thumburl") if ii["width"] > ancho else ii["url"]
                destino.write_bytes(pedir(url))
                print(f"{ruta.parent.name}: descargado {destino.name} ({destino.stat().st_size // 1024} KB)")
            elif not f["licencia_verificada"]:
                print(f"{ruta.parent.name}: licencia '{f['licencia']}' no permite uso comercial; no se descarga")
        ruta.write_text(json.dumps(f, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        time.sleep(1)


if __name__ == "__main__":
    main()
