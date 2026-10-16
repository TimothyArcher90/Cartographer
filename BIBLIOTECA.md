# Biblioteca de Cartographer

Documento generado por `scripts/comprender.py`. No editar a mano.

- Mapas analizados: **909,635** · con país asignado: **537,353** · sin país: 372,282
  (sobre todo mapamundis, cartas oceánicas o registros sin datos de lugar).
- Países con mapas: **244**.
- Tipos: general 567,603, topográfico 209,484, histórico/temático 63,095, plano urbano 35,665, militar 11,397, mapamundi 7,762, ferroviario/viario 6,939, carta náutica 6,217, portulano 787, ptolemaico 686.
- Escalas: desconocida 639,839, local o ciudad 245,025, provincia o comarca 14,152, región o país 6,100, continente 2,997, mundo 1,522.

Cómo se asigna un país: por **nombre** actual (25+ idiomas, Natural Earth), por **nombre histórico**
(`catalogo/nombres_historicos.json`) o por **coordenadas** de la cobertura del mapa. Cada mapa guarda
la vía en el campo `via`; las asignaciones por coordenadas de mapas grandes pueden incluir países
vecinos. Los siglos salen del año de los metadatos de cada archivo y pueden tener errores puntuales.

Mapas de un país: `catalogo/biblioteca/paises/<ISO3>.jsonl.gz` o
`python scripts/buscar_lugar.py "<país>"`.

