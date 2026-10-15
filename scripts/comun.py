"""Utilidades compartidas por los scripts de Cartographer."""
import json
import re
import unicodedata
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
AVISO_FRONTERAS = "Fronteras aproximadas"


def leer_json(ruta):
    return json.loads(Path(ruta).read_text(encoding="utf-8"))


def escribir_json(ruta, datos, compacto=False):
    ruta = Path(ruta)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    if compacto:
        texto = json.dumps(datos, ensure_ascii=False, separators=(",", ":"))
    else:
        texto = json.dumps(datos, ensure_ascii=False, indent=2)
    ruta.write_text(texto + "\n", encoding="utf-8")


def slug(texto):
    t = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    t = re.sub(r"[^a-zA-Z0-9]+", "-", t).strip("-").lower()
    return t or "sin-nombre"


def fuente(id_fuente):
    for f in leer_json(RAIZ / "fuentes/fuentes.json")["fuentes"]:
        if f["id"] == id_fuente:
            return f
    raise KeyError(id_fuente)


def descargar(url, destino):
    destino = Path(destino)
    if destino.exists() and destino.stat().st_size > 0:
        return destino
    destino.parent.mkdir(parents=True, exist_ok=True)
    print(f"Descargando {url}")
    with urllib.request.urlopen(url, timeout=120) as r:
        destino.write_bytes(r.read())
    return destino
