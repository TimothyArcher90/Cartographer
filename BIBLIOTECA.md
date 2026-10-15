# Biblioteca de Cartographer

Documento generado por `scripts/comprender.py`. No editar a mano.

- Mapas analizados: **286,363** · con país asignado: **267,921** · sin país: 18,442
  (sobre todo mapamundis, cartas oceánicas o registros sin datos de lugar).
- Países con mapas: **239**.
- Tipos: topográfico 188,614, general 88,851, plano urbano 2,375, mapamundi 1,908, ferroviario/viario 1,397, carta náutica 1,325, histórico/temático 1,082, militar 670, ptolemaico 104, portulano 37.
- Escalas: local o ciudad 233,680, desconocida 21,336, provincia o comarca 17,234, región o país 8,454, continente 3,931, mundo 1,728.

Cómo se asigna un país: por **nombre** actual (25+ idiomas, Natural Earth), por **nombre histórico**
(`catalogo/nombres_historicos.json`) o por **coordenadas** de la cobertura del mapa. Cada mapa guarda
la vía en el campo `via`; las asignaciones por coordenadas de mapas grandes pueden incluir países
vecinos. Los siglos salen del año de los metadatos de cada archivo y pueden tener errores puntuales.

Mapas de un país: `catalogo/biblioteca/paises/<ISO3>.jsonl.gz` o
`python scripts/buscar_lugar.py "<país>"`.

