"""Descarga, normaliza y simplifica las épocas de epocas/config.json.

Uso: python scripts/normalizar_epocas.py [--tolerancia 0.02]
Salida: epocas/<id>.geojson + epocas/indice.json
"""
import argparse
import sys

import shapely
from shapely.geometry import mapping, shape
from shapely.validation import make_valid
from shapely.geometry import MultiPolygon, Polygon, GeometryCollection

from comun import AVISO_FRONTERAS, RAIZ, descargar, escribir_json, fuente, leer_json, slug

PRECISION = {1: "aproximada", 2: "moderada", 3: "derecho internacional"}


def solo_poligonos(g):
    if isinstance(g, (Polygon, MultiPolygon)):
        return g
    if isinstance(g, GeometryCollection):
        partes = []
        for p in g.geoms:
            if isinstance(p, Polygon):
                partes.append(p)
            elif isinstance(p, MultiPolygon):
                partes.extend(p.geoms)
        return MultiPolygon(partes) if partes else None
    return None


def limpiar(geom, tolerancia):
    g = shape(geom)
    if not g.is_valid:
        g = make_valid(g)
    g = g.simplify(tolerancia, preserve_topology=True)
    if not g.is_valid:
        g = make_valid(g)
    g = solo_poligonos(g)
    if g is None or g.is_empty:
        return None
    # Rejilla de 0,0001° (~11 m): reduce tamaño y conserva validez topológica.
    g = solo_poligonos(shapely.set_precision(g, 1e-4))
    if g is None or g.is_empty:
        return None
    return g


def a_listas(coords):
    if isinstance(coords, (list, tuple)) and coords and isinstance(coords[0], (int, float)):
        return [round(coords[0], 4), round(coords[1], 4)]
    return [a_listas(c) for c in coords]


def procesar(epoca, tolerancia, traducciones, hb):
    anio = epoca["anio_fuente"]
    if anio not in leer_json(RAIZ / "fuentes/fuentes.json")["anios_disponibles_historical_basemaps"]:
        sys.exit(f"ERROR: la fuente no tiene el año {anio}")
    nombre_archivo = f"world_bc{-anio}.geojson" if anio < 0 else f"world_{anio}.geojson"
    url = hb["url_descarga"].format(commit=hb["commit"], anio=anio).replace(f"world_{anio}.geojson", nombre_archivo)
    bruto = leer_json(descargar(url, RAIZ / "fuentes/cache" / nombre_archivo))

    salida, usados, sin_traducir = [], {}, set()
    for f in bruto["features"]:
        p = f["properties"] or {}
        nombre = (p.get("NAME") or "").strip()
        if not nombre or not f.get("geometry"):
            continue
        g = limpiar(f["geometry"], tolerancia)
        if g is None:
            continue
        base = f"{epoca['id']}-{slug(nombre)}"
        usados[base] = usados.get(base, 0) + 1
        ident = base if usados[base] == 1 else f"{base}-{usados[base]}"
        es = traducciones.get(nombre)
        if es is None:
            sin_traducir.add(nombre)
        prec = p.get("BORDERPRECISION")
        try:
            prec = int(prec) if prec is not None else None
        except (TypeError, ValueError):
            prec = None
        geo = mapping(g)
        geo = {"type": geo["type"], "coordinates": a_listas(geo["coordinates"])}
        salida.append({
            "type": "Feature",
            "id": ident,
            "properties": {
                "id": ident,
                "nombre_original": nombre,
                "nombre_es": es if es else nombre,
                "nombre_es_verificado": es is not None,
                "soberano": (p.get("SUBJECTO") or "").strip() or None,
                "parte_de": (p.get("PARTOF") or "").strip() or None,
                "anio": anio,
                "precision": prec,
                "precision_texto": PRECISION.get(prec, "desconocida"),
                "fuente": hb["id"],
                "licencia": hb["licencia"],
            },
            "geometry": geo,
        })

    archivo = f"{epoca['id']}.geojson"
    escribir_json(RAIZ / "epocas" / archivo, {
        "type": "FeatureCollection",
        "cartographer": {
            "epoca": epoca["id"], "anio": anio, "titulo": epoca["titulo"],
            "aviso": AVISO_FRONTERAS, "fuente": hb["id"], "commit_fuente": hb["commit"],
            "licencia": hb["licencia"], "tolerancia_simplificacion_grados": tolerancia,
        },
        "features": salida,
    }, compacto=True)
    traducidas = sum(1 for x in salida if x["properties"]["nombre_es_verificado"])
    print(f"{epoca['id']}: {len(salida)} entidades, {traducidas} con nombre en español verificado")
    return {
        "id": epoca["id"], "anio": anio, "titulo": epoca["titulo"], "nota": epoca.get("nota"),
        "archivo": f"epocas/{archivo}", "entidades": len(salida),
        "entidades_nombre_es_verificado": traducidas,
        "fuente": hb["id"], "licencia": hb["licencia"], "aviso": AVISO_FRONTERAS,
        "sin_traducir": sorted(sin_traducir),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tolerancia", type=float, default=0.02, help="grados (0.02 ≈ 2 km)")
    a = ap.parse_args()
    hb = fuente("historical-basemaps")
    traducciones = {k: v for k, v in leer_json(RAIZ / "traducciones/es.json").items() if not k.startswith("_")}
    config = leer_json(RAIZ / "epocas/config.json")["epocas"]
    indice = [procesar(e, a.tolerancia, traducciones, hb) for e in config]
    escribir_json(RAIZ / "epocas/indice.json", {
        "version": 1, "aviso": AVISO_FRONTERAS,
        "epocas": [{k: v for k, v in e.items() if k != "sin_traducir"} for e in indice],
    })
    escribir_json(RAIZ / "traducciones/pendientes.json",
                  {e["id"]: e["sin_traducir"] for e in indice})


if __name__ == "__main__":
    main()
