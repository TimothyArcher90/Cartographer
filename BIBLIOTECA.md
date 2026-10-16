# Biblioteca de Cartographer

Documento generado por `scripts/comprender.py`. No editar a mano.

- Mapas analizados: **897,564** · con país asignado: **534,361** · sin país: 363,203
  (sobre todo mapamundis, cartas oceánicas o registros sin datos de lugar).
- Países con mapas: **244**.
- Tipos: general 557,133, topográfico 209,348, histórico/temático 62,739, plano urbano 35,495, militar 11,227, mapamundi 7,406, ferroviario/viario 6,717, carta náutica 6,069, portulano 787, ptolemaico 643.
- Escalas: desconocida 627,768, local o ciudad 245,025, provincia o comarca 14,152, región o país 6,100, continente 2,997, mundo 1,522.

Cómo se asigna un país: por **nombre** actual (25+ idiomas, Natural Earth), por **nombre histórico**
(`catalogo/nombres_historicos.json`) o por **coordenadas** de la cobertura del mapa. Cada mapa guarda
la vía en el campo `via`; las asignaciones por coordenadas de mapas grandes pueden incluir países
vecinos. Los siglos salen del año de los metadatos de cada archivo y pueden tener errores puntuales.

Mapas de un país: `catalogo/biblioteca/paises/<ISO3>.jsonl.gz` o
`python scripts/buscar_lugar.py "<país>"`.

