"""Georreferencia un mapa antiguo a partir de su ficha.json.

Uso: python scripts/georreferenciar.py mapas/<id>
Lee:   mapas/<id>/ficha.json  (imagen_original, gcp, metodo)
Crea:  mapas/<id>/salida/mapa.tif   (COG, EPSG:3857)
       mapas/<id>/salida/vista.png  (versión ligera, máx. 2048 px)
y actualiza en la ficha: salida, limites (4 esquinas lon/lat) y error_medio_km.

Equivale a (con la CLI de GDAL): gdal_translate -gcp ... + gdalwarp -tps (o -order 1/2) -t_srs EPSG:3857.
Métodos: "tps" (thin-plate spline), "poli1" (afín), "poli2" (polinómico de 2.º grado).
La deformación se calcula con numpy (mismo modelo con el que se mide el error) y
GDAL (vía rasterio) solo escribe el COG.
El error se mide como validación cruzada «dejando uno fuera» en km: con TPS el error
en los propios puntos es 0, así que solo el error dejando uno fuera es honesto.
"""
import math
import sys
from pathlib import Path

import numpy as np
import rasterio
import rasterio.shutil
from affine import Affine
from PIL import Image
from rasterio.crs import CRS
from rasterio.enums import ColorInterp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import escribir_json, leer_json  # noqa: E402

ORDEN = {"tps": None, "poli1": 1, "poli2": 2}
MIN_GCP = {"tps": 4, "poli1": 3, "poli2": 6}


def km(lon1, lat1, lon2, lat2):
    r = 6371.0088
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp, dl = p2 - p1, math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))


R_MERC = 6378137.0


def a_mercator(lon, lat):
    lon, lat = np.asarray(lon, float), np.clip(np.asarray(lat, float), -85.05, 85.05)
    return R_MERC * np.radians(lon), R_MERC * np.log(np.tan(np.pi / 4 + np.radians(lat) / 2))


def de_mercator(x, y):
    return np.degrees(x / R_MERC), np.degrees(2 * np.arctan(np.exp(y / R_MERC)) - np.pi / 2)


def bilineal(img, sx, sy):
    """Muestrea img (alto, ancho, 4) en coordenadas de píxel; fuera de la imagen -> transparente."""
    alto, ancho = img.shape[:2]
    x, y = sx - 0.5, sy - 0.5
    fuera = (x < -0.5) | (y < -0.5) | (x > ancho - 0.5) | (y > alto - 0.5)
    x, y = np.clip(x, 0, ancho - 1), np.clip(y, 0, alto - 1)
    x0, y0 = np.floor(x).astype(int), np.floor(y).astype(int)
    x1, y1 = np.minimum(x0 + 1, ancho - 1), np.minimum(y0 + 1, alto - 1)
    fx, fy = (x - x0)[:, None], (y - y0)[:, None]
    i = img.astype(np.float32)
    v = (i[y0, x0] * (1 - fx) * (1 - fy) + i[y0, x1] * fx * (1 - fy)
         + i[y1, x0] * (1 - fx) * fy + i[y1, x1] * fx * fy)
    v[fuera] = 0
    return np.clip(v + 0.5, 0, 255).astype(np.uint8)


def _base_poli(px, py, orden):
    cols = [np.ones_like(px), px, py]
    if orden == 2:
        cols += [px * px, px * py, py * py]
    return np.stack(cols, axis=1)


def ajustar(metodo, px, py, lon, lat):
    """Devuelve una función (px, py) -> (lon, lat)."""
    if metodo == "tps":
        pts = np.stack([px, py], axis=1)
        n = len(pts)

        def u(r):
            with np.errstate(divide="ignore", invalid="ignore"):
                v = r * r * np.log(r * r)
            return np.nan_to_num(v)

        k = u(np.linalg.norm(pts[:, None] - pts[None], axis=2))
        p = np.hstack([np.ones((n, 1)), pts])
        a = np.zeros((n + 3, n + 3))
        a[:n, :n], a[:n, n:], a[n:, :n] = k, p, p.T
        b = np.zeros((n + 3, 2))
        b[:n, 0], b[:n, 1] = lon, lat
        w = np.linalg.solve(a, b)

        def f(qx, qy):
            q = np.stack([np.atleast_1d(qx), np.atleast_1d(qy)], axis=1)
            kq = u(np.linalg.norm(q[:, None] - pts[None], axis=2))
            pq = np.hstack([np.ones((len(q), 1)), q])
            r = kq @ w[:n] + pq @ w[n:]
            return r[:, 0], r[:, 1]
        return f
    orden = ORDEN[metodo]
    m = _base_poli(px, py, orden)
    cx = np.linalg.lstsq(m, lon, rcond=None)[0]
    cy = np.linalg.lstsq(m, lat, rcond=None)[0]

    def f(qx, qy):
        q = _base_poli(np.atleast_1d(np.asarray(qx, float)), np.atleast_1d(np.asarray(qy, float)), orden)
        return q @ cx, q @ cy
    return f


