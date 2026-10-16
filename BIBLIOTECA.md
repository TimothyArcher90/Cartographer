# Biblioteca de Cartographer

Documento generado por `scripts/comprender.py`. No editar a mano.

- Mapas analizados: **882,152** · con país asignado: **530,816** · sin país: 351,336
  (sobre todo mapamundis, cartas oceánicas o registros sin datos de lugar).
- Países con mapas: **244**.
- Tipos: general 551,282, topográfico 209,143, histórico/temático 62,651, plano urbano 26,802, militar 11,049, mapamundi 7,264, ferroviario/viario 6,635, carta náutica 5,914, portulano 776, ptolemaico 636.
- Escalas: desconocida 612,356, local o ciudad 245,025, provincia o comarca 14,152, región o país 6,100, continente 2,997, mundo 1,522.

Cómo se asigna un país: por **nombre** actual (25+ idiomas, Natural Earth), por **nombre histórico**
(`catalogo/nombres_historicos.json`) o por **coordenadas** de la cobertura del mapa. Cada mapa guarda
la vía en el campo `via`; las asignaciones por coordenadas de mapas grandes pueden incluir países
vecinos. Los siglos salen del año de los metadatos de cada archivo y pueden tener errores puntuales.

Mapas de un país: `catalogo/biblioteca/paises/<ISO3>.jsonl.gz` o
`python scripts/buscar_lugar.py "<país>"`.

