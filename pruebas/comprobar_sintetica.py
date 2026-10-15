"""Comprueba la georreferenciación de la prueba sintética con puntos que NO son GCP.

Como se conoce la deformación exacta, se mide el error real en km en puntos de control
independientes. Falla si el error medio supera 30 km.
"""
import sys
from pathlib import Path

import numpy as np

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
sys.path.insert(0, str(RAIZ / "pruebas"))
from comun import leer_json  # noqa: E402
from georreferenciar import ajustar, km  # noqa: E402
from generar_prueba_sintetica import deformar  # noqa: E402

UMBRAL_KM = 30

f = leer_json(RAIZ / "mapas/prueba-sintetica/ficha.json")
g = f["gcp"]
modelo = ajustar(f["metodo"], *(np.array([p[k] for p in g], float) for k in ("px", "py", "lon", "lat")))
errores = []
for lon in (-5, 5, 15, 25, 35):
    for lat in (34, 42):
        x, y = deformar(lon, lat)
        elon, elat = modelo(x, y)
        errores.append(km(lon, lat, float(elon[0]), float(elat[0])))
media = float(np.mean(errores))
print(f"Prueba sintética: error real medio {media:.2f} km, máx. {max(errores):.2f} km en {len(errores)} puntos independientes")
if media > UMBRAL_KM:
    sys.exit(f"ERROR: supera {UMBRAL_KM} km")
