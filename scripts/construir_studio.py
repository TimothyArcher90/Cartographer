"""Prepara los datos ligeros del estudio web (studio/).

Uso: python scripts/construir_studio.py
Salida:
  studio/datos/paises.geojson  (fronteras actuales simplificadas, nombre en español)
  studio/datos/nombres.json    (nombre normalizado -> {"iso": [...], "region": [...]}) para el buscador
  studio/datos/paises.json     (resumen por país: nombre, total de mapas, por siglo)
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

import shapely
from shapely.geometry import mapping, shape

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
from comprender import EEUU, EXCLUIR_TERMINOS, IDIOMAS  # noqa: E402


def norm(t):
    t = unicodedata.normalize("NFKD", str(t)).encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", t).strip()


def main():
    destino = RAIZ / "studio/datos"
    destino.mkdir(parents=True, exist_ok=True)
    nombres = {}

    def poner(n, clave, valor):
        n = norm(n)
        if len(n) < 3 or n in EXCLUIR_TERMINOS:
            return
        d = nombres.setdefault(n, {})
        if valor not in d.setdefault(clave, []):
            d[clave].append(valor)

    datos = json.loads((RAIZ / "catalogo/geo/paises.geojson").read_text(encoding="utf-8"))
    feats = []
    for f in datos["features"]:
        p = f["properties"]
        iso = p.get("ISO_A3") if p.get("ISO_A3") not in (None, "-99") else p.get("ADM0_A3")
        if not iso:
            continue
        for c in IDIOMAS:
            if p.get(c):
                poner(p[c], "iso", iso)
        g = shapely.set_precision(shape(f["geometry"]).simplify(0.03), 0.001)
        feats.append({"type": "Feature", "properties": {"iso": iso, "nombre": p.get("NAME_ES") or p.get("NAME"),
                                                        "lon": round(p.get("LABEL_X") or g.centroid.x, 3),
                                                        "lat": round(p.get("LABEL_Y") or g.centroid.y, 3)},
                      "geometry": mapping(g)})
    (destino / "paises.geojson").write_text(json.dumps({"type": "FeatureCollection", "features": feats},
                                                       ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    hist = json.loads((RAIZ / "catalogo/nombres_historicos.json").read_text(encoding="utf-8"))
    for iso, lista in hist.items():
        if not iso.startswith("_"):
            for v in lista:
                poner(v, "iso", iso)
    for v in EEUU:
        poner(v, "iso", "USA")
    regiones = json.loads((RAIZ / "catalogo/geo/regiones.geojson").read_text(encoding="utf-8"))
    for f in regiones["features"]:
        p = f["properties"]
        for v in [p.get("nombre"), p.get("nombre_es")] + (p.get("alternativos") or []):
            if v:
                poner(v, "region", [p["id"], p["pais"], p.get("nombre_es") or p.get("nombre")])
    (destino / "nombres.json").write_text(json.dumps(nombres, ensure_ascii=False, separators=(",", ":")),
                                          encoding="utf-8")
    resumen = json.loads((RAIZ / "catalogo/biblioteca/paises.json").read_text(encoding="utf-8"))
    ligero = {iso: {"nombre": d["nombre_es"], "total": d["total"], "por_siglo": d["por_siglo"]}
              for iso, d in resumen.items()}
    (destino / "paises.json").write_text(json.dumps(ligero, ensure_ascii=False, separators=(",", ":")),
                                         encoding="utf-8")
    print(f"{len(feats)} países · {len(nombres)} nombres buscables")


if __name__ == "__main__":
    main()
