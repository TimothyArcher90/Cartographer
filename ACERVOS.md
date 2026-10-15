# Acervos de mapas históricos

Guía de dónde conseguir **mapas históricos reales** (escaneos de originales conservados en archivos y
bibliotecas) y en qué condiciones se pueden usar en vídeo.

**Regla de Cartographer:** solo se incluyen mapas históricos reales. Nada sintético, reconstruido ni
dibujado por nosotros. Cada mapa debe tener su ficha con URL, autor, año, institución y licencia
**comprobada en la página del propio archivo**. Si algo no se puede comprobar, se marca «sin verificar»
y no se usa en vídeo.

## Cómo se ha verificado esta tabla

- Revisado el **2026-10-15** mediante búsqueda web. El entorno de desarrollo no podía abrir las webs de
  los archivos, así que **ninguna condición se ha leído directamente en la página oficial**. Se resume
  lo que dicen los resultados de búsqueda y se cita su origen.
- Las condiciones cambian. Antes de usar una imagen, hay que confirmarlo en el registro del ítem.
- No soy abogado. Ojo: «dominio público en EE. UU.» no garantiza lo mismo en otros países.

## Resumen: ¿sirve para un vídeo con fines comerciales?

| Acervo | Condiciones según la búsqueda | ¿Uso comercial? | Fiabilidad del dato |
|---|---|---|---|
| **NYPL Digital Collections** (Lionel Pincus & Princess Firyal Map Division) | Más de 20 000 mapas publicados en 2014; sin restricciones de copyright conocidas en EE. UU.; reproducciones con CC0 1.0. Atribución opcional. | **Sí** | Media: notas de prensa y blogs de 2014; confirmar en cada ítem |
| **Biblioteca Nacional de España** (Biblioteca Digital Hispánica) | Imágenes de obras en dominio público con CC BY 4.0; tasa por uso comercial suprimida desde el 1-11-2020. Hay que citar a la BNE y no usar su logo. | **Sí, con atribución** | Media: documento de la BNE y prensa; aviso legal actual sin confirmar |
| **John Carter Brown Library** (Brown University) | CC BY 4.0 en todo su acervo digital; uso comercial permitido; atribución «Courtesy of the John Carter Brown Library». | **Sí, con atribución** | Alta: página de permisos de la propia JCB |
| **Rijksmuseum** (Rijksstudio) | Imágenes de dominio público con CC0 1.0 (información de 2021). | **Sí** | Media: prensa de 2021 |
| **Yale** (Beinecke y otras colecciones) | Política de acceso abierto de 2011: imágenes de dominio público sin licencia ni limitaciones de uso. | **Probablemente sí** | Baja-media: fuentes de 2011-2012 |
| **Library of Congress** (Geography and Map Division) | La LoC no conoce restricciones de copyright en EE. UU. para estos mapas (sobre todo anteriores a 1922 u oficiales). El usuario debe comprobar cada caso. | **Normalmente sí; revisar cada ítem** | Media |
| **Leventhal Map Center** (Boston Public Library) | Mapas anteriores a 1923 presentados como «sin copyright conocido»; atribución de cortesía. | **Probablemente sí** | Baja: fuentes indirectas |
| **British Library** (Flickr Commons) | Más de un millón de imágenes de libros de los siglos XVII-XIX, con al menos 50 000 mapas; CC0 o «No known copyright restrictions» según el ítem. | **Sí, revisando cada imagen** | Media: fuentes de 2013-2015 |
| **Wikimedia Commons** | Reproducciones fieles de obras 2D de dominio público = dominio público (política PD-Art). La obra original debe ser de dominio público en EE. UU. y en su país de origen. | **Sí, según la etiqueta de cada archivo** | Alta: páginas de política de Commons |
| **David Rumsey Map Collection** (Stanford) | CC BY-NC-SA 3.0; para uso comercial, pedir permiso a rumseymapcenter@stanford.edu. | **No, salvo permiso** | Alta: registros de Stanford |
| **Bodleian Libraries** (Digital Bodleian) | La mayoría de las imágenes son CC BY-NC 4.0; para uso comercial hace falta licencia de pago. | **No, salvo licencia** | Alta: página de condiciones de Digital Bodleian |
| **Gallica** (BnF) | Reutilización no comercial gratuita citando la fuente; la comercial requiere licencia y pago. | **No, salvo licencia** | Media: condiciones citadas por terceros; tarifas actuales sin ver |
| **Biblioteca Apostólica Vaticana** | Reproducciones profesionales con licencia, crédito © obligatorio y marca de agua. | **Solo con licencia** | Media |
| **National Library of Scotland** (maps.nls.uk) | Licencia distinta según el mapa: unos CC BY (comercial sí) y otros CC BY-NC-SA (no). | **Depende del mapa** | Media |
| **IGN España** (Cartoteca histórica) | No se ha encontrado la licencia de la cartoteca histórica; CC BY 4.0 consta solo para productos actuales. | **Sin verificar** | — |
| **Europeana** (agregador) | Cada objeto lleva su declaración de derechos; existe un filtro «¿puedo usarlo?». | **Depende del objeto** | Media |
| **Old Maps Online** (buscador) | Portal gratuito que busca por lugar y fecha en muchos archivos y enlaza al archivo de origen. Las condiciones son las del archivo de cada mapa. | **Depende del archivo** | Media |
| **Allmaps** (herramienta) | Herramienta libre de código abierto para georreferenciar mapas IIIF en el navegador. Sus datos de georreferencia se publican con licencia abierta. | Herramienta, no acervo | Media: web del proyecto y del IIIF |

