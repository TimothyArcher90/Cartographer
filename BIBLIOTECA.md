# Biblioteca de Cartographer

Documento generado por `scripts/comprender.py`. No editar a mano.

- Mapas analizados: **763,188** · con país asignado: **475,650** · sin país: 287,538
  (sobre todo mapamundis, cartas oceánicas o registros sin datos de lugar).
- Países con mapas: **243**.
- Tipos: general 507,132, topográfico 202,065, plano urbano 23,443, militar 9,655, histórico/temático 7,076, mapamundi 5,021, ferroviario/viario 4,540, carta náutica 3,610, portulano 472, ptolemaico 174.
- Escalas: desconocida 493,392, local o ciudad 245,025, provincia o comarca 14,152, región o país 6,100, continente 2,997, mundo 1,522.

Cómo se asigna un país: por **nombre** actual (25+ idiomas, Natural Earth), por **nombre histórico**
(`catalogo/nombres_historicos.json`) o por **coordenadas** de la cobertura del mapa. Cada mapa guarda
la vía en el campo `via`; las asignaciones por coordenadas de mapas grandes pueden incluir países
vecinos. Los siglos salen del año de los metadatos de cada archivo y pueden tener errores puntuales.

Mapas de un país: `catalogo/biblioteca/paises/<ISO3>.jsonl.gz` o
`python scripts/buscar_lugar.py "<país>"`.