| País | ISO | Total | Antes del s. IX | IX | X | XI | XII | XIII | XIV | XV | XVI | XVII | XVIII | XIX | XX |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Afganistán | AFG | 539 | 1 |  |  |  |  |  | 1 |  | 21 | 7 | 12 | 230 | 113 |
| Albania | ALB | 363 | 1 |  |  |  |  | 2 | 2 | 7 | 28 | 36 | 31 | 88 | 66 |
| Alemania | DEU | 15,573 | 6 | 4 | 4 | 4 | 3 | 3 | 2 | 12 | 162 | 415 | 614 | 2,138 | 992 |
| Andorra | AND | 43 | 2 |  |  |  |  |  |  |  |  |  | 2 | 5 | 22 |
| Angola | AGO | 249 |  |  |  |  |  |  |  | 1 | 4 | 17 | 29 | 66 | 92 |
| Anguila | AIA | 14 |  |  |  |  |  |  |  |  |  | 2 | 6 | 2 | 1 |
| Antigua y Barbuda | ATG | 40 |  |  |  |  |  |  |  |  |  | 2 | 16 | 17 | 1 |
| Antártida | ATA | 120 |  |  |  |  |  |  |  |  |  | 13 | 24 | 10 | 55 |
| Arabia Saudita | SAU | 706 | 1 |  |  |  |  |  |  | 6 | 51 | 44 | 89 | 204 | 149 |
| Argelia | DZA | 885 | 2 |  |  |  |  | 1 | 1 | 3 | 26 | 44 | 48 | 390 | 157 |
| Argentina | ARG | 1,010 |  |  |  |  |  |  |  |  | 9 | 110 | 123 | 212 | 385 |
| Armenia | ARM | 456 | 2 | 1 |  | 1 |  |  | 1 | 2 | 22 | 18 | 37 | 189 | 106 |
| Aruba | ABW | 23 |  |  |  |  |  |  |  |  |  |  | 3 | 6 | 4 |
| Australia | AUS | 2,560 | 5 |  |  |  |  |  | 1 |  | 8 | 19 | 57 | 470 | 115 |
| Austria | AUT | 2,544 | 2 | 1 |  |  |  |  | 1 | 4 | 52 | 75 | 154 | 630 | 297 |
| Azerbaiyán | AZE | 141 |  |  |  |  |  |  |  | 1 | 8 | 7 | 10 | 46 | 38 |
| Bahamas | BHS | 210 |  |  |  |  |  | 1 |  |  |  | 9 | 69 | 65 | 33 |
| Bangladés | BGD | 57 |  |  |  |  |  |  |  | 1 | 4 | 5 | 4 | 7 | 8 |
| Barbados | BRB | 135 |  |  |  |  |  |  |  |  |  | 12 | 47 | 16 | 30 |
| Baréin | BHR | 82 |  |  |  |  |  |  |  | 2 | 6 | 6 | 11 | 19 | 27 |
| Belice | BLZ | 73 |  |  |  |  |  |  |  |  |  | 9 | 5 | 17 | 34 |
| Benín | BEN | 73 |  |  |  |  |  |  |  |  | 4 | 7 | 6 | 11 | 16 |
| Bermudas | BMU | 135 |  |  |  |  |  |  |  |  | 1 | 13 | 39 | 30 | 16 |
| Bielorrusia | BLR | 312 | 1 |  |  |  |  |  |  | 3 | 22 | 20 | 33 | 46 | 85 |
| Birmania | MMR | 245 | 1 |  |  |  |  |  |  | 1 | 11 | 9 | 28 | 64 | 71 |
| Bolivia | BOL | 331 |  |  |  |  |  |  |  |  | 5 | 19 | 11 | 103 | 88 |
| Bosnia y Herzegovina | BIH | 464 | 2 |  |  |  |  |  |  | 6 | 37 | 15 | 22 | 113 | 75 |
| Botsuana | BWA | 163 |  |  |  | 2 |  |  |  |  | 2 |  | 5 | 47 | 56 |
| Brasil | BRA | 2,516 | 3 |  |  | 2 |  |  |  | 3 | 28 | 252 | 346 | 601 | 481 |
| Brunéi | BRN | 30 |  |  |  |  |  |  |  |  | 1 |  | 1 | 11 | 7 |
| Bulgaria | BGR | 552 |  |  |  |  |  |  | 1 | 2 | 29 | 23 | 50 | 146 | 88 |
| Burkina Faso | BFA | 57 |  |  |  |  |  |  |  |  | 2 | 5 | 3 | 7 | 14 |
| Burundi | BDI | 44 | 1 |  |  |  |  |  |  |  |  |  |  | 3 | 34 |
| Bután | BTN | 123 | 1 |  |  |  |  |  |  |  |  |  | 5 | 36 | 55 |
| Bélgica | BEL | 6,189 | 2 |  | 1 |  |  |  | 1 | 4 | 74 | 273 | 592 | 878 | 343 |
| Cabo Verde | CPV | 133 |  |  |  |  |  |  |  |  | 4 | 23 | 50 | 31 | 3 |
| Camboya | KHM | 142 |  |  |  |  |  |  |  |  | 3 | 13 | 6 | 27 | 58 |
| Camerún | CMR | 138 |  |  |  |  |  |  |  |  | 2 | 6 | 8 | 17 | 57 |
| Canadá | CAN | 6,933 | 8 |  |  |  |  |  | 2 |  | 22 | 147 | 1,652 | 1,841 | 1,866 |
| Catar | QAT | 100 |  |  |  |  |  |  |  | 3 | 8 | 7 | 13 | 34 | 32 |
| Chad | TCD | 86 |  |  |  |  |  |  |  |  |  | 3 | 4 | 18 | 36 |
| Chile | CHL | 1,109 |  |  |  |  |  |  |  | 2 | 9 | 145 | 207 | 351 | 151 |
| China | CHN | 4,663 | 2 | 1 |  | 1 | 9 | 2 | 4 | 5 | 48 | 162 | 491 | 1,760 | 1,287 |
| Chipre | CYP | 299 | 1 |  |  |  |  | 1 |  | 4 | 35 | 26 | 25 | 26 | 95 |
| Ciudad del Vaticano | VAT | 78 |  |  |  |  |  |  |  |  | 1 | 24 | 5 | 10 | 15 |
| Colombia | COL | 781 |  |  |  |  |  |  |  |  | 10 | 57 | 117 | 237 | 154 |
| Comoras | COM | 28 |  |  |  |  |  |  |  |  |  | 1 | 5 | 10 | 9 |
| Corea del Norte | PRK | 136 |  |  |  |  |  |  |  |  | 1 | 9 | 12 | 13 | 54 |
| Corea del Sur | KOR | 864 | 1 |  |  |  |  |  |  |  | 6 | 15 | 70 | 156 | 226 |
| Costa Rica | CRI | 194 |  |  |  |  |  |  |  |  |  | 16 | 17 | 52 | 91 |
| Costa de Marfil | CIV | 110 |  |  |  |  |  |  |  |  | 3 | 5 | 13 | 15 | 42 |
| Croacia | HRV | 975 | 5 |  |  |  |  |  | 2 | 9 | 60 | 51 | 64 | 231 | 89 |
| Cuba | CUB | 1,401 | 17 | 8 | 5 |  |  |  |  | 1 | 15 | 121 | 265 | 310 | 328 |
| Curazao | CUW | 107 |  |  |  | 1 |  |  |  |  | 1 | 3 | 27 | 12 | 2 |
| Dinamarca | DNK | 1,521 | 5 |  |  | 1 |  |  | 3 |  | 14 | 77 | 82 | 435 | 90 |
| Dominica | DMA | 41 |  |  |  |  |  |  |  |  |  | 3 | 26 | 2 |  |
| ESB | ESB | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ecuador | ECU | 435 |  |  |  |  |  |  |  | 1 | 8 | 25 | 82 | 115 | 93 |
| Egipto | EGY | 2,589 | 8 |  |  | 2 | 1 | 3 | 2 | 6 | 66 | 62 | 184 | 935 | 825 |
| El Salvador | SLV | 200 |  |  |  |  |  | 1 |  |  | 2 | 11 | 9 | 96 | 61 |
| Emiratos Árabes Unidos | ARE | 55 |  |  |  |  |  |  |  | 3 | 7 | 6 | 12 | 13 | 7 |
| Eritrea | ERI | 430 |  |  |  |  |  |  |  |  | 1 | 7 | 9 | 109 | 276 |
| Eslovaquia | SVK | 542 |  |  |  |  |  |  |  | 2 | 17 | 15 | 23 | 103 | 128 |
| Eslovenia | SVN | 325 | 1 |  |  |  |  |  |  | 2 | 22 | 9 | 5 | 18 | 108 |
| España | ESP | 8,733 | 18 |  | 25 | 12 | 17 | 10 | 10 | 23 | 126 | 451 | 1,672 | 2,971 | 1,020 |
| Estados Federados de Micronesia | FSM | 69 |  |  |  |  |  |  |  |  |  | 1 | 4 | 23 | 32 |
| Estados Unidos | USA | 376,954 | 49 |  | 2 |  | 1 | 6 | 1 | 4 | 39 | 695 | 5,486 | 119,952 | 214,248 |
| Estonia | EST | 1,098 |  |  |  |  |  |  |  | 1 | 8 | 19 | 28 | 151 | 516 |
| Etiopía | ETH | 602 | 8 |  |  |  |  | 1 | 1 | 1 | 17 | 29 | 34 | 165 | 240 |
| Filipinas | PHL | 744 |  |  |  |  |  |  |  |  | 10 | 25 | 147 | 228 | 196 |
| Finlandia | FIN | 313 |  |  |  |  |  |  |  | 1 | 8 | 25 | 45 | 60 | 37 |
| Fiyi | FJI | 78 |  |  |  |  |  |  |  |  |  | 2 | 4 | 43 | 11 |
| Francia | FRA | 22,378 | 22 | 4 | 7 | 5 | 9 | 20 | 20 | 17 | 300 | 1,406 | 3,499 | 6,781 | 1,302 |
| GIB | GIB | 5 |  |  |  |  |  |  |  |  |  |  | 5 |  |  |
| Gabón | GAB | 92 |  |  |  |  |  |  |  |  | 2 | 8 | 10 | 23 | 17 |
| Gambia | GMB | 89 |  |  |  |  |  |  |  |  | 1 | 6 | 31 | 23 | 5 |
| Georgia | GEO | 286 |  |  |  |  |  |  |  | 1 | 12 | 7 | 68 | 66 | 46 |
| Ghana | GHA | 87 |  |  |  |  |  |  | 1 |  | 2 | 8 | 8 | 9 | 20 |
| Granada | GRD | 499 | 1 |  |  |  |  | 3 |  |  | 2 | 37 | 91 | 233 | 30 |
| Grecia | GRC | 2,383 | 18 | 1 | 1 |  |  | 1 | 3 | 11 | 132 | 230 | 197 | 763 | 255 |
| Groenlandia | GRL | 229 | 2 |  |  |  |  |  | 1 |  | 8 | 15 | 44 | 90 | 29 |
| Guam | GUM | 158 |  |  |  |  |  |  |  |  |  | 4 | 19 | 10 | 111 |
| Guatemala | GTM | 244 | 1 | 1 |  |  |  |  |  |  | 3 | 17 | 12 | 63 | 82 |
| Guernsey | GGY | 251 |  |  |  |  |  |  |  |  |  | 4 | 6 | 105 | 112 |
| Guinea | GIN | 147 |  |  |  |  |  |  |  |  | 1 | 11 | 43 | 15 | 17 |
| Guinea Ecuatorial | GNQ | 40 |  |  |  |  |  |  |  |  | 1 | 2 | 2 | 11 | 18 |
| Guinea-Bisáu | GNB | 10 |  |  |  |  |  |  |  |  | 1 |  | 3 | 2 | 2 |
| Guyana | GUY | 451 |  |  |  |  |  |  |  |  | 8 | 36 | 85 | 101 | 65 |
| Haití | HTI | 412 |  |  |  |  |  | 1 |  |  | 6 | 26 | 124 | 66 | 124 |
| Honduras | HND | 287 |  |  |  |  |  |  |  |  |  | 32 | 54 | 70 | 96 |
| Hong Kong | HKG | 65 |  |  |  |  |  |  |  |  |  |  |  | 27 | 25 |
| Hungría | HUN | 1,638 |  |  |  |  |  |  | 2 | 4 | 60 | 113 | 135 | 401 | 159 |
| India | IND | 3,056 | 3 |  |  |  |  |  | 7 | 7 | 89 | 155 | 516 | 945 | 265 |
| Indonesia | IDN | 2,213 | 4 |  |  |  |  |  | 1 | 2 | 28 | 281 | 480 | 201 | 244 |
| Irak | IRQ | 658 | 7 |  |  |  | 1 |  |  | 6 | 46 | 38 | 34 | 122 | 182 |
| Irlanda | IRL | 2,450 | 5 | 1 | 2 | 2 |  |  | 1 | 4 | 88 | 134 | 198 | 751 | 66 |
| Irán | IRN | 822 | 3 |  |  |  |  |  | 3 | 5 | 48 | 52 | 141 | 261 | 90 |
| Isla Norfolk | NFK | 1,365 |  |  |  |  |  |  |  |  |  | 4 | 41 | 1,083 | 206 |
| Isla Santa Elena | SHN | 135 |  |  |  |  |  |  |  |  | 2 | 9 | 8 | 90 | 5 |
| Isla de Man | IMN | 51 |  |  |  |  |  |  |  |  |  | 3 | 4 | 22 |  |
| Islandia | ISL | 291 | 1 |  |  |  |  |  |  | 1 | 22 | 23 | 34 | 83 | 28 |
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
| Israel | ISR | 1,667 |  |  | 2 | 2 | 2 | 2 | 5 | 22 | 83 | 102 | 199 | 499 | 167 |
| Italia | ITA | 8,604 | 30 | 5 |  | 6 | 6 | 8 | 3 | 72 | 444 | 572 | 817 | 1,981 | 617 |
| Jamaica | JAM | 967 | 1 |  |  |  |  |  |  | 1 | 1 | 27 | 224 | 562 | 56 |
| Japón | JPN | 1,630 | 3 |  |  |  |  |  | 1 | 3 | 12 | 101 | 199 | 389 | 294 |
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
| Libia | LBY | 407 | 4 |  |  |  |  |  |  | 9 | 31 | 38 | 35 | 50 | 126 |
| Liechtenstein | LIE | 27 |  |  |  |  |  |  |  | 1 |  | 1 |  | 6 |  |
| Lituania | LTU | 326 |  |  |  |  |  |  | 1 | 3 | 13 | 20 | 49 | 22 | 51 |
| Luxemburgo | LUX | 546 |  |  |  |  |  |  | 1 | 1 | 15 | 63 | 101 | 104 | 60 |
| Líbano | LBN | 750 | 3 |  |  | 1 | 1 |  |  | 2 | 17 | 7 | 15 | 470 | 137 |
| Macao | MAC | 120 |  |  |  |  |  |  |  |  |  | 7 | 28 | 27 | 36 |
| Macedonia del Norte | MKD | 119 |  |  |  |  |  |  |  | 2 | 13 | 11 | 5 | 19 | 26 |
| Madagascar | MDG | 485 | 1 |  |  |  |  |  |  | 1 | 15 | 33 | 138 | 101 | 54 |
| Malasia | MYS | 264 | 4 |  |  |  |  |  |  |  | 8 | 9 | 12 | 35 | 45 |
| Malaui | MWI | 37 | 1 |  |  |  |  |  |  |  | 1 |  | 2 | 14 | 14 |
| Maldivas | MDV | 77 |  |  |  |  |  |  |  |  | 1 | 8 | 30 | 9 | 14 |
| Malta | MLT | 397 | 2 |  |  |  |  | 1 | 1 | 2 | 34 | 36 | 106 | 91 | 13 |
| Malí | MLI | 121 |  |  |  |  |  |  | 3 | 2 | 4 | 5 | 8 | 26 | 20 |
| Marruecos | MAR | 688 | 1 |  |  | 1 |  | 1 |  | 2 | 15 | 49 | 75 | 165 | 215 |
| Mauricio | MUS | 246 | 2 |  |  | 1 |  |  |  | 1 | 7 | 31 | 42 | 66 | 28 |
| Mauritania | MRT | 100 |  |  |  |  |  |  |  |  | 10 | 4 | 13 | 16 | 22 |
| Moldavia | MDA | 142 |  |  |  |  |  |  |  | 1 | 5 | 15 | 26 | 26 | 13 |
| Mongolia | MNG | 152 |  |  |  |  |  |  |  |  | 4 | 11 | 12 | 39 | 62 |
| Montenegro | MNE | 170 |  |  |  |  |  |  |  |  | 8 | 9 | 5 | 39 | 27 |
| Montserrat | MSR | 133 |  |  |  |  |  |  |  |  |  |  |  | 106 | 21 |
| Mozambique | MOZ | 270 | 1 |  |  |  |  |  |  |  | 11 | 16 | 38 | 72 | 54 |
| México | MEX | 4,162 | 3 |  |  | 1 |  | 1 | 2 | 3 | 70 | 146 | 416 | 1,253 | 1,289 |
| Mónaco | MCO | 72 | 1 |  |  |  |  |  |  |  |  | 7 | 13 | 20 | 9 |
| Namibia | NAM | 137 |  |  |  |  |  |  |  |  | 3 |  | 8 | 41 | 29 |
| Nauru | NRU | 17 |  |  |  |  |  |  |  |  |  |  |  | 3 | 11 |
| Nepal | NPL | 87 |  |  |  |  |  |  |  | 1 | 3 | 2 | 1 | 20 | 31 |
| Nicaragua | NIC | 343 |  |  |  |  |  |  |  |  | 2 | 25 | 27 | 173 | 69 |
| Nigeria | NGA | 137 |  |  |  |  |  |  |  |  | 3 | 10 | 8 | 16 | 59 |
| Niue | NIU | 7 |  |  |  |  |  |  |  |  |  |  |  | 1 | 5 |
| Noruega | NOR | 1,413 | 1 |  |  |  |  |  | 1 | 2 | 21 | 58 | 108 | 421 | 67 |
| Nueva Caledonia | NCL | 34 |  |  |  |  |  |  |  |  |  | 1 | 3 | 10 | 11 |
| Nueva Zelanda | NZL | 480 | 2 |  |  | 1 |  |  |  |  | 1 | 4 | 32 | 242 | 84 |
| Níger | NER | 70 |  |  |  |  |  |  |  |  | 4 | 5 | 3 | 5 | 26 |
| Omán | OMN | 107 |  |  |  |  |  |  |  | 4 | 12 | 10 | 31 | 18 | 11 |
| PSX | PSX | 298 |  |  |  |  |  |  |  | 1 | 17 | 8 | 7 | 106 | 2 |
| Pakistán | PAK | 434 |  |  |  |  |  |  |  |  | 28 | 7 | 11 | 112 | 131 |
| Palaos | PLW | 57 |  |  |  |  |  |  |  |  | 2 | 1 | 10 | 12 | 21 |
| Palestina | PSE | 1,565 | 5 |  |  |  | 2 | 1 | 1 | 10 | 50 | 50 | 99 | 601 | 220 |
| Panamá | PAN | 443 |  |  |  |  |  |  |  |  | 3 | 51 | 65 | 109 | 116 |
| Papúa Nueva Guinea | PNG | 152 |  |  |  |  |  |  |  |  | 2 | 4 | 4 | 38 | 77 |
| Paraguay | PRY | 370 |  |  |  |  |  |  |  |  | 1 | 21 | 65 | 105 | 58 |
| Países Bajos | NLD | 20,443 | 1 |  | 5 |  |  |  | 1 | 1 | 131 | 694 | 1,208 | 592 | 1,182 |
| Perú | PER | 1,247 | 1 |  |  |  |  |  |  |  | 26 | 71 | 134 | 457 | 230 |
| Polinesia Francesa | PYF | 70 |  |  |  |  |  |  |  |  |  | 1 | 35 | 26 | 5 |
| Polonia | POL | 3,615 | 2 |  | 2 | 3 | 3 |  | 2 | 10 | 63 | 110 | 300 | 766 | 556 |
| Portugal | PRT | 3,270 | 2 |  |  |  |  | 1 | 1 | 10 | 64 | 166 | 560 | 1,226 | 230 |
| Puerto Rico | PRI | 1,100 |  |  |  |  |  |  |  | 1 | 2 | 20 | 75 | 41 | 907 |
| Reino Unido | GBR | 13,136 | 8 | 2 | 3 | 3 | 3 | 13 |  | 9 | 75 | 524 | 1,514 | 3,244 | 551 |
| República Centroafricana | CAF | 160 |  |  |  |  |  |  |  |  |  | 2 | 3 | 10 | 114 |
| República Checa | CZE | 1,344 | 2 |  |  |  |  |  |  | 1 | 19 | 44 | 104 | 237 | 235 |
| República Democrática del Congo | COD | 225 |  |  |  |  |  |  |  |  | 3 | 6 | 9 | 31 | 128 |
| República Dominicana | DOM | 261 |  |  |  |  |  |  |  |  | 5 | 27 | 72 | 47 | 59 |
| República Turca del Norte de Chipre | CYN | 15 |  |  |  |  |  |  |  |  | 2 | 5 |  |  |  |
| República de China | TWN | 213 |  |  |  |  |  |  | 1 |  | 2 | 17 | 9 | 50 | 87 |
| República del Congo | COG | 346 | 2 |  |  |  |  |  | 1 | 1 | 11 | 15 | 38 | 129 | 84 |
| Ruanda | RWA | 45 | 1 |  |  |  |  |  |  |  |  |  |  | 4 | 34 |
| Rumania | ROU | 1,201 |  |  |  |  |  |  |  | 3 | 56 | 36 | 56 | 198 | 211 |
| Rusia | RUS | 5,588 | 5 |  |  | 1 |  | 1 | 2 | 7 | 87 | 176 | 406 | 1,950 | 1,277 |
| SAH | SAH | 4 |  |  |  |  |  |  |  |  |  | 2 |  | 1 |  |
| SDS | SDS | 82 |  |  |  |  |  |  |  |  |  | 1 |  | 10 | 19 |
| Sahara Occidental | ESH | 41 |  |  |  |  |  |  | 1 |  |  | 2 | 1 | 19 | 16 |
| Samoa | WSM | 72 | 1 |  |  |  |  |  |  |  |  |  | 6 | 31 | 25 |
| Samoa Estadounidense | ASM | 26 |  |  |  |  |  |  |  |  |  |  |  | 14 | 7 |
| San Bartolomé | BLM | 6 |  |  |  |  |  |  |  |  |  |  | 3 | 2 |  |
| San Cristóbal y Nieves | KNA | 34 |  |  |  |  |  |  |  |  |  | 5 | 17 | 2 | 3 |
| San Marino | SMR | 8 |  |  | 1 |  |  |  |  |  |  | 1 | 1 | 1 | 2 |
| San Martín | MAF | 94 |  |  |  |  |  |  |  |  |  | 3 | 15 | 43 | 8 |
| San Martín | SXM | 48 |  |  |  |  |  |  |  | 1 |  | 2 | 9 | 23 | 3 |
| San Pedro y Miquelón | SPM | 8 |  |  |  |  |  |  |  |  |  |  | 1 | 5 | 1 |
| San Vicente y las Granadinas | VCT | 23 | 1 |  |  |  |  |  |  |  |  |  | 6 | 11 | 4 |
| Santa Lucía | LCA | 42 |  |  |  |  |  |  |  |  |  | 1 | 21 | 6 | 5 |
| Santo Tomé y Príncipe | STP | 28 |  |  |  | 1 |  |  |  |  |  | 10 | 10 | 4 | 1 |
| Senegal | SEN | 243 |  |  |  |  |  |  |  |  | 2 | 14 | 80 | 84 | 18 |
| Serbia | SRB | 571 |  |  |  |  |  |  |  | 4 | 30 | 20 | 39 | 146 | 77 |
| Seychelles | SYC | 4 |  |  |  |  |  |  |  |  |  |  | 1 | 3 |  |
| Sierra Leona | SLE | 198 |  |  |  |  |  |  |  | 1 | 2 | 10 | 23 | 20 | 106 |
| Singapur | SGP | 91 |  |  |  |  |  |  |  | 1 | 2 | 1 | 7 | 29 | 19 |
| Siria | SYR | 1,074 | 2 |  |  | 1 | 1 |  | 1 | 4 | 47 | 39 | 90 | 516 | 125 |
| Somalia | SOM | 200 |  |  |  |  |  |  |  | 1 | 11 | 7 | 6 | 22 | 108 |
| Somalilandia | SOL | 225 |  |  |  |  |  |  |  |  | 2 | 4 |  | 33 | 170 |
| Sri Lanka | LKA | 304 |  |  |  |  |  |  | 2 | 2 | 21 | 43 | 38 | 60 | 27 |
| Suazilandia | SWZ | 46 |  |  |  | 1 |  |  |  |  |  |  |  | 3 | 39 |
| Sudáfrica | ZAF | 787 | 5 |  |  |  |  | 1 |  |  | 6 | 28 | 51 | 310 | 176 |
| Sudán | SDN | 575 | 1 | 3 |  |  |  |  |  | 2 | 9 | 19 | 16 | 131 | 258 |
| Sudán del Sur | SSD | 202 |  |  |  |  |  |  |  |  | 1 | 4 | 2 | 17 | 89 |
| Suecia | SWE | 1,784 | 2 |  |  |  |  |  | 1 | 3 | 15 | 73 | 116 | 422 | 60 |
| Suiza | CHE | 2,744 | 3 |  |  |  |  | 1 | 1 | 5 | 61 | 72 | 177 | 606 | 196 |
| Surinam | SUR | 514 |  |  |  |  |  |  |  |  | 6 | 28 | 58 | 63 | 63 |
| Tailandia | THA | 280 | 1 |  |  |  |  |  | 2 | 1 | 13 | 27 | 31 | 71 | 63 |
| Tanzania | TZA | 215 | 1 |  |  |  |  |  |  |  | 4 | 2 | 3 | 51 | 85 |
| Tayikistán | TJK | 61 |  |  |  |  |  |  |  |  | 6 |  |  | 29 | 15 |
| Territorio Británico del Océano Índico | IOT | 1 |  |  |  |  |  |  |  |  |  |  |  |  | 1 |
| Territorios Australianos del Océano Índico | IOA | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Tierras Australes y Antárticas Francesas | ATF | 4 |  |  |  |  |  |  |  |  |  |  |  | 1 |  |
| Timor Oriental | TLS | 15 |  |  |  |  |  |  |  |  |  |  |  |  | 2 |
| Togo | TGO | 61 |  |  |  |  |  |  |  |  | 1 | 1 | 2 | 8 | 20 |
| Tonga | TON | 49 |  |  |  |  |  |  |  |  |  | 4 | 7 | 15 | 11 |
| Trinidad y Tobago | TTO | 102 |  |  |  |  |  |  |  |  | 1 | 19 | 35 | 12 | 32 |
| Turkmenistán | TKM | 137 |  |  |  |  |  |  |  |  | 14 | 6 | 5 | 54 | 20 |
| Turquía | TUR | 2,772 | 14 |  |  | 2 |  | 1 | 7 | 8 | 114 | 160 | 306 | 930 | 359 |
| Tuvalu | TUV | 14 |  |  |  |  |  |  |  |  |  |  |  | 8 | 4 |
| Túnez | TUN | 652 | 3 |  |  |  |  | 1 | 1 | 2 | 35 | 26 | 34 | 229 | 182 |
| UMI | UMI | 2 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |
| USG | USG | 3 |  |  |  |  |  |  |  |  |  |  | 1 | 1 |  |
| Ucrania | UKR | 830 | 1 |  |  |  |  |  | 4 | 4 | 32 | 92 | 80 | 101 | 100 |
| Uganda | UGA | 254 |  |  |  |  |  |  |  |  | 1 | 3 | 3 | 19 | 194 |
| Uruguay | URY | 386 |  |  |  |  |  |  |  |  | 4 | 22 | 55 | 137 | 79 |
| Uzbekistán | UZB | 135 |  |  |  |  |  |  |  |  | 7 | 6 | 6 | 65 | 31 |
| Vanuatu | VUT | 15 |  |  |  |  |  |  |  |  |  |  |  | 2 | 13 |
| Venezuela | VEN | 640 |  |  |  |  |  |  |  | 1 | 12 | 89 | 129 | 169 | 80 |
| Vietnam | VNM | 346 |  |  |  |  |  |  |  | 2 | 8 | 5 | 18 | 53 | 87 |
| Yemen | YEM | 454 |  |  |  |  |  |  |  | 5 | 25 | 16 | 29 | 48 | 276 |
| Yibuti | DJI | 59 |  |  |  |  |  |  |  |  | 2 | 2 | 3 | 28 | 21 |
| Zambia | ZMB | 106 |  |  |  |  |  |  |  |  | 1 | 3 | 4 | 21 | 45 |
| Zimbabue | ZWE | 110 |  |  |  |  |  |  |  |  | 2 | 1 | 6 | 26 | 43 |
| Åland | ALA | 12 |  |  |  |  |  |  |  |  |  | 1 | 2 | 6 |  |