Sin evaluar todavía (pendientes): Internet Archive, Smithsonian Open Access, Harvard Map Collection,
Princeton (maps.princeton.edu), Archivo General de Indias / PARES, Real Academia de la Historia,
Biblioteca Virtual del Patrimonio Bibliográfico, e-rara (Suiza), Biblioteca Digital Mundial (ahora en la
LoC), Huntington Library, Osher Map Library, Bayerische Staatsbibliothek, Österreichische
Nationalbibliothek, Biblioteca Nacional de Portugal y Biblioteca Nacional de Brasil.

## Orden de prioridad para buscar un mapa

1. **NYPL, BNE, John Carter Brown, Rijksmuseum, Library of Congress y Wikimedia Commons** (con su
   etiqueta de dominio público): permiten uso comercial.
2. **Old Maps Online** y **Europeana** para localizar el mapa; luego se comprueba la licencia en el archivo de origen.
3. **Rumsey, Bodleian, Gallica y la Vaticana** solo con permiso o licencia por escrito, guardada en la ficha.

## Tipos de mapa y cómo usarlos

| Época y tipo | Ejemplos conocidos | Georreferenciable | Modo en Cartographer |
|---|---|---|---|
| Antigüedad (copias medievales o renacentistas) | Tabula Peutingeriana; mapas ptolemaicos | Mal: proyección y escala muy distorsionadas | `decorativo` |
| Mapamundis medievales | T-O, Hereford, Ebstorf | No | `decorativo` |
| Portulanos (siglos XIII-XVI) | Carta Pisana; portulanos mallorquines y genoveses | Sí, por regiones (costas bastante fieles) | `superpuesto` por recortes regionales |
| Mapamundis renacentistas | Waldseemüller (1507); Ortelius (1570); Mercator | Parcialmente, con muchos GCP y por regiones | `superpuesto` o `decorativo` |
| Siglos XVII-XIX | Atlas nacionales, mapas militares y catastrales | Bien | `superpuesto` |

Los ejemplos son obras conocidas, pero **en qué archivo está cada copia y con qué licencia está sin
verificar**: hay que confirmarlo antes de crear la ficha.

## Pasos para incorporar un mapa real

1. Localiza el mapa (Old Maps Online, Europeana o el catálogo del archivo).
2. Abre el registro del ítem y copia: título, autor o cartógrafo, año, institución, signatura, URL y
   declaración de derechos **literal**.
3. Si la licencia permite uso comercial, descarga la imagen de mayor resolución que ofrezca.
4. Crea `mapas/<id>/ficha.json` (formato en el README) con `licencia_verificada: true` y la licencia literal en `notas`.
5. Pon los GCP (QGIS Georreferenciador o Allmaps) y ejecuta `scripts/georreferenciar.py`.
6. `scripts/validar.py`: si falta URL, autor, año o licencia verificada, la validación falla.

## Fuentes de esta tabla (resultados de búsqueda del 2026-10-15)

- NYPL: https://publicdomainreview.org/collection/highlights-from-the-20000-maps-made-freely-available-online-by-new-york-public-library/ · https://openglam.org/?p=2680
- BNE: https://www.bne.es/sites/default/files/repositorio-archivos/procedimiento_normas_reproduccion.pdf · https://www.xataka.com/legislacion-y-derechos/bne-libera-25-millones-digitalizaciones-obras-dominio-publico-se-podran-usar-gratis-incluso-para-fines-comerciales
- John Carter Brown: https://americana.jcblibrary.org/permissions/ · https://jcblibrary.org/node/1755
- Rijksmuseum: https://www.ianvisits.co.uk/blog/2021/01/21/over-700000-paintings-from-the-rijksmuseum-online-copyright-free/
- Yale: https://news.yale.edu/2011/05/10/digital-images-yale-s-vast-cultural-collections-now-available-free
- Library of Congress: https://www.loc.gov/item/90680842/
- Leventhal: https://serc.carleton.edu/details/images/148237.html · https://publicdomainreview.org/collections/source/nlmec/
- British Library: https://www.glbtrt.ala.org/news/archives/433 · https://hyperorg.com/2015/08/11/1m-copyright-free-images-ready-for-viewing-and-tagging/
- Wikimedia Commons: https://commons.wikimedia.org/wiki/Commons:When_to_use_the_PD-Art_tag
- David Rumsey: https://purl.stanford.edu/xh235dd9059
- Bodleian: https://digital.bodleian.ox.ac.uk/terms/
- Gallica: https://linuxfr.org/users/pamputt/journaux/conditions-d-utilisation-des-contenus-de-gallica · https://questions.assemblee-nationale.fr/dyn/14/questions/QANR5L14QE23878.pdf
- Vaticana: https://bav.vatican.va/en/information-readers/fotoriproduzione-uso-professionale.html?n=1
- National Library of Scotland: https://maps.nls.uk/copyright.html
- IGN: https://historylab.es/es/cartoteca-del-instituto-geografico-nacional-ign/ · https://datos.gob.es/en/aplicaciones/iberpix
- Europeana: https://europeana.atlassian.net/wiki/spaces/EF/pages/1532592129/How+do+I+choose+a+rights+statement+when+submitting+data+to+Europeana
- Old Maps Online: https://community.oldmapsonline.org/ar/maps/about-oldmapsonline · https://www.davidrumsey.com/blog/2016/7/4/old-maps-online-historical-maps-search-portal
- Allmaps: https://allmaps.org/ · https://iiif.io/news/2023/05/15/georef-extension-published/
- Pleiades (lugares; CC BY 3.0 según sus páginas de lugar): https://pleiades.stoa.org/places/140517/14-g3-no-86 · https://zenodo.org/records/8206033/latest
- DARE (teselas; CC BY, versión sin confirmar): https://wiki.digitalclassicist.org/Digital_Atlas_of_the_Roman_Empire