| País | ISO | Total | Antes del s. IX | IX | X | XI | XII | XIII | XIV | XV | XVI | XVII | XVIII | XIX | XX |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Afganistán | AFG | 533 | 1 |  |  |  |  |  | 1 |  | 21 | 7 | 12 | 224 | 113 |
| Albania | ALB | 359 | 1 |  |  |  |  | 2 | 2 | 7 | 28 | 35 | 30 | 87 | 65 |
| Alemania | DEU | 15,504 | 6 | 4 | 4 | 2 | 3 | 3 | 2 | 12 | 154 | 400 | 597 | 2,119 | 980 |
| Andorra | AND | 43 | 2 |  |  |  |  |  |  |  |  |  | 2 | 5 | 22 |
| Angola | AGO | 246 |  |  |  |  |  |  |  | 1 | 4 | 16 | 28 | 66 | 92 |
| Anguila | AIA | 14 |  |  |  |  |  |  |  |  |  | 2 | 6 | 2 | 1 |
| Antigua y Barbuda | ATG | 40 |  |  |  |  |  |  |  |  |  | 2 | 16 | 17 | 1 |
| Antártida | ATA | 120 |  |  |  |  |  |  |  |  |  | 13 | 24 | 10 | 55 |
| Arabia Saudita | SAU | 698 | 1 |  |  |  |  |  |  | 6 | 51 | 43 | 87 | 199 | 149 |
| Argelia | DZA | 869 | 2 |  |  |  |  | 1 | 1 | 3 | 25 | 44 | 47 | 379 | 154 |
| Argentina | ARG | 1,000 |  |  |  |  |  |  |  |  | 8 | 108 | 123 | 207 | 382 |
| Armenia | ARM | 454 | 2 | 1 |  | 1 |  |  | 1 | 2 | 22 | 18 | 36 | 189 | 105 |
| Aruba | ABW | 23 |  |  |  |  |  |  |  |  |  |  | 3 | 6 | 4 |
| Australia | AUS | 2,535 | 5 |  |  |  |  |  | 1 |  | 8 | 19 | 54 | 454 | 112 |
| Austria | AUT | 2,500 | 2 | 1 |  |  |  |  | 1 | 4 | 50 | 73 | 146 | 605 | 292 |
| Azerbaiyán | AZE | 141 |  |  |  |  |  |  |  | 1 | 8 | 7 | 10 | 46 | 38 |
| Bahamas | BHS | 209 |  |  |  |  |  | 1 |  |  |  | 9 | 68 | 65 | 33 |
| Bangladés | BGD | 57 |  |  |  |  |  |  |  | 1 | 4 | 5 | 4 | 7 | 8 |
| Barbados | BRB | 135 |  |  |  |  |  |  |  |  |  | 12 | 47 | 16 | 30 |
| Baréin | BHR | 82 |  |  |  |  |  |  |  | 2 | 6 | 6 | 11 | 19 | 27 |
| Belice | BLZ | 73 |  |  |  |  |  |  |  |  |  | 9 | 5 | 17 | 34 |
| Benín | BEN | 72 |  |  |  |  |  |  |  |  | 4 | 7 | 6 | 11 | 16 |
| Bermudas | BMU | 132 |  |  |  |  |  |  |  |  | 1 | 13 | 36 | 30 | 16 |
| Bielorrusia | BLR | 312 | 1 |  |  |  |  |  |  | 3 | 22 | 20 | 33 | 46 | 85 |
| Birmania | MMR | 244 | 1 |  |  |  |  |  |  | 1 | 11 | 9 | 28 | 64 | 70 |
| Bolivia | BOL | 327 |  |  |  |  |  |  |  |  | 5 | 19 | 11 | 99 | 88 |
| Bosnia y Herzegovina | BIH | 464 | 2 |  |  |  |  |  |  | 6 | 37 | 15 | 22 | 113 | 75 |
| Botsuana | BWA | 163 |  |  |  | 2 |  |  |  |  | 2 |  | 5 | 47 | 56 |
| Brasil | BRA | 2,457 | 3 |  |  |  |  |  |  | 3 | 28 | 251 | 341 | 595 | 478 |
| Brunéi | BRN | 30 |  |  |  |  |  |  |  |  | 1 |  | 1 | 11 | 7 |
| Bulgaria | BGR | 548 |  |  |  |  |  |  | 1 | 2 | 28 | 23 | 49 | 145 | 87 |
| Burkina Faso | BFA | 57 |  |  |  |  |  |  |  |  | 2 | 5 | 3 | 7 | 14 |
| Burundi | BDI | 44 | 1 |  |  |  |  |  |  |  |  |  |  | 3 | 34 |
| Bután | BTN | 123 | 1 |  |  |  |  |  |  |  |  |  | 5 | 36 | 55 |
| Bélgica | BEL | 6,158 | 2 |  | 1 |  |  |  | 1 | 4 | 74 | 262 | 587 | 869 | 338 |
| Cabo Verde | CPV | 132 |  |  |  |  |  |  |  |  | 4 | 22 | 50 | 31 | 3 |
| Camboya | KHM | 142 |  |  |  |  |  |  |  |  | 3 | 13 | 6 | 27 | 58 |
| Camerún | CMR | 133 |  |  |  |  |  |  |  |  | 2 | 6 | 8 | 14 | 55 |
| Canadá | CAN | 6,901 | 8 |  |  |  |  |  | 2 |  | 22 | 145 | 1,641 | 1,832 | 1,859 |
| Catar | QAT | 100 |  |  |  |  |  |  |  | 3 | 8 | 7 | 13 | 34 | 32 |
| Chad | TCD | 85 |  |  |  |  |  |  |  |  |  | 3 | 4 | 18 | 35 |
| Chile | CHL | 1,095 |  |  |  |  |  |  |  | 2 | 8 | 142 | 203 | 347 | 150 |
| China | CHN | 4,631 | 2 | 1 |  |  | 9 | 2 | 4 | 5 | 48 | 159 | 485 | 1,743 | 1,285 |
| Chipre | CYP | 298 | 1 |  |  |  |  | 1 |  | 4 | 35 | 26 | 25 | 25 | 95 |
| Ciudad del Vaticano | VAT | 78 |  |  |  |  |  |  |  |  | 1 | 24 | 5 | 10 | 15 |
| Colombia | COL | 701 |  |  |  |  |  |  |  |  | 10 | 55 | 117 | 160 | 154 |
| Comoras | COM | 27 |  |  |  |  |  |  |  |  |  | 1 | 5 | 10 | 9 |
| Corea del Norte | PRK | 136 |  |  |  |  |  |  |  |  | 1 | 9 | 12 | 13 | 54 |
| Corea del Sur | KOR | 861 | 1 |  |  |  |  |  |  |  | 6 | 15 | 70 | 153 | 226 |
| Costa Rica | CRI | 194 |  |  |  |  |  |  |  |  |  | 16 | 17 | 52 | 91 |
| Costa de Marfil | CIV | 110 |  |  |  |  |  |  |  |  | 3 | 5 | 13 | 15 | 42 |
| Croacia | HRV | 969 | 5 |  |  |  |  |  | 2 | 9 | 59 | 49 | 63 | 231 | 89 |
| Cuba | CUB | 1,392 | 17 | 8 | 5 |  |  |  |  | 1 | 15 | 120 | 260 | 308 | 328 |
| Curazao | CUW | 105 |  |  |  |  |  |  |  |  | 1 | 2 | 27 | 12 | 2 |
| Dinamarca | DNK | 1,509 | 5 |  |  |  |  |  | 3 |  | 13 | 75 | 81 | 427 | 90 |
| Dominica | DMA | 38 |  |  |  |  |  |  |  |  |  | 3 | 24 | 2 |  |
| ESB | ESB | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ecuador | ECU | 423 |  |  |  |  |  |  |  | 1 | 8 | 24 | 81 | 107 | 93 |
| Egipto | EGY | 2,558 | 8 |  |  | 2 | 1 | 3 | 2 | 6 | 65 | 57 | 179 | 928 | 813 |
| El Salvador | SLV | 198 |  |  |  |  |  | 1 |  |  | 2 | 10 | 8 | 96 | 61 |
| Emiratos Árabes Unidos | ARE | 55 |  |  |  |  |  |  |  | 3 | 7 | 6 | 12 | 13 | 7 |
| Eritrea | ERI | 428 |  |  |  |  |  |  |  |  | 1 | 7 | 9 | 107 | 276 |
| Eslovaquia | SVK | 540 |  |  |  |  |  |  |  | 2 | 17 | 15 | 23 | 103 | 126 |
| Eslovenia | SVN | 325 | 1 |  |  |  |  |  |  | 2 | 22 | 9 | 5 | 18 | 108 |
| España | ESP | 8,656 | 18 |  | 23 | 10 | 16 | 9 | 10 | 23 | 125 | 434 | 1,657 | 2,944 | 1,010 |
| Estados Federados de Micronesia | FSM | 69 |  |  |  |  |  |  |  |  |  | 1 | 4 | 23 | 32 |
| Estados Unidos | USA | 376,702 | 50 |  | 2 |  | 1 | 6 | 1 | 4 | 39 | 690 | 5,479 | 119,749 | 214,199 |
| Estonia | EST | 1,098 |  |  |  |  |  |  |  | 1 | 8 | 19 | 28 | 151 | 516 |
| Etiopía | ETH | 597 | 8 |  |  |  |  | 1 | 1 | 1 | 16 | 28 | 34 | 162 | 240 |
| Filipinas | PHL | 724 |  |  |  |  |  |  |  |  | 10 | 25 | 135 | 226 | 191 |
| Finlandia | FIN | 297 |  |  |  |  |  |  |  | 1 | 8 | 24 | 37 | 56 | 35 |
| Fiyi | FJI | 78 |  |  |  |  |  |  |  |  |  | 2 | 4 | 43 | 11 |
| Francia | FRA | 22,074 | 22 | 4 | 7 | 4 | 9 | 20 | 20 | 17 | 292 | 1,373 | 3,396 | 6,676 | 1,250 |
| GIB | GIB | 5 |  |  |  |  |  |  |  |  |  |  | 5 |  |  |
| Gabón | GAB | 92 |  |  |  |  |  |  |  |  | 2 | 8 | 10 | 23 | 17 |
| Gambia | GMB | 82 |  |  |  |  |  |  |  |  | 1 | 6 | 31 | 23 | 4 |
| Georgia | GEO | 286 |  |  |  |  |  |  |  | 1 | 12 | 7 | 68 | 66 | 46 |
| Ghana | GHA | 87 |  |  |  |  |  |  | 1 |  | 2 | 8 | 8 | 9 | 20 |
| Granada | GRD | 490 | 1 |  |  |  |  | 3 |  |  | 2 | 34 | 89 | 229 | 30 |
| Grecia | GRC | 2,366 | 18 | 1 | 1 |  |  | 1 | 3 | 11 | 130 | 226 | 188 | 760 | 254 |
| Groenlandia | GRL | 228 | 2 |  |  |  |  |  | 1 |  | 8 | 15 | 44 | 90 | 29 |
| Guam | GUM | 158 |  |  |  |  |  |  |  |  |  | 4 | 19 | 10 | 111 |
| Guatemala | GTM | 243 | 1 | 1 |  |  |  |  |  |  | 3 | 17 | 12 | 62 | 82 |
| Guernsey | GGY | 247 |  |  |  |  |  |  |  |  |  | 4 | 6 | 104 | 111 |
| Guinea | GIN | 146 |  |  |  |  |  |  |  |  | 1 | 11 | 42 | 15 | 17 |
| Guinea Ecuatorial | GNQ | 40 |  |  |  |  |  |  |  |  | 1 | 2 | 2 | 11 | 18 |
| Guinea-Bisáu | GNB | 10 |  |  |  |  |  |  |  |  | 1 |  | 3 | 2 | 2 |
| Guyana | GUY | 444 |  |  |  |  |  |  |  |  | 8 | 35 | 83 | 99 | 64 |
| Haití | HTI | 410 |  |  |  |  |  | 1 |  |  | 6 | 26 | 123 | 66 | 124 |
| Honduras | HND | 285 |  |  |  |  |  |  |  |  |  | 32 | 52 | 70 | 96 |
| Hong Kong | HKG | 65 |  |  |  |  |  |  |  |  |  |  |  | 27 | 25 |
| Hungría | HUN | 1,611 |  |  |  |  |  |  | 2 | 4 | 60 | 113 | 126 | 388 | 155 |
| India | IND | 3,019 | 3 |  |  |  |  |  | 7 | 7 | 88 | 149 | 505 | 932 | 258 |
| Indonesia | IDN | 2,181 | 4 |  |  |  |  |  | 1 | 2 | 28 | 274 | 461 | 201 | 243 |
| Irak | IRQ | 650 | 7 |  |  |  | 1 |  |  | 6 | 46 | 38 | 32 | 121 | 178 |
| Irlanda | IRL | 2,398 | 5 | 1 | 2 | 2 |  |  | 1 | 4 | 87 | 120 | 170 | 751 | 64 |
| Irán | IRN | 813 | 3 |  |  |  |  |  | 3 | 5 | 48 | 49 | 139 | 257 | 89 |
| Isla Norfolk | NFK | 1,362 |  |  |  |  |  |  |  |  |  | 3 | 40 | 1,083 | 206 |
| Isla Santa Elena | SHN | 134 |  |  |  |  |  |  |  |  | 2 | 9 | 8 | 89 | 5 |
| Isla de Man | IMN | 47 |  |  |  |  |  |  |  |  |  | 1 | 3 | 22 |  |
| Islandia | ISL | 289 | 1 |  |  |  |  |  |  | 1 | 22 | 23 | 34 | 81 | 28 |
| Islas Caimán | CYM | 9 |  |  |  |  |  |  |  |  |  |  | 1 | 1 | 7 |
| Islas Feroe | FRO | 89 | 1 |  |  |  |  |  | 1 |  |  | 9 | 12 | 30 | 12 |
| Islas Georgias del Sur y Sandwich del Sur | SGS | 2 |  |  |  |  |  |  |  |  |  |  |  |  | 1 |
| Islas Malvinas | FLK | 50 |  |  |  |  |  |  |  |  |  | 11 | 12 | 6 | 4 |
| Islas Marianas del Norte | MNP | 42 |  |  |  |  |  |  |  |  | 2 |  | 7 | 2 | 24 |
| Islas Marshall | MHL | 65 | 2 |  |  |  |  |  |  |  |  |  |  | 21 | 34 |
| Islas Pitcairn | PCN | 11 |  |  |  |  |  |  |  |  |  |  | 1 | 1 | 8 |
| Islas Salomón | SLB | 43 |  |  |  |  |  |  |  |  | 1 | 2 | 2 | 6 | 13 |
| Islas Turcas y Caicos | TCA | 6 |  |  |  |  |  |  |  |  |  |  | 2 | 2 | 2 |
| Islas Vírgenes Británicas | VGB | 9 |  |  |  |  |  |  |  |  |  |  | 3 | 1 | 5 |
| Islas Vírgenes de los Estados Unidos | VIR | 102 |  |  |  |  |  |  |  |  |  | 1 | 49 | 3 | 44 |
| Israel | ISR | 1,652 |  |  | 2 | 2 | 2 | 2 | 5 | 21 | 79 | 96 | 198 | 499 | 166 |
| Italia | ITA | 8,427 | 30 | 5 |  | 4 | 6 | 8 | 3 | 64 | 398 | 554 | 774 | 1,957 | 602 |
| Jamaica | JAM | 963 | 1 |  |  |  |  |  |  | 1 | 1 | 27 | 224 | 560 | 55 |
| Japón | JPN | 1,613 | 3 |  |  |  |  |  | 1 | 3 | 12 | 100 | 198 | 382 | 288 |
| Jersey | JEY | 13 |  |  |  |  |  |  |  |  |  | 4 |  | 8 |  |
| Jordania | JOR | 381 |  |  |  |  |  |  |  | 1 | 37 | 18 | 22 | 148 | 28 |
| Kazajistán | KAZ | 152 |  |  |  |  |  |  |  | 1 | 15 | 17 | 10 | 35 | 31 |
| Kenia | KEN | 231 |  |  |  |  |  |  |  |  | 2 | 4 | 2 | 26 | 155 |
| Kirguistán | KGZ | 54 |  |  |  |  |  |  |  |  | 7 | 2 |  | 23 | 11 |
| Kiribati | KIR | 25 |  |  |  |  |  |  |  |  |  |  |  | 15 | 9 |
| Kosovo | KOS | 60 |  |  |  |  |  |  |  |  | 1 | 2 | 2 | 3 | 33 |
| Kuwait | KWT | 78 |  |  |  |  |  |  |  | 3 | 7 | 5 | 12 | 15 | 21 |
| Laos | LAO | 77 |  |  |  |  |  |  |  | 1 | 3 |  | 1 | 13 | 23 |
| Lesoto | LSO | 91 |  |  |  | 1 |  |  |  |  |  |  | 1 | 12 | 72 |
| Letonia | LVA | 260 | 1 |  |  |  |  |  |  | 2 | 14 | 23 | 24 | 26 | 93 |
| Liberia | LBR | 164 |  |  |  |  |  |  |  |  | 2 | 3 | 5 | 77 | 38 |
| Libia | LBY | 397 | 4 |  |  |  |  |  |  | 9 | 25 | 36 | 35 | 49 | 125 |
| Liechtenstein | LIE | 27 |  |  |  |  |  |  |  | 1 |  | 1 |  | 6 |  |
| Lituania | LTU | 321 |  |  |  |  |  |  |  | 3 | 13 | 17 | 49 | 22 | 50 |
| Luxemburgo | LUX | 540 |  |  |  |  |  |  | 1 | 1 | 15 | 61 | 98 | 104 | 60 |
| Líbano | LBN | 747 | 3 |  |  | 1 | 1 |  |  | 2 | 17 | 7 | 15 | 470 | 135 |
| Macao | MAC | 114 |  |  |  |  |  |  |  |  |  | 7 | 26 | 25 | 36 |
| Macedonia del Norte | MKD | 119 |  |  |  |  |  |  |  | 2 | 13 | 11 | 5 | 19 | 26 |
| Madagascar | MDG | 478 | 1 |  |  |  |  |  |  | 1 | 15 | 32 | 138 | 100 | 50 |
| Malasia | MYS | 264 | 4 |  |  |  |  |  |  |  | 8 | 9 | 12 | 35 | 45 |
| Malaui | MWI | 37 | 1 |  |  |  |  |  |  |  | 1 |  | 2 | 14 | 14 |
| Maldivas | MDV | 77 |  |  |  |  |  |  |  |  | 1 | 8 | 30 | 9 | 14 |
| Malta | MLT | 388 | 2 |  |  |  |  | 1 | 1 | 2 | 30 | 36 | 106 | 90 | 12 |
| Malí | MLI | 121 |  |  |  |  |  |  | 3 | 2 | 4 | 5 | 8 | 26 | 20 |
| Marruecos | MAR | 680 | 1 |  |  |  |  | 1 |  | 2 | 15 | 48 | 75 | 163 | 211 |
| Mauricio | MUS | 232 | 2 |  |  | 1 |  |  |  | 1 | 7 | 20 | 42 | 65 | 26 |
| Mauritania | MRT | 96 |  |  |  |  |  |  |  |  | 10 | 4 | 13 | 16 | 18 |
| Moldavia | MDA | 142 |  |  |  |  |  |  |  | 1 | 5 | 15 | 26 | 26 | 13 |
| Mongolia | MNG | 150 |  |  |  |  |  |  |  |  | 4 | 11 | 10 | 39 | 62 |
| Montenegro | MNE | 166 |  |  |  |  |  |  |  |  | 8 | 9 | 5 | 36 | 26 |
| Montserrat | MSR | 133 |  |  |  |  |  |  |  |  |  |  |  | 106 | 21 |
| Mozambique | MOZ | 269 | 1 |  |  |  |  |  |  |  | 11 | 16 | 38 | 71 | 54 |
| México | MEX | 4,145 | 3 |  |  |  |  | 1 | 2 | 3 | 69 | 141 | 412 | 1,249 | 1,284 |
| Mónaco | MCO | 71 | 1 |  |  |  |  |  |  |  |  | 7 | 12 | 20 | 9 |
| Namibia | NAM | 137 |  |  |  |  |  |  |  |  | 3 |  | 8 | 41 | 29 |
| Nauru | NRU | 17 |  |  |  |  |  |  |  |  |  |  |  | 3 | 11 |
| Nepal | NPL | 87 |  |  |  |  |  |  |  | 1 | 3 | 2 | 1 | 20 | 31 |
| Nicaragua | NIC | 343 |  |  |  |  |  |  |  |  | 2 | 25 | 27 | 173 | 69 |
| Nigeria | NGA | 135 |  |  |  |  |  |  |  |  | 3 | 10 | 8 | 16 | 57 |
| Niue | NIU | 7 |  |  |  |  |  |  |  |  |  |  |  | 1 | 5 |
| Noruega | NOR | 1,405 | 1 |  |  |  |  |  | 1 | 2 | 21 | 56 | 107 | 419 | 64 |
| Nueva Caledonia | NCL | 32 |  |  |  |  |  |  |  |  |  | 1 | 3 | 9 | 10 |
| Nueva Zelanda | NZL | 476 | 2 |  |  | 1 |  |  |  |  | 1 | 3 | 32 | 242 | 81 |
| Níger | NER | 70 |  |  |  |  |  |  |  |  | 4 | 5 | 3 | 5 | 26 |
| Omán | OMN | 107 |  |  |  |  |  |  |  | 4 | 12 | 10 | 31 | 18 | 11 |
| PSX | PSX | 298 |  |  |  |  |  |  |  | 1 | 17 | 8 | 7 | 106 | 2 |
| Pakistán | PAK | 434 |  |  |  |  |  |  |  |  | 28 | 7 | 11 | 112 | 131 |
| Palaos | PLW | 56 |  |  |  |  |  |  |  |  | 2 | 1 | 10 | 12 | 20 |
| Palestina | PSE | 1,541 | 5 |  |  |  | 2 | 1 | 1 | 10 | 49 | 47 | 93 | 596 | 215 |
| Panamá | PAN | 436 |  |  |  |  |  |  |  |  | 3 | 51 | 63 | 106 | 115 |
| Papúa Nueva Guinea | PNG | 152 |  |  |  |  |  |  |  |  | 2 | 4 | 4 | 38 | 77 |
| Paraguay | PRY | 366 |  |  |  |  |  |  |  |  | 1 | 20 | 64 | 104 | 58 |
| Países Bajos | NLD | 19,617 | 1 |  | 5 |  |  |  | 1 | 1 | 128 | 562 | 737 | 570 | 1,039 |
| Perú | PER | 1,237 | 1 |  |  |  |  |  |  |  | 26 | 69 | 131 | 453 | 230 |
| Polinesia Francesa | PYF | 70 |  |  |  |  |  |  |  |  |  | 1 | 35 | 26 | 5 |
| Polonia | POL | 3,589 | 2 |  | 2 | 1 | 3 |  | 2 | 8 | 61 | 103 | 296 | 761 | 549 |
| Portugal | PRT | 3,254 | 2 |  |  |  |  | 1 | 1 | 10 | 63 | 163 | 553 | 1,223 | 228 |
| Puerto Rico | PRI | 1,095 |  |  |  |  |  |  |  | 1 | 2 | 20 | 75 | 41 | 906 |
| Reino Unido | GBR | 13,061 | 8 | 2 | 3 | 3 | 3 | 13 |  | 9 | 74 | 501 | 1,486 | 3,227 | 537 |
| República Centroafricana | CAF | 160 |  |  |  |  |  |  |  |  |  | 2 | 3 | 10 | 114 |
| República Checa | CZE | 1,331 | 2 |  |  |  |  |  |  | 1 | 19 | 41 | 97 | 236 | 232 |
| República Democrática del Congo | COD | 225 |  |  |  |  |  |  |  |  | 3 | 6 | 9 | 31 | 128 |
| República Dominicana | DOM | 260 |  |  |  |  |  |  |  |  | 5 | 27 | 71 | 47 | 59 |
| República Turca del Norte de Chipre | CYN | 15 |  |  |  |  |  |  |  |  | 2 | 5 |  |  |  |
| República de China | TWN | 212 |  |  |  |  |  |  | 1 |  | 2 | 17 | 9 | 50 | 87 |
| República del Congo | COG | 327 | 2 |  |  |  |  |  | 1 | 1 | 8 | 14 | 37 | 119 | 80 |
| Ruanda | RWA | 43 | 1 |  |  |  |  |  |  |  |  |  |  | 4 | 32 |
| Rumania | ROU | 1,182 |  |  |  |  |  |  |  | 3 | 51 | 32 | 55 | 194 | 207 |
| Rusia | RUS | 5,516 | 5 |  |  |  |  | 1 | 2 | 7 | 86 | 164 | 384 | 1,931 | 1,260 |
| SAH | SAH | 4 |  |  |  |  |  |  |  |  |  | 2 |  | 1 |  |
| SDS | SDS | 82 |  |  |  |  |  |  |  |  |  | 1 |  | 10 | 19 |
| Sahara Occidental | ESH | 39 |  |  |  |  |  |  | 1 |  |  | 2 | 1 | 19 | 14 |
| Samoa | WSM | 72 | 1 |  |  |  |  |  |  |  |  |  | 6 | 31 | 25 |
| Samoa Estadounidense | ASM | 26 |  |  |  |  |  |  |  |  |  |  |  | 14 | 7 |
| San Bartolomé | BLM | 6 |  |  |  |  |  |  |  |  |  |  | 3 | 2 |  |
| San Cristóbal y Nieves | KNA | 34 |  |  |  |  |  |  |  |  |  | 5 | 17 | 2 | 3 |
| San Marino | SMR | 8 |  |  | 1 |  |  |  |  |  |  | 1 | 1 | 1 | 2 |
| San Martín | MAF | 91 |  |  |  |  |  |  |  |  |  | 3 | 15 | 40 | 8 |
| San Martín | SXM | 45 |  |  |  |  |  |  |  | 1 |  | 2 | 9 | 20 | 3 |
| San Pedro y Miquelón | SPM | 8 |  |  |  |  |  |  |  |  |  |  | 1 | 5 | 1 |
| San Vicente y las Granadinas | VCT | 23 | 1 |  |  |  |  |  |  |  |  |  | 6 | 11 | 4 |
| Santa Lucía | LCA | 42 |  |  |  |  |  |  |  |  |  | 1 | 21 | 6 | 5 |
| Santo Tomé y Príncipe | STP | 28 |  |  |  | 1 |  |  |  |  |  | 10 | 10 | 4 | 1 |
| Senegal | SEN | 233 |  |  |  |  |  |  |  |  | 2 | 12 | 80 | 79 | 15 |
| Serbia | SRB | 565 |  |  |  |  |  |  |  | 4 | 29 | 20 | 38 | 145 | 74 |
| Seychelles | SYC | 3 |  |  |  |  |  |  |  |  |  |  |  | 3 |  |
| Sierra Leona | SLE | 190 |  |  |  |  |  |  |  | 1 | 2 | 10 | 22 | 20 | 99 |
| Singapur | SGP | 84 |  |  |  |  |  |  |  | 1 | 2 | 1 | 1 | 29 | 19 |
| Siria | SYR | 1,046 | 2 |  |  | 1 | 1 |  | 1 | 4 | 47 | 36 | 83 | 514 | 115 |
| Somalia | SOM | 199 |  |  |  |  |  |  |  | 1 | 11 | 7 | 6 | 22 | 107 |
| Somalilandia | SOL | 224 |  |  |  |  |  |  |  |  | 2 | 4 |  | 33 | 169 |
| Sri Lanka | LKA | 299 |  |  |  |  |  |  | 2 | 2 | 18 | 42 | 38 | 60 | 26 |
| Suazilandia | SWZ | 46 |  |  |  | 1 |  |  |  |  |  |  |  | 3 | 39 |
| Sudáfrica | ZAF | 777 | 5 |  |  |  |  | 1 |  |  | 6 | 28 | 51 | 300 | 176 |
| Sudán | SDN | 559 | 1 | 3 |  |  |  |  |  | 2 | 9 | 19 | 16 | 119 | 256 |
| Sudán del Sur | SSD | 202 |  |  |  |  |  |  |  |  | 1 | 4 | 2 | 17 | 89 |
| Suecia | SWE | 1,737 | 2 |  |  |  |  |  | 1 | 3 | 15 | 69 | 106 | 396 | 56 |
| Suiza | CHE | 2,728 | 3 |  |  |  |  | 1 | 1 | 5 | 61 | 72 | 177 | 602 | 183 |
| Surinam | SUR | 514 |  |  |  |  |  |  |  |  | 6 | 28 | 58 | 63 | 63 |
| Tailandia | THA | 271 | 1 |  |  |  |  |  | 2 | 1 | 13 | 23 | 29 | 70 | 61 |
| Tanzania | TZA | 215 | 1 |  |  |  |  |  |  |  | 4 | 2 | 3 | 51 | 85 |
| Tayikistán | TJK | 61 |  |  |  |  |  |  |  |  | 6 |  |  | 29 | 15 |
| Territorio Británico del Océano Índico | IOT | 1 |  |  |  |  |  |  |  |  |  |  |  |  | 1 |
| Territorios Australianos del Océano Índico | IOA | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Tierras Australes y Antárticas Francesas | ATF | 4 |  |  |  |  |  |  |  |  |  |  |  | 1 |  |
| Timor Oriental | TLS | 15 |  |  |  |  |  |  |  |  |  |  |  |  | 2 |
| Togo | TGO | 59 |  |  |  |  |  |  |  |  | 1 | 1 | 2 | 8 | 18 |
| Tonga | TON | 48 |  |  |  |  |  |  |  |  |  | 4 | 7 | 15 | 10 |
| Trinidad y Tobago | TTO | 102 |  |  |  |  |  |  |  |  | 1 | 19 | 35 | 12 | 32 |
| Turkmenistán | TKM | 133 |  |  |  |  |  |  |  |  | 14 | 6 | 5 | 51 | 20 |
| Turquía | TUR | 2,716 | 14 |  |  | 1 |  | 1 | 7 | 8 | 112 | 156 | 295 | 918 | 336 |
| Tuvalu | TUV | 14 |  |  |  |  |  |  |  |  |  |  |  | 8 | 4 |
| Túnez | TUN | 638 | 3 |  |  |  |  | 1 | 1 | 2 | 32 | 26 | 32 | 223 | 180 |
| UMI | UMI | 2 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |
| USG | USG | 3 |  |  |  |  |  |  |  |  |  |  | 1 | 1 |  |
| Ucrania | UKR | 809 | 1 |  |  |  |  |  | 4 | 4 | 32 | 78 | 75 | 101 | 98 |
| Uganda | UGA | 253 |  |  |  |  |  |  |  |  | 1 | 3 | 3 | 19 | 193 |
| Uruguay | URY | 383 |  |  |  |  |  |  |  |  | 4 | 22 | 55 | 135 | 77 |
| Uzbekistán | UZB | 135 |  |  |  |  |  |  |  |  | 7 | 6 | 6 | 65 | 31 |
| Vanuatu | VUT | 15 |  |  |  |  |  |  |  |  |  |  |  | 2 | 13 |
| Venezuela | VEN | 586 |  |  |  |  |  |  |  | 1 | 12 | 84 | 128 | 125 | 79 |
| Vietnam | VNM | 346 |  |  |  |  |  |  |  | 2 | 8 | 5 | 18 | 53 | 87 |
| Yemen | YEM | 444 |  |  |  |  |  |  |  | 5 | 25 | 16 | 22 | 46 | 276 |
| Yibuti | DJI | 58 |  |  |  |  |  |  |  |  | 2 | 2 | 3 | 28 | 20 |
| Zambia | ZMB | 106 |  |  |  |  |  |  |  |  | 1 | 3 | 4 | 21 | 45 |
| Zimbabue | ZWE | 110 |  |  |  |  |  |  |  |  | 2 | 1 | 6 | 26 | 43 |
| Åland | ALA | 7 |  |  |  |  |  |  |  |  |  |  | 1 | 3 |  |
