# Biblioteca de Cartographer

Documento generado por `scripts/comprender.py`. No editar a mano.

- Mapas analizados: **758,715** · con país asignado: **474,122** · sin país: 284,593
  (sobre todo mapamundis, cartas oceánicas o registros sin datos de lugar).
- Países con mapas: **243**.
- Tipos: general 503,563, topográfico 201,829, plano urbano 23,400, militar 9,367, histórico/temático 6,990, mapamundi 4,999, ferroviario/viario 4,510, carta náutica 3,440, portulano 448, ptolemaico 169.
- Escalas: desconocida 488,919, local o ciudad 245,025, provincia o comarca 14,152, región o país 6,100, continente 2,997, mundo 1,522.

Cómo se asigna un país: por **nombre** actual (25+ idiomas, Natural Earth), por **nombre histórico**
(`catalogo/nombres_historicos.json`) o por **coordenadas** de la cobertura del mapa. Cada mapa guarda
la vía en el campo `via`; las asignaciones por coordenadas de mapas grandes pueden incluir países
vecinos. Los siglos salen del año de los metadatos de cada archivo y pueden tener errores puntuales.

Mapas de un país: `catalogo/biblioteca/paises/<ISO3>.jsonl.gz` o
`python scripts/buscar_lugar.py "<país>"`.

