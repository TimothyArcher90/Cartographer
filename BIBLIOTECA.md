# Biblioteca de Cartographer

Documento generado por `scripts/comprender.py`. No editar a mano.

- Mapas analizados: **207,288** · con país asignado: **192,604** · sin país: 14,684
  (sobre todo mapamundis, cartas oceánicas o registros sin datos de lugar).
- Países con mapas: **217**.
- Tipos: topográfico 188,310, general 14,835, mapamundi 1,201, ferroviario/viario 922, histórico/temático 837, plano urbano 524, militar 324, carta náutica 243, ptolemaico 77, portulano 15.
- Escalas: local o ciudad 181,232, desconocida 14,514, provincia o comarca 6,794, región o país 2,454, continente 1,221, mundo 1,073.

Cómo se asigna un país: por **nombre** actual (25+ idiomas, Natural Earth), por **nombre histórico**
(`catalogo/nombres_historicos.json`) o por **coordenadas** de la cobertura del mapa. Cada mapa guarda
la vía en el campo `via`; las asignaciones por coordenadas de mapas grandes pueden incluir países
vecinos. Los siglos salen del año de los metadatos de cada archivo y pueden tener errores puntuales.

Mapas de un país: `catalogo/biblioteca/paises/<ISO3>.jsonl.gz` o
`python scripts/buscar_lugar.py "<país>"`.

| País | ISO | Total | Antes del s. IX | IX | X | XI | XII | XIII | XIV | XV | XVI | XVII | XVIII | XIX | XX |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Afganistán | AFG | 72 |  |  |  |  |  |  |  |  | 18 | 3 | 4 | 36 | 11 |
| Albania | ALB | 82 |  |  |  |  |  |  |  |  | 18 | 17 | 7 | 29 | 11 |
| Alemania | DEU | 755 | 1 |  |  |  |  |  |  |  | 71 | 58 | 94 | 285 | 241 |
| Angola | AGO | 50 |  |  |  |  |  |  |  |  | 1 | 5 | 8 | 11 | 9 |
| Anguila | AIA | 1 |  |  |  |  |  |  |  |  |  |  |  | 1 |  |
| Antártida | ATA | 14 |  |  |  |  |  |  |  |  |  | 2 | 1 | 6 | 5 |
| Arabia Saudita | SAU | 182 |  |  |  |  |  |  |  | 1 | 27 | 20 | 12 | 46 | 73 |
| Argelia | DZA | 95 |  |  |  |  |  |  |  |  | 14 | 13 | 6 | 33 | 26 |
| Argentina | ARG | 89 |  |  |  |  |  |  |  |  | 2 | 20 | 20 | 34 | 11 |
| Armenia | ARM | 28 |  |  |  |  |  |  |  |  | 7 | 3 | 3 | 12 | 2 |
| Aruba | ABW | 23 |  |  |  |  |  |  |  |  |  | 1 | 1 | 13 | 8 |
| Australia | AUS | 84 |  |  |  |  |  |  |  |  |  | 1 | 3 | 46 | 31 |
| Austria | AUT | 342 | 1 |  |  |  |  |  |  |  | 27 | 15 | 21 | 124 | 152 |
| Azerbaiyán | AZE | 35 |  |  |  |  |  |  |  |  | 6 | 2 | 3 | 19 | 5 |
| Bahamas | BHS | 11 |  |  |  |  |  |  |  |  |  |  | 2 | 9 |  |
| Bangladés | BGD | 18 |  |  |  |  |  |  |  | 1 | 1 | 3 | 2 | 5 | 4 |
| Barbados | BRB | 1 |  |  |  |  |  |  |  |  |  |  |  | 1 |  |
| Belice | BLZ | 6 |  |  |  |  |  |  |  |  |  |  |  | 3 | 3 |
| Benín | BEN | 14 |  |  |  |  |  |  |  |  | 2 | 5 |  | 2 | 5 |
| Bermudas | BMU | 2 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |
| Bielorrusia | BLR | 66 |  |  |  |  |  |  |  |  | 15 | 10 | 10 | 7 | 24 |
| Birmania | MMR | 61 |  |  |  |  |  |  |  |  | 6 | 4 | 8 | 23 | 18 |
| Bolivia | BOL | 53 |  |  |  |  |  |  |  |  | 5 | 6 | 6 | 27 | 9 |
| Bosnia y Herzegovina | BIH | 146 |  |  |  |  |  |  |  |  | 29 | 8 | 12 | 75 | 22 |
| Botsuana | BWA | 95 |  |  |  |  |  |  |  |  | 1 | 1 | 6 | 36 | 32 |
| Brasil | BRA | 159 |  |  |  |  |  |  |  |  | 7 | 32 | 28 | 67 | 21 |
| Bulgaria | BGR | 117 |  |  |  |  |  |  |  |  | 16 | 11 | 21 | 46 | 22 |
| Burkina Faso | BFA | 24 |  |  |  |  |  |  |  |  | 1 | 5 | 3 | 7 | 5 |
| Burundi | BDI | 4 |  |  |  |  |  |  |  |  |  |  |  | 2 | 2 |
| Bután | BTN | 8 |  |  |  |  |  |  |  |  |  |  | 1 | 6 | 1 |
| Bélgica | BEL | 241 |  |  |  |  |  |  |  |  | 36 | 42 | 35 | 69 | 58 |
| Cabo Verde | CPV | 9 |  |  |  |  |  |  |  |  | 1 | 1 | 3 | 1 |  |
| Camboya | KHM | 18 |  |  |  |  |  |  |  |  |  | 1 |  | 3 | 14 |
| Camerún | CMR | 52 |  |  |  |  |  |  |  |  |  | 4 | 6 | 6 | 29 |
| Canadá | CAN | 2,018 |  |  |  |  |  |  |  |  | 7 | 39 | 173 | 513 | 1,274 |
| Catar | QAT | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Chad | TCD | 39 |  |  |  |  |  |  |  |  |  | 1 | 4 | 7 | 24 |
| Chile | CHL | 96 |  |  |  |  |  |  |  |  | 2 | 28 | 24 | 36 | 6 |
| China | CHN | 466 |  |  |  |  | 1 |  |  | 1 | 14 | 50 | 26 | 93 | 265 |
| Chipre | CYP | 26 |  |  |  |  |  |  |  |  | 9 | 10 | 5 | 1 | 1 |
| Ciudad del Vaticano | VAT | 2 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |
| Colombia | COL | 65 |  |  |  |  |  |  |  |  | 5 | 8 | 8 | 37 | 6 |
| Comoras | COM | 3 |  |  |  |  |  |  |  |  |  |  |  | 2 | 1 |
| Corea del Norte | PRK | 51 |  |  |  |  |  |  |  |  |  | 4 | 1 | 5 | 36 |
| Corea del Sur | KOR | 68 |  |  |  |  |  |  |  |  |  | 5 | 8 | 6 | 41 |
| Costa Rica | CRI | 30 |  |  |  |  |  |  |  |  |  | 14 | 7 | 2 | 5 |
| Costa de Marfil | CIV | 36 |  |  |  |  |  |  |  |  | 1 | 4 | 8 | 9 | 11 |
| Croacia | HRV | 189 |  |  |  |  |  |  |  |  | 33 | 11 | 15 | 101 | 29 |
| Cuba | CUB | 35 |  |  |  |  |  |  |  |  | 5 | 2 | 8 | 17 | 2 |
| Curazao | CUW | 10 |  |  |  |  |  |  |  |  |  | 1 | 2 | 4 | 2 |
| Dinamarca | DNK | 31 |  |  |  |  |  |  |  |  | 6 | 7 |  | 11 | 7 |
| Ecuador | ECU | 53 |  |  |  |  |  |  |  |  | 5 | 5 | 7 | 31 | 3 |
| Egipto | EGY | 208 |  |  |  |  |  |  |  | 1 | 35 | 25 | 22 | 101 | 18 |
| El Salvador | SLV | 10 |  |  |  |  |  |  |  |  |  |  | 1 | 3 | 6 |
| Emiratos Árabes Unidos | ARE | 3 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |
| Eritrea | ERI | 33 |  |  |  |  |  |  |  |  | 1 | 5 | 1 | 13 | 11 |
| Eslovaquia | SVK | 143 |  |  |  |  |  |  |  |  | 10 | 5 | 10 | 77 | 41 |
| Eslovenia | SVN | 127 |  |  |  |  |  |  |  |  | 16 | 2 | 1 | 9 | 98 |
| España | ESP | 257 |  |  |  |  |  |  |  | 1 | 54 | 46 | 68 | 74 | 10 |
| Estados Federados de Micronesia | FSM | 27 |  |  |  |  |  |  |  |  |  |  |  |  | 22 |
| Estados Unidos | USA | 183,866 | 3 |  |  |  |  |  |  |  | 7 | 94 | 312 | 11,144 | 169,917 |
| Estonia | EST | 14 |  |  |  |  |  |  |  |  | 1 | 7 | 1 | 1 | 4 |
| Etiopía | ETH | 162 |  |  |  |  |  |  |  | 1 | 8 | 10 | 3 | 23 | 102 |
| Filipinas | PHL | 68 |  |  |  |  |  |  |  |  | 1 | 4 | 5 | 5 | 49 |
| Finlandia | FIN | 45 |  |  |  |  |  |  |  |  | 6 | 10 | 6 | 8 | 14 |
| Fiyi | FJI | 6 |  |  |  |  |  |  |  |  |  |  |  |  | 6 |
| Francia | FRA | 701 |  |  |  |  |  |  |  |  | 101 | 73 | 169 | 236 | 116 |
| Gabón | GAB | 29 |  |  |  |  |  |  |  |  |  | 4 | 6 | 5 | 10 |
| Gambia | GMB | 12 |  |  |  |  |  |  |  |  |  |  | 4 | 3 | 5 |
| Georgia | GEO | 55 |  |  |  |  |  |  |  |  | 7 | 3 | 4 | 15 | 26 |
| Ghana | GHA | 28 |  |  |  |  |  |  |  |  | 1 | 5 | 7 | 8 | 7 |
| Granada | GRD | 4 |  |  |  |  |  |  |  |  |  | 1 | 1 |  | 2 |
| Grecia | GRC | 306 |  |  |  |  |  |  |  | 1 | 62 | 60 | 54 | 105 | 24 |
| Groenlandia | GRL | 19 |  |  |  |  |  |  | 1 |  | 3 | 4 | 1 | 7 | 3 |
| Guam | GUM | 12 |  |  |  |  |  |  |  |  |  |  |  |  | 2 |
| Guatemala | GTM | 38 |  |  |  |  |  |  |  |  |  | 16 | 7 | 6 | 9 |
| Guernsey | GGY | 6 |  |  |  |  |  |  |  |  |  | 4 |  | 2 |  |
| Guinea | GIN | 40 |  |  |  |  |  |  |  |  | 1 | 4 | 12 | 8 | 12 |
| Guinea Ecuatorial | GNQ | 5 |  |  |  |  |  |  |  |  |  |  |  | 2 | 2 |
| Guinea-Bisáu | GNB | 3 |  |  |  |  |  |  |  |  |  |  |  | 1 | 2 |
| Guyana | GUY | 33 |  |  |  |  |  |  |  |  | 1 | 7 | 5 | 15 | 5 |
| Haití | HTI | 12 |  |  |  |  |  |  |  |  | 2 | 2 | 5 | 3 |  |
| Honduras | HND | 31 |  |  |  |  |  |  |  |  |  | 15 | 6 | 3 | 7 |
| Hong Kong | HKG | 7 |  |  |  |  |  |  |  |  |  |  |  | 1 | 6 |
| Hungría | HUN | 223 |  |  |  |  |  |  |  |  | 28 | 9 | 21 | 111 | 54 |
| India | IND | 203 |  |  |  |  |  |  |  | 1 | 33 | 16 | 46 | 71 | 25 |
| Indonesia | IDN | 126 | 1 |  |  |  |  |  |  |  | 6 | 10 | 18 | 11 | 75 |
| Irak | IRQ | 143 |  |  |  |  |  |  |  |  | 20 | 8 | 40 | 59 | 15 |
| Irlanda | IRL | 300 |  |  |  |  |  |  |  |  | 19 | 22 | 22 | 231 | 6 |
| Irán | IRN | 139 |  |  |  |  |  |  |  |  | 29 | 12 | 10 | 69 | 14 |
| Isla Norfolk | NFK | 6 |  |  |  |  |  |  |  |  |  |  |  | 6 |  |
| Isla Santa Elena | SHN | 6 |  |  |  |  |  |  |  |  | 1 |  |  | 4 | 1 |
| Isla de Man | IMN | 3 |  |  |  |  |  |  |  |  |  |  |  | 3 |  |
| Islandia | ISL | 15 |  |  |  |  |  |  |  |  | 2 | 3 | 4 | 5 | 1 |
| Islas Georgias del Sur y Sandwich del Sur | SGS | 2 |  |  |  |  |  |  |  |  |  |  |  |  | 1 |
| Islas Malvinas | FLK | 3 |  |  |  |  |  |  |  |  |  |  | 2 | 1 |  |
| Islas Marianas del Norte | MNP | 17 |  |  |  |  |  |  |  |  |  |  |  |  | 17 |
| Islas Marshall | MHL | 6 |  |  |  |  |  |  |  |  |  |  |  |  | 6 |
| Islas Pitcairn | PCN | 1 |  |  |  |  |  |  |  |  |  |  | 1 |  |  |
| Islas Salomón | SLB | 11 |  |  |  |  |  |  |  |  | 1 | 2 | 1 |  | 7 |
| Islas Vírgenes Británicas | VGB | 1 |  |  |  |  |  |  |  |  |  |  |  |  | 1 |
| Islas Vírgenes de los Estados Unidos | VIR | 29 |  |  |  |  |  |  |  |  |  |  |  |  | 29 |
| Israel | ISR | 263 |  |  |  |  |  |  |  | 2 | 40 | 29 | 21 | 162 | 7 |
| Italia | ITA | 671 | 1 |  |  |  |  |  |  |  | 148 | 118 | 68 | 172 | 150 |
| Jamaica | JAM | 19 |  |  |  |  |  |  |  |  |  | 2 | 5 | 11 | 1 |
| Japón | JPN | 261 |  |  |  |  |  |  |  |  | 1 | 14 | 12 | 45 | 173 |
| Jersey | JEY | 4 |  |  |  |  |  |  |  |  |  | 4 |  |  |  |
| Jordania | JOR | 228 |  |  |  |  |  |  |  |  | 34 | 16 | 21 | 137 | 20 |
| Kazajistán | KAZ | 38 |  |  |  |  |  |  |  |  | 8 | 8 | 2 | 15 | 5 |
| Kenia | KEN | 117 |  |  |  |  |  |  |  |  | 1 | 3 | 1 | 13 | 89 |
| Kirguistán | KGZ | 21 |  |  |  |  |  |  |  |  | 6 | 2 |  | 8 | 5 |
| Kiribati | KIR | 4 |  |  |  |  |  |  |  |  |  |  |  |  | 4 |
| Kosovo | KOS | 12 |  |  |  |  |  |  |  |  | 1 | 1 | 1 |  | 6 |
| Laos | LAO | 23 |  |  |  |  |  |  |  |  | 1 |  |  | 6 | 16 |
| Lesoto | LSO | 73 |  |  |  |  |  |  |  |  |  |  | 1 | 9 | 63 |
| Letonia | LVA | 28 |  |  |  |  |  |  |  |  | 6 | 5 | 3 | 4 | 10 |
| Liberia | LBR | 39 |  |  |  |  |  |  |  |  | 1 | 1 | 1 | 12 | 24 |
| Libia | LBY | 108 |  |  |  |  |  |  |  | 2 | 16 | 11 | 6 | 22 | 47 |
| Liechtenstein | LIE | 2 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |
| Lituania | LTU | 47 |  |  |  |  |  |  |  |  | 7 | 7 | 3 | 7 | 23 |
| Luxemburgo | LUX | 36 |  |  |  |  |  |  |  |  | 6 | 6 | 4 | 9 | 11 |
| Líbano | LBN | 130 |  |  |  |  |  |  |  |  | 16 | 3 | 8 | 98 | 3 |
| Macao | MAC | 1 |  |  |  |  |  |  |  |  |  |  | 1 |  |  |
| Macedonia del Norte | MKD | 51 |  |  |  |  |  |  |  |  | 11 | 11 | 4 | 15 | 10 |
| Madagascar | MDG | 88 |  |  |  |  |  |  |  |  | 2 | 2 | 7 | 24 | 35 |
| Malasia | MYS | 35 |  |  |  |  |  |  |  |  | 1 | 3 | 2 | 7 | 21 |
| Malaui | MWI | 30 |  |  |  |  |  |  |  |  | 1 |  | 2 | 13 | 14 |
| Maldivas | MDV | 2 |  |  |  |  |  |  |  |  |  |  | 1 |  | 1 |
| Malta | MLT | 29 |  |  |  |  |  |  |  |  | 8 | 10 | 5 | 5 | 1 |
| Malí | MLI | 29 |  |  |  |  |  |  |  |  | 1 | 3 | 5 | 10 | 6 |
| Marruecos | MAR | 64 |  |  |  |  |  |  |  |  | 9 | 9 | 9 | 16 | 19 |
| Mauricio | MUS | 6 |  |  |  |  |  |  |  |  |  |  |  | 5 | 1 |
| Mauritania | MRT | 28 |  |  |  |  |  |  |  |  | 3 | 2 | 7 | 9 | 4 |
| Moldavia | MDA | 25 |  |  |  |  |  |  |  |  | 2 | 1 | 7 | 9 | 6 |
| Mongolia | MNG | 29 |  |  |  |  |  |  |  |  | 1 | 6 | 2 | 4 | 14 |
| Montenegro | MNE | 23 |  |  |  |  |  |  |  |  | 6 | 6 | 1 | 4 | 6 |
| Mozambique | MOZ | 87 |  |  |  |  |  |  |  |  | 3 | 3 | 5 | 30 | 21 |
| México | MEX | 1,103 |  |  |  |  |  |  |  |  | 13 | 41 | 49 | 162 | 813 |
| Mónaco | MCO | 2 |  |  |  |  |  |  |  |  |  |  | 1 | 1 |  |
| Namibia | NAM | 75 |  |  |  |  |  |  |  |  | 1 | 1 | 6 | 31 | 17 |
| Nauru | NRU | 2 |  |  |  |  |  |  |  |  |  |  |  |  | 2 |
| Nepal | NPL | 12 |  |  |  |  |  |  |  | 1 | 1 | 1 |  | 5 | 2 |
| Nicaragua | NIC | 31 |  |  |  |  |  |  |  |  |  | 14 | 7 | 5 | 5 |
| Nigeria | NGA | 53 |  |  |  |  |  |  |  |  | 1 | 5 | 6 | 7 | 29 |
| Noruega | NOR | 32 |  |  |  |  |  |  |  |  |  | 8 | 3 | 9 | 12 |
| Nueva Caledonia | NCL | 5 |  |  |  |  |  |  |  |  |  |  |  |  | 5 |
| Nueva Zelanda | NZL | 25 |  |  |  |  |  |  |  |  |  |  | 3 | 7 | 15 |
| Níger | NER | 41 |  |  |  |  |  |  |  |  | 1 | 3 | 3 | 5 | 24 |
| Omán | OMN | 14 |  |  |  |  |  |  |  |  | 4 | 1 |  | 2 | 2 |
| Pakistán | PAK | 87 |  |  |  |  |  |  |  |  | 22 | 4 | 5 | 43 | 11 |
| Palaos | PLW | 18 |  |  |  |  |  |  |  |  |  |  |  |  | 14 |
| Palestina | PSE | 201 |  |  |  |  |  |  |  | 2 | 35 | 21 | 13 | 120 | 8 |
| Panamá | PAN | 47 |  |  |  |  |  |  |  |  |  | 18 | 7 | 12 | 10 |
| Papúa Nueva Guinea | PNG | 34 |  |  |  |  |  |  |  |  | 1 | 4 | 2 | 9 | 18 |
| Paraguay | PRY | 36 |  |  |  |  |  |  |  |  |  | 5 | 7 | 18 | 6 |
| Países Bajos | NLD | 236 |  |  |  |  |  |  |  |  | 35 | 59 | 54 | 66 | 20 |
| Perú | PER | 73 |  |  |  |  |  |  |  |  | 9 | 9 | 10 | 34 | 10 |
| Polinesia Francesa | PYF | 10 |  |  |  |  |  |  |  |  |  |  | 5 | 3 | 2 |
| Polonia | POL | 293 |  |  |  |  |  |  |  |  | 30 | 13 | 22 | 121 | 106 |
| Portugal | PRT | 121 |  |  |  |  |  |  |  | 1 | 21 | 14 | 28 | 43 | 8 |
| Puerto Rico | PRI | 760 |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 | 757 |
| Reino Unido | GBR | 583 |  |  |  |  |  |  |  | 1 | 47 | 170 | 85 | 216 | 57 |
| República Centroafricana | CAF | 116 |  |  |  |  |  |  |  |  |  | 1 | 4 | 6 | 103 |
| República Checa | CZE | 264 |  |  |  |  |  |  |  |  | 13 | 15 | 17 | 91 | 128 |
| República Democrática del Congo | COD | 108 |  |  |  |  |  |  |  | 1 | 2 | 6 | 11 | 28 | 40 |
| República Dominicana | DOM | 9 |  |  |  |  |  |  |  |  | 2 | 2 | 4 | 1 |  |
| República Turca del Norte de Chipre | CYN | 7 |  |  |  |  |  |  |  |  | 2 | 5 |  |  |  |
| República de China | TWN | 44 |  |  |  |  |  |  |  |  |  | 2 |  | 4 | 35 |
| República del Congo | COG | 55 |  |  |  |  |  |  |  | 1 |  | 5 | 12 | 10 | 17 |
| Ruanda | RWA | 7 |  |  |  |  |  |  |  |  |  |  |  | 2 | 5 |
| Rumania | ROU | 180 |  |  |  |  |  |  |  |  | 30 | 10 | 18 | 83 | 39 |
| Rusia | RUS | 445 | 3 |  |  |  |  |  |  |  | 41 | 77 | 43 | 99 | 171 |
| Sahara Occidental | ESH | 5 |  |  |  |  |  |  |  |  |  | 2 |  | 3 |  |
| Samoa | WSM | 2 |  |  |  |  |  |  |  |  |  |  |  |  | 2 |
| Samoa Estadounidense | ASM | 10 |  |  |  |  |  |  |  |  |  |  |  |  | 6 |
| San Cristóbal y Nieves | KNA | 1 |  |  |  |  |  |  |  |  |  |  | 1 |  |  |
| San Marino | SMR | 1 |  |  |  |  |  |  |  |  |  |  | 1 |  |  |
| San Martín | SXM | 3 |  |  |  |  |  |  |  | 1 |  |  |  | 2 |  |
| San Martín | MAF | 1 |  |  |  |  |  |  |  |  |  |  |  | 1 |  |
| San Pedro y Miquelón | SPM | 1 |  |  |  |  |  |  |  |  |  |  |  | 1 |  |
| Santo Tomé y Príncipe | STP | 2 |  |  |  |  |  |  |  |  |  | 1 |  |  | 1 |
| Senegal | SEN | 29 |  |  |  |  |  |  |  |  | 1 |  | 9 | 10 | 9 |
| Serbia | SRB | 130 |  |  |  |  |  |  |  |  | 18 | 5 | 11 | 72 | 23 |
| Seychelles | SYC | 1 |  |  |  |  |  |  |  |  |  |  |  | 1 |  |
| Sierra Leona | SLE | 27 |  |  |  |  |  |  |  |  | 1 | 1 | 4 | 7 | 14 |
| Singapur | SGP | 7 |  |  |  |  |  |  |  |  |  |  |  | 1 | 4 |
| Siria | SYR | 261 |  |  |  |  |  |  |  |  | 33 | 19 | 27 | 158 | 23 |
| Somalia | SOM | 100 |  |  |  |  |  |  |  |  | 5 | 5 | 1 | 4 | 77 |
| Somalilandia | SOL | 31 |  |  |  |  |  |  |  |  | 2 | 4 |  | 3 | 18 |
| Sri Lanka | LKA | 25 |  |  |  |  |  |  |  |  | 6 | 6 | 8 | 1 | 4 |
| Suazilandia | SWZ | 34 |  |  |  |  |  |  |  |  |  |  |  | 3 | 31 |
| Sudáfrica | ZAF | 261 |  |  |  |  |  |  |  |  | 1 | 1 | 11 | 69 | 123 |
| Sudán | SDN | 159 |  |  |  |  |  |  |  |  | 6 | 7 | 5 | 24 | 110 |
| Sudán del Sur | SSD | 114 |  |  |  |  |  |  |  |  | 1 | 3 | 3 | 15 | 86 |
| Suecia | SWE | 51 |  |  |  |  |  |  |  |  | 7 | 14 | 6 | 11 | 13 |
| Suiza | CHE | 209 | 1 |  |  |  |  |  |  |  | 37 | 21 | 30 | 86 | 33 |
| Surinam | SUR | 21 |  |  |  |  |  |  |  |  | 1 | 7 | 3 | 7 | 3 |
| Tailandia | THA | 43 |  |  |  |  |  |  |  |  | 3 | 3 | 3 | 15 | 18 |
| Tanzania | TZA | 115 |  |  |  |  |  |  |  |  | 2 | 2 | 1 | 38 | 60 |
| Tayikistán | TJK | 26 |  |  |  |  |  |  |  |  | 5 |  |  | 14 | 7 |
| Timor Oriental | TLS | 1 |  |  |  |  |  |  |  |  |  |  |  |  | 1 |
| Togo | TGO | 5 |  |  |  |  |  |  |  |  |  |  | 1 | 1 | 3 |
| Tonga | TON | 2 |  |  |  |  |  |  |  |  |  |  | 1 |  | 1 |
| Trinidad y Tobago | TTO | 1 |  |  |  |  |  |  |  |  |  |  |  | 1 |  |
| Turkmenistán | TKM | 60 |  |  |  |  |  |  |  |  | 13 | 4 | 2 | 34 | 7 |
| Turquía | TUR | 350 |  |  |  |  |  |  |  | 1 | 47 | 33 | 36 | 172 | 59 |
| Túnez | TUN | 104 |  |  |  |  |  |  |  |  | 19 | 3 | 3 | 24 | 55 |
| Ucrania | UKR | 137 | 4 |  |  |  |  |  |  |  | 19 | 36 | 27 | 14 | 35 |
| Uganda | UGA | 116 |  |  |  |  |  |  |  |  | 1 | 3 | 3 | 11 | 97 |
| Uruguay | URY | 26 |  |  |  |  |  |  |  |  |  | 3 | 4 | 16 | 3 |
| Uzbekistán | UZB | 38 |  |  |  |  |  |  |  |  | 6 | 3 | 2 | 24 | 3 |
| Venezuela | VEN | 62 |  |  |  |  |  |  |  |  | 5 | 14 | 5 | 35 | 3 |
| Vietnam | VNM | 25 |  |  |  |  |  |  |  |  |  | 2 |  | 7 | 15 |
| Yemen | YEM | 93 |  |  |  |  |  |  |  |  | 6 | 3 |  | 13 | 70 |
| Yibuti | DJI | 5 |  |  |  |  |  |  |  |  |  |  |  | 1 | 2 |
| Zambia | ZMB | 77 |  |  |  |  |  |  |  |  | 1 | 3 | 5 | 16 | 35 |
| Zimbabue | ZWE | 74 |  |  |  |  |  |  |  |  | 2 | 1 | 6 | 22 | 32 |