| País | ISO | Total | Antes del s. IX | IX | X | XI | XII | XIII | XIV | XV | XVI | XVII | XVIII | XIX | XX |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Afganistán | AFG | 528 | 1 |  |  |  |  |  | 1 |  | 21 | 7 | 12 | 221 | 111 |
| Albania | ALB | 358 | 1 |  |  |  |  | 2 | 2 | 7 | 27 | 35 | 30 | 87 | 65 |
| Alemania | DEU | 15,443 | 6 | 4 | 4 | 2 | 3 | 3 | 2 | 12 | 146 | 389 | 583 | 2,098 | 976 |
| Andorra | AND | 43 | 2 |  |  |  |  |  |  |  |  |  | 2 | 5 | 22 |
| Angola | AGO | 242 |  |  |  |  |  |  |  | 1 | 4 | 13 | 28 | 66 | 92 |
| Anguila | AIA | 11 |  |  |  |  |  |  |  |  |  |  | 6 | 2 | 1 |
| Antigua y Barbuda | ATG | 40 |  |  |  |  |  |  |  |  |  | 2 | 16 | 17 | 1 |
| Antártida | ATA | 120 |  |  |  |  |  |  |  |  |  | 13 | 24 | 10 | 55 |
| Arabia Saudita | SAU | 679 | 1 |  |  |  |  |  |  | 6 | 51 | 42 | 73 | 197 | 149 |
| Argelia | DZA | 813 | 2 |  |  |  |  | 1 | 1 | 3 | 24 | 41 | 40 | 348 | 152 |
| Argentina | ARG | 974 |  |  |  |  |  |  |  |  | 8 | 107 | 112 | 201 | 375 |
| Armenia | ARM | 453 | 2 | 1 |  | 1 |  |  | 1 | 2 | 22 | 18 | 36 | 188 | 105 |
| Aruba | ABW | 23 |  |  |  |  |  |  |  |  |  |  | 3 | 6 | 4 |
| Australia | AUS | 2,524 | 5 |  |  |  |  |  | 1 |  | 8 | 19 | 51 | 447 | 111 |
| Austria | AUT | 2,473 | 2 | 1 |  |  |  |  | 1 | 4 | 50 | 71 | 136 | 598 | 289 |
| Azerbaiyán | AZE | 141 |  |  |  |  |  |  |  | 1 | 8 | 7 | 10 | 46 | 38 |
| Bahamas | BHS | 206 |  |  |  |  |  | 1 |  |  |  | 8 | 68 | 65 | 33 |
| Bangladés | BGD | 57 |  |  |  |  |  |  |  | 1 | 4 | 5 | 4 | 7 | 8 |
| Barbados | BRB | 131 |  |  |  |  |  |  |  |  |  | 12 | 43 | 16 | 30 |
| Baréin | BHR | 82 |  |  |  |  |  |  |  | 2 | 6 | 6 | 11 | 19 | 27 |
| Belice | BLZ | 73 |  |  |  |  |  |  |  |  |  | 9 | 5 | 17 | 34 |
| Benín | BEN | 70 |  |  |  |  |  |  |  |  | 4 | 7 | 4 | 11 | 16 |
| Bermudas | BMU | 124 |  |  |  |  |  |  |  |  | 1 | 12 | 34 | 28 | 16 |
| Bielorrusia | BLR | 312 | 1 |  |  |  |  |  |  | 3 | 22 | 20 | 33 | 46 | 85 |
| Birmania | MMR | 241 | 1 |  |  |  |  |  |  | 1 | 11 | 9 | 25 | 64 | 70 |
| Bolivia | BOL | 317 |  |  |  |  |  |  |  |  | 5 | 18 | 11 | 94 | 88 |
| Bosnia y Herzegovina | BIH | 464 | 2 |  |  |  |  |  |  | 6 | 37 | 15 | 22 | 113 | 75 |
| Botsuana | BWA | 163 |  |  |  | 2 |  |  |  |  | 2 |  | 5 | 47 | 56 |
| Brasil | BRA | 2,374 | 3 |  |  |  |  |  |  | 3 | 27 | 249 | 290 | 577 | 475 |
| Brunéi | BRN | 30 |  |  |  |  |  |  |  |  | 1 |  | 1 | 11 | 7 |
| Bulgaria | BGR | 543 |  |  |  |  |  |  | 1 | 2 | 28 | 23 | 49 | 142 | 87 |
| Burkina Faso | BFA | 57 |  |  |  |  |  |  |  |  | 2 | 5 | 3 | 7 | 14 |
| Burundi | BDI | 44 | 1 |  |  |  |  |  |  |  |  |  |  | 3 | 34 |
| Bután | BTN | 123 | 1 |  |  |  |  |  |  |  |  |  | 5 | 36 | 55 |
| Bélgica | BEL | 6,010 | 1 |  | 1 |  |  |  | 1 | 4 | 73 | 245 | 553 | 804 | 327 |
| Cabo Verde | CPV | 132 |  |  |  |  |  |  |  |  | 4 | 22 | 50 | 31 | 3 |
| Camboya | KHM | 140 |  |  |  |  |  |  |  |  | 3 | 13 | 6 | 27 | 57 |
| Camerún | CMR | 132 |  |  |  |  |  |  |  |  | 2 | 6 | 8 | 14 | 54 |
| Canadá | CAN | 6,845 | 8 |  |  |  |  |  | 2 |  | 22 | 137 | 1,611 | 1,827 | 1,856 |
| Catar | QAT | 100 |  |  |  |  |  |  |  | 3 | 8 | 7 | 13 | 34 | 32 |
| Chad | TCD | 85 |  |  |  |  |  |  |  |  |  | 3 | 4 | 18 | 35 |
| Chile | CHL | 1,068 |  |  |  |  |  |  |  | 2 | 8 | 141 | 190 | 343 | 149 |
| China | CHN | 4,548 | 2 | 1 |  |  | 9 | 2 | 4 | 5 | 46 | 152 | 467 | 1,702 | 1,282 |
| Chipre | CYP | 290 | 1 |  |  |  |  | 1 |  | 4 | 35 | 19 | 25 | 25 | 95 |
| Ciudad del Vaticano | VAT | 78 |  |  |  |  |  |  |  |  | 1 | 24 | 5 | 10 | 15 |
| Colombia | COL | 692 |  |  |  |  |  |  |  |  | 10 | 55 | 115 | 159 | 153 |
| Comoras | COM | 26 |  |  |  |  |  |  |  |  |  | 1 | 4 | 10 | 9 |
| Corea del Norte | PRK | 136 |  |  |  |  |  |  |  |  | 1 | 9 | 12 | 13 | 54 |
| Corea del Sur | KOR | 858 | 1 |  |  |  |  |  |  |  | 6 | 15 | 69 | 152 | 225 |
| Costa Rica | CRI | 194 |  |  |  |  |  |  |  |  |  | 16 | 17 | 52 | 91 |
| Costa de Marfil | CIV | 110 |  |  |  |  |  |  |  |  | 3 | 5 | 13 | 15 | 42 |
| Croacia | HRV | 960 | 5 |  |  |  |  |  | 2 | 9 | 59 | 46 | 62 | 228 | 89 |
| Cuba | CUB | 1,353 | 17 | 8 | 5 |  |  |  |  | 1 | 15 | 110 | 247 | 298 | 328 |
| Curazao | CUW | 103 |  |  |  |  |  |  |  |  | 1 | 2 | 25 | 12 | 2 |
| Dinamarca | DNK | 1,503 | 5 |  |  |  |  |  | 3 |  | 13 | 75 | 78 | 425 | 89 |
| Dominica | DMA | 30 |  |  |  |  |  |  |  |  |  | 3 | 19 | 2 |  |
| ESB | ESB | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ecuador | ECU | 407 |  |  |  |  |  |  |  | 1 | 8 | 24 | 71 | 103 | 92 |
| Egipto | EGY | 2,539 | 8 |  |  | 2 | 1 | 3 | 2 | 6 | 65 | 49 | 178 | 924 | 809 |
| El Salvador | SLV | 195 |  |  |  |  |  | 1 |  |  | 1 | 10 | 6 | 96 | 61 |
| Emiratos Árabes Unidos | ARE | 55 |  |  |  |  |  |  |  | 3 | 7 | 6 | 12 | 13 | 7 |
| Eritrea | ERI | 426 |  |  |  |  |  |  |  |  | 1 | 7 | 7 | 107 | 276 |
| Eslovaquia | SVK | 539 |  |  |  |  |  |  |  | 2 | 17 | 15 | 23 | 103 | 125 |
| Eslovenia | SVN | 325 | 1 |  |  |  |  |  |  | 2 | 22 | 9 | 5 | 18 | 108 |
| España | ESP | 8,532 | 18 |  | 23 | 10 | 16 | 9 | 10 | 22 | 123 | 399 | 1,626 | 2,928 | 1,007 |
| Estados Federados de Micronesia | FSM | 69 |  |  |  |  |  |  |  |  |  | 1 | 4 | 23 | 32 |
| Estados Unidos | USA | 376,608 | 50 |  | 2 |  | 1 | 6 | 1 | 4 | 39 | 686 | 5,469 | 119,696 | 214,176 |
| Estonia | EST | 1,098 |  |  |  |  |  |  |  | 1 | 8 | 19 | 28 | 151 | 516 |
| Etiopía | ETH | 594 | 8 |  |  |  |  | 1 | 1 | 1 | 16 | 28 | 32 | 161 | 240 |
| Filipinas | PHL | 683 |  |  |  |  |  |  |  |  | 10 | 24 | 100 | 226 | 191 |
| Finlandia | FIN | 290 |  |  |  |  |  |  |  | 1 | 8 | 24 | 33 | 56 | 35 |
| Fiyi | FJI | 78 |  |  |  |  |  |  |  |  |  | 2 | 4 | 43 | 11 |
| Francia | FRA | 20,848 | 22 | 4 | 7 | 4 | 9 | 20 | 20 | 17 | 261 | 1,246 | 3,059 | 6,241 | 1,138 |
| GIB | GIB | 5 |  |  |  |  |  |  |  |  |  |  | 5 |  |  |
| Gabón | GAB | 91 |  |  |  |  |  |  |  |  | 2 | 8 | 10 | 22 | 17 |
| Gambia | GMB | 79 |  |  |  |  |  |  |  |  |  | 6 | 30 | 23 | 4 |
| Georgia | GEO | 286 |  |  |  |  |  |  |  | 1 | 12 | 7 | 68 | 66 | 46 |
| Ghana | GHA | 87 |  |  |  |  |  |  | 1 |  | 2 | 8 | 8 | 9 | 20 |
| Granada | GRD | 463 | 1 |  |  |  |  | 3 |  |  | 2 | 27 | 78 | 227 | 30 |
| Grecia | GRC | 2,349 | 18 | 1 | 1 |  |  | 1 | 3 | 10 | 129 | 219 | 183 | 757 | 254 |
| Groenlandia | GRL | 227 | 2 |  |  |  |  |  | 1 |  | 8 | 15 | 43 | 90 | 29 |
| Guam | GUM | 153 |  |  |  |  |  |  |  |  |  | 4 | 15 | 9 | 111 |
| Guatemala | GTM | 240 | 1 | 1 |  |  |  |  |  |  | 3 | 17 | 12 | 60 | 82 |
| Guernsey | GGY | 246 |  |  |  |  |  |  |  |  |  | 4 | 6 | 104 | 111 |
| Guinea | GIN | 146 |  |  |  |  |  |  |  |  | 1 | 11 | 42 | 15 | 17 |
| Guinea Ecuatorial | GNQ | 40 |  |  |  |  |  |  |  |  | 1 | 2 | 2 | 11 | 18 |
| Guinea-Bisáu | GNB | 10 |  |  |  |  |  |  |  |  | 1 |  | 3 | 2 | 2 |
| Guyana | GUY | 439 |  |  |  |  |  |  |  |  | 8 | 34 | 80 | 98 | 64 |
| Haití | HTI | 406 |  |  |  |  |  | 1 |  |  | 6 | 26 | 121 | 64 | 124 |
| Honduras | HND | 282 |  |  |  |  |  |  |  |  |  | 29 | 52 | 70 | 96 |
| Hong Kong | HKG | 63 |  |  |  |  |  |  |  |  |  |  |  | 26 | 24 |
| Hungría | HUN | 1,598 |  |  |  |  |  |  | 2 | 4 | 60 | 111 | 121 | 387 | 153 |
| India | IND | 2,941 | 3 |  |  |  |  |  | 7 | 6 | 87 | 141 | 461 | 928 | 258 |
| Indonesia | IDN | 2,103 | 4 |  |  |  |  |  | 1 | 2 | 28 | 271 | 391 | 199 | 243 |
| Irak | IRQ | 648 | 7 |  |  |  | 1 |  |  | 6 | 46 | 38 | 31 | 121 | 177 |
| Irlanda | IRL | 2,381 | 5 | 1 | 2 | 2 |  |  | 1 | 4 | 87 | 117 | 164 | 747 | 62 |
| Irán | IRN | 789 | 3 |  |  |  |  |  | 3 | 5 | 48 | 45 | 130 | 252 | 89 |
| Isla Norfolk | NFK | 1,361 |  |  |  |  |  |  |  |  |  | 3 | 40 | 1,082 | 206 |
| Isla Santa Elena | SHN | 134 |  |  |  |  |  |  |  |  | 2 | 9 | 8 | 89 | 5 |
| Isla de Man | IMN | 47 |  |  |  |  |  |  |  |  |  | 1 | 3 | 22 |  |
| Islandia | ISL | 268 | 1 |  |  |  |  |  |  | 1 | 22 | 23 | 30 | 65 | 28 |
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
| Israel | ISR | 1,616 |  |  | 2 | 2 | 2 | 2 | 4 | 21 | 76 | 83 | 193 | 488 | 166 |
| Italia | ITA | 8,185 | 29 | 5 |  | 4 | 6 | 8 | 3 | 58 | 369 | 530 | 714 | 1,885 | 585 |
| Jamaica | JAM | 954 | 1 |  |  |  |  |  |  | 1 | 1 | 24 | 221 | 559 | 55 |
| Japón | JPN | 1,588 | 3 |  |  |  |  |  | 1 | 2 | 11 | 95 | 192 | 373 | 286 |
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
| Libia | LBY | 377 | 4 |  |  |  |  |  |  | 9 | 25 | 30 | 29 | 48 | 123 |
| Liechtenstein | LIE | 27 |  |  |  |  |  |  |  | 1 |  | 1 |  | 6 |  |
| Lituania | LTU | 318 |  |  |  |  |  |  |  | 3 | 13 | 16 | 47 | 22 | 50 |
| Luxemburgo | LUX | 504 |  |  |  |  |  |  | 1 | 1 | 14 | 49 | 80 | 102 | 58 |
| Líbano | LBN | 742 | 3 |  |  | 1 | 1 |  |  | 2 | 17 | 6 | 15 | 470 | 134 |
| Macao | MAC | 104 |  |  |  |  |  |  |  |  |  | 5 | 22 | 23 | 36 |
| Macedonia del Norte | MKD | 119 |  |  |  |  |  |  |  | 2 | 13 | 11 | 5 | 19 | 26 |
| Madagascar | MDG | 406 | 1 |  |  |  |  |  |  |  | 15 | 32 | 98 | 99 | 50 |
| Malasia | MYS | 264 | 4 |  |  |  |  |  |  |  | 8 | 9 | 12 | 35 | 45 |
| Malaui | MWI | 37 | 1 |  |  |  |  |  |  |  | 1 |  | 2 | 14 | 14 |
| Maldivas | MDV | 74 |  |  |  |  |  |  |  |  | 1 | 8 | 28 | 9 | 14 |
| Malta | MLT | 345 | 2 |  |  |  |  | 1 | 1 | 2 | 30 | 30 | 87 | 87 | 11 |
| Malí | MLI | 121 |  |  |  |  |  |  | 3 | 2 | 4 | 5 | 8 | 26 | 20 |
| Marruecos | MAR | 667 | 1 |  |  |  |  | 1 |  | 2 | 15 | 47 | 74 | 161 | 202 |
| Mauricio | MUS | 216 | 2 |  |  | 1 |  |  |  | 1 | 5 | 19 | 36 | 62 | 26 |
| Mauritania | MRT | 96 |  |  |  |  |  |  |  |  | 10 | 4 | 13 | 16 | 18 |
| Moldavia | MDA | 142 |  |  |  |  |  |  |  | 1 | 5 | 15 | 26 | 26 | 13 |
| Mongolia | MNG | 149 |  |  |  |  |  |  |  |  | 4 | 11 | 10 | 39 | 62 |
| Montenegro | MNE | 165 |  |  |  |  |  |  |  |  | 8 | 9 | 5 | 36 | 26 |
| Montserrat | MSR | 133 |  |  |  |  |  |  |  |  |  |  |  | 106 | 21 |
| Mozambique | MOZ | 260 | 1 |  |  |  |  |  |  |  | 11 | 16 | 36 | 70 | 54 |
| México | MEX | 4,113 | 3 |  |  |  |  | 1 | 2 | 3 | 67 | 135 | 406 | 1,239 | 1,282 |
| Mónaco | MCO | 66 | 1 |  |  |  |  |  |  |  |  | 7 | 11 | 20 | 7 |
| Namibia | NAM | 137 |  |  |  |  |  |  |  |  | 3 |  | 8 | 41 | 29 |
| Nauru | NRU | 17 |  |  |  |  |  |  |  |  |  |  |  | 3 | 11 |
| Nepal | NPL | 87 |  |  |  |  |  |  |  | 1 | 3 | 2 | 1 | 20 | 31 |
| Nicaragua | NIC | 340 |  |  |  |  |  |  |  |  | 2 | 25 | 26 | 172 | 69 |
| Nigeria | NGA | 135 |  |  |  |  |  |  |  |  | 3 | 10 | 8 | 16 | 57 |
| Niue | NIU | 7 |  |  |  |  |  |  |  |  |  |  |  | 1 | 5 |
| Noruega | NOR | 1,399 | 1 |  |  |  |  |  | 1 | 2 | 21 | 55 | 106 | 416 | 64 |
| Nueva Caledonia | NCL | 31 |  |  |  |  |  |  |  |  |  | 1 | 3 | 9 | 10 |
| Nueva Zelanda | NZL | 471 | 2 |  |  | 1 |  |  |  |  | 1 | 3 | 28 | 242 | 80 |
| Níger | NER | 70 |  |  |  |  |  |  |  |  | 4 | 5 | 3 | 5 | 26 |
| Omán | OMN | 101 |  |  |  |  |  |  |  | 4 | 12 | 10 | 25 | 18 | 11 |
| PSX | PSX | 298 |  |  |  |  |  |  |  | 1 | 17 | 8 | 7 | 106 | 2 |
| Pakistán | PAK | 433 |  |  |  |  |  |  |  |  | 28 | 7 | 11 | 112 | 130 |
| Palaos | PLW | 56 |  |  |  |  |  |  |  |  | 2 | 1 | 10 | 12 | 20 |
| Palestina | PSE | 1,526 | 5 |  |  |  | 2 | 1 | 1 | 10 | 49 | 47 | 92 | 589 | 209 |
| Panamá | PAN | 425 |  |  |  |  |  |  |  |  | 3 | 51 | 60 | 100 | 115 |
| Papúa Nueva Guinea | PNG | 152 |  |  |  |  |  |  |  |  | 2 | 4 | 4 | 38 | 77 |
| Paraguay | PRY | 357 |  |  |  |  |  |  |  |  | 1 | 16 | 63 | 101 | 57 |
| Países Bajos | NLD | 19,560 | 1 |  | 5 |  |  |  | 1 | 1 | 125 | 552 | 713 | 564 | 1,038 |
| Perú | PER | 1,162 | 1 |  |  |  |  |  |  |  | 24 | 68 | 102 | 442 | 230 |
| Polinesia Francesa | PYF | 70 |  |  |  |  |  |  |  |  |  | 1 | 35 | 26 | 5 |
| Polonia | POL | 3,557 | 2 |  | 2 | 1 | 2 |  | 2 | 8 | 58 | 101 | 278 | 761 | 541 |
| Portugal | PRT | 3,223 | 2 |  |  |  |  | 1 | 1 | 10 | 62 | 158 | 543 | 1,212 | 228 |
| Puerto Rico | PRI | 1,082 |  |  |  |  |  |  |  | 1 | 2 | 19 | 71 | 40 | 906 |
| Reino Unido | GBR | 13,013 | 8 | 2 | 3 | 3 | 3 | 13 |  | 8 | 74 | 495 | 1,464 | 3,223 | 535 |
| República Centroafricana | CAF | 160 |  |  |  |  |  |  |  |  |  | 2 | 3 | 10 | 114 |
| República Checa | CZE | 1,321 | 2 |  |  |  |  |  |  | 1 | 19 | 38 | 94 | 234 | 230 |
| República Democrática del Congo | COD | 225 |  |  |  |  |  |  |  |  | 3 | 6 | 9 | 31 | 128 |
| República Dominicana | DOM | 258 |  |  |  |  |  |  |  |  | 5 | 27 | 70 | 46 | 59 |
| República Turca del Norte de Chipre | CYN | 15 |  |  |  |  |  |  |  |  | 2 | 5 |  |  |  |
| República de China | TWN | 212 |  |  |  |  |  |  | 1 |  | 2 | 17 | 9 | 50 | 87 |
| República del Congo | COG | 322 | 2 |  |  |  |  |  | 1 | 1 | 8 | 11 | 37 | 118 | 80 |
| Ruanda | RWA | 43 | 1 |  |  |  |  |  |  |  |  |  |  | 4 | 32 |
| Rumania | ROU | 1,179 |  |  |  |  |  |  |  | 3 | 51 | 32 | 54 | 193 | 207 |
| Rusia | RUS | 5,482 | 5 |  |  |  |  | 1 | 2 | 7 | 86 | 163 | 362 | 1,921 | 1,260 |
| SAH | SAH | 4 |  |  |  |  |  |  |  |  |  | 2 |  | 1 |  |
| SDS | SDS | 82 |  |  |  |  |  |  |  |  |  | 1 |  | 10 | 19 |
| Sahara Occidental | ESH | 39 |  |  |  |  |  |  | 1 |  |  | 2 | 1 | 19 | 14 |
| Samoa | WSM | 72 | 1 |  |  |  |  |  |  |  |  |  | 6 | 31 | 25 |
| Samoa Estadounidense | ASM | 26 |  |  |  |  |  |  |  |  |  |  |  | 14 | 7 |
| San Bartolomé | BLM | 6 |  |  |  |  |  |  |  |  |  |  | 3 | 2 |  |
| San Cristóbal y Nieves | KNA | 34 |  |  |  |  |  |  |  |  |  | 5 | 17 | 2 | 3 |
| San Marino | SMR | 8 |  |  | 1 |  |  |  |  |  |  | 1 | 1 | 1 | 2 |
| San Martín | MAF | 75 |  |  |  |  |  |  |  |  |  | 1 | 10 | 36 | 8 |
| San Martín | SXM | 34 |  |  |  |  |  |  |  | 1 |  |  | 6 | 17 | 3 |
| San Pedro y Miquelón | SPM | 8 |  |  |  |  |  |  |  |  |  |  | 1 | 5 | 1 |
| San Vicente y las Granadinas | VCT | 23 | 1 |  |  |  |  |  |  |  |  |  | 6 | 11 | 4 |
| Santa Lucía | LCA | 38 |  |  |  |  |  |  |  |  |  | 1 | 20 | 5 | 5 |
| Santo Tomé y Príncipe | STP | 28 |  |  |  | 1 |  |  |  |  |  | 10 | 10 | 4 | 1 |
| Senegal | SEN | 220 |  |  |  |  |  |  |  |  | 2 | 10 | 72 | 77 | 15 |
| Serbia | SRB | 562 |  |  |  |  |  |  |  | 4 | 29 | 20 | 37 | 145 | 74 |
| Seychelles | SYC | 3 |  |  |  |  |  |  |  |  |  |  |  | 3 |  |
| Sierra Leona | SLE | 186 |  |  |  |  |  |  |  | 1 | 2 | 10 | 22 | 19 | 98 |
| Singapur | SGP | 82 |  |  |  |  |  |  |  | 1 | 2 | 1 | 1 | 29 | 17 |
| Siria | SYR | 1,036 | 2 |  |  | 1 | 1 |  | 1 | 4 | 47 | 35 | 81 | 509 | 113 |
| Somalia | SOM | 199 |  |  |  |  |  |  |  | 1 | 11 | 7 | 6 | 22 | 107 |
| Somalilandia | SOL | 224 |  |  |  |  |  |  |  |  | 2 | 4 |  | 33 | 169 |
| Sri Lanka | LKA | 294 |  |  |  |  |  |  | 2 | 2 | 18 | 41 | 34 | 60 | 26 |
| Suazilandia | SWZ | 46 |  |  |  | 1 |  |  |  |  |  |  |  | 3 | 39 |
| Sudáfrica | ZAF | 772 | 5 |  |  |  |  | 1 |  |  | 6 | 28 | 46 | 300 | 176 |
| Sudán | SDN | 556 | 1 | 3 |  |  |  |  |  | 2 | 9 | 18 | 16 | 118 | 255 |
| Sudán del Sur | SSD | 202 |  |  |  |  |  |  |  |  | 1 | 4 | 2 | 17 | 89 |
| Suecia | SWE | 1,710 | 2 |  |  |  |  |  | 1 | 3 | 14 | 65 | 94 | 392 | 55 |
| Suiza | CHE | 2,719 | 3 |  |  |  |  | 1 | 1 | 5 | 60 | 72 | 177 | 595 | 182 |
| Surinam | SUR | 502 |  |  |  |  |  |  |  |  | 6 | 25 | 49 | 63 | 63 |
| Tailandia | THA | 264 | 1 |  |  |  |  |  | 2 | 1 | 13 | 20 | 27 | 70 | 60 |
| Tanzania | TZA | 215 | 1 |  |  |  |  |  |  |  | 4 | 2 | 3 | 51 | 85 |
| Tayikistán | TJK | 61 |  |  |  |  |  |  |  |  | 6 |  |  | 29 | 15 |
| Territorio Británico del Océano Índico | IOT | 1 |  |  |  |  |  |  |  |  |  |  |  |  | 1 |
| Territorios Australianos del Océano Índico | IOA | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Tierras Australes y Antárticas Francesas | ATF | 4 |  |  |  |  |  |  |  |  |  |  |  | 1 |  |
| Timor Oriental | TLS | 15 |  |  |  |  |  |  |  |  |  |  |  |  | 2 |
| Togo | TGO | 59 |  |  |  |  |  |  |  |  | 1 | 1 | 2 | 8 | 18 |
| Tonga | TON | 47 |  |  |  |  |  |  |  |  |  | 4 | 7 | 14 | 10 |
| Trinidad y Tobago | TTO | 102 |  |  |  |  |  |  |  |  | 1 | 19 | 35 | 12 | 32 |
| Turkmenistán | TKM | 133 |  |  |  |  |  |  |  |  | 14 | 6 | 5 | 51 | 20 |
| Turquía | TUR | 2,648 | 14 |  |  | 1 |  | 1 | 7 | 8 | 111 | 145 | 278 | 902 | 332 |
| Tuvalu | TUV | 14 |  |  |  |  |  |  |  |  |  |  |  | 8 | 4 |
| Túnez | TUN | 622 | 3 |  |  |  |  | 1 | 1 | 2 | 32 | 19 | 28 | 221 | 179 |
| UMI | UMI | 2 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |
| USG | USG | 3 |  |  |  |  |  |  |  |  |  |  | 1 | 1 |  |
| Ucrania | UKR | 799 | 1 |  |  |  |  |  | 4 | 4 | 32 | 78 | 67 | 99 | 98 |
| Uganda | UGA | 253 |  |  |  |  |  |  |  |  | 1 | 3 | 3 | 19 | 193 |
| Uruguay | URY | 369 |  |  |  |  |  |  |  |  | 4 | 22 | 53 | 129 | 71 |
| Uzbekistán | UZB | 135 |  |  |  |  |  |  |  |  | 7 | 6 | 6 | 65 | 31 |
| Vanuatu | VUT | 15 |  |  |  |  |  |  |  |  |  |  |  | 2 | 13 |
| Venezuela | VEN | 580 |  |  |  |  |  |  |  | 1 | 12 | 84 | 125 | 122 | 79 |
| Vietnam | VNM | 346 |  |  |  |  |  |  |  | 2 | 8 | 5 | 18 | 53 | 87 |
| Yemen | YEM | 442 |  |  |  |  |  |  |  | 5 | 25 | 16 | 20 | 46 | 276 |
| Yibuti | DJI | 58 |  |  |  |  |  |  |  |  | 2 | 2 | 3 | 28 | 20 |
| Zambia | ZMB | 106 |  |  |  |  |  |  |  |  | 1 | 3 | 4 | 21 | 45 |
| Zimbabue | ZWE | 110 |  |  |  |  |  |  |  |  | 2 | 1 | 6 | 26 | 43 |
| Åland | ALA | 7 |  |  |  |  |  |  |  |  |  |  | 1 | 3 |  |
