"""Validaciones automáticas. Sale con código 1 si hay algún ERROR.

Uso: python scripts/validar.py
Comprueba:
  - épocas: GeoJSON legible, geometrías válidas, id único, nombre_es presente,
    licencia y fuente en cada elemento, aviso de fronteras aproximadas, índice coherente.
  - mapas: ficha completa, licencia presente y verificada si uso_en_video != "no",
    GCP suficientes, salida georreferenciada con error_medio_km anotado.
  - fuentes: toda fuente usada está registrada y verificada.
"""
import sys
from pathlib import Path

from shapely.geometry import shape

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import AVISO_FRONTERAS, RAIZ, leer_json  # noqa: E402

errores, avisos = [], []


def error(m):
    errores.append(m)


def aviso(m):
    avisos.append(m)


def fuentes_verificadas():
    return {f["id"]: f for f in leer_json(RAIZ / "fuentes/fuentes.json")["fuentes"]}


def validar_epocas(fuentes):
    indice = leer_json(RAIZ / "epocas/indice.json")
    if indice.get("aviso") != AVISO_FRONTERAS:
        error("epocas/indice.json: falta el aviso de fronteras aproximadas")
    for e in indice["epocas"]:
        ruta = RAIZ / e["archivo"]
        if not ruta.exists():
            error(f"{e['id']}: no existe {e['archivo']}")
            continue
        datos = leer_json(ruta)
        meta = datos.get("cartographer", {})
        if meta.get("aviso") != AVISO_FRONTERAS:
            error(f"{e['id']}: falta el aviso de fronteras aproximadas en el GeoJSON")
        if meta.get("anio") != e["anio"]:
            error(f"{e['id']}: el año del GeoJSON ({meta.get('anio')}) no coincide con el índice ({e['anio']})")
        ids, verificados = set(), 0
        for f in datos["features"]:
            p = f.get("properties", {})
            fid = p.get("id")
            if not fid or fid in ids:
                error(f"{e['id']}: id vacío o repetido ({fid})")
            ids.add(fid)
            if not p.get("nombre_es"):
                error(f"{fid}: falta nombre_es")
            if "nombre_es_verificado" not in p:
                error(f"{fid}: falta nombre_es_verificado")
            verificados += bool(p.get("nombre_es_verificado"))
            if not p.get("licencia") or not p.get("fuente"):
                error(f"{fid}: falta licencia o fuente")
            elif fuentes.get(p["fuente"], {}).get("estado") != "verificada":
                error(f"{fid}: la fuente {p['fuente']} no está verificada")
            if p.get("anio") != e["anio"]:
                error(f"{fid}: año incorrecto")
            g = shape(f["geometry"])
            if g.is_empty or not g.is_valid or g.geom_type not in ("Polygon", "MultiPolygon"):
                error(f"{fid}: geometría inválida ({g.geom_type})")
        if len(ids) != e["entidades"]:
            error(f"{e['id']}: el índice dice {e['entidades']} entidades y hay {len(ids)}")
        pct = 100 * verificados / max(1, len(ids))
        aviso(f"{e['id']}: {verificados}/{len(ids)} nombres en español verificados ({pct:.0f} %); "
              "el resto conserva el nombre original (ver traducciones/pendientes.json)")


CAMPOS_FICHA = ["id", "titulo", "autor", "anio", "fuente", "url", "licencia", "licencia_verificada",
                "uso_en_video", "imagen_original", "metodo", "modo", "calidad", "gcp"]


def validar_mapas():
    for ficha_ruta in sorted((RAIZ / "mapas").glob("*/ficha.json")):
        c = ficha_ruta.parent
        f = leer_json(ficha_ruta)
        nombre = c.name
        for campo in CAMPOS_FICHA:
            if campo not in f:
                error(f"mapa {nombre}: falta el campo '{campo}' en ficha.json")
        if f.get("id") != nombre:
            error(f"mapa {nombre}: el id de la ficha no coincide con la carpeta")
        if not f.get("licencia"):
            error(f"mapa {nombre}: falta licencia")
        if f.get("uso_en_video") != "no" and not f.get("licencia_verificada"):
            error(f"mapa {nombre}: se marca para vídeo sin licencia verificada")
        if f.get("modo") not in ("superpuesto", "decorativo"):
            error(f"mapa {nombre}: modo debe ser 'superpuesto' o 'decorativo'")
        if not (c / f.get("imagen_original", "")).exists():
            error(f"mapa {nombre}: falta la imagen original")
        if f.get("modo") == "superpuesto":
            if len(f.get("gcp", [])) < 5:
                error(f"mapa {nombre}: menos de 5 GCP")
            if "error_medio_km" not in f:
                error(f"mapa {nombre}: sin error_medio_km (ejecuta scripts/georreferenciar.py)")
            if not (c / f.get("salida", {}).get("cog", "-")).exists():
                error(f"mapa {nombre}: falta la salida COG")
            if not (c / f.get("salida", {}).get("vista", "-")).exists():
                error(f"mapa {nombre}: falta la vista ligera")
            if len(f.get("limites", [])) != 4:
                error(f"mapa {nombre}: límites incorrectos")


def validar_paquete():
    cat = RAIZ / "paquetes/cartographer/catalogo.json"
    if not cat.exists():
        aviso("paquete no generado todavía (scripts/empaquetar.py)")
        return
    c = leer_json(cat)
    for e in c.get("epocas", []):
        if not (cat.parent / e["archivo"]).exists():
            error(f"paquete: falta {e['archivo']}")
    for m in c.get("mapas", []):
        if not (cat.parent / m["imagen"]).exists():
            error(f"paquete: falta {m['imagen']}")
        if m.get("uso_en_video") != "no" and not m.get("licencia_verificada"):
            error(f"paquete: el mapa {m['id']} no tiene licencia verificada")


def main():
    fuentes = fuentes_verificadas()
    validar_epocas(fuentes)
    validar_mapas()
    validar_paquete()
    for a in avisos:
        print("AVISO:", a)
    for e in errores[:200]:
        print("ERROR:", e)
    if errores:
        print(f"\n{len(errores)} errores.")
        sys.exit(1)
    print("\nValidación correcta: 0 errores.")


if __name__ == "__main__":
    main()