| País | ISO | Total | Antes del s. IX | IX | X | XI | XII | XIII | XIV | XV | XVI | XVII | XVIII | XIX | XX |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Afganistán | AFG | 371 |  |  |  |  |  |  |  |  | 21 | 6 | 9 | 146 | 100 |
| Albania | ALB | 262 |  |  |  |  |  |  | 1 | 3 | 23 | 22 | 19 | 63 | 48 |
| Alemania | DEU | 12,970 | 1 |  |  |  |  |  |  | 4 | 96 | 208 | 334 | 1,510 | 816 |
| Andorra | AND | 27 |  |  |  |  |  |  |  |  |  |  | 1 | 2 | 18 |
| Angola | AGO | 189 |  |  |  |  |  |  |  |  | 3 | 9 | 13 | 48 | 88 |
| Anguila | AIA | 7 |  |  |  |  |  |  |  |  |  |  | 6 | 1 |  |
| Antigua y Barbuda | ATG | 26 |  |  |  |  |  |  |  |  |  | 1 | 13 | 10 | 1 |
| Antártida | ATA | 89 |  |  |  |  |  |  |  |  |  | 8 | 11 | 9 | 50 |
| Arabia Saudita | SAU | 502 |  |  |  |  |  |  |  | 6 | 45 | 32 | 51 | 145 | 126 |
| Argelia | DZA | 393 |  |  |  |  |  |  |  | 2 | 20 | 21 | 33 | 103 | 102 |
| Argentina | ARG | 753 |  |  |  |  |  |  |  |  | 7 | 98 | 95 | 124 | 355 |
| Armenia | ARM | 141 |  |  |  |  |  |  | 1 | 1 | 11 | 7 | 15 | 61 | 21 |
| Aruba | ABW | 22 |  |  |  |  |  |  |  |  |  |  | 2 | 6 | 4 |
| Australia | AUS | 1,952 |  |  |  |  |  |  |  |  | 1 | 7 | 18 | 275 | 63 |
| Austria | AUT | 1,583 | 1 |  |  |  |  |  |  | 2 | 38 | 36 | 63 | 385 | 254 |
| Azerbaiyán | AZE | 94 |  |  |  |  |  |  |  | 1 | 8 | 4 | 5 | 30 | 22 |
| Bahamas | BHS | 138 |  |  |  |  |  |  |  |  |  | 4 | 58 | 49 | 22 |
| Bangladés | BGD | 53 |  |  |  |  |  |  |  | 1 | 3 | 5 | 4 | 7 | 8 |
| Barbados | BRB | 84 |  |  |  |  |  |  |  |  |  | 6 | 33 | 6 | 23 |
| Baréin | BHR | 63 |  |  |  |  |  |  |  | 2 | 6 | 6 | 9 | 14 | 16 |
| Belice | BLZ | 67 |  |  |  |  |  |  |  |  |  | 9 | 5 | 15 | 34 |
| Benín | BEN | 47 |  |  |  |  |  |  |  |  | 3 | 6 |  | 2 | 16 |
| Bermudas | BMU | 78 |  |  |  |  |  |  |  |  |  | 11 | 30 | 22 | 8 |
| Bielorrusia | BLR | 243 |  |  |  |  |  |  |  | 3 | 22 | 19 | 25 | 22 | 54 |
| Birmania | MMR | 151 |  |  |  |  |  |  |  |  | 8 | 5 | 14 | 38 | 37 |
| Bolivia | BOL | 194 |  |  |  |  |  |  |  |  | 5 | 15 | 9 | 66 | 73 |
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
| Camboya | KHM | 92 |  |  |  |  |  |  |  |  | 1 | 1 | 1 | 10 | 47 |
| Camerún | CMR | 98 |  |  |  |  |  |  |  |  | 2 | 4 | 8 | 9 | 43 |
| Canadá | CAN | 5,389 |  |  |  |  |  |  |  |  | 13 | 81 | 1,392 | 1,541 | 1,551 |
| Catar | QAT | 55 |  |  |  |  |  |  |  | 3 | 8 | 7 | 11 | 13 | 10 |
| Chad | TCD | 67 |  |  |  |  |  |  |  |  |  | 3 | 4 | 10 | 29 |
| Chile | CHL | 698 |  |  |  |  |  |  |  | 2 | 6 | 108 | 134 | 263 | 128 |
| China | CHN | 3,495 |  |  |  |  | 8 | 1 | 2 | 4 | 35 | 96 | 335 | 1,413 | 1,124 |
| Chipre | CYP | 178 |  |  |  |  |  |  |  | 1 | 10 | 13 | 11 | 18 | 91 |
| Ciudad del Vaticano | VAT | 40 |  |  |  |  |  |  |  |  | 1 | 24 | 1 | 3 | 3 |
| Colombia | COL | 492 |  |  |  |  |  |  |  |  | 10 | 55 | 101 | 103 | 141 |
| Comoras | COM | 9 |  |  |  |  |  |  |  |  |  |  |  | 2 | 7 |
| Corea del Norte | PRK | 134 |  |  |  |  |  |  |  |  | 1 | 9 | 11 | 13 | 54 |
| Corea del Sur | KOR | 727 |  |  |  |  |  |  |  |  | 2 | 12 | 50 | 117 | 199 |
| Costa Rica | CRI | 169 |  |  |  |  |  |  |  |  |  | 14 | 15 | 39 | 89 |
| Costa de Marfil | CIV | 84 |  |  |  |  |  |  |  |  | 3 | 5 | 9 | 10 | 25 |
| Croacia | HRV | 734 |  |  |  |  |  |  |  | 6 | 41 | 18 | 34 | 188 | 69 |
| Cuba | CUB | 963 |  |  |  |  |  |  |  | 1 | 7 | 99 | 217 | 261 | 241 |
| Curazao | CUW | 81 |  |  |  |  |  |  |  |  |  |  | 19 | 10 | 2 |
| Dinamarca | DNK | 1,040 |  |  |  |  |  |  | 1 |  | 10 | 47 | 47 | 275 | 69 |
| Dominica | DMA | 15 |  |  |  |  |  |  |  |  |  |  | 12 | 2 |  |
| ESB | ESB | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ecuador | ECU | 253 |  |  |  |  |  |  |  |  | 8 | 19 | 36 | 65 | 85 |
| Egipto | EGY | 1,921 |  |  |  |  | 1 | 1 |  | 3 | 44 | 39 | 114 | 779 | 752 |
| El Salvador | SLV | 154 |  |  |  |  |  |  |  |  |  | 2 | 4 | 86 | 54 |
| Emiratos Árabes Unidos | ARE | 53 |  |  |  |  |  |  |  | 3 | 7 | 6 | 12 | 13 | 6 |
| Eritrea | ERI | 398 |  |  |  |  |  |  |  |  | 1 | 6 | 7 | 99 | 260 |
| Eslovaquia | SVK | 494 |  |  |  |  |  |  |  | 2 | 16 | 13 | 19 | 94 | 101 |
| Eslovenia | SVN | 305 |  |  |  |  |  |  |  | 2 | 20 | 7 | 3 | 15 | 106 |
| España | ESP | 6,983 | 6 |  |  |  | 1 | 1 | 6 | 13 | 95 | 285 | 1,368 | 2,641 | 977 |
| Estados Federados de Micronesia | FSM | 44 |  |  |  |  |  |  |  |  |  | 1 | 1 | 11 | 25 |
| Estados Unidos | USA | 367,013 | 3 |  |  |  |  |  |  | 4 | 29 | 519 | 5,124 | 116,660 | 213,171 |
| Estonia | EST | 954 |  |  |  |  |  |  |  |  | 2 | 11 | 14 | 79 | 489 |
| Etiopía | ETH | 441 |  |  |  |  |  | 1 |  | 1 | 11 | 15 | 12 | 104 | 222 |
| Filipinas | PHL | 366 |  |  |  |  |  |  |  |  | 5 | 5 | 56 | 72 | 179 |
| Finlandia | FIN | 201 |  |  |  |  |  |  |  | 1 | 8 | 15 | 18 | 32 | 29 |
| Fiyi | FJI | 43 |  |  |  |  |  |  |  |  |  | 1 |  | 29 | 10 |
| Francia | FRA | 11,984 |  |  | 1 |  | 1 | 1 | 1 | 3 | 138 | 468 | 1,496 | 3,957 | 623 |
| GIB | GIB | 5 |  |  |  |  |  |  |  |  |  |  | 5 |  |  |
| Gabón | GAB | 56 |  |  |  |  |  |  |  |  | 2 | 5 | 7 | 6 | 12 |
| Gambia | GMB | 27 |  |  |  |  |  |  |  |  |  | 2 | 11 | 9 | 4 |
| Georgia | GEO | 230 |  |  |  |  |  |  |  | 1 | 11 | 4 | 48 | 60 | 40 |
| Ghana | GHA | 81 |  |  |  |  |  |  |  |  | 2 | 7 | 7 | 8 | 19 |
| Granada | GRD | 336 |  |  |  |  |  |  |  |  |  | 19 | 61 | 207 | 27 |
| Grecia | GRC | 1,278 |  |  |  |  |  |  |  | 3 | 75 | 93 | 89 | 506 | 178 |
| Groenlandia | GRL | 150 |  |  |  |  |  |  | 1 |  | 6 | 11 | 31 | 74 | 13 |
| Guam | GUM | 24 |  |  |  |  |  |  |  |  |  |  | 4 | 6 | 3 |
| Guatemala | GTM | 152 |  |  |  |  |  |  |  |  | 2 | 15 | 10 | 38 | 72 |
| Guernsey | GGY | 217 |  |  |  |  |  |  |  |  |  | 4 |  | 102 | 109 |
| Guinea | GIN | 84 |  |  |  |  |  |  |  |  | 1 | 11 | 32 | 10 | 12 |
| Guinea Ecuatorial | GNQ | 38 |  |  |  |  |  |  |  |  | 1 |  | 2 | 11 | 18 |
| Guinea-Bisáu | GNB | 6 |  |  |  |  |  |  |  |  |  |  | 2 | 2 | 2 |
| Guyana | GUY | 240 |  |  |  |  |  |  |  |  | 3 | 20 | 30 | 46 | 51 |
| Haití | HTI | 342 |  |  |  |  |  |  |  |  | 4 | 17 | 102 | 60 | 118 |
| Honduras | HND | 233 |  |  |  |  |  |  |  |  |  | 26 | 47 | 60 | 83 |
| Hong Kong | HKG | 43 |  |  |  |  |  |  |  |  |  |  |  | 21 | 12 |
| Hungría | HUN | 995 |  |  |  |  |  |  |  | 3 | 39 | 28 | 66 | 283 | 102 |
| India | IND | 1,600 |  |  |  |  |  |  | 5 | 2 | 61 | 41 | 319 | 564 | 149 |
| Indonesia | IDN | 1,432 | 1 |  |  |  |  |  | 1 |  | 15 | 117 | 75 | 174 | 213 |
| Irak | IRQ | 491 |  |  |  |  | 1 |  |  | 3 | 31 | 24 | 25 | 92 | 143 |
| Irlanda | IRL | 1,563 |  |  |  |  |  |  |  | 1 | 30 | 65 | 99 | 573 | 31 |
| Irán | IRN | 437 |  |  |  |  |  |  |  | 5 | 40 | 17 | 61 | 158 | 68 |
| Isla Norfolk | NFK | 1,318 |  |  |  |  |  |  |  |  |  | 1 | 35 | 1,074 | 202 |
| Isla Santa Elena | SHN | 102 |  |  |  |  |  |  |  |  | 1 | 2 | 5 | 82 | 5 |
| Isla de Man | IMN | 29 |  |  |  |  |  |  |  |  |  |  | 2 | 19 |  |
| Islandia | ISL | 105 |  |  |  |  |  |  |  |  | 5 | 8 | 10 | 38 | 18 |
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
| Israel | ISR | 1,236 |  |  |  |  |  | 1 | 1 | 9 | 53 | 61 | 156 | 426 | 110 |
| Italia | ITA | 5,106 | 2 |  |  | 2 | 4 | 1 |  | 12 | 204 | 340 | 306 | 1,294 | 462 |
| Jamaica | JAM | 828 |  |  |  |  |  |  |  | 1 | 1 | 15 | 199 | 543 | 46 |
| Japón | JPN | 1,112 |  |  |  |  |  |  |  | 1 | 6 | 41 | 131 | 294 | 227 |
| Jersey | JEY | 13 |  |  |  |  |  |  |  |  |  | 4 |  | 8 |  |
| Jordania | JOR | 380 |  |  |  |  |  |  |  | 1 | 37 | 18 | 22 | 148 | 27 |
| Kazajistán | KAZ | 111 |  |  |  |  |  |  |  | 1 | 15 | 15 | 4 | 22 | 22 |
| Kenia | KEN | 214 |  |  |  |  |  |  |  |  | 2 | 4 | 1 | 21 | 147 |
| Kirguistán | KGZ | 42 |  |  |  |  |  |  |  |  | 7 | 2 |  | 15 | 10 |
| Kiribati | KIR | 22 |  |  |  |  |  |  |  |  |  |  |  | 14 | 8 |
| Kosovo | KOS | 49 |  |  |  |  |  |  |  |  | 1 | 2 | 2 |  | 26 |
| Kuwait | KWT | 67 |  |  |  |  |  |  |  | 3 | 7 | 5 | 12 | 12 | 13 |
| Laos | LAO | 63 |  |  |  |  |  |  |  | 1 | 3 |  |  | 8 | 16 |
| Lesoto | LSO | 90 |  |  |  |  |  |  |  |  |  |  | 1 | 12 | 72 |
| Letonia | LVA | 192 |  |  |  |  |  |  |  | 2 | 12 | 11 | 11 | 18 | 75 |
| Liberia | LBR | 132 |  |  |  |  |  |  |  |  | 2 | 2 | 4 | 68 | 38 |
| Libia | LBY | 264 |  |  |  |  |  |  |  | 6 | 22 | 17 | 11 | 32 | 103 |
| Liechtenstein | LIE | 13 |  |  |  |  |  |  |  | 1 |  | 1 |  | 3 |  |
| Lituania | LTU | 278 |  |  |  |  |  |  |  | 2 | 12 | 14 | 41 | 20 | 48 |
| Luxemburgo | LUX | 273 |  |  |  |  |  |  |  |  | 6 | 22 | 44 | 35 | 19 |
| Líbano | LBN | 663 |  |  |  |  |  |  |  | 1 | 17 | 6 | 15 | 444 | 115 |
| Macao | MAC | 73 |  |  |  |  |  |  |  |  |  | 1 | 13 | 16 | 33 |
| Macedonia del Norte | MKD | 115 |  |  |  |  |  |  |  | 2 | 13 | 11 | 5 | 19 | 24 |
| Madagascar | MDG | 155 |  |  |  |  |  |  |  |  | 5 | 9 | 25 | 41 | 36 |
| Malasia | MYS | 202 |  |  |  |  |  |  |  |  | 4 | 5 | 5 | 22 | 33 |
| Malaui | MWI | 34 |  |  |  |  |  |  |  |  | 1 |  | 2 | 13 | 14 |
| Maldivas | MDV | 12 |  |  |  |  |  |  |  |  |  |  | 4 |  | 7 |
| Malta | MLT | 152 |  |  |  |  |  |  |  |  | 10 | 16 | 64 | 31 | 8 |
| Malí | MLI | 96 |  |  |  |  |  |  | 1 |  | 4 | 5 | 7 | 12 | 17 |
| Marruecos | MAR | 413 |  |  |  |  |  |  |  | 1 | 11 | 32 | 55 | 96 | 115 |
| Mauricio | MUS | 71 |  |  |  |  |  |  |  |  |  | 1 | 8 | 21 | 9 |
| Mauritania | MRT | 75 |  |  |  |  |  |  |  |  | 6 | 3 | 12 | 13 | 14 |
| Moldavia | MDA | 109 |  |  |  |  |  |  |  | 1 | 5 | 8 | 18 | 25 | 10 |
| Mongolia | MNG | 93 |  |  |  |  |  |  |  |  | 1 | 9 | 4 | 29 | 36 |
| Montenegro | MNE | 103 |  |  |  |  |  |  |  |  | 8 | 8 | 5 | 22 | 19 |
| Montserrat | MSR | 130 |  |  |  |  |  |  |  |  |  |  |  | 105 | 21 |
| Mozambique | MOZ | 175 |  |  |  |  |  |  |  |  | 6 | 6 | 15 | 52 | 43 |
| México | MEX | 3,124 |  |  |  |  |  |  |  | 3 | 54 | 103 | 314 | 899 | 1,260 |
| Mónaco | MCO | 8 |  |  |  |  |  |  |  |  |  |  | 3 | 1 | 3 |
| Namibia | NAM | 132 |  |  |  |  |  |  |  |  | 3 |  | 6 | 41 | 28 |
| Nauru | NRU | 6 |  |  |  |  |  |  |  |  |  |  |  |  | 5 |
| Nepal | NPL | 46 |  |  |  |  |  |  |  | 1 | 3 | 2 |  | 8 | 14 |
| Nicaragua | NIC | 280 |  |  |  |  |  |  |  |  |  | 24 | 22 | 152 | 67 |
| Nigeria | NGA | 118 |  |  |  |  |  |  |  |  | 3 | 8 | 7 | 8 | 52 |
| Noruega | NOR | 832 |  |  |  |  |  |  |  | 2 | 5 | 19 | 24 | 267 | 26 |
| Nueva Caledonia | NCL | 9 |  |  |  |  |  |  |  |  |  |  | 1 | 3 | 5 |
| Nueva Zelanda | NZL | 193 |  |  |  |  |  |  |  |  |  |  | 3 | 132 | 19 |
| Níger | NER | 70 |  |  |  |  |  |  |  |  | 4 | 5 | 3 | 5 | 26 |
| Omán | OMN | 75 |  |  |  |  |  |  |  | 4 | 12 | 6 | 13 | 16 | 9 |
| PSX | PSX | 298 |  |  |  |  |  |  |  | 1 | 17 | 8 | 7 | 106 | 2 |
| Pakistán | PAK | 382 |  |  |  |  |  |  |  |  | 28 | 7 | 10 | 99 | 116 |
| Palaos | PLW | 40 |  |  |  |  |  |  |  |  |  | 1 | 2 | 9 | 19 |
| Palestina | PSE | 1,060 |  |  |  |  |  |  |  | 6 | 42 | 33 | 67 | 492 | 169 |
| Panamá | PAN | 304 |  |  |  |  |  |  |  |  | 2 | 42 | 44 | 73 | 99 |
| Papúa Nueva Guinea | PNG | 65 |  |  |  |  |  |  |  |  | 1 | 4 | 2 | 14 | 33 |
| Paraguay | PRY | 190 |  |  |  |  |  |  |  |  |  | 12 | 38 | 64 | 56 |
| Países Bajos | NLD | 18,177 |  |  | 1 |  |  |  |  | 1 | 94 | 351 | 451 | 412 | 1,022 |
| Perú | PER | 733 |  |  |  |  |  |  |  |  | 19 | 45 | 65 | 329 | 216 |
| Polinesia Francesa | PYF | 69 |  |  |  |  |  |  |  |  |  | 1 | 35 | 26 | 5 |
| Polonia | POL | 2,794 |  |  |  |  |  |  | 1 | 6 | 41 | 52 | 155 | 603 | 472 |
| Portugal | PRT | 2,425 | 1 |  |  |  |  |  |  | 2 | 50 | 129 | 463 | 973 | 206 |
| Puerto Rico | PRI | 1,041 |  |  |  |  |  |  |  | 1 | 1 | 10 | 70 | 38 | 897 |
| Reino Unido | GBR | 8,881 |  |  |  |  | 2 | 8 |  | 1 | 55 | 429 | 1,197 | 2,240 | 466 |
| República Centroafricana | CAF | 155 |  |  |  |  |  |  |  |  |  | 2 | 3 | 8 | 112 |
| República Checa | CZE | 1,090 |  |  |  |  |  |  |  | 1 | 16 | 31 | 57 | 190 | 213 |
| República Democrática del Congo | COD | 224 |  |  |  |  |  |  |  |  | 3 | 6 | 9 | 31 | 128 |
| República Dominicana | DOM | 223 |  |  |  |  |  |  |  |  | 4 | 21 | 65 | 45 | 49 |
| República Turca del Norte de Chipre | CYN | 15 |  |  |  |  |  |  |  |  | 2 | 5 |  |  |  |
| República de China | TWN | 152 |  |  |  |  |  |  |  |  | 1 | 9 | 2 | 43 | 64 |
| República del Congo | COG | 151 |  |  |  |  |  |  |  | 1 | 2 | 5 | 16 | 43 | 49 |
| Ruanda | RWA | 24 |  |  |  |  |  |  |  |  |  |  |  | 3 | 17 |
| Rumania | ROU | 1,020 |  |  |  |  |  |  |  | 3 | 37 | 21 | 41 | 161 | 172 |
| Rusia | RUS | 4,101 |  |  |  |  |  |  |  | 5 | 63 | 106 | 233 | 1,574 | 1,174 |
| SAH | SAH | 4 |  |  |  |  |  |  |  |  |  | 2 |  | 1 |  |
| SDS | SDS | 82 |  |  |  |  |  |  |  |  |  | 1 |  | 10 | 19 |
| Sahara Occidental | ESH | 18 |  |  |  |  |  |  | 1 |  |  | 2 |  | 9 | 5 |
| Samoa | WSM | 33 |  |  |  |  |  |  |  |  |  |  | 3 | 21 | 9 |
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
| Senegal | SEN | 80 |  |  |  |  |  |  |  |  | 2 | 3 | 27 | 19 | 10 |
| Serbia | SRB | 481 |  |  |  |  |  |  |  | 4 | 26 | 14 | 27 | 128 | 64 |
| Seychelles | SYC | 2 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |
| Sierra Leona | SLE | 134 |  |  |  |  |  |  |  |  | 2 | 3 | 9 | 14 | 97 |
| Singapur | SGP | 38 |  |  |  |  |  |  |  |  |  |  | 1 | 19 | 4 |
| Siria | SYR | 743 |  |  |  |  |  |  |  | 4 | 41 | 31 | 57 | 370 | 85 |
| Somalia | SOM | 163 |  |  |  |  |  |  |  |  | 8 | 7 | 4 | 14 | 98 |
| Somalilandia | SOL | 209 |  |  |  |  |  |  |  |  | 2 | 4 |  | 31 | 159 |
| Sri Lanka | LKA | 174 |  |  |  |  |  |  | 2 | 2 | 10 | 13 | 16 | 48 | 18 |
| Suazilandia | SWZ | 42 |  |  |  |  |  |  |  |  |  |  |  | 3 | 37 |
| Sudáfrica | ZAF | 546 |  |  |  |  |  |  |  |  | 4 | 3 | 22 | 220 | 159 |
| Sudán | SDN | 461 |  |  |  |  |  |  |  | 2 | 9 | 15 | 12 | 78 | 247 |
| Sudán del Sur | SSD | 202 |  |  |  |  |  |  |  |  | 1 | 4 | 2 | 17 | 89 |
| Suecia | SWE | 1,158 |  |  |  |  |  |  |  | 2 | 13 | 31 | 45 | 247 | 43 |
| Suiza | CHE | 1,974 | 1 |  |  |  |  |  |  | 3 | 48 | 49 | 90 | 373 | 145 |
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
| Trinidad y Tobago | TTO | 58 |  |  |  |  |  |  |  |  |  | 12 | 21 | 6 | 18 |
| Turkmenistán | TKM | 102 |  |  |  |  |  |  |  |  | 14 | 5 | 3 | 46 | 16 |
| Turquía | TUR | 1,349 |  |  |  |  |  |  | 1 | 3 | 59 | 56 | 121 | 549 | 224 |
| Tuvalu | TUV | 6 |  |  |  |  |  |  |  |  |  |  |  | 5 | 1 |
| Túnez | TUN | 414 |  |  |  |  |  |  |  | 2 | 26 | 7 | 14 | 163 | 138 |
| UMI | UMI | 2 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |
| USG | USG | 3 |  |  |  |  |  |  |  |  |  |  | 1 | 1 |  |
| Ucrania | UKR | 676 |  |  |  |  |  |  | 2 | 4 | 29 | 48 | 48 | 87 | 78 |
| Uganda | UGA | 188 |  |  |  |  |  |  |  |  | 1 | 3 | 3 | 14 | 140 |
| Uruguay | URY | 252 |  |  |  |  |  |  |  |  | 1 | 22 | 45 | 90 | 64 |
| Uzbekistán | UZB | 94 |  |  |  |  |  |  |  |  | 7 | 4 | 2 | 48 | 18 |
| Vanuatu | VUT | 6 |  |  |  |  |  |  |  |  |  |  |  | 2 | 4 |
| Venezuela | VEN | 405 |  |  |  |  |  |  |  |  | 9 | 67 | 104 | 82 | 72 |
| Vietnam | VNM | 232 |  |  |  |  |  |  |  | 1 | 4 | 3 | 4 | 25 | 47 |
| Yemen | YEM | 354 |  |  |  |  |  |  |  | 4 | 16 | 11 | 14 | 35 | 238 |
| Yibuti | DJI | 49 |  |  |  |  |  |  |  |  | 2 | 2 | 3 | 26 | 14 |
| Zambia | ZMB | 97 |  |  |  |  |  |  |  |  | 1 | 3 | 4 | 19 | 45 |
| Zimbabue | ZWE | 103 |  |  |  |  |  |  |  |  | 2 | 1 | 5 | 25 | 43 |
| Åland | ALA | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |
