"""Genera un «mapa antiguo» SINTÉTICO para probar la cadena de georreferenciación.

NO es un mapa histórico y NUNCA entra en mapas/, en el paquete ni en el visor.
Se dibujan las fronteras de 1492 (historical-basemaps) con una
deformación conocida, y se anotan GCP exactos. Así se puede comprobar que
scripts/georreferenciar.py recupera la geometría y que el error en km es coherente.

Uso: python pruebas/generar_prueba_sintetica.py
"""
import json
import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw
from shapely.geometry import box, shape

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
from comun import escribir_json  # noqa: E402

OESTE, ESTE, SUR, NORTE = -12.0, 42.0, 28.0, 48.0


def deformar(lon, lat):
    x = 40 + (lon - OESTE) * 28 + 25 * math.sin(lat * math.pi / 30)
    y = 40 + (NORTE - lat) * 32 + 0.15 * (lon - 15) ** 2
    return x, y


def main():
    datos = json.loads((RAIZ / "epocas/anio-1492.geojson").read_text(encoding="utf-8"))
    marco = box(OESTE, SUR, ESTE, NORTE)
    ancho, alto = 1640, 900
    img = Image.new("RGB", (ancho, alto), (214, 196, 160))
    d = ImageDraw.Draw(img)
    colores = [(176, 92, 72), (110, 130, 90), (150, 120, 70), (120, 100, 140), (90, 120, 140)]
    for i, f in enumerate(datos["features"]):
        g = shape(f["geometry"]).intersection(marco)
        if g.is_empty:
            continue
        for p in getattr(g, "geoms", [g]):
            if p.geom_type != "Polygon":
                continue
            pts = [deformar(x, y) for x, y in p.exterior.coords]
            if len(pts) > 2:
                d.polygon(pts, fill=colores[i % len(colores)], outline=(40, 30, 20))
    for lon in range(-10, 41, 10):
        d.line([deformar(lon, la / 2) for la in range(int(SUR * 2), int(NORTE * 2) + 1)], fill=(60, 50, 40))
    carpeta = RAIZ / "pruebas/salida/prueba-sintetica"
    carpeta.mkdir(parents=True, exist_ok=True)
    img.save(carpeta / "original.png")
    gcp = []
    for lon in (-10, 0, 10, 20, 30, 40):
        for lat in (30, 38, 46):
            x, y = deformar(lon, lat)
            gcp.append({"px": round(x, 2), "py": round(y, 2), "lon": lon, "lat": lat,
                        "etiqueta": f"cuadrícula {lon},{lat}"})
    escribir_json(carpeta / "ficha.json", {
        "id": "prueba-sintetica",
        "titulo": "Prueba sintética de georreferenciación (NO es un mapa histórico)",
        "autor": "Cartographer (generado)",
        "anio": None,
        "fuente": "historical-basemaps",
        "url": None,
        "licencia": "GPL-3.0",
        "licencia_verificada": True,
        "uso_en_video": "no",
        "imagen_original": "original.png",
        "metodo": "tps",
        "modo": "superpuesto",
        "calidad": "prueba",
        "notas": "Fronteras de 1492 dibujadas con una deformación conocida. Solo sirve para probar la cadena.",
        "gcp": gcp,
    })
    print(f"Creado {carpeta}")


if __name__ == "__main__":
    main()
