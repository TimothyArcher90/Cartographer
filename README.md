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
| Georreferenciación (TPS / polinómica) | Código probado con una prueba interna sintética (`pruebas/`, error real medio ≈ 6 km). Esa prueba **no es un mapa** y nunca entra en `mapas/`, el paquete ni el visor. |
| Mapas antiguos | **9 mapas históricos reales** (escaneos de originales), licencia verificada en la API oficial de Wikimedia Commons. 2 georreferenciados encima del mapa actual y 7 decorativos. Tabla abajo. |
| Visor | Hecho (`visor/`), capturas en `capturas/`. |

## Mapas históricos incluidos

| Mapa | Autor (según Commons) | Año | Modo | Error medio (km) | Licencia (Commons) | Origen |
|---|---|---|---|---|---|---|
| Atlas catalán de Cresques Abraham (1375) | Cresques Abraham | 1375 | decorativo | — | Public domain | [Commons](https://commons.wikimedia.org/wiki/File:1375_Atlas_Catalan_Abraham_Cresques.jpg) |
| Carta de Juan de la Cosa (1500) | Juan de la Cosa | 1500 | decorativo | — | Public domain | [Commons](https://commons.wikimedia.org/wiki/File:1500_map_by_Juan_de_la_Cosa_rotated.jpg) |
| Mapa T-O de las Etimologías de Isidoro (impresión de Günther Zainer, 1472) | Isidore of Seville | 1472 | decorativo | — | Public domain | [Commons](https://commons.wikimedia.org/wiki/File:T_and_O_map_Guntherus_Ziner_1472.jpg) |
| Mappa mundi de Hereford (hacia 1300) | Richard of Haldingham | 1300 (aprox.) | decorativo | — | Public domain | [Commons](https://commons.wikimedia.org/wiki/File:Hereford_Mappa_Mundi.jpg) |
| Abraham Ortelius, «Romani Imperii Imago» | Abraham Ortelius | 1603 | superpuesto | 85.22 | Public domain | [Commons](https://commons.wikimedia.org/wiki/File:Romani_Imperii_Imago.jpg) |
| Abraham Ortelius, «Typus Orbis Terrarum» (1570) | Abraham Ortelius | 1570 | decorativo | — | Public domain | [Commons](https://commons.wikimedia.org/wiki/File:1570_Typus_Ortelius_cropped.jpg) |
| Carta portulana del Mediterráneo y Europa (1590) | Joan Riezo figlo de mastro dominico [Olives] in missina año  | 1590 | superpuesto | 66.92 | Public domain | [Commons](https://commons.wikimedia.org/wiki/File:1590_Portolan_chart_of_the_Mediterranean_Sea_and_Europe.png) |
| Carta portulana del Mediterráneo (siglo XIV) | anonymous, probably Genoan | 1320 (aprox.) | decorativo | — | Public domain | [Commons](https://commons.wikimedia.org/wiki/File:Mediterranean_chart_fourteenth_century2.jpg) |
| Tabula Peutingeriana, segmento 1 (copia medieval, ÖNB) | Unknown authorUnknown author Peutinger, Konrad (1465-1547) | 1150 (aprox.) | decorativo | — | Public domain | [Commons](https://commons.wikimedia.org/wiki/File:Tabula_Peutingeriana_(%C3%96NB)_01-Rodez-Lyon.jpg) |

Los errores (validación cruzada dejando un punto fuera) reflejan sobre todo la inexactitud del propio mapa antiguo. Los mapas decorativos (mapamundis medievales, Tabula Peutingeriana, etc.) no se pueden superponer a la geografía real: se usan como imagen con transición.

**Cómo llegan las imágenes:** el flujo `.github/workflows/acervos.yml` corre en GitHub Actions, busca en Commons (`scripts/buscar_commons.py`) y descarga los mapas con ficha (`scripts/descargar_mapas.py`). Solo baja la imagen si la licencia oficial permite uso comercial, y guarda en la ficha (campo `commons`) la licencia, autor, fecha y crédito literales.

## Catálogo de todos los mapas libres

Además de los mapas ya procesados (`mapas/`), Cartographer mantiene un **catálogo masivo** de mapas
antiguos de licencia libre de varios acervos, que se rastrea solo en GitHub Actions:

| Fuente | Qué aporta | Cómo se decide si es libre |
|---|---|---|
| Wikimedia Commons (`scripts/catalogar_commons.py`) | Árbol de categorías «Old maps», portulanos, Ptolomeo, mappae mundi… con lugar y siglo deducidos de las categorías | Licencia oficial de cada archivo; se descartan NC/ND |
| OpenGeoMetadata (`scripts/acervos.py ogm`) | Catálogos de mapas escaneados de muchas bibliotecas universitarias (Stanford, Princeton, Harvard…), **con coordenadas de cobertura** e IIIF | Licencia o derechos declarados; o anterior a 1900 sin restricciones (inferido) |
| Library of Congress (`acervos.py loc`) | Colección de mapas de la LoC | La LoC indica que, en general, no conoce restricciones; **comprobar el registro** |
| Internet Archive (`acervos.py ia`) | Mapas y atlas escaneados | Licencia declarada; o anterior a 1900 sin restricciones (inferido) |
| Europeana (`acervos.py europeana`) | Agregador de archivos europeos | Filtro oficial «reutilización abierta» + declaración de derechos |
| Digital Commonwealth (`acervos.py dc`) | Bibliotecas de Massachusetts, incluido el Leventhal Map Center (Boston) | Derechos declarados; o anterior a 1900 sin restricciones (inferido) |
| Allmaps (`acervos.py allmaps`) | Mapas de muchas bibliotecas **georreferenciados por la comunidad** (contorno real sobre el terreno) | La georreferencia es abierta; la imagen conserva la licencia de su institución (verificar) |
| Biblioteca Nacional de España (`acervos.py bne`) | Conjunto «Material cartográfico» de datos.gob.es | **Bloqueado**: el servidor de la BNE rechaza las descargas automáticas desde GitHub (error 403). Pendiente de otra vía |

- Resultado: `catalogo/indice/` → `mapas-NNN.jsonl.gz` (un mapa por línea), `lugares.json` y `resumen.json` (totales por fuente, siglo y licencia).
- Las imágenes **no** se guardan en el repositorio (serían terabytes): cada registro tiene enlace, miniatura e IIIF cuando existe. Para usar un mapa en vídeo se crea su ficha en `mapas/` y se descarga.
- Las licencias marcadas «inferido, verificar» deben revisarse en el registro original antes de publicar.
- Lanzar: Actions → «Catálogo de mapas libres» (todas) o «Catálogo (una fuente)». Se relanzan solos hasta terminar.

### Buscar mapas de un lugar

```bash
python scripts/buscar_lugar.py "Turquía"                  # todos los siglos
python scripts/buscar_lugar.py "Turquía" --siglo 16
python scripts/buscar_lugar.py "Imperio otomano" --desde 1500 --hasta 1700
```

Amplía la consulta con `catalogo/alias_es.json` (Turquía → Turkey, Anatolia, Asia Minor, Natolia,
Ottoman Empire, Constantinople…) y, para los mapas con coordenadas, también busca por cobertura
geográfica. Genera `salidas/busquedas/<lugar>.html` (galería) y `.json`.

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
| `pruebas/` | Prueba interna del código de georreferenciación (sintética; no se publica). |

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
