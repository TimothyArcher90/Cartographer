# Biblioteca de Cartographer

Documento generado por `scripts/comprender.py`. No editar a mano.

- Mapas analizados: **889,552** · con país asignado: **532,624** · sin país: 356,928
  (sobre todo mapamundis, cartas oceánicas o registros sin datos de lugar).
- Países con mapas: **244**.
- Tipos: general 553,267, topográfico 209,154, histórico/temático 62,687, plano urbano 32,077, militar 11,093, mapamundi 7,270, ferroviario/viario 6,660, carta náutica 5,930, portulano 777, ptolemaico 637.
- Escalas: desconocida 619,756, local o ciudad 245,025, provincia o comarca 14,152, región o país 6,100, continente 2,997, mundo 1,522.

Cómo se asigna un país: por **nombre** actual (25+ idiomas, Natural Earth), por **nombre histórico**
(`catalogo/nombres_historicos.json`) o por **coordenadas** de la cobertura del mapa. Cada mapa guarda
la vía en el campo `via`; las asignaciones por coordenadas de mapas grandes pueden incluir países
vecinos. Los siglos salen del año de los metadatos de cada archivo y pueden tener errores puntuales.

Mapas de un país: `catalogo/biblioteca/paises/<ISO3>.jsonl.gz` o
`python scripts/buscar_lugar.py "<país>"`.

| País | ISO | Total | Antes del s. IX | IX | X | XI | XII | XIII | XIV | XV | XVI | XVII | XVIII | XIX | XX |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Afganistán | AFG | 532 | 1 |  |  |  |  |  | 1 |  | 21 | 7 | 12 | 223 | 113 |
| Albania | ALB | 358 | 1 |  |  |  |  | 2 | 2 | 7 | 27 | 35 | 30 | 87 | 65 |
| Alemania | DEU | 15,469 | 6 | 4 | 4 | 2 | 3 | 3 | 2 | 12 | 147 | 392 | 590 | 2,108 | 979 |
| Andorra | AND | 43 | 2 |  |  |  |  |  |  |  |  |  | 2 | 5 | 22 |
| Angola | AGO | 243 |  |  |  |  |  |  |  | 1 | 4 | 14 | 28 | 66 | 92 |
| Anguila | AIA | 14 |  |  |  |  |  |  |  |  |  | 2 | 6 | 2 | 1 |
| Antigua y Barbuda | ATG | 40 |  |  |  |  |  |  |  |  |  | 2 | 16 | 17 | 1 |
| Antártida | ATA | 120 |  |  |  |  |  |  |  |  |  | 13 | 24 | 10 | 55 |
| Arabia Saudita | SAU | 689 | 1 |  |  |  |  |  |  | 6 | 51 | 43 | 79 | 198 | 149 |
| Argelia | DZA | 841 | 2 |  |  |  |  | 1 | 1 | 3 | 24 | 44 | 44 | 361 | 153 |
| Argentina | ARG | 978 |  |  |  |  |  |  |  |  | 8 | 108 | 112 | 204 | 375 |
| Armenia | ARM | 453 | 2 | 1 |  | 1 |  |  | 1 | 2 | 22 | 18 | 36 | 188 | 105 |
| Aruba | ABW | 23 |  |  |  |  |  |  |  |  |  |  | 3 | 6 | 4 |
| Australia | AUS | 2,526 | 5 |  |  |  |  |  | 1 |  | 8 | 19 | 51 | 449 | 111 |
| Austria | AUT | 2,487 | 2 | 1 |  |  |  |  | 1 | 4 | 50 | 73 | 143 | 599 | 291 |
| Azerbaiyán | AZE | 141 |  |  |  |  |  |  |  | 1 | 8 | 7 | 10 | 46 | 38 |
| Bahamas | BHS | 209 |  |  |  |  |  | 1 |  |  |  | 9 | 68 | 65 | 33 |
| Bangladés | BGD | 57 |  |  |  |  |  |  |  | 1 | 4 | 5 | 4 | 7 | 8 |
| Barbados | BRB | 133 |  |  |  |  |  |  |  |  |  | 12 | 45 | 16 | 30 |
| Baréin | BHR | 82 |  |  |  |  |  |  |  | 2 | 6 | 6 | 11 | 19 | 27 |
| Belice | BLZ | 73 |  |  |  |  |  |  |  |  |  | 9 | 5 | 17 | 34 |
| Benín | BEN | 72 |  |  |  |  |  |  |  |  | 4 | 7 | 6 | 11 | 16 |
| Bermudas | BMU | 127 |  |  |  |  |  |  |  |  | 1 | 13 | 34 | 29 | 16 |
| Bielorrusia | BLR | 312 | 1 |  |  |  |  |  |  | 3 | 22 | 20 | 33 | 46 | 85 |
| Birmania | MMR | 242 | 1 |  |  |  |  |  |  | 1 | 11 | 9 | 26 | 64 | 70 |
| Bolivia | BOL | 323 |  |  |  |  |  |  |  |  | 5 | 19 | 11 | 96 | 88 |
| Bosnia y Herzegovina | BIH | 464 | 2 |  |  |  |  |  |  | 6 | 37 | 15 | 22 | 113 | 75 |
| Botsuana | BWA | 163 |  |  |  | 2 |  |  |  |  | 2 |  | 5 | 47 | 56 |
| Brasil | BRA | 2,402 | 3 |  |  |  |  |  |  | 3 | 27 | 249 | 312 | 582 | 475 |
| Brunéi | BRN | 30 |  |  |  |  |  |  |  |  | 1 |  | 1 | 11 | 7 |
| Bulgaria | BGR | 545 |  |  |  |  |  |  | 1 | 2 | 28 | 23 | 49 | 142 | 87 |
| Burkina Faso | BFA | 57 |  |  |  |  |  |  |  |  | 2 | 5 | 3 | 7 | 14 |
| Burundi | BDI | 44 | 1 |  |  |  |  |  |  |  |  |  |  | 3 | 34 |
| Bután | BTN | 123 | 1 |  |  |  |  |  |  |  |  |  | 5 | 36 | 55 |
| Bélgica | BEL | 6,106 | 1 |  | 1 |  |  |  | 1 | 4 | 74 | 259 | 573 | 844 | 336 |
| Cabo Verde | CPV | 132 |  |  |  |  |  |  |  |  | 4 | 22 | 50 | 31 | 3 |
| Camboya | KHM | 141 |  |  |  |  |  |  |  |  | 3 | 13 | 6 | 27 | 57 |
| Camerún | CMR | 132 |  |  |  |  |  |  |  |  | 2 | 6 | 8 | 14 | 54 |
| Canadá | CAN | 6,879 | 8 |  |  |  |  |  | 2 |  | 22 | 142 | 1,631 | 1,829 | 1,856 |
| Catar | QAT | 100 |  |  |  |  |  |  |  | 3 | 8 | 7 | 13 | 34 | 32 |
| Chad | TCD | 85 |  |  |  |  |  |  |  |  |  | 3 | 4 | 18 | 35 |
| Chile | CHL | 1,081 |  |  |  |  |  |  |  | 2 | 8 | 142 | 197 | 344 | 149 |
| China | CHN | 4,587 | 2 | 1 |  |  | 9 | 2 | 4 | 5 | 47 | 157 | 473 | 1,719 | 1,283 |
| Chipre | CYP | 298 | 1 |  |  |  |  | 1 |  | 4 | 35 | 26 | 25 | 25 | 95 |
| Ciudad del Vaticano | VAT | 78 |  |  |  |  |  |  |  |  | 1 | 24 | 5 | 10 | 15 |
| Colombia | COL | 693 |  |  |  |  |  |  |  |  | 10 | 55 | 116 | 159 | 153 |
| Comoras | COM | 26 |  |  |  |  |  |  |  |  |  | 1 | 4 | 10 | 9 |
| Corea del Norte | PRK | 136 |  |  |  |  |  |  |  |  | 1 | 9 | 12 | 13 | 54 |
| Corea del Sur | KOR | 859 | 1 |  |  |  |  |  |  |  | 6 | 15 | 70 | 152 | 225 |
| Costa Rica | CRI | 194 |  |  |  |  |  |  |  |  |  | 16 | 17 | 52 | 91 |
| Costa de Marfil | CIV | 110 |  |  |  |  |  |  |  |  | 3 | 5 | 13 | 15 | 42 |
| Croacia | HRV | 966 | 5 |  |  |  |  |  | 2 | 9 | 59 | 49 | 62 | 230 | 89 |
| Cuba | CUB | 1,371 | 17 | 8 | 5 |  |  |  |  | 1 | 15 | 118 | 250 | 301 | 328 |
| Curazao | CUW | 104 |  |  |  |  |  |  |  |  | 1 | 2 | 26 | 12 | 2 |
| Dinamarca | DNK | 1,506 | 5 |  |  |  |  |  | 3 |  | 13 | 75 | 79 | 427 | 89 |
| Dominica | DMA | 34 |  |  |  |  |  |  |  |  |  | 3 | 22 | 2 |  |
| ESB | ESB | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ecuador | ECU | 415 |  |  |  |  |  |  |  | 1 | 8 | 24 | 77 | 104 | 92 |
| Egipto | EGY | 2,546 | 8 |  |  | 2 | 1 | 3 | 2 | 6 | 65 | 52 | 179 | 925 | 810 |
| El Salvador | SLV | 197 |  |  |  |  |  | 1 |  |  | 1 | 10 | 8 | 96 | 61 |
| Emiratos Árabes Unidos | ARE | 55 |  |  |  |  |  |  |  | 3 | 7 | 6 | 12 | 13 | 7 |
| Eritrea | ERI | 426 |  |  |  |  |  |  |  |  | 1 | 7 | 7 | 107 | 276 |
| Eslovaquia | SVK | 539 |  |  |  |  |  |  |  | 2 | 17 | 15 | 23 | 103 | 125 |
| Eslovenia | SVN | 325 | 1 |  |  |  |  |  |  | 2 | 22 | 9 | 5 | 18 | 108 |
| España | ESP | 8,586 | 18 |  | 23 | 10 | 16 | 9 | 10 | 22 | 123 | 414 | 1,639 | 2,932 | 1,007 |
| Estados Federados de Micronesia | FSM | 69 |  |  |  |  |  |  |  |  |  | 1 | 4 | 23 | 32 |
| Estados Unidos | USA | 376,632 | 50 |  | 2 |  | 1 | 6 | 1 | 4 | 39 | 690 | 5,474 | 119,708 | 214,177 |
| Estonia | EST | 1,098 |  |  |  |  |  |  |  | 1 | 8 | 19 | 28 | 151 | 516 |
| Etiopía | ETH | 595 | 8 |  |  |  |  | 1 | 1 | 1 | 16 | 28 | 32 | 162 | 240 |
| Filipinas | PHL | 697 |  |  |  |  |  |  |  |  | 10 | 25 | 108 | 226 | 191 |
| Finlandia | FIN | 297 |  |  |  |  |  |  |  | 1 | 8 | 24 | 37 | 56 | 35 |
| Fiyi | FJI | 78 |  |  |  |  |  |  |  |  |  | 2 | 4 | 43 | 11 |
| Francia | FRA | 21,495 | 22 | 4 | 7 | 4 | 9 | 20 | 20 | 17 | 289 | 1,322 | 3,212 | 6,469 | 1,201 |
| GIB | GIB | 5 |  |  |  |  |  |  |  |  |  |  | 5 |  |  |
| Gabón | GAB | 92 |  |  |  |  |  |  |  |  | 2 | 8 | 10 | 23 | 17 |
| Gambia | GMB | 82 |  |  |  |  |  |  |  |  | 1 | 6 | 31 | 23 | 4 |
| Georgia | GEO | 286 |  |  |  |  |  |  |  | 1 | 12 | 7 | 68 | 66 | 46 |
| Ghana | GHA | 87 |  |  |  |  |  |  | 1 |  | 2 | 8 | 8 | 9 | 20 |
| Granada | GRD | 472 | 1 |  |  |  |  | 3 |  |  | 2 | 31 | 82 | 228 | 30 |
| Grecia | GRC | 2,359 | 18 | 1 | 1 |  |  | 1 | 3 | 10 | 130 | 225 | 184 | 759 | 254 |
| Groenlandia | GRL | 228 | 2 |  |  |  |  |  | 1 |  | 8 | 15 | 44 | 90 | 29 |
| Guam | GUM | 155 |  |  |  |  |  |  |  |  |  | 4 | 16 | 10 | 111 |
| Guatemala | GTM | 240 | 1 | 1 |  |  |  |  |  |  | 3 | 17 | 12 | 60 | 82 |
| Guernsey | GGY | 246 |  |  |  |  |  |  |  |  |  | 4 | 6 | 104 | 111 |
| Guinea | GIN | 146 |  |  |  |  |  |  |  |  | 1 | 11 | 42 | 15 | 17 |
| Guinea Ecuatorial | GNQ | 40 |  |  |  |  |  |  |  |  | 1 | 2 | 2 | 11 | 18 |
| Guinea-Bisáu | GNB | 10 |  |  |  |  |  |  |  |  | 1 |  | 3 | 2 | 2 |
| Guyana | GUY | 442 |  |  |  |  |  |  |  |  | 8 | 35 | 81 | 99 | 64 |
| Haití | HTI | 410 |  |  |  |  |  | 1 |  |  | 6 | 26 | 123 | 66 | 124 |
| Honduras | HND | 285 |  |  |  |  |  |  |  |  |  | 32 | 52 | 70 | 96 |
| Hong Kong | HKG | 63 |  |  |  |  |  |  |  |  |  |  |  | 26 | 24 |
| Hungría | HUN | 1,609 |  |  |  |  |  |  | 2 | 4 | 60 | 113 | 126 | 388 | 153 |
| India | IND | 2,990 | 3 |  |  |  |  |  | 7 | 7 | 88 | 147 | 484 | 930 | 258 |
| Indonesia | IDN | 2,111 | 4 |  |  |  |  |  | 1 | 2 | 28 | 272 | 397 | 199 | 243 |
| Irak | IRQ | 650 | 7 |  |  |  | 1 |  |  | 6 | 46 | 38 | 32 | 121 | 178 |
| Irlanda | IRL | 2,389 | 5 | 1 | 2 | 2 |  |  | 1 | 4 | 87 | 119 | 167 | 749 | 63 |
| Irán | IRN | 803 | 3 |  |  |  |  |  | 3 | 5 | 48 | 47 | 134 | 257 | 89 |
| Isla Norfolk | NFK | 1,362 |  |  |  |  |  |  |  |  |  | 3 | 40 | 1,083 | 206 |
| Isla Santa Elena | SHN | 134 |  |  |  |  |  |  |  |  | 2 | 9 | 8 | 89 | 5 |
| Isla de Man | IMN | 47 |  |  |  |  |  |  |  |  |  | 1 | 3 | 22 |  |
| Islandia | ISL | 279 | 1 |  |  |  |  |  |  | 1 | 22 | 23 | 32 | 73 | 28 |
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
| Israel | ISR | 1,637 |  |  | 2 | 2 | 2 | 2 | 4 | 21 | 78 | 88 | 196 | 496 | 166 |
| Italia | ITA | 8,336 | 30 | 5 |  | 4 | 6 | 8 | 3 | 59 | 381 | 540 | 761 | 1,928 | 599 |
| Jamaica | JAM | 959 | 1 |  |  |  |  |  |  | 1 | 1 | 26 | 223 | 560 | 55 |
| Japón | JPN | 1,605 | 3 |  |  |  |  |  | 1 | 3 | 12 | 99 | 198 | 377 | 286 |
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
| Libia | LBY | 386 | 4 |  |  |  |  |  |  | 9 | 25 | 34 | 31 | 49 | 123 |
| Liechtenstein | LIE | 27 |  |  |  |  |  |  |  | 1 |  | 1 |  | 6 |  |
| Lituania | LTU | 319 |  |  |  |  |  |  |  | 3 | 13 | 16 | 48 | 22 | 50 |
| Luxemburgo | LUX | 533 |  |  |  |  |  |  | 1 | 1 | 15 | 58 | 96 | 104 | 58 |
| Líbano | LBN | 746 | 3 |  |  | 1 | 1 |  |  | 2 | 17 | 7 | 15 | 470 | 134 |
| Macao | MAC | 111 |  |  |  |  |  |  |  |  |  | 6 | 26 | 24 | 36 |
| Macedonia del Norte | MKD | 119 |  |  |  |  |  |  |  | 2 | 13 | 11 | 5 | 19 | 26 |
| Madagascar | MDG | 455 | 1 |  |  |  |  |  |  | 1 | 15 | 32 | 124 | 100 | 50 |
| Malasia | MYS | 264 | 4 |  |  |  |  |  |  |  | 8 | 9 | 12 | 35 | 45 |
| Malaui | MWI | 37 | 1 |  |  |  |  |  |  |  | 1 |  | 2 | 14 | 14 |
| Maldivas | MDV | 76 |  |  |  |  |  |  |  |  | 1 | 8 | 29 | 9 | 14 |
| Malta | MLT | 364 | 2 |  |  |  |  | 1 | 1 | 2 | 30 | 34 | 92 | 88 | 12 |
| Malí | MLI | 121 |  |  |  |  |  |  | 3 | 2 | 4 | 5 | 8 | 26 | 20 |
| Marruecos | MAR | 675 | 1 |  |  |  |  | 1 |  | 2 | 15 | 48 | 75 | 162 | 207 |
| Mauricio | MUS | 219 | 2 |  |  | 1 |  |  |  | 1 | 7 | 20 | 36 | 62 | 26 |
| Mauritania | MRT | 96 |  |  |  |  |  |  |  |  | 10 | 4 | 13 | 16 | 18 |
| Moldavia | MDA | 142 |  |  |  |  |  |  |  | 1 | 5 | 15 | 26 | 26 | 13 |
| Mongolia | MNG | 150 |  |  |  |  |  |  |  |  | 4 | 11 | 10 | 39 | 62 |
| Montenegro | MNE | 166 |  |  |  |  |  |  |  |  | 8 | 9 | 5 | 36 | 26 |
| Montserrat | MSR | 133 |  |  |  |  |  |  |  |  |  |  |  | 106 | 21 |
| Mozambique | MOZ | 266 | 1 |  |  |  |  |  |  |  | 11 | 16 | 36 | 70 | 54 |
| México | MEX | 4,128 | 3 |  |  |  |  | 1 | 2 | 3 | 68 | 138 | 410 | 1,241 | 1,282 |
| Mónaco | MCO | 69 | 1 |  |  |  |  |  |  |  |  | 7 | 12 | 20 | 7 |
| Namibia | NAM | 137 |  |  |  |  |  |  |  |  | 3 |  | 8 | 41 | 29 |
| Nauru | NRU | 17 |  |  |  |  |  |  |  |  |  |  |  | 3 | 11 |
| Nepal | NPL | 87 |  |  |  |  |  |  |  | 1 | 3 | 2 | 1 | 20 | 31 |
| Nicaragua | NIC | 340 |  |  |  |  |  |  |  |  | 2 | 25 | 26 | 172 | 69 |
| Nigeria | NGA | 135 |  |  |  |  |  |  |  |  | 3 | 10 | 8 | 16 | 57 |
| Niue | NIU | 7 |  |  |  |  |  |  |  |  |  |  |  | 1 | 5 |
| Noruega | NOR | 1,403 | 1 |  |  |  |  |  | 1 | 2 | 21 | 56 | 107 | 417 | 64 |
| Nueva Caledonia | NCL | 31 |  |  |  |  |  |  |  |  |  | 1 | 3 | 9 | 10 |
| Nueva Zelanda | NZL | 476 | 2 |  |  | 1 |  |  |  |  | 1 | 3 | 32 | 242 | 81 |
| Níger | NER | 70 |  |  |  |  |  |  |  |  | 4 | 5 | 3 | 5 | 26 |
| Omán | OMN | 101 |  |  |  |  |  |  |  | 4 | 12 | 10 | 25 | 18 | 11 |
| PSX | PSX | 298 |  |  |  |  |  |  |  | 1 | 17 | 8 | 7 | 106 | 2 |
| Pakistán | PAK | 433 |  |  |  |  |  |  |  |  | 28 | 7 | 11 | 112 | 130 |
| Palaos | PLW | 56 |  |  |  |  |  |  |  |  | 2 | 1 | 10 | 12 | 20 |
| Palestina | PSE | 1,537 | 5 |  |  |  | 2 | 1 | 1 | 10 | 49 | 47 | 93 | 594 | 213 |
| Panamá | PAN | 429 |  |  |  |  |  |  |  |  | 3 | 51 | 62 | 101 | 115 |
| Papúa Nueva Guinea | PNG | 152 |  |  |  |  |  |  |  |  | 2 | 4 | 4 | 38 | 77 |
| Paraguay | PRY | 363 |  |  |  |  |  |  |  |  | 1 | 20 | 64 | 102 | 57 |
| Países Bajos | NLD | 19,600 | 1 |  | 5 |  |  |  | 1 | 1 | 127 | 559 | 729 | 569 | 1,038 |
| Perú | PER | 1,203 | 1 |  |  |  |  |  |  |  | 26 | 69 | 120 | 445 | 230 |
| Polinesia Francesa | PYF | 70 |  |  |  |  |  |  |  |  |  | 1 | 35 | 26 | 5 |
| Polonia | POL | 3,567 | 2 |  | 2 | 1 | 2 |  | 2 | 8 | 59 | 101 | 287 | 761 | 541 |
| Portugal | PRT | 3,238 | 2 |  |  |  |  | 1 | 1 | 10 | 62 | 163 | 548 | 1,216 | 228 |
| Puerto Rico | PRI | 1,084 |  |  |  |  |  |  |  | 1 | 2 | 20 | 71 | 40 | 906 |
| Reino Unido | GBR | 13,027 | 8 | 2 | 3 | 3 | 3 | 13 |  | 8 | 74 | 496 | 1,471 | 3,226 | 535 |
| República Centroafricana | CAF | 160 |  |  |  |  |  |  |  |  |  | 2 | 3 | 10 | 114 |
| República Checa | CZE | 1,321 | 2 |  |  |  |  |  |  | 1 | 19 | 38 | 94 | 234 | 230 |
| República Democrática del Congo | COD | 225 |  |  |  |  |  |  |  |  | 3 | 6 | 9 | 31 | 128 |
| República Dominicana | DOM | 260 |  |  |  |  |  |  |  |  | 5 | 27 | 71 | 47 | 59 |
| República Turca del Norte de Chipre | CYN | 15 |  |  |  |  |  |  |  |  | 2 | 5 |  |  |  |
| República de China | TWN | 212 |  |  |  |  |  |  | 1 |  | 2 | 17 | 9 | 50 | 87 |
| República del Congo | COG | 324 | 2 |  |  |  |  |  | 1 | 1 | 8 | 12 | 37 | 119 | 80 |
| Ruanda | RWA | 43 | 1 |  |  |  |  |  |  |  |  |  |  | 4 | 32 |
| Rumania | ROU | 1,180 |  |  |  |  |  |  |  | 3 | 51 | 32 | 54 | 193 | 207 |
| Rusia | RUS | 5,512 | 5 |  |  |  |  | 1 | 2 | 7 | 86 | 164 | 383 | 1,928 | 1,260 |
| SAH | SAH | 4 |  |  |  |  |  |  |  |  |  | 2 |  | 1 |  |
| SDS | SDS | 82 |  |  |  |  |  |  |  |  |  | 1 |  | 10 | 19 |
| Sahara Occidental | ESH | 39 |  |  |  |  |  |  | 1 |  |  | 2 | 1 | 19 | 14 |
| Samoa | WSM | 72 | 1 |  |  |  |  |  |  |  |  |  | 6 | 31 | 25 |
| Samoa Estadounidense | ASM | 26 |  |  |  |  |  |  |  |  |  |  |  | 14 | 7 |
| San Bartolomé | BLM | 6 |  |  |  |  |  |  |  |  |  |  | 3 | 2 |  |
| San Cristóbal y Nieves | KNA | 34 |  |  |  |  |  |  |  |  |  | 5 | 17 | 2 | 3 |
| San Marino | SMR | 8 |  |  | 1 |  |  |  |  |  |  | 1 | 1 | 1 | 2 |
| San Martín | MAF | 81 |  |  |  |  |  |  |  |  |  | 2 | 12 | 39 | 8 |
| San Martín | SXM | 38 |  |  |  |  |  |  |  | 1 |  | 1 | 7 | 19 | 3 |
| San Pedro y Miquelón | SPM | 8 |  |  |  |  |  |  |  |  |  |  | 1 | 5 | 1 |
| San Vicente y las Granadinas | VCT | 23 | 1 |  |  |  |  |  |  |  |  |  | 6 | 11 | 4 |
| Santa Lucía | LCA | 40 |  |  |  |  |  |  |  |  |  | 1 | 21 | 6 | 5 |
| Santo Tomé y Príncipe | STP | 28 |  |  |  | 1 |  |  |  |  |  | 10 | 10 | 4 | 1 |
| Senegal | SEN | 226 |  |  |  |  |  |  |  |  | 2 | 10 | 76 | 78 | 15 |
| Serbia | SRB | 565 |  |  |  |  |  |  |  | 4 | 29 | 20 | 38 | 145 | 74 |
| Seychelles | SYC | 3 |  |  |  |  |  |  |  |  |  |  |  | 3 |  |
| Sierra Leona | SLE | 188 |  |  |  |  |  |  |  | 1 | 2 | 10 | 22 | 19 | 98 |
| Singapur | SGP | 82 |  |  |  |  |  |  |  | 1 | 2 | 1 | 1 | 29 | 17 |
| Siria | SYR | 1,041 | 2 |  |  | 1 | 1 |  | 1 | 4 | 47 | 36 | 83 | 511 | 113 |
| Somalia | SOM | 199 |  |  |  |  |  |  |  | 1 | 11 | 7 | 6 | 22 | 107 |
| Somalilandia | SOL | 224 |  |  |  |  |  |  |  |  | 2 | 4 |  | 33 | 169 |
| Sri Lanka | LKA | 298 |  |  |  |  |  |  | 2 | 2 | 18 | 42 | 37 | 60 | 26 |
| Suazilandia | SWZ | 46 |  |  |  | 1 |  |  |  |  |  |  |  | 3 | 39 |
| Sudáfrica | ZAF | 775 | 5 |  |  |  |  | 1 |  |  | 6 | 28 | 49 | 300 | 176 |
| Sudán | SDN | 558 | 1 | 3 |  |  |  |  |  | 2 | 9 | 19 | 16 | 119 | 255 |
| Sudán del Sur | SSD | 202 |  |  |  |  |  |  |  |  | 1 | 4 | 2 | 17 | 89 |
| Suecia | SWE | 1,720 | 2 |  |  |  |  |  | 1 | 3 | 15 | 67 | 96 | 395 | 55 |
| Suiza | CHE | 2,721 | 3 |  |  |  |  | 1 | 1 | 5 | 60 | 72 | 177 | 597 | 182 |
| Surinam | SUR | 511 |  |  |  |  |  |  |  |  | 6 | 27 | 56 | 63 | 63 |
| Tailandia | THA | 266 | 1 |  |  |  |  |  | 2 | 1 | 13 | 21 | 27 | 70 | 60 |
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
| Turquía | TUR | 2,691 | 14 |  |  | 1 |  | 1 | 7 | 8 | 111 | 151 | 285 | 915 | 335 |
| Tuvalu | TUV | 14 |  |  |  |  |  |  |  |  |  |  |  | 8 | 4 |
| Túnez | TUN | 632 | 3 |  |  |  |  | 1 | 1 | 2 | 32 | 24 | 29 | 222 | 180 |
| UMI | UMI | 2 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |
| USG | USG | 3 |  |  |  |  |  |  |  |  |  |  | 1 | 1 |  |
| Ucrania | UKR | 807 | 1 |  |  |  |  |  | 4 | 4 | 32 | 78 | 75 | 99 | 98 |
| Uganda | UGA | 253 |  |  |  |  |  |  |  |  | 1 | 3 | 3 | 19 | 193 |
| Uruguay | URY | 372 |  |  |  |  |  |  |  |  | 4 | 22 | 53 | 132 | 71 |
| Uzbekistán | UZB | 135 |  |  |  |  |  |  |  |  | 7 | 6 | 6 | 65 | 31 |
| Vanuatu | VUT | 15 |  |  |  |  |  |  |  |  |  |  |  | 2 | 13 |
| Venezuela | VEN | 582 |  |  |  |  |  |  |  | 1 | 12 | 84 | 125 | 124 | 79 |
| Vietnam | VNM | 346 |  |  |  |  |  |  |  | 2 | 8 | 5 | 18 | 53 | 87 |
| Yemen | YEM | 442 |  |  |  |  |  |  |  | 5 | 25 | 16 | 20 | 46 | 276 |
| Yibuti | DJI | 58 |  |  |  |  |  |  |  |  | 2 | 2 | 3 | 28 | 20 |
| Zambia | ZMB | 106 |  |  |  |  |  |  |  |  | 1 | 3 | 4 | 21 | 45 |
| Zimbabue | ZWE | 110 |  |  |  |  |  |  |  |  | 2 | 1 | 6 | 26 | 43 |
| Åland | ALA | 7 |  |  |  |  |  |  |  |  |  |  | 1 | 3 |  |
