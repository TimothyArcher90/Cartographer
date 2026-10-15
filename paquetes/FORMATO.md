# Formato del paquete Cartographer (versión 1)

Carpeta autocontenida: `paquetes/cartographer/`. Electric Eye solo necesita leer este formato.

```
cartographer/
  catalogo.json
  epocas/<id>.geojson
  mapas/<id>.png
  LICENSE-historical-basemaps.txt
```

## catalogo.json

```json
{
  "formato": "cartographer-paquete",
  "version_formato": 1,
  "aviso_fronteras": "Fronteras aproximadas",
  "epocas": [{
    "id": "anio-1000", "anio": 1000, "titulo": "El mundo hacia el año 1000", "nota": null,
    "archivo": "epocas/anio-1000.geojson", "entidades": 132,
    "aviso": "Fronteras aproximadas",
    "fuente": { "id": "historical-basemaps", "nombre": "...", "url": "...", "commit": "..." },
    "licencia": "GPL-3.0"
  }],
  "mapas": [{
    "id": "...", "titulo": "...", "autor": "...", "anio": 1570,
    "imagen": "mapas/<id>.png",
    "esquinas": [[lon,lat],[lon,lat],[lon,lat],[lon,lat]],
    "esquinas_orden": "noroeste, noreste, sureste, suroeste (lon, lat)",
    "error_medio_km": 6.4, "modo": "superpuesto",
    "licencia": "...", "licencia_verificada": true, "uso_en_video": "si|no",
    "url": "...", "calidad": "..."
  }]
}
```

- Rutas relativas a `catalogo.json`.
- `anio` negativo = antes de Cristo.
- La imagen está en Web Mercator (EPSG:3857) y alineada al norte, así que las `esquinas` se pueden
  pasar tal cual a una fuente `image` de MapLibre (`coordinates`).
- **Electric Eye debe ignorar los mapas con `uso_en_video` distinto de `"si"`** y mostrar siempre
  `aviso_fronteras` al usar una época.

## Propiedades de cada entidad (GeoJSON)

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | texto | Estable entre ejecuciones: `<época>-<nombre>` (+ `-2`, `-3` si se repite) |
| `nombre_es` | texto | Nombre a rotular |
| `nombre_es_verificado` | bool | `false` = conserva el nombre original de la fuente |
| `nombre_original` | texto | Nombre en la fuente |
| `soberano` | texto o null | Potencia que ejerce autoridad (útil para colorear por bando) |
| `parte_de` | texto o null | Entidad mayor |
| `anio` | entero | Año de la fuente |
| `precision` | 1, 2, 3 o null | 1 aproximada, 2 moderada, 3 derecho internacional |
| `fuente`, `licencia` | texto | Procedencia |

Cambios incompatibles subirán `version_formato`.