def error_dejando_uno(metodo, px, py, lon, lat):
    errores = []
    for i in range(len(px)):
        m = np.ones(len(px), bool)
        m[i] = False
        f = ajustar(metodo, px[m], py[m], lon[m], lat[m])
        elon, elat = f(px[i], py[i])
        errores.append(km(lon[i], lat[i], float(elon[0]), float(elat[0])))
    return errores


def georreferenciar(carpeta):
    carpeta = Path(carpeta)
    ficha_ruta = carpeta / "ficha.json"
    ficha = leer_json(ficha_ruta)
    metodo = ficha.get("metodo", "tps")
    if metodo not in ORDEN:
        sys.exit(f"Método desconocido: {metodo}")
    gcp = ficha.get("gcp") or []
    if len(gcp) < MIN_GCP[metodo] + 1:
        sys.exit(f"{carpeta.name}: hacen falta al menos {MIN_GCP[metodo] + 1} GCP para '{metodo}' (hay {len(gcp)})")
    original = carpeta / ficha["imagen_original"]
    if not original.exists():
        sys.exit(f"{carpeta.name}: falta la imagen original {original}")

    px = np.array([g["px"] for g in gcp], float)
    py = np.array([g["py"] for g in gcp], float)
    lon = np.array([g["lon"] for g in gcp], float)
    lat = np.array([g["lat"] for g in gcp], float)
    errores = error_dejando_uno(metodo, px, py, lon, lat)

    salida = carpeta / "salida"
    salida.mkdir(exist_ok=True)
    img = np.array(Image.open(original).convert("RGBA"))
    alto, ancho = img.shape[:2]

    # Modelo directo (píxel -> lon/lat) para los límites e inverso (Mercator -> píxel) para remuestrear.
    directo = ajustar(metodo, px, py, lon, lat)
    mx, my = a_mercator(lon, lat)
    inverso = ajustar(metodo, mx, my, px, py)
    borde = np.concatenate([
        np.stack([np.linspace(0, ancho, 200), np.zeros(200)], 1),
        np.stack([np.linspace(0, ancho, 200), np.full(200, alto)], 1),
        np.stack([np.zeros(200), np.linspace(0, alto, 200)], 1),
        np.stack([np.full(200, ancho), np.linspace(0, alto, 200)], 1)])
    blon, blat = directo(borde[:, 0], borde[:, 1])
    bx, by = a_mercator(blon, blat)
    oeste, este, sur, norte = bx.min(), bx.max(), by.min(), by.max()
    res = max(este - oeste, norte - sur) / max(ancho, alto)
    w, h = int(math.ceil((este - oeste) / res)), int(math.ceil((norte - sur) / res))
    dst_t = Affine(res, 0, oeste, 0, -res, norte)

    destino = np.zeros((4, h, w), np.uint8)
    for f0 in range(0, h, 256):
        filas = np.arange(f0, min(h, f0 + 256))
        cx, cy = np.meshgrid(np.arange(w) + 0.5, filas + 0.5)
        gx, gy = oeste + cx.ravel() * res, norte - cy.ravel() * res
        sx, sy = inverso(gx, gy)
        destino[:, filas[0]:filas[-1] + 1, :] = bilineal(img, sx, sy).reshape(len(filas), w, 4).transpose(2, 0, 1)

    merc = CRS.from_epsg(3857)
    tif = salida / "mapa.tif"
    tmp = salida / "_tmp.tif"
    with rasterio.open(tmp, "w", driver="GTiff", width=w, height=h, count=4, dtype="uint8",
                       crs=merc, transform=dst_t, photometric="RGB") as d:
        d.write(destino)
        d.colorinterp = [ColorInterp.red, ColorInterp.green, ColorInterp.blue, ColorInterp.alpha]
    rasterio.shutil.copy(tmp, tif, driver="COG", compress="DEFLATE")
    tmp.unlink()

    escala = min(1.0, 2048 / max(w, h))
    vista = Image.fromarray(np.moveaxis(destino, 0, 2), "RGBA")
    if escala < 1:
        vista = vista.resize((max(1, int(w * escala)), max(1, int(h * escala))), Image.LANCZOS)
    vista.save(salida / "vista.png", optimize=True)

    xs, ys = de_mercator(np.array([oeste, este, este, oeste]), np.array([norte, norte, sur, sur]))
    ficha["salida"] = {"cog": "salida/mapa.tif", "vista": "salida/vista.png", "crs": "EPSG:3857",
                      "ancho": w, "alto": h}
    ficha["limites"] = [[round(x, 6), round(y, 6)] for x, y in zip(xs, ys)]
    ficha["error_medio_km"] = round(float(np.mean(errores)), 2)
    ficha["error_max_km"] = round(float(np.max(errores)), 2)
    ficha["error_metodo"] = "validación cruzada dejando un GCP fuera"
    escribir_json(ficha_ruta, ficha)
    print(f"{carpeta.name}: {len(gcp)} GCP, {metodo}, error medio {ficha['error_medio_km']} km "
          f"(máx. {ficha['error_max_km']} km) -> {tif}")
    return ficha


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for c in sys.argv[1:]:
        georreferenciar(c)