| País | ISO | Total | Antes del s. IX | IX | X | XI | XII | XIII | XIV | XV | XVI | XVII | XVIII | XIX | XX |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Afganistán | AFG | 182 |  |  |  |  |  |  |  |  | 19 | 4 | 5 | 40 | 12 |
| Albania | ALB | 220 |  |  |  |  |  |  |  | 2 | 21 | 21 | 10 | 35 | 22 |
| Alemania | DEU | 5,757 | 1 |  |  |  |  |  |  | 2 | 78 | 133 | 142 | 437 | 309 |
| Andorra | AND | 8 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Angola | AGO | 72 |  |  |  |  |  |  |  |  | 1 | 5 | 9 | 14 | 14 |
| Anguila | AIA | 3 |  |  |  |  |  |  |  |  |  |  | 2 | 1 |  |
| Antigua y Barbuda | ATG | 19 |  |  |  |  |  |  |  |  |  | 1 | 12 | 2 |  |
| Antártida | ATA | 25 |  |  |  |  |  |  |  |  |  | 3 | 2 | 7 | 9 |
| Arabia Saudita | SAU | 378 |  |  |  |  |  |  |  | 3 | 36 | 24 | 21 | 60 | 87 |
| Argelia | DZA | 251 |  |  |  |  |  |  |  | 2 | 18 | 16 | 9 | 37 | 33 |
| Argentina | ARG | 273 |  |  |  |  |  |  |  |  | 2 | 42 | 22 | 64 | 32 |
| Armenia | ARM | 60 |  |  |  |  |  |  |  | 1 | 10 | 3 | 3 | 17 | 3 |
| Aruba | ABW | 33 |  |  |  |  |  |  |  |  |  | 1 | 2 | 13 | 9 |
| Australia | AUS | 1,696 |  |  |  |  |  |  |  |  |  | 4 | 4 | 57 | 35 |
| Austria | AUT | 1,564 | 1 |  |  |  |  |  |  | 2 | 35 | 30 | 33 | 196 | 192 |
| Azerbaiyán | AZE | 107 |  |  |  |  |  |  |  | 1 | 8 | 2 | 3 | 26 | 10 |
| Bahamas | BHS | 50 |  |  |  |  |  |  |  |  |  |  | 15 | 32 | 2 |
| Bangladés | BGD | 51 |  |  |  |  |  |  |  | 1 | 1 | 4 | 2 | 5 | 5 |
| Barbados | BRB | 37 |  |  |  |  |  |  |  |  |  | 3 | 12 | 3 |  |
| Belice | BLZ | 20 |  |  |  |  |  |  |  |  |  |  | 1 | 7 | 6 |
| Benín | BEN | 29 |  |  |  |  |  |  |  |  | 2 | 6 |  | 2 | 6 |
| Bermudas | BMU | 30 |  |  |  |  |  |  |  |  |  | 8 | 10 | 4 | 2 |
| Bielorrusia | BLR | 334 |  |  |  |  |  |  |  | 3 | 22 | 18 | 17 | 15 | 41 |
| Birmania | MMR | 168 |  |  |  |  |  |  |  |  | 7 | 4 | 10 | 27 | 25 |
| Bolivia | BOL | 131 |  |  |  |  |  |  |  |  | 4 | 11 | 6 | 34 | 18 |
| Bosnia y Herzegovina | BIH | 602 |  |  |  |  |  |  |  | 6 | 36 | 12 | 19 | 99 | 42 |
| Botsuana | BWA | 147 |  |  |  |  |  |  |  |  | 1 |  | 6 | 46 | 37 |
| Brasil | BRA | 520 |  |  |  |  |  |  |  |  | 8 | 64 | 40 | 102 | 38 |
| Brunéi | BRN | 7 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Bulgaria | BGR | 459 |  |  |  |  |  |  |  | 2 | 19 | 16 | 29 | 73 | 47 |
| Burkina Faso | BFA | 55 |  |  |  |  |  |  |  |  | 1 | 5 | 3 | 7 | 5 |
| Burundi | BDI | 5 |  |  |  |  |  |  |  |  |  |  |  | 2 | 3 |
| Bután | BTN | 22 |  |  |  |  |  |  |  |  |  |  | 1 | 6 | 1 |
| Bélgica | BEL | 3,270 |  |  |  |  |  |  |  | 1 | 39 | 77 | 56 | 122 | 90 |
| Cabo Verde | CPV | 55 |  |  |  |  |  |  |  |  | 1 | 13 | 30 | 5 |  |
| Camboya | KHM | 64 |  |  |  |  |  |  |  |  |  | 1 |  | 5 | 17 |
| Camerún | CMR | 91 |  |  |  |  |  |  |  |  |  | 4 | 8 | 7 | 36 |
| Canadá | CAN | 4,556 |  |  |  |  |  |  |  |  | 12 | 69 | 799 | 967 | 1,468 |
| Catar | QAT | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Chad | TCD | 69 |  |  |  |  |  |  |  |  |  | 3 | 5 | 8 | 29 |
| Chile | CHL | 282 |  |  |  |  |  |  |  |  | 2 | 45 | 27 | 99 | 17 |
| China | CHN | 1,110 |  |  |  |  | 1 |  |  | 4 | 27 | 58 | 40 | 147 | 353 |
| Chipre | CYP | 39 |  |  |  |  |  |  |  | 1 | 10 | 10 | 5 | 1 | 1 |
| Ciudad del Vaticano | VAT | 5 |  |  |  |  |  |  |  |  |  |  |  | 2 | 1 |
| Colombia | COL | 190 |  |  |  |  |  |  |  |  | 5 | 17 | 21 | 58 | 15 |
| Comoras | COM | 3 |  |  |  |  |  |  |  |  |  |  |  | 2 | 1 |
| Corea del Norte | PRK | 108 |  |  |  |  |  |  |  |  |  | 8 | 6 | 11 | 43 |
| Corea del Sur | KOR | 133 |  |  |  |  |  |  |  |  |  | 9 | 13 | 17 | 48 |
| Costa Rica | CRI | 61 |  |  |  |  |  |  |  |  |  | 13 | 7 | 20 | 8 |
| Costa de Marfil | CIV | 74 |  |  |  |  |  |  |  |  | 1 | 5 | 9 | 10 | 13 |
| Croacia | HRV | 846 |  |  |  |  |  |  |  | 6 | 40 | 15 | 25 | 132 | 52 |
| Cuba | CUB | 233 |  |  |  |  |  |  |  |  | 4 | 11 | 43 | 51 | 21 |
| Curazao | CUW | 62 |  |  |  |  |  |  |  |  |  | 1 | 4 | 6 | 3 |
| Dinamarca | DNK | 318 |  |  |  |  |  |  |  |  | 6 | 40 | 6 | 23 | 8 |
| Dominica | DMA | 12 |  |  |  |  |  |  |  |  |  |  | 7 | 2 |  |
| ESB | ESB | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ecuador | ECU | 118 |  |  |  |  |  |  |  |  | 5 | 8 | 9 | 41 | 5 |
| Egipto | EGY | 468 |  |  |  |  |  |  |  | 2 | 41 | 30 | 29 | 126 | 33 |
| El Salvador | SLV | 25 |  |  |  |  |  |  |  |  |  |  | 2 | 6 | 10 |
| Emiratos Árabes Unidos | ARE | 9 |  |  |  |  |  |  |  |  | 1 |  |  | 2 |  |
| Eritrea | ERI | 58 |  |  |  |  |  |  |  |  | 1 | 5 | 1 | 14 | 11 |
| Eslovaquia | SVK | 714 |  |  |  |  |  |  |  | 2 | 16 | 10 | 16 | 92 | 72 |
| Eslovenia | SVN | 360 |  |  |  |  |  |  |  | 2 | 18 | 3 | 3 | 11 | 106 |
| España | ESP | 991 |  |  |  |  |  |  |  | 3 | 58 | 68 | 92 | 106 | 18 |
| Estados Federados de Micronesia | FSM | 32 |  |  |  |  |  |  |  |  |  |  |  | 4 | 23 |
| Estados Unidos | USA | 221,739 | 4 |  |  |  |  |  |  |  | 13 | 170 | 2,345 | 15,060 | 172,399 |
| Estonia | EST | 81 |  |  |  |  |  |  |  |  | 1 | 8 | 1 | 3 | 7 |
| Etiopía | ETH | 236 |  |  |  |  |  |  |  | 1 | 8 | 13 | 5 | 26 | 104 |
| Filipinas | PHL | 146 |  |  |  |  |  |  |  |  | 3 | 5 | 9 | 31 | 65 |
| Finlandia | FIN | 203 |  |  |  |  |  |  |  | 1 | 7 | 11 | 10 | 11 | 15 |
| Fiyi | FJI | 27 |  |  |  |  |  |  |  |  |  |  |  | 20 | 6 |
| Francia | FRA | 4,764 |  |  |  |  |  |  |  | 1 | 125 | 202 | 294 | 426 | 179 |
| GIB | GIB | 6 |  |  |  |  |  |  |  |  |  |  | 5 |  |  |
| Gabón | GAB | 47 |  |  |  |  |  |  |  |  |  | 5 | 6 | 6 | 12 |
| Gambia | GMB | 13 |  |  |  |  |  |  |  |  |  |  | 5 | 3 | 5 |
| Georgia | GEO | 140 |  |  |  |  |  |  |  | 1 | 11 | 3 | 11 | 25 | 28 |
| Ghana | GHA | 67 |  |  |  |  |  |  |  |  | 1 | 6 | 7 | 8 | 7 |
| Granada | GRD | 19 |  |  |  |  |  |  |  |  |  | 5 | 7 | 2 | 2 |
| Grecia | GRC | 716 |  |  |  |  |  |  |  | 3 | 68 | 70 | 69 | 139 | 55 |
| Groenlandia | GRL | 60 |  |  |  |  |  |  | 1 |  | 4 | 10 | 20 | 12 | 5 |
| Guam | GUM | 12 |  |  |  |  |  |  |  |  |  |  |  |  | 2 |
| Guatemala | GTM | 72 |  |  |  |  |  |  |  |  |  | 16 | 10 | 12 | 13 |
| Guernsey | GGY | 6 |  |  |  |  |  |  |  |  |  | 4 |  | 2 |  |
| Guinea | GIN | 65 |  |  |  |  |  |  |  |  | 1 | 5 | 14 | 8 | 12 |
| Guinea Ecuatorial | GNQ | 10 |  |  |  |  |  |  |  |  |  |  |  | 2 | 2 |
| Guinea-Bisáu | GNB | 8 |  |  |  |  |  |  |  |  |  |  | 2 | 1 | 2 |
| Guyana | GUY | 173 |  |  |  |  |  |  |  |  | 1 | 17 | 18 | 17 | 7 |
| Haití | HTI | 115 |  |  |  |  |  |  |  |  | 3 | 8 | 39 | 24 | 4 |
| Honduras | HND | 75 |  |  |  |  |  |  |  |  |  | 16 | 12 | 13 | 14 |
| Hong Kong | HKG | 20 |  |  |  |  |  |  |  |  |  |  |  | 5 | 6 |
| Hungría | HUN | 1,056 |  |  |  |  |  |  |  | 3 | 35 | 16 | 35 | 160 | 94 |
| India | IND | 582 |  |  |  |  |  |  |  | 1 | 45 | 23 | 74 | 90 | 32 |
| Indonesia | IDN | 915 | 1 |  |  |  |  |  |  |  | 9 | 13 | 25 | 29 | 91 |
| Irak | IRQ | 353 |  |  |  |  |  |  |  | 2 | 26 | 13 | 42 | 70 | 33 |
| Irlanda | IRL | 705 |  |  |  |  |  |  |  | 1 | 22 | 36 | 45 | 251 | 17 |
| Irán | IRN | 304 |  |  |  |  |  |  |  | 4 | 35 | 14 | 11 | 75 | 22 |
| Isla Norfolk | NFK | 172 |  |  |  |  |  |  |  |  |  |  | 23 | 124 | 25 |
| Isla Santa Elena | SHN | 14 |  |  |  |  |  |  |  |  | 1 |  | 2 | 5 | 1 |
| Isla de Man | IMN | 12 |  |  |  |  |  |  |  |  |  |  |  | 3 |  |
| Islandia | ISL | 55 |  |  |  |  |  |  |  |  | 2 | 4 | 4 | 6 | 2 |
| Islas Caimán | CYM | 1 |  |  |  |  |  |  |  |  |  |  |  | 1 |  |
| Islas Feroe | FRO | 2 |  |  |  |  |  |  |  |  |  | 1 |  |  |  |
| Islas Georgias del Sur y Sandwich del Sur | SGS | 4 |  |  |  |  |  |  |  |  |  |  |  |  | 1 |
| Islas Malvinas | FLK | 6 |  |  |  |  |  |  |  |  |  |  | 2 | 1 |  |
| Islas Marianas del Norte | MNP | 20 |  |  |  |  |  |  |  |  |  |  |  | 1 | 17 |
| Islas Marshall | MHL | 8 |  |  |  |  |  |  |  |  |  |  |  | 2 | 6 |
| Islas Pitcairn | PCN | 1 |  |  |  |  |  |  |  |  |  |  | 1 |  |  |
| Islas Salomón | SLB | 16 |  |  |  |  |  |  |  |  | 1 | 2 | 1 | 3 | 9 |
| Islas Turcas y Caicos | TCA | 3 |  |  |  |  |  |  |  |  |  |  | 1 | 2 |  |
| Islas Vírgenes Británicas | VGB | 1 |  |  |  |  |  |  |  |  |  |  |  |  | 1 |
| Islas Vírgenes de los Estados Unidos | VIR | 85 |  |  |  |  |  |  |  |  |  | 1 | 42 | 2 | 34 |
| Israel | ISR | 699 |  |  |  |  |  |  |  | 4 | 45 | 30 | 25 | 176 | 12 |
| Italia | ITA | 2,495 | 1 |  |  |  |  |  |  | 8 | 162 | 158 | 108 | 311 | 196 |
| Jamaica | JAM | 115 |  |  |  |  |  |  |  |  | 1 | 9 | 32 | 34 | 14 |
| Japón | JPN | 753 |  |  |  |  |  |  |  | 1 | 3 | 20 | 18 | 104 | 192 |
| Jersey | JEY | 6 |  |  |  |  |  |  |  |  |  | 4 |  |  |  |
| Jordania | JOR | 434 |  |  |  |  |  |  |  | 1 | 37 | 16 | 22 | 145 | 25 |
| Kazajistán | KAZ | 138 |  |  |  |  |  |  |  | 1 | 15 | 15 | 4 | 18 | 10 |
| Kenia | KEN | 148 |  |  |  |  |  |  |  |  | 1 | 3 | 1 | 15 | 92 |
| Kirguistán | KGZ | 50 |  |  |  |  |  |  |  |  | 7 | 2 |  | 12 | 6 |
| Kiribati | KIR | 17 |  |  |  |  |  |  |  |  |  |  |  | 13 | 4 |
| Kosovo | KOS | 44 |  |  |  |  |  |  |  |  | 1 | 2 | 2 |  | 8 |
| Kuwait | KWT | 2 |  |  |  |  |  |  |  | 1 | 1 |  |  |  |  |
| Laos | LAO | 64 |  |  |  |  |  |  |  | 1 | 3 |  |  | 8 | 18 |
| Lesoto | LSO | 85 |  |  |  |  |  |  |  |  |  |  | 1 | 11 | 66 |
| Letonia | LVA | 167 |  |  |  |  |  |  |  | 2 | 10 | 8 | 8 | 7 | 15 |
| Liberia | LBR | 58 |  |  |  |  |  |  |  |  | 1 | 2 | 1 | 15 | 27 |
| Libia | LBY | 228 |  |  |  |  |  |  |  | 6 | 21 | 15 | 7 | 24 | 70 |
| Liechtenstein | LIE | 7 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |
| Lituania | LTU | 314 |  |  |  |  |  |  |  | 2 | 10 | 8 | 10 | 15 | 35 |
| Luxemburgo | LUX | 228 |  |  |  |  |  |  |  |  | 6 | 13 | 9 | 16 | 17 |
| Líbano | LBN | 224 |  |  |  |  |  |  |  | 1 | 17 | 4 | 10 | 105 | 7 |
| Macao | MAC | 4 |  |  |  |  |  |  |  |  |  |  | 1 |  |  |
| Macedonia del Norte | MKD | 147 |  |  |  |  |  |  |  | 2 | 13 | 11 | 5 | 19 | 20 |
| Madagascar | MDG | 117 |  |  |  |  |  |  |  |  | 2 | 2 | 8 | 34 | 35 |
| Malasia | MYS | 184 |  |  |  |  |  |  |  |  | 2 | 4 | 3 | 13 | 22 |
| Malaui | MWI | 35 |  |  |  |  |  |  |  |  | 1 |  | 2 | 13 | 14 |
| Maldivas | MDV | 2 |  |  |  |  |  |  |  |  |  |  | 1 |  | 1 |
| Malta | MLT | 49 |  |  |  |  |  |  |  |  | 8 | 12 | 6 | 6 | 1 |
| Malí | MLI | 97 |  |  |  |  |  |  |  |  | 2 | 5 | 6 | 12 | 7 |
| Marruecos | MAR | 191 |  |  |  |  |  |  |  | 1 | 10 | 11 | 13 | 24 | 30 |
| Mauricio | MUS | 13 |  |  |  |  |  |  |  |  |  |  | 2 | 6 | 1 |
| Mauritania | MRT | 70 |  |  |  |  |  |  |  |  | 4 | 3 | 9 | 9 | 4 |
| Moldavia | MDA | 107 |  |  |  |  |  |  |  | 1 | 3 | 4 | 9 | 16 | 10 |
| Mongolia | MNG | 60 |  |  |  |  |  |  |  |  | 1 | 6 | 2 | 8 | 23 |
| Montenegro | MNE | 92 |  |  |  |  |  |  |  |  | 6 | 6 | 2 | 8 | 10 |
| Mozambique | MOZ | 140 |  |  |  |  |  |  |  |  | 3 | 3 | 6 | 38 | 32 |
| México | MEX | 1,869 |  |  |  |  |  |  |  |  | 17 | 60 | 87 | 309 | 852 |
| Mónaco | MCO | 2 |  |  |  |  |  |  |  |  |  |  | 1 | 1 |  |
| Namibia | NAM | 122 |  |  |  |  |  |  |  |  | 1 |  | 7 | 40 | 21 |
| Nauru | NRU | 2 |  |  |  |  |  |  |  |  |  |  |  |  | 2 |
| Nepal | NPL | 49 |  |  |  |  |  |  |  | 1 | 2 | 2 |  | 5 | 2 |
| Nicaragua | NIC | 70 |  |  |  |  |  |  |  |  |  | 14 | 8 | 17 | 11 |
| Nigeria | NGA | 99 |  |  |  |  |  |  |  |  | 1 | 8 | 7 | 8 | 29 |
| Noruega | NOR | 234 |  |  |  |  |  |  |  | 2 | 2 | 12 | 10 | 14 | 16 |
| Nueva Caledonia | NCL | 8 |  |  |  |  |  |  |  |  |  |  | 1 | 1 | 5 |
| Nueva Zelanda | NZL | 69 |  |  |  |  |  |  |  |  |  |  | 3 | 12 | 15 |
| Níger | NER | 79 |  |  |  |  |  |  |  |  | 4 | 5 | 3 | 5 | 26 |
| Omán | OMN | 43 |  |  |  |  |  |  |  | 1 | 6 | 1 |  | 4 | 3 |
| PSX | PSX | 327 |  |  |  |  |  |  |  | 1 | 17 | 8 | 7 | 106 | 2 |
| Pakistán | PAK | 241 |  |  |  |  |  |  |  |  | 24 | 5 | 8 | 50 | 13 |
| Palaos | PLW | 19 |  |  |  |  |  |  |  |  |  |  |  | 1 | 14 |
| Palestina | PSE | 441 |  |  |  |  |  |  |  | 3 | 37 | 22 | 14 | 131 | 11 |
| Panamá | PAN | 121 |  |  |  |  |  |  |  |  |  | 25 | 22 | 23 | 19 |
| Papúa Nueva Guinea | PNG | 56 |  |  |  |  |  |  |  |  | 1 | 4 | 2 | 10 | 24 |
| Paraguay | PRY | 121 |  |  |  |  |  |  |  |  |  | 10 | 8 | 24 | 14 |
| Países Bajos | NLD | 11,429 |  |  |  |  |  |  |  |  | 38 | 101 | 74 | 118 | 33 |
| Perú | PER | 206 |  |  |  |  |  |  |  |  | 11 | 20 | 14 | 55 | 22 |
| Polinesia Francesa | PYF | 31 |  |  |  |  |  |  |  |  |  |  | 5 | 20 | 2 |
| Polonia | POL | 2,017 |  |  |  |  |  |  |  | 6 | 40 | 35 | 45 | 169 | 148 |
| Portugal | PRT | 391 |  |  |  |  |  |  |  | 1 | 22 | 27 | 39 | 66 | 9 |
| Puerto Rico | PRI | 809 |  |  |  |  |  |  |  |  |  | 4 | 9 | 6 | 771 |
| Reino Unido | GBR | 5,211 |  |  |  |  |  |  |  | 2 | 51 | 251 | 169 | 329 | 94 |
| República Centroafricana | CAF | 142 |  |  |  |  |  |  |  |  |  | 2 | 4 | 8 | 104 |
| República Checa | CZE | 1,307 |  |  |  |  |  |  |  | 1 | 16 | 28 | 25 | 138 | 167 |
| República Democrática del Congo | COD | 227 |  |  |  |  |  |  |  | 1 | 2 | 7 | 12 | 33 | 124 |
| República Dominicana | DOM | 82 |  |  |  |  |  |  |  |  | 3 | 8 | 28 | 16 | 2 |
| República Turca del Norte de Chipre | CYN | 18 |  |  |  |  |  |  |  |  | 2 | 5 |  |  |  |
| República de China | TWN | 67 |  |  |  |  |  |  |  |  |  | 2 |  | 4 | 37 |
| República del Congo | COG | 70 |  |  |  |  |  |  |  | 1 |  | 6 | 13 | 10 | 19 |
| Ruanda | RWA | 8 |  |  |  |  |  |  |  |  |  |  |  | 2 | 5 |
| Rumania | ROU | 834 |  |  |  |  |  |  |  | 2 | 36 | 15 | 28 | 121 | 81 |
| Rusia | RUS | 1,749 | 3 |  |  |  |  |  |  | 5 | 56 | 90 | 70 | 182 | 447 |
| SAH | SAH | 4 |  |  |  |  |  |  |  |  |  | 2 |  | 1 |  |
| SDS | SDS | 84 |  |  |  |  |  |  |  |  |  | 1 |  | 10 | 19 |
| Sahara Occidental | ESH | 6 |  |  |  |  |  |  |  |  |  | 2 |  | 3 |  |
| Samoa | WSM | 18 |  |  |  |  |  |  |  |  |  |  |  | 14 | 2 |
| Samoa Estadounidense | ASM | 23 |  |  |  |  |  |  |  |  |  |  |  | 13 | 6 |
| San Bartolomé | BLM | 2 |  |  |  |  |  |  |  |  |  |  | 2 |  |  |
| San Cristóbal y Nieves | KNA | 17 |  |  |  |  |  |  |  |  |  | 2 | 12 |  |  |
| San Marino | SMR | 1 |  |  |  |  |  |  |  |  |  |  | 1 |  |  |
| San Martín | SXM | 8 |  |  |  |  |  |  |  | 1 |  |  | 2 | 3 |  |
| San Martín | MAF | 7 |  |  |  |  |  |  |  |  |  |  | 2 | 3 |  |
| San Pedro y Miquelón | SPM | 7 |  |  |  |  |  |  |  |  |  |  | 1 | 5 | 1 |
| San Vicente y las Granadinas | VCT | 4 |  |  |  |  |  |  |  |  |  |  | 2 | 1 |  |
| Santa Lucía | LCA | 6 |  |  |  |  |  |  |  |  |  |  | 5 |  |  |
| Santo Tomé y Príncipe | STP | 2 |  |  |  |  |  |  |  |  |  | 1 |  |  | 1 |
| Senegal | SEN | 60 |  |  |  |  |  |  |  |  | 1 |  | 16 | 10 | 10 |
| Serbia | SRB | 578 |  |  |  |  |  |  |  | 4 | 23 | 10 | 19 | 96 | 51 |
| Seychelles | SYC | 2 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |
| Sierra Leona | SLE | 42 |  |  |  |  |  |  |  |  | 1 | 1 | 7 | 7 | 17 |
| Singapur | SGP | 16 |  |  |  |  |  |  |  |  |  |  |  | 4 | 4 |
| Siria | SYR | 529 |  |  |  |  |  |  |  | 3 | 40 | 24 | 32 | 173 | 35 |
| Somalia | SOM | 129 |  |  |  |  |  |  |  |  | 5 | 5 | 1 | 8 | 83 |
| Somalilandia | SOL | 47 |  |  |  |  |  |  |  |  | 2 | 4 |  | 4 | 18 |
| Sri Lanka | LKA | 79 |  |  |  |  |  |  |  | 1 | 6 | 7 | 9 | 1 | 5 |
| Suazilandia | SWZ | 36 |  |  |  |  |  |  |  |  |  |  |  | 3 | 31 |
| Sudáfrica | ZAF | 354 |  |  |  |  |  |  |  |  | 1 |  | 16 | 84 | 132 |
| Sudán | SDN | 263 |  |  |  |  |  |  |  | 2 | 8 | 10 | 7 | 27 | 117 |
| Sudán del Sur | SSD | 202 |  |  |  |  |  |  |  |  | 1 | 4 | 3 | 17 | 87 |
| Suecia | SWE | 360 |  |  |  |  |  |  |  | 2 | 9 | 26 | 14 | 17 | 18 |
| Suiza | CHE | 1,327 | 1 |  |  |  |  |  |  | 1 | 41 | 40 | 55 | 148 | 57 |
| Surinam | SUR | 320 |  |  |  |  |  |  |  |  | 1 | 11 | 13 | 9 | 4 |
| Tailandia | THA | 98 |  |  |  |  |  |  |  |  | 4 | 3 | 4 | 17 | 21 |
| Tanzania | TZA | 152 |  |  |  |  |  |  |  |  | 2 | 2 | 2 | 45 | 67 |
| Tayikistán | TJK | 61 |  |  |  |  |  |  |  |  | 6 |  |  | 15 | 7 |
| Territorios Australianos del Océano Índico | IOA | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Tierras Australes y Antárticas Francesas | ATF | 4 |  |  |  |  |  |  |  |  |  |  |  | 1 |  |
| Timor Oriental | TLS | 5 |  |  |  |  |  |  |  |  |  |  |  |  | 1 |
| Togo | TGO | 16 |  |  |  |  |  |  |  |  |  |  | 2 | 1 | 3 |
| Tonga | TON | 3 |  |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| Trinidad y Tobago | TTO | 9 |  |  |  |  |  |  |  |  |  |  | 4 | 2 |  |
| Turkmenistán | TKM | 140 |  |  |  |  |  |  |  |  | 14 | 4 | 2 | 37 | 10 |
| Turquía | TUR | 810 |  |  |  |  |  |  |  | 3 | 55 | 44 | 48 | 218 | 90 |
| Tuvalu | TUV | 4 |  |  |  |  |  |  |  |  |  |  |  | 4 |  |
| Túnez | TUN | 233 |  |  |  |  |  |  |  | 2 | 23 | 4 | 9 | 31 | 60 |
| UMI | UMI | 2 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |
| USG | USG | 3 |  |  |  |  |  |  |  |  |  |  | 1 | 1 |  |
| Ucrania | UKR | 623 | 4 |  |  |  |  |  |  | 4 | 28 | 39 | 33 | 35 | 62 |
| Uganda | UGA | 143 |  |  |  |  |  |  |  |  | 1 | 3 | 3 | 11 | 100 |
| Uruguay | URY | 64 |  |  |  |  |  |  |  |  |  | 9 | 5 | 19 | 4 |
| Uzbekistán | UZB | 99 |  |  |  |  |  |  |  |  | 7 | 4 | 2 | 27 | 4 |
| Vanuatu | VUT | 3 |  |  |  |  |  |  |  |  |  |  |  | 1 | 1 |
| Venezuela | VEN | 200 |  |  |  |  |  |  |  |  | 6 | 28 | 10 | 42 | 6 |
| Vietnam | VNM | 228 |  |  |  |  |  |  |  | 1 | 2 | 2 |  | 11 | 20 |
| Yemen | YEM | 148 |  |  |  |  |  |  |  | 1 | 8 | 3 |  | 17 | 72 |
| Yibuti | DJI | 5 |  |  |  |  |  |  |  |  |  |  |  | 1 | 2 |
| Zambia | ZMB | 94 |  |  |  |  |  |  |  |  | 1 | 3 | 5 | 19 | 42 |
| Zimbabue | ZWE | 106 |  |  |  |  |  |  |  |  | 2 |  | 6 | 25 | 40 |
