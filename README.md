# Cartographer

Fronteras de época (Antigüedad, Medievo, Edad Moderna) y mapas antiguos georreferenciados,
listos para usar en vídeo. Proyecto independiente de Electric Eye: lo único que comparten es
el **paquete Cartographer** (`paquetes/cartographer/`), cuyo formato está en
[`paquetes/FORMATO.md`](paquetes/FORMATO.md).

> Regla del proyecto: no se inventan fechas, fronteras, autores ni licencias. Lo que no se ha
> podido comprobar se marca «sin verificar» y no se usa en vídeo. Las fronteras antiguas se
> muestran siempre con el aviso **«Fronteras aproximadas»**.

## Estado de la primera entrega

| Elemento | Estado |
|---|---|
| Época «Imperio romano» | Hecha con el **año 100**. La fuente **no tiene 117** (tiene 100 y 200). |
| Época año 1000 | Hecha (132 entidades). |
| Época año 1492 | Hecha (1317 entidades). |
| Nombres en español | Diccionario verificado en `traducciones/es.json`: 32 % (100), 52 % (1000), 4 % (1492; la mayoría son pueblos indígenas con endónimo, que se deja tal cual). Lo pendiente está en `traducciones/pendientes.json`. |
| Georreferenciación (TPS / polinómica) | Hecha y probada con un mapa **sintético** (error real medio ≈ 6 km en puntos independientes). |
| 2 mapas antiguos reales | **Pendiente.** El entorno donde se construyó no tenía acceso a Wikimedia, LoC, Rumsey ni Gallica. Candidatos en `mapas/candidatos.json` (sin verificar). |
| Visor | Hecho (`visor/`), capturas en `capturas/`. |

## Instalación

Requisitos: Python 3.10+ y Node 18+ (Node solo para las capturas).

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
npm install            # solo para capturas automáticas (Playwright)
```

## Uso rápido

```bash
scripts/comprobar.sh   # todo: épocas, georreferenciado, paquete, validación y capturas
npm run visor          # abre http://localhost:5180/visor/
```

`CAPTURAS=0 scripts/comprobar.sh` se salta las capturas.

## Estructura

| Carpeta | Contenido |
|---|---|
| `fuentes/` | `fuentes.json`: cada fuente con URL, licencia y estado de verificación. Licencia GPL-3.0 de historical-basemaps. `cache/` (no se sube) guarda las descargas. |
| `epocas/` | `config.json` (qué épocas se procesan), GeoJSON normalizados por época e `indice.json`. |
| `traducciones/` | `es.json` (original → español, solo traducciones seguras) y `pendientes.json`. |
| `mapas/<id>/` | `ficha.json`, imagen original y `salida/` (COG + vista ligera). `candidatos.json` con mapas propuestos. |
| `scripts/` | `normalizar_epocas.py`, `georreferenciar.py`, `empaquetar.py`, `validar.py`, `capturas.mjs`, `comprobar.sh`. |
| `visor/` | Visor MapLibre con selector de época y opacidad del mapa antiguo. MapLibre 4.7.1 incluido en `vendor/`. |
| `paquetes/` | Paquete exportable para Electric Eye y su especificación. |
| `pruebas/` | Prueba sintética de georreferenciación. |

## Cómo añadir una época

1. Comprueba que el año existe en la fuente: `fuentes/fuentes.json` → `anios_disponibles_historical_basemaps`
   (lista comprobada en el commit `da7a4b7` de historical-basemaps). Años negativos = a. C.
2. Añade una entrada a `epocas/config.json` (`id`, `anio_fuente`, `titulo` y, si hace falta, `nota`).
3. `python scripts/normalizar_epocas.py` → genera `epocas/<id>.geojson` e `indice.json`.
4. Añade a `traducciones/es.json` las traducciones que estén claras (mira `pendientes.json`) y repite el paso 3.
5. `python scripts/empaquetar.py && python scripts/validar.py`.

Cada entidad lleva: `id` estable (`<época>-<nombre>`), `nombre_original`, `nombre_es`,
`nombre_es_verificado`, `soberano`, `parte_de`, `anio`, `precision` (1 aproximada, 2 moderada,
3 derecho internacional; viene de la fuente), `fuente` y `licencia`. Simplificación por defecto:
0,02° (≈ 2 km), ajustable con `--tolerancia`.

## Cómo añadir un mapa antiguo

1. Busca la imagen en su origen y **comprueba la licencia en la página del archivo**. Solo dominio
   público o licencias que permitan uso comercial en vídeo. Apunta URL, autor, año y licencia.
2. Crea `mapas/<id>/` con la imagen (`original.jpg`/`.png`) y `ficha.json`:

```json
{
  "id": "<id>", "titulo": "...", "autor": "...", "anio": 1570,
  "fuente": "wikimedia-commons", "url": "https://...",
  "licencia": "Dominio público", "licencia_verificada": true, "uso_en_video": "si",
  "imagen_original": "original.jpg",
  "metodo": "tps",
  "modo": "superpuesto",
  "calidad": "media",
  "notas": "...",
  "gcp": [ { "px": 812.5, "py": 403.0, "lon": 12.33, "lat": 45.44, "etiqueta": "Venecia" } ]
}
```

   - `px`, `py`: píxel en la imagen original (origen arriba a la izquierda).
   - `metodo`: `tps` (thin-plate spline; mínimo 5 GCP), `poli1` (afín; mín. 4) o `poli2` (mín. 7).
     Los GCP se pueden sacar con QGIS (Georreferenciador) o con Allmaps (sin verificar desde aquí).
   - `modo`: `superpuesto` o `decorativo`. Los mapas muy deformados (T-O, ptolemaicos) van como
     `decorativo`: imagen con transición, **nunca encima del mapa real**, y no necesitan GCP.
3. `python scripts/georreferenciar.py mapas/<id>` → `salida/mapa.tif` (COG, EPSG:3857),
   `salida/vista.png` (≤ 2048 px) y, en la ficha, `limites`, `error_medio_km` y `error_max_km`.
   El error es validación cruzada dejando un GCP fuera (con TPS el error en los propios GCP sería 0,
   así que ese dato no serviría). Equivalente con la CLI de GDAL:
   `gdal_translate -gcp px py lon lat ... original.jpg tmp.tif && gdalwarp -tps -t_srs EPSG:3857 tmp.tif mapa.tif`.
4. `python scripts/empaquetar.py && python scripts/validar.py`.

## Validaciones (`scripts/validar.py`)

Error (bloquea) si: geometría inválida, id repetido, falta `nombre_es`, falta licencia o fuente,
fuente no verificada, falta el aviso de fronteras aproximadas, mapa para vídeo sin licencia verificada,
mapa superpuesto sin GCP suficientes, sin COG o sin `error_medio_km`. Aviso (no bloquea): porcentaje
de nombres sin traducción verificada.

## Integración con Electric Eye (fase posterior)

No incluida ahora. Plan: en Electric Eye, una fuente raster `image` con las 4 esquinas del catálogo y
opacidad animada, y un selector de épocas que lea `catalogo.json`. Ver `paquetes/FORMATO.md`.

## Licencias

Ver [LICENCIAS.md](LICENCIAS.md). Los datos de fronteras derivan de historical-basemaps (GPL-3.0).
