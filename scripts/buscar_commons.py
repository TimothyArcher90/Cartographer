"""Busca mapas en Wikimedia Commons y guarda sus metadatos de licencia tal como los publica Commons.

Se ejecuta en GitHub Actions (tiene acceso a internet). Solo usa la biblioteca estándar.
Uso: python scripts/buscar_commons.py
Salida: fuentes/commons/resultados.json
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


def api(**p):
    p.update(format="json", formatversion="2")
    url = API + "?" + urllib.parse.urlencode(p)
    for intento in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except Exception:
            time.sleep(2 ** intento)
    raise RuntimeError(url)


def limpiar(html):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", html or "")).strip()


def main():
    terminos = json.loads((RAIZ / "fuentes/commons/busquedas.json").read_text())["busquedas"]
    salida = {"fecha": time.strftime("%Y-%m-%d"), "api": API, "resultados": {}}
    for t in terminos:
        r = api(action="query", generator="search", gsrsearch=f"filetype:bitmap {t}", gsrnamespace=6,
                gsrlimit=12, prop="imageinfo", iiprop="url|size|mime|extmetadata", iiurlwidth=2400)
        lista = []
        for pagina in sorted(r.get("query", {}).get("pages", []), key=lambda x: x.get("index", 0)):
            ii = (pagina.get("imageinfo") or [{}])[0]
            m = ii.get("extmetadata", {})
            v = lambda k: limpiar(m.get(k, {}).get("value"))
            lista.append({
                "titulo": pagina["title"],
                "pagina": ii.get("descriptionurl"),
                "url_original": ii.get("url"),
                "url_2400": ii.get("thumburl"),
                "ancho": ii.get("width"), "alto": ii.get("height"), "mime": ii.get("mime"),
                "licencia": v("LicenseShortName"), "licencia_url": v("LicenseUrl"),
                "uso": v("UsageTerms"), "con_copyright": v("Copyrighted"),
                "autor": v("Artist"), "fecha": v("DateTimeOriginal"), "credito": v("Credit"),
                "descripcion": v("ImageDescription")[:600],
            })
        salida["resultados"][t] = lista
        print(t, len(lista))
        time.sleep(1)
    destino = RAIZ / "fuentes/commons/resultados.json"
    destino.write_text(json.dumps(salida, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