| País | ISO | Total | Antes del s. IX | IX | X | XI | XII | XIII | XIV | XV | XVI | XVII | XVIII | XIX | XX |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Afganistán | AFG | 374 |  |  |  |  |  |  |  |  | 21 | 6 | 9 | 149 | 100 |
| Albania | ALB | 262 |  |  |  |  |  |  | 1 | 3 | 23 | 22 | 19 | 63 | 48 |
| Alemania | DEU | 12,990 | 1 |  |  |  |  |  |  | 4 | 96 | 208 | 337 | 1,515 | 828 |
| Andorra | AND | 27 |  |  |  |  |  |  |  |  |  |  | 1 | 2 | 18 |
| Angola | AGO | 190 |  |  |  |  |  |  |  |  | 3 | 9 | 13 | 48 | 89 |
| Anguila | AIA | 7 |  |  |  |  |  |  |  |  |  |  | 6 | 1 |  |
| Antigua y Barbuda | ATG | 26 |  |  |  |  |  |  |  |  |  | 1 | 13 | 10 | 1 |
| Antártida | ATA | 89 |  |  |  |  |  |  |  |  |  | 8 | 11 | 9 | 50 |
| Arabia Saudita | SAU | 507 |  |  |  |  |  |  |  | 6 | 45 | 32 | 52 | 146 | 129 |
| Argelia | DZA | 396 |  |  |  |  |  |  |  | 2 | 20 | 21 | 33 | 106 | 102 |
| Argentina | ARG | 755 |  |  |  |  |  |  |  |  | 7 | 98 | 95 | 126 | 355 |
| Armenia | ARM | 141 |  |  |  |  |  |  | 1 | 1 | 11 | 7 | 15 | 61 | 21 |
| Aruba | ABW | 22 |  |  |  |  |  |  |  |  |  |  | 2 | 6 | 4 |
| Australia | AUS | 1,954 | 1 |  |  |  |  |  |  |  | 2 | 7 | 18 | 275 | 63 |
| Austria | AUT | 1,586 | 1 |  |  |  |  |  |  | 2 | 38 | 36 | 63 | 387 | 254 |
| Azerbaiyán | AZE | 96 |  |  |  |  |  |  |  | 1 | 8 | 4 | 5 | 30 | 24 |
| Bahamas | BHS | 139 |  |  |  |  |  |  |  |  |  | 4 | 58 | 49 | 23 |
| Bangladés | BGD | 53 |  |  |  |  |  |  |  | 1 | 3 | 5 | 4 | 7 | 8 |
| Barbados | BRB | 85 |  |  |  |  |  |  |  |  |  | 6 | 33 | 6 | 24 |
| Baréin | BHR | 63 |  |  |  |  |  |  |  | 2 | 6 | 6 | 9 | 14 | 16 |
| Belice | BLZ | 67 |  |  |  |  |  |  |  |  |  | 9 | 5 | 15 | 34 |
| Benín | BEN | 47 |  |  |  |  |  |  |  |  | 3 | 6 |  | 2 | 16 |
| Bermudas | BMU | 78 |  |  |  |  |  |  |  |  |  | 11 | 30 | 22 | 8 |
| Bielorrusia | BLR | 243 |  |  |  |  |  |  |  | 3 | 22 | 19 | 25 | 22 | 54 |
| Birmania | MMR | 152 |  |  |  |  |  |  |  |  | 8 | 5 | 14 | 38 | 37 |
| Bolivia | BOL | 195 |  |  |  |  |  |  |  |  | 5 | 15 | 9 | 66 | 73 |
| Bosnia y Herzegovina | BIH | 439 |  |  |  |  |  |  |  | 6 | 37 | 13 | 21 | 101 | 70 |
| Botsuana | BWA | 158 |  |  |  |  |  |  |  |  | 2 |  | 5 | 46 | 55 |
| Brasil | BRA | 1,556 |  |  |  |  |  |  |  | 3 | 16 | 193 | 239 | 460 | 424 |
| Brunéi | BRN | 17 |  |  |  |  |  |  |  |  |  |  |  | 6 | 4 |
| Bulgaria | BGR | 442 |  |  |  |  |  |  | 1 | 2 | 22 | 19 | 42 | 123 | 71 |
| Burkina Faso | BFA | 55 |  |  |  |  |  |  |  |  | 2 | 5 | 3 | 7 | 13 |
| Burundi | BDI | 37 |  |  |  |  |  |  |  |  |  |  |  | 3 | 30 |
| Bután | BTN | 38 |  |  |  |  |  |  |  |  |  |  | 1 | 9 | 11 |
| Bélgica | BEL | 4,651 |  |  |  |  |  |  |  | 2 | 52 | 136 | 339 | 360 | 271 |
| Cabo Verde | CPV | 93 |  |  |  |  |  |  |  |  | 3 | 15 | 37 | 21 | 3 |
| Camboya | KHM | 94 |  |  |  |  |  |  |  |  | 1 | 1 | 2 | 10 | 48 |
| Camerún | CMR | 98 |  |  |  |  |  |  |  |  | 2 | 4 | 8 | 9 | 43 |
| Canadá | CAN | 5,406 |  |  |  |  |  |  |  |  | 13 | 81 | 1,396 | 1,546 | 1,559 |
| Catar | QAT | 55 |  |  |  |  |  |  |  | 3 | 8 | 7 | 11 | 13 | 10 |
| Chad | TCD | 67 |  |  |  |  |  |  |  |  |  | 3 | 4 | 10 | 29 |
| Chile | CHL | 706 |  |  |  |  |  |  |  | 2 | 6 | 109 | 138 | 265 | 128 |
| China | CHN | 3,513 |  |  |  |  | 8 | 1 | 2 | 4 | 35 | 97 | 337 | 1,424 | 1,125 |
| Chipre | CYP | 179 |  |  |  |  |  |  |  | 1 | 10 | 13 | 11 | 18 | 92 |
| Ciudad del Vaticano | VAT | 42 |  |  |  |  |  |  |  |  | 1 | 24 | 1 | 3 | 5 |
| Colombia | COL | 493 |  |  |  |  |  |  |  |  | 10 | 55 | 102 | 103 | 141 |
| Comoras | COM | 9 |  |  |  |  |  |  |  |  |  |  |  | 2 | 7 |
| Corea del Norte | PRK | 134 |  |  |  |  |  |  |  |  | 1 | 9 | 11 | 13 | 54 |
| Corea del Sur | KOR | 730 |  |  |  |  |  |  |  |  | 2 | 12 | 51 | 117 | 201 |
| Costa Rica | CRI | 169 |  |  |  |  |  |  |  |  |  | 14 | 15 | 39 | 89 |
| Costa de Marfil | CIV | 84 |  |  |  |  |  |  |  |  | 3 | 5 | 9 | 10 | 25 |
| Croacia | HRV | 735 |  |  |  |  |  |  |  | 6 | 41 | 18 | 34 | 188 | 69 |
| Cuba | CUB | 966 |  |  |  |  |  |  |  | 1 | 7 | 99 | 217 | 261 | 244 |
| Curazao | CUW | 81 |  |  |  |  |  |  |  |  |  |  | 19 | 10 | 2 |
| Dinamarca | DNK | 1,041 |  |  |  |  |  |  | 1 |  | 10 | 47 | 47 | 276 | 69 |
| Dominica | DMA | 15 |  |  |  |  |  |  |  |  |  |  | 12 | 2 |  |
| ESB | ESB | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ecuador | ECU | 253 |  |  |  |  |  |  |  |  | 8 | 19 | 36 | 65 | 85 |
| Egipto | EGY | 1,930 |  |  |  |  | 1 | 1 |  | 3 | 44 | 39 | 114 | 785 | 755 |
| El Salvador | SLV | 156 |  |  |  |  |  |  |  |  |  | 4 | 4 | 86 | 54 |
| Emiratos Árabes Unidos | ARE | 54 |  |  |  |  |  |  |  | 3 | 7 | 6 | 12 | 13 | 6 |
| Eritrea | ERI | 398 |  |  |  |  |  |  |  |  | 1 | 6 | 7 | 99 | 260 |
| Eslovaquia | SVK | 494 |  |  |  |  |  |  |  | 2 | 16 | 13 | 19 | 94 | 101 |
| Eslovenia | SVN | 306 |  |  |  |  |  |  |  | 2 | 20 | 7 | 3 | 16 | 106 |
| España | ESP | 6,986 | 6 |  |  |  | 1 | 1 | 6 | 13 | 96 | 285 | 1,369 | 2,642 | 977 |
| Estados Federados de Micronesia | FSM | 44 |  |  |  |  |  |  |  |  |  | 1 | 1 | 11 | 25 |
| Estados Unidos | USA | 368,006 | 3 |  |  |  |  |  |  | 4 | 30 | 525 | 5,158 | 117,035 | 213,642 |
| Estonia | EST | 954 |  |  |  |  |  |  |  |  | 2 | 11 | 14 | 79 | 489 |
| Etiopía | ETH | 442 |  |  |  |  |  | 1 |  | 1 | 11 | 15 | 12 | 105 | 222 |
| Filipinas | PHL | 368 |  |  |  |  |  |  |  |  | 5 | 7 | 56 | 72 | 179 |
| Finlandia | FIN | 201 |  |  |  |  |  |  |  | 1 | 8 | 15 | 18 | 32 | 29 |
| Fiyi | FJI | 43 |  |  |  |  |  |  |  |  |  | 1 |  | 29 | 10 |
| Francia | FRA | 11,993 | 1 |  | 1 |  | 1 | 1 | 2 | 3 | 138 | 468 | 1,497 | 3,963 | 623 |
| GIB | GIB | 5 |  |  |  |  |  |  |  |  |  |  | 5 |  |  |
| Gabón | GAB | 56 |  |  |  |  |  |  |  |  | 2 | 5 | 7 | 6 | 12 |
| Gambia | GMB | 27 |  |  |  |  |  |  |  |  |  | 2 | 11 | 9 | 4 |
| Georgia | GEO | 231 |  |  |  |  |  |  |  | 1 | 11 | 4 | 49 | 60 | 40 |
| Ghana | GHA | 81 |  |  |  |  |  |  |  |  | 2 | 7 | 7 | 8 | 19 |
| Granada | GRD | 336 |  |  |  |  |  |  |  |  |  | 19 | 61 | 207 | 27 |
| Grecia | GRC | 1,282 |  |  |  |  |  |  |  | 3 | 75 | 93 | 89 | 509 | 179 |
| Groenlandia | GRL | 152 |  |  |  |  |  |  | 1 |  | 7 | 11 | 31 | 74 | 14 |
| Guam | GUM | 24 |  |  |  |  |  |  |  |  |  |  | 4 | 6 | 3 |
| Guatemala | GTM | 152 |  |  |  |  |  |  |  |  | 2 | 15 | 10 | 38 | 72 |
| Guernsey | GGY | 217 |  |  |  |  |  |  |  |  |  | 4 |  | 102 | 109 |
| Guinea | GIN | 84 |  |  |  |  |  |  |  |  | 1 | 11 | 32 | 10 | 12 |
| Guinea Ecuatorial | GNQ | 38 |  |  |  |  |  |  |  |  | 1 |  | 2 | 11 | 18 |
| Guinea-Bisáu | GNB | 6 |  |  |  |  |  |  |  |  |  |  | 2 | 2 | 2 |
| Guyana | GUY | 243 |  |  |  |  |  |  |  |  | 3 | 20 | 30 | 46 | 54 |
| Haití | HTI | 345 |  |  |  |  |  |  |  |  | 4 | 18 | 102 | 62 | 118 |
| Honduras | HND | 234 |  |  |  |  |  |  |  |  |  | 26 | 47 | 61 | 83 |
| Hong Kong | HKG | 44 |  |  |  |  |  |  |  |  |  |  |  | 21 | 12 |
| Hungría | HUN | 997 |  |  |  |  |  |  |  | 3 | 39 | 28 | 66 | 284 | 102 |
| India | IND | 1,616 |  |  |  |  |  |  | 5 | 4 | 63 | 41 | 321 | 573 | 150 |
| Indonesia | IDN | 1,435 | 1 |  |  |  |  |  | 1 | 1 | 15 | 117 | 76 | 174 | 213 |
| Irak | IRQ | 494 |  |  |  |  | 1 |  |  | 3 | 32 | 24 | 25 | 92 | 145 |
| Irlanda | IRL | 1,568 |  |  |  |  |  |  |  | 1 | 31 | 65 | 100 | 574 | 33 |
| Irán | IRN | 442 |  |  |  |  |  |  |  | 5 | 40 | 17 | 65 | 159 | 68 |
| Isla Norfolk | NFK | 1,324 |  |  |  |  |  |  |  |  |  | 1 | 35 | 1,076 | 206 |
| Isla Santa Elena | SHN | 102 |  |  |  |  |  |  |  |  | 1 | 2 | 5 | 82 | 5 |
| Isla de Man | IMN | 29 |  |  |  |  |  |  |  |  |  |  | 2 | 19 |  |
| Islandia | ISL | 107 |  |  |  |  |  |  |  |  | 6 | 8 | 10 | 38 | 19 |
| Islas Caimán | CYM | 9 |  |  |  |  |  |  |  |  |  |  | 1 | 1 | 7 |
| Islas Feroe | FRO | 4 |  |  |  |  |  |  |  |  |  | 1 | 1 | 2 |  |
| Islas Georgias del Sur y Sandwich del Sur | SGS | 2 |  |  |  |  |  |  |  |  |  |  |  |  | 1 |
| Islas Malvinas | FLK | 33 |  |  |  |  |  |  |  |  |  | 11 | 10 | 6 | 3 |
| Islas Marianas del Norte | MNP | 25 |  |  |  |  |  |  |  |  |  |  |  | 2 | 20 |
| Islas Marshall | MHL | 17 |  |  |  |  |  |  |  |  |  |  |  | 3 | 14 |
| Islas Pitcairn | PCN | 10 |  |  |  |  |  |  |  |  |  |  | 1 | 1 | 8 |
| Islas Salomón | SLB | 35 |  |  |  |  |  |  |  |  | 1 | 2 | 1 | 5 | 12 |
| Islas Turcas y Caicos | TCA | 6 |  |  |  |  |  |  |  |  |  |  | 2 | 2 | 2 |
| Islas Vírgenes Británicas | VGB | 9 |  |  |  |  |  |  |  |  |  |  | 3 | 1 | 5 |
| Islas Vírgenes de los Estados Unidos | VIR | 101 |  |  |  |  |  |  |  |  |  | 1 | 49 | 2 | 44 |
| Israel | ISR | 1,241 |  |  |  |  |  | 1 | 2 | 9 | 53 | 61 | 156 | 428 | 112 |
| Italia | ITA | 5,132 | 2 |  |  | 2 | 4 | 1 |  | 12 | 217 | 340 | 306 | 1,300 | 469 |
| Jamaica | JAM | 828 |  |  |  |  |  |  |  | 1 | 1 | 15 | 199 | 543 | 46 |
| Japón | JPN | 1,117 |  |  |  |  |  |  |  | 2 | 7 | 41 | 131 | 294 | 229 |
| Jersey | JEY | 13 |  |  |  |  |  |  |  |  |  | 4 |  | 8 |  |
| Jordania | JOR | 380 |  |  |  |  |  |  |  | 1 | 37 | 18 | 22 | 148 | 27 |
| Kazajistán | KAZ | 111 |  |  |  |  |  |  |  | 1 | 15 | 15 | 4 | 22 | 22 |
| Kenia | KEN | 219 |  |  |  |  |  |  |  |  | 2 | 4 | 1 | 21 | 152 |
| Kirguistán | KGZ | 42 |  |  |  |  |  |  |  |  | 7 | 2 |  | 15 | 10 |
| Kiribati | KIR | 22 |  |  |  |  |  |  |  |  |  |  |  | 14 | 8 |
| Kosovo | KOS | 51 |  |  |  |  |  |  |  |  | 1 | 2 | 2 |  | 28 |
| Kuwait | KWT | 67 |  |  |  |  |  |  |  | 3 | 7 | 5 | 12 | 12 | 13 |
| Laos | LAO | 64 |  |  |  |  |  |  |  | 1 | 3 |  |  | 8 | 17 |
| Lesoto | LSO | 90 |  |  |  |  |  |  |  |  |  |  | 1 | 12 | 72 |
| Letonia | LVA | 192 |  |  |  |  |  |  |  | 2 | 12 | 11 | 11 | 18 | 75 |
| Liberia | LBR | 132 |  |  |  |  |  |  |  |  | 2 | 2 | 4 | 68 | 38 |
| Libia | LBY | 267 |  |  |  |  |  |  |  | 6 | 22 | 17 | 13 | 33 | 103 |
| Liechtenstein | LIE | 13 |  |  |  |  |  |  |  | 1 |  | 1 |  | 3 |  |
| Lituania | LTU | 279 |  |  |  |  |  |  |  | 2 | 13 | 14 | 41 | 20 | 48 |
| Luxemburgo | LUX | 273 |  |  |  |  |  |  |  |  | 6 | 22 | 44 | 35 | 19 |
| Líbano | LBN | 668 |  |  |  |  |  |  |  | 1 | 17 | 6 | 15 | 447 | 117 |
| Macao | MAC | 79 |  |  |  |  |  |  |  |  |  | 1 | 13 | 18 | 33 |
| Macedonia del Norte | MKD | 115 |  |  |  |  |  |  |  | 2 | 13 | 11 | 5 | 19 | 24 |
| Madagascar | MDG | 162 |  |  |  |  |  |  |  |  | 5 | 9 | 27 | 46 | 36 |
| Malasia | MYS | 202 |  |  |  |  |  |  |  |  | 4 | 5 | 5 | 22 | 33 |
| Malaui | MWI | 34 |  |  |  |  |  |  |  |  | 1 |  | 2 | 13 | 14 |
| Maldivas | MDV | 12 |  |  |  |  |  |  |  |  |  |  | 4 |  | 7 |
| Malta | MLT | 154 |  |  |  |  |  |  |  |  | 10 | 16 | 64 | 33 | 8 |
| Malí | MLI | 98 |  |  |  |  |  |  | 1 | 2 | 4 | 5 | 7 | 12 | 17 |
| Marruecos | MAR | 416 |  |  |  |  |  |  |  | 1 | 11 | 32 | 56 | 98 | 115 |
| Mauricio | MUS | 72 |  |  |  |  |  |  |  |  |  | 1 | 8 | 22 | 9 |
| Mauritania | MRT | 75 |  |  |  |  |  |  |  |  | 6 | 3 | 12 | 13 | 14 |
| Moldavia | MDA | 109 |  |  |  |  |  |  |  | 1 | 5 | 8 | 18 | 25 | 10 |
| Mongolia | MNG | 93 |  |  |  |  |  |  |  |  | 1 | 9 | 4 | 29 | 36 |
| Montenegro | MNE | 103 |  |  |  |  |  |  |  |  | 8 | 8 | 5 | 22 | 19 |
| Montserrat | MSR | 130 |  |  |  |  |  |  |  |  |  |  |  | 105 | 21 |
| Mozambique | MOZ | 177 |  |  |  |  |  |  |  |  | 6 | 6 | 15 | 52 | 45 |
| México | MEX | 3,129 |  |  |  |  |  |  |  | 3 | 54 | 103 | 316 | 902 | 1,260 |
| Mónaco | MCO | 10 |  |  |  |  |  |  |  |  |  |  | 3 | 2 | 4 |
| Namibia | NAM | 132 |  |  |  |  |  |  |  |  | 3 |  | 6 | 41 | 28 |
| Nauru | NRU | 6 |  |  |  |  |  |  |  |  |  |  |  |  | 5 |
| Nepal | NPL | 46 |  |  |  |  |  |  |  | 1 | 3 | 2 |  | 8 | 14 |
| Nicaragua | NIC | 282 |  |  |  |  |  |  |  |  |  | 24 | 22 | 154 | 67 |
| Nigeria | NGA | 119 |  |  |  |  |  |  |  |  | 3 | 8 | 7 | 8 | 53 |
| Noruega | NOR | 832 |  |  |  |  |  |  |  | 2 | 5 | 19 | 24 | 267 | 26 |
| Nueva Caledonia | NCL | 9 |  |  |  |  |  |  |  |  |  |  | 1 | 3 | 5 |
| Nueva Zelanda | NZL | 195 |  |  |  |  |  |  |  |  |  |  | 3 | 132 | 21 |
| Níger | NER | 70 |  |  |  |  |  |  |  |  | 4 | 5 | 3 | 5 | 26 |
| Omán | OMN | 76 |  |  |  |  |  |  |  | 4 | 12 | 6 | 13 | 16 | 9 |
| PSX | PSX | 298 |  |  |  |  |  |  |  | 1 | 17 | 8 | 7 | 106 | 2 |
| Pakistán | PAK | 382 |  |  |  |  |  |  |  |  | 28 | 7 | 10 | 99 | 116 |
| Palaos | PLW | 40 |  |  |  |  |  |  |  |  |  | 1 | 2 | 9 | 19 |
| Palestina | PSE | 1,073 |  |  |  |  |  |  |  | 6 | 42 | 33 | 67 | 492 | 178 |
| Panamá | PAN | 304 |  |  |  |  |  |  |  |  | 2 | 42 | 44 | 73 | 99 |
| Papúa Nueva Guinea | PNG | 65 |  |  |  |  |  |  |  |  | 1 | 4 | 2 | 14 | 33 |
| Paraguay | PRY | 195 |  |  |  |  |  |  |  |  |  | 12 | 42 | 65 | 56 |
| Países Bajos | NLD | 18,181 |  |  | 1 |  |  |  |  | 1 | 94 | 352 | 452 | 412 | 1,023 |
| Perú | PER | 734 |  |  |  |  |  |  |  |  | 19 | 46 | 65 | 329 | 216 |
| Polinesia Francesa | PYF | 69 |  |  |  |  |  |  |  |  |  | 1 | 35 | 26 | 5 |
| Polonia | POL | 2,798 |  |  |  |  | 1 |  | 1 | 6 | 41 | 52 | 155 | 606 | 472 |
| Portugal | PRT | 2,428 | 1 |  |  |  |  |  |  | 2 | 50 | 129 | 463 | 976 | 206 |
| Puerto Rico | PRI | 1,046 |  |  |  |  |  |  |  | 1 | 1 | 10 | 70 | 38 | 902 |
| Reino Unido | GBR | 8,921 |  |  |  |  | 2 | 8 |  | 1 | 55 | 429 | 1,204 | 2,254 | 485 |
| República Centroafricana | CAF | 155 |  |  |  |  |  |  |  |  |  | 2 | 3 | 8 | 112 |
| República Checa | CZE | 1,090 |  |  |  |  |  |  |  | 1 | 16 | 31 | 57 | 190 | 213 |
| República Democrática del Congo | COD | 224 |  |  |  |  |  |  |  |  | 3 | 6 | 9 | 31 | 128 |
| República Dominicana | DOM | 224 |  |  |  |  |  |  |  |  | 4 | 22 | 65 | 45 | 49 |
| República Turca del Norte de Chipre | CYN | 15 |  |  |  |  |  |  |  |  | 2 | 5 |  |  |  |
| República de China | TWN | 155 |  |  |  |  |  |  |  |  | 1 | 11 | 3 | 43 | 64 |
| República del Congo | COG | 154 |  |  |  |  |  |  |  | 1 | 3 | 5 | 16 | 43 | 51 |
| Ruanda | RWA | 24 |  |  |  |  |  |  |  |  |  |  |  | 3 | 17 |
| Rumania | ROU | 1,021 |  |  |  |  |  |  |  | 3 | 37 | 21 | 41 | 162 | 172 |
| Rusia | RUS | 4,118 |  |  |  |  |  |  |  | 5 | 63 | 107 | 234 | 1,582 | 1,181 |
| SAH | SAH | 4 |  |  |  |  |  |  |  |  |  | 2 |  | 1 |  |
| SDS | SDS | 82 |  |  |  |  |  |  |  |  |  | 1 |  | 10 | 19 |
| Sahara Occidental | ESH | 24 |  |  |  |  |  |  | 1 |  |  | 2 |  | 9 | 11 |
| Samoa | WSM | 39 |  |  |  |  |  |  |  |  |  |  | 3 | 21 | 15 |
| Samoa Estadounidense | ASM | 24 |  |  |  |  |  |  |  |  |  |  |  | 13 | 6 |
| San Bartolomé | BLM | 5 |  |  |  |  |  |  |  |  |  |  | 3 | 2 |  |
| San Cristóbal y Nieves | KNA | 18 |  |  |  |  |  |  |  |  |  | 2 | 12 | 1 | 3 |
| San Marino | SMR | 2 |  |  |  |  |  |  |  |  |  |  |  | 1 | 1 |
| San Martín | MAF | 42 |  |  |  |  |  |  |  |  |  |  | 5 | 26 | 6 |
| San Martín | SXM | 17 |  |  |  |  |  |  |  | 1 |  |  | 4 | 8 | 1 |
| San Pedro y Miquelón | SPM | 7 |  |  |  |  |  |  |  |  |  |  | 1 | 5 | 1 |
| San Vicente y las Granadinas | VCT | 19 |  |  |  |  |  |  |  |  |  |  | 6 | 10 | 3 |
| Santa Lucía | LCA | 28 |  |  |  |  |  |  |  |  |  | 1 | 19 | 4 | 4 |
| Santo Tomé y Príncipe | STP | 10 |  |  |  |  |  |  |  |  |  | 1 | 8 |  | 1 |
| Senegal | SEN | 82 |  |  |  |  |  |  |  |  | 2 | 3 | 28 | 20 | 10 |
| Serbia | SRB | 483 |  |  |  |  |  |  |  | 4 | 26 | 14 | 27 | 128 | 66 |
| Seychelles | SYC | 2 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |
| Sierra Leona | SLE | 135 |  |  |  |  |  |  |  |  | 2 | 3 | 10 | 14 | 97 |
| Singapur | SGP | 40 |  |  |  |  |  |  |  | 1 |  |  | 1 | 19 | 5 |
| Siria | SYR | 746 |  |  |  |  |  |  |  | 4 | 41 | 31 | 58 | 372 | 85 |
| Somalia | SOM | 169 |  |  |  |  |  |  |  | 1 | 11 | 7 | 6 | 14 | 98 |
| Somalilandia | SOL | 213 |  |  |  |  |  |  |  |  | 2 | 4 |  | 32 | 161 |
| Sri Lanka | LKA | 176 |  |  |  |  |  |  | 2 | 2 | 11 | 13 | 17 | 48 | 18 |
| Suazilandia | SWZ | 42 |  |  |  |  |  |  |  |  |  |  |  | 3 | 37 |
| Sudáfrica | ZAF | 547 |  |  |  |  |  |  |  |  | 4 | 3 | 22 | 221 | 159 |
| Sudán | SDN | 463 |  |  |  |  |  |  |  | 2 | 9 | 15 | 13 | 78 | 248 |
| Sudán del Sur | SSD | 202 |  |  |  |  |  |  |  |  | 1 | 4 | 2 | 17 | 89 |
| Suecia | SWE | 1,159 |  |  |  |  |  |  |  | 2 | 13 | 31 | 45 | 248 | 43 |
| Suiza | CHE | 1,976 | 1 |  |  |  |  |  |  | 3 | 48 | 49 | 90 | 375 | 145 |
| Surinam | SUR | 371 |  |  |  |  |  |  |  |  | 3 | 14 | 23 | 17 | 38 |
| Tailandia | THA | 150 |  |  |  |  |  |  |  |  | 5 | 3 | 11 | 48 | 36 |
| Tanzania | TZA | 202 |  |  |  |  |  |  |  |  | 3 | 2 | 2 | 48 | 81 |
| Tayikistán | TJK | 47 |  |  |  |  |  |  |  |  | 6 |  |  | 20 | 11 |
| Territorio Británico del Océano Índico | IOT | 1 |  |  |  |  |  |  |  |  |  |  |  |  | 1 |
| Territorios Australianos del Océano Índico | IOA | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Tierras Australes y Antárticas Francesas | ATF | 4 |  |  |  |  |  |  |  |  |  |  |  | 1 |  |
| Timor Oriental | TLS | 15 |  |  |  |  |  |  |  |  |  |  |  |  | 2 |
| Togo | TGO | 36 |  |  |  |  |  |  |  |  |  | 1 | 2 | 2 | 12 |
| Tonga | TON | 12 |  |  |  |  |  |  |  |  |  | 1 | 1 | 5 | 4 |
| Trinidad y Tobago | TTO | 60 |  |  |  |  |  |  |  |  |  | 12 | 21 | 6 | 20 |
| Turkmenistán | TKM | 112 |  |  |  |  |  |  |  |  | 14 | 5 | 3 | 46 | 20 |
| Turquía | TUR | 1,388 |  |  |  |  |  |  | 1 | 3 | 59 | 57 | 124 | 568 | 233 |
| Tuvalu | TUV | 8 |  |  |  |  |  |  |  |  |  |  |  | 5 | 3 |
| Túnez | TUN | 436 |  |  |  |  |  |  |  | 2 | 26 | 7 | 15 | 164 | 158 |
| UMI | UMI | 2 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |
| USG | USG | 3 |  |  |  |  |  |  |  |  |  |  | 1 | 1 |  |
| Ucrania | UKR | 687 |  |  |  |  |  |  | 2 | 4 | 30 | 48 | 49 | 90 | 84 |
| Uganda | UGA | 198 |  |  |  |  |  |  |  |  | 1 | 3 | 3 | 14 | 146 |
| Uruguay | URY | 256 |  |  |  |  |  |  |  |  | 1 | 22 | 45 | 90 | 68 |
| Uzbekistán | UZB | 102 |  |  |  |  |  |  |  |  | 7 | 4 | 2 | 48 | 26 |
| Vanuatu | VUT | 12 |  |  |  |  |  |  |  |  |  |  |  | 2 | 10 |
| Venezuela | VEN | 410 |  |  |  |  |  |  |  |  | 9 | 69 | 104 | 83 | 72 |
| Vietnam | VNM | 245 |  |  |  |  |  |  |  | 1 | 4 | 3 | 6 | 26 | 51 |
| Yemen | YEM | 397 |  |  |  |  |  |  |  | 4 | 16 | 11 | 14 | 35 | 271 |
| Yibuti | DJI | 50 |  |  |  |  |  |  |  |  | 2 | 2 | 3 | 26 | 15 |
| Zambia | ZMB | 101 |  |  |  |  |  |  |  |  | 1 | 3 | 4 | 19 | 45 |
| Zimbabue | ZWE | 107 |  |  |  |  |  |  |  |  | 2 | 1 | 5 | 25 | 43 |
| Åland | ALA | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |
