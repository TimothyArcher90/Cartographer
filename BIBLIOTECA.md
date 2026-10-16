# Biblioteca de Cartographer

Documento generado por `scripts/comprender.py`. No editar a mano.

- Mapas analizados: **809,539** · con país asignado: **500,647** · sin país: 308,892
  (sobre todo mapamundis, cartas oceánicas o registros sin datos de lugar).
- Países con mapas: **244**.
- Tipos: general 523,056, topográfico 204,172, histórico/temático 30,574, plano urbano 24,164, militar 10,271, mapamundi 6,086, ferroviario/viario 5,335, carta náutica 4,732, portulano 758, ptolemaico 391.
- Escalas: desconocida 539,743, local o ciudad 245,025, provincia o comarca 14,152, región o país 6,100, continente 2,997, mundo 1,522.

Cómo se asigna un país: por **nombre** actual (25+ idiomas, Natural Earth), por **nombre histórico**
(`catalogo/nombres_historicos.json`) o por **coordenadas** de la cobertura del mapa. Cada mapa guarda
la vía en el campo `via`; las asignaciones por coordenadas de mapas grandes pueden incluir países
vecinos. Los siglos salen del año de los metadatos de cada archivo y pueden tener errores puntuales.

Mapas de un país: `catalogo/biblioteca/paises/<ISO3>.jsonl.gz` o
`python scripts/buscar_lugar.py "<país>"`.

| País | ISO | Total | Antes del s. IX | IX | X | XI | XII | XIII | XIV | XV | XVI | XVII | XVIII | XIX | XX |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Afganistán | AFG | 463 |  |  |  |  |  |  |  |  | 21 | 6 | 12 | 194 | 110 |
| Albania | ALB | 322 | 1 |  |  |  |  | 2 | 2 | 7 | 23 | 26 | 22 | 84 | 61 |
| Alemania | DEU | 13,927 | 7 | 3 | 3 | 1 | 2 | 3 | 1 | 8 | 104 | 255 | 427 | 1,737 | 897 |
| Andorra | AND | 41 | 2 |  |  |  |  |  |  |  |  |  | 2 | 5 | 22 |
| Angola | AGO | 225 |  |  |  |  |  |  |  | 1 | 4 | 13 | 21 | 63 | 90 |
| Anguila | AIA | 8 |  |  |  |  |  |  |  |  |  |  | 6 | 1 |  |
| Antigua y Barbuda | ATG | 40 |  |  |  |  |  |  |  |  |  | 2 | 16 | 17 | 1 |
| Antártida | ATA | 96 |  |  |  |  |  |  |  |  |  | 8 | 11 | 10 | 53 |
| Arabia Saudita | SAU | 585 |  |  |  |  |  |  |  | 6 | 47 | 35 | 62 | 160 | 143 |
| Argelia | DZA | 573 | 2 |  |  |  |  | 1 | 1 | 3 | 23 | 27 | 38 | 198 | 113 |
| Argentina | ARG | 861 |  |  |  |  |  |  |  |  | 7 | 101 | 103 | 160 | 363 |
| Armenia | ARM | 404 |  | 1 |  | 1 |  |  | 1 | 2 | 20 | 12 | 27 | 181 | 93 |
| Aruba | ABW | 23 |  |  |  |  |  |  |  |  |  |  | 3 | 6 | 4 |
| Australia | AUS | 2,315 | 5 |  |  |  |  |  | 1 |  | 8 | 16 | 40 | 386 | 100 |
| Austria | AUT | 2,011 | 4 |  |  |  |  |  | 1 | 3 | 41 | 48 | 100 | 499 | 268 |
| Azerbaiyán | AZE | 138 |  |  |  |  |  |  |  | 1 | 8 | 7 | 10 | 46 | 36 |
| Bahamas | BHS | 177 |  |  |  |  |  | 1 |  |  |  | 5 | 61 | 61 | 30 |
| Bangladés | BGD | 57 |  |  |  |  |  |  |  | 1 | 4 | 5 | 4 | 7 | 8 |
| Barbados | BRB | 117 |  |  |  |  |  |  |  |  |  | 11 | 39 | 14 | 30 |
| Baréin | BHR | 82 |  |  |  |  |  |  |  | 2 | 6 | 6 | 11 | 19 | 27 |
| Belice | BLZ | 70 |  |  |  |  |  |  |  |  |  | 9 | 5 | 16 | 34 |
| Benín | BEN | 60 |  |  |  |  |  |  |  |  | 4 | 7 | 4 | 5 | 16 |
| Bermudas | BMU | 104 |  |  |  |  |  |  |  |  | 1 | 12 | 30 | 24 | 16 |
| Bielorrusia | BLR | 312 | 1 |  |  |  |  |  |  | 3 | 22 | 20 | 33 | 46 | 85 |
| Birmania | MMR | 232 | 1 |  |  |  |  |  |  | 1 | 11 | 9 | 22 | 62 | 69 |
| Bolivia | BOL | 241 |  |  |  |  |  |  |  |  | 5 | 15 | 11 | 71 | 80 |
| Bosnia y Herzegovina | BIH | 464 | 2 |  |  |  |  |  |  | 6 | 37 | 15 | 22 | 113 | 75 |
| Botsuana | BWA | 163 |  |  |  | 2 |  |  |  |  | 2 |  | 5 | 47 | 56 |
| Brasil | BRA | 2,055 | 3 |  |  |  |  |  |  | 3 | 23 | 221 | 248 | 504 | 439 |
| Brunéi | BRN | 30 |  |  |  |  |  |  |  |  | 1 |  | 1 | 11 | 7 |
| Bulgaria | BGR | 496 |  |  |  |  |  |  | 1 | 2 | 23 | 20 | 44 | 137 | 80 |
| Burkina Faso | BFA | 57 |  |  |  |  |  |  |  |  | 2 | 5 | 3 | 7 | 14 |
| Burundi | BDI | 44 | 1 |  |  |  |  |  |  |  |  |  |  | 3 | 34 |
| Bután | BTN | 122 | 1 |  |  |  |  |  |  |  |  |  | 5 | 36 | 55 |
| Bélgica | BEL | 5,077 | 1 |  | 1 |  |  |  | 1 | 3 | 56 | 146 | 396 | 433 | 282 |
| Cabo Verde | CPV | 119 |  |  |  |  |  |  |  |  | 4 | 21 | 48 | 26 | 3 |
| Camboya | KHM | 106 |  |  |  |  |  |  |  |  | 2 | 3 | 5 | 15 | 49 |
| Camerún | CMR | 113 |  |  |  |  |  |  |  |  | 2 | 6 | 8 | 10 | 47 |
| Canadá | CAN | 6,201 | 8 |  |  |  |  |  | 2 |  | 21 | 103 | 1,497 | 1,723 | 1,710 |
| Catar | QAT | 100 |  |  |  |  |  |  |  | 3 | 8 | 7 | 13 | 34 | 32 |
| Chad | TCD | 70 |  |  |  |  |  |  |  |  |  | 3 | 4 | 11 | 29 |
| Chile | CHL | 906 |  |  |  |  |  |  |  | 2 | 8 | 126 | 167 | 316 | 143 |
| China | CHN | 3,981 | 2 | 1 |  |  | 9 | 2 | 3 | 5 | 39 | 135 | 396 | 1,511 | 1,190 |
| Chipre | CYP | 225 | 1 |  |  |  |  |  |  | 2 | 17 | 16 | 16 | 22 | 95 |
| Ciudad del Vaticano | VAT | 76 |  |  |  |  |  |  |  |  | 1 | 24 | 5 | 10 | 15 |
| Colombia | COL | 583 |  |  |  |  |  |  |  |  | 10 | 55 | 101 | 127 | 146 |
| Comoras | COM | 20 |  |  |  |  |  |  |  |  |  |  | 2 | 9 | 7 |
| Corea del Norte | PRK | 136 |  |  |  |  |  |  |  |  | 1 | 9 | 12 | 13 | 54 |
| Corea del Sur | KOR | 830 | 1 |  |  |  |  |  |  |  | 5 | 15 | 65 | 138 | 220 |
| Costa Rica | CRI | 181 |  |  |  |  |  |  |  |  |  | 16 | 16 | 46 | 89 |
| Costa de Marfil | CIV | 94 |  |  |  |  |  |  |  |  | 3 | 5 | 13 | 13 | 28 |
| Croacia | HRV | 847 | 5 |  |  |  |  |  | 2 | 7 | 44 | 23 | 42 | 223 | 87 |
| Cuba | CUB | 1,200 | 17 | 8 | 5 |  |  |  |  | 1 | 7 | 107 | 230 | 280 | 325 |
| Curazao | CUW | 88 |  |  |  |  |  |  |  |  |  | 1 | 20 | 11 | 2 |
| Dinamarca | DNK | 1,342 | 5 |  |  |  |  |  | 2 |  | 11 | 66 | 68 | 387 | 81 |
| Dominica | DMA | 16 |  |  |  |  |  |  |  |  |  |  | 12 | 2 |  |
| ESB | ESB | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ecuador | ECU | 290 |  |  |  |  |  |  |  |  | 8 | 21 | 37 | 72 | 87 |
| Egipto | EGY | 2,269 | 8 |  |  | 2 | 1 | 1 | 1 | 4 | 48 | 40 | 123 | 853 | 785 |
| El Salvador | SLV | 184 |  |  |  |  |  | 1 |  |  | 1 | 10 | 5 | 93 | 61 |
| Emiratos Árabes Unidos | ARE | 55 |  |  |  |  |  |  |  | 3 | 7 | 6 | 12 | 13 | 7 |
| Eritrea | ERI | 417 |  |  |  |  |  |  |  |  | 1 | 6 | 7 | 104 | 271 |
| Eslovaquia | SVK | 539 |  |  |  |  |  |  |  | 2 | 17 | 15 | 23 | 103 | 125 |
| Eslovenia | SVN | 322 | 1 |  |  |  |  |  |  | 2 | 22 | 8 | 5 | 18 | 108 |
| España | ESP | 7,516 | 16 |  | 23 | 9 | 16 | 7 | 9 | 21 | 103 | 300 | 1,427 | 2,703 | 1,000 |
| Estados Federados de Micronesia | FSM | 68 |  |  |  |  |  |  |  |  |  | 1 | 4 | 23 | 32 |
| Estados Unidos | USA | 372,292 | 32 |  | 2 |  | 3 | 4 |  | 4 | 41 | 665 | 5,343 | 118,040 | 214,088 |
| Estonia | EST | 981 |  |  |  |  |  |  |  |  | 2 | 12 | 18 | 83 | 500 |
| Etiopía | ETH | 526 | 8 |  |  |  |  | 1 | 1 | 1 | 12 | 17 | 17 | 139 | 233 |
| Filipinas | PHL | 569 |  |  |  | 1 |  |  |  |  | 7 | 14 | 70 | 220 | 187 |
| Finlandia | FIN | 225 |  |  |  |  |  |  |  | 1 | 8 | 18 | 21 | 37 | 32 |
| Fiyi | FJI | 58 |  |  |  |  |  |  |  |  |  | 2 | 2 | 34 | 10 |
| Francia | FRA | 15,112 | 17 | 1 | 4 | 4 | 4 | 14 | 15 | 10 | 166 | 627 | 1,977 | 4,490 | 768 |
| GIB | GIB | 5 |  |  |  |  |  |  |  |  |  |  | 5 |  |  |
| Gabón | GAB | 78 |  |  |  |  |  |  |  |  | 2 | 8 | 10 | 14 | 16 |
| Gambia | GMB | 38 |  |  |  |  |  |  |  |  |  | 2 | 15 | 13 | 4 |
| Georgia | GEO | 254 |  |  |  |  |  |  |  | 1 | 11 | 5 | 53 | 62 | 43 |
| Ghana | GHA | 87 |  |  |  |  |  |  | 1 |  | 2 | 8 | 8 | 9 | 20 |
| Granada | GRD | 369 | 1 |  |  |  |  | 2 |  |  |  | 19 | 63 | 211 | 27 |
| Grecia | GRC | 1,753 | 18 |  |  |  |  | 1 | 2 | 3 | 88 | 133 | 115 | 611 | 242 |
| Groenlandia | GRL | 180 |  |  |  |  |  |  | 1 |  | 8 | 14 | 35 | 77 | 17 |
| Guam | GUM | 153 |  |  |  |  |  |  |  |  |  | 4 | 15 | 9 | 111 |
| Guatemala | GTM | 192 | 1 | 1 |  |  |  |  |  |  | 3 | 16 | 12 | 45 | 81 |
| Guernsey | GGY | 224 |  |  |  |  |  |  |  |  |  | 4 |  | 102 | 109 |
| Guinea | GIN | 114 |  |  |  |  |  |  |  |  | 1 | 11 | 36 | 13 | 13 |
| Guinea Ecuatorial | GNQ | 40 |  |  |  |  |  |  |  |  | 1 | 2 | 2 | 11 | 18 |
| Guinea-Bisáu | GNB | 10 |  |  |  |  |  |  |  |  | 1 |  | 3 | 2 | 2 |
| Guyana | GUY | 330 |  |  |  |  |  |  |  |  | 6 | 31 | 48 | 68 | 55 |
| Haití | HTI | 379 |  |  |  |  |  | 1 |  |  | 5 | 23 | 112 | 63 | 122 |
| Honduras | HND | 259 |  |  |  |  |  |  |  |  |  | 28 | 50 | 65 | 93 |
| Hong Kong | HKG | 48 |  |  |  |  |  |  |  |  |  |  |  | 22 | 13 |
| Hungría | HUN | 1,238 | 1 |  |  |  |  |  | 1 | 4 | 53 | 47 | 84 | 344 | 134 |
| India | IND | 2,289 | 2 |  |  |  |  |  | 6 | 5 | 70 | 92 | 383 | 789 | 240 |
| Indonesia | IDN | 1,886 | 3 |  |  |  |  |  | 1 | 1 | 22 | 251 | 319 | 182 | 225 |
| Irak | IRQ | 606 | 7 |  |  |  | 1 |  |  | 5 | 37 | 35 | 28 | 117 | 169 |
| Irlanda | IRL | 1,861 | 4 | 1 | 2 | 2 |  |  |  | 2 | 45 | 84 | 117 | 613 | 48 |
| Irán | IRN | 581 | 2 |  |  |  |  |  | 2 | 5 | 40 | 26 | 97 | 189 | 86 |
| Isla Norfolk | NFK | 1,341 |  |  |  |  |  |  |  |  |  | 2 | 36 | 1,080 | 206 |
| Isla Santa Elena | SHN | 117 |  |  |  |  |  |  |  |  | 1 | 8 | 7 | 85 | 5 |
| Isla de Man | IMN | 35 |  |  |  |  |  |  |  |  |  |  | 2 | 19 |  |
| Islandia | ISL | 180 | 1 |  |  |  |  |  |  |  | 10 | 14 | 17 | 52 | 25 |
| Islas Caimán | CYM | 9 |  |  |  |  |  |  |  |  |  |  | 1 | 1 | 7 |
| Islas Feroe | FRO | 81 | 1 |  |  |  |  |  | 1 |  |  | 9 | 12 | 25 | 12 |
| Islas Georgias del Sur y Sandwich del Sur | SGS | 2 |  |  |  |  |  |  |  |  |  |  |  |  | 1 |
| Islas Malvinas | FLK | 43 |  |  |  |  |  |  |  |  |  | 11 | 11 | 6 | 4 |
| Islas Marianas del Norte | MNP | 42 |  |  |  |  |  |  |  |  | 2 |  | 7 | 2 | 24 |
| Islas Marshall | MHL | 61 | 2 |  |  |  |  |  |  |  |  |  |  | 19 | 34 |
| Islas Pitcairn | PCN | 10 |  |  |  |  |  |  |  |  |  |  | 1 | 1 | 8 |
| Islas Salomón | SLB | 39 |  |  |  |  |  |  |  |  | 1 | 2 | 2 | 6 | 13 |
| Islas Turcas y Caicos | TCA | 6 |  |  |  |  |  |  |  |  |  |  | 2 | 2 | 2 |
| Islas Vírgenes Británicas | VGB | 9 |  |  |  |  |  |  |  |  |  |  | 3 | 1 | 5 |
| Islas Vírgenes de los Estados Unidos | VIR | 102 |  |  |  |  |  |  |  |  |  | 1 | 49 | 3 | 44 |
| Israel | ISR | 1,437 |  |  | 1 | 1 | 1 | 2 | 3 | 17 | 53 | 63 | 169 | 469 | 158 |
| Italia | ITA | 6,184 | 28 | 3 |  | 3 | 5 | 5 | 2 | 50 | 248 | 399 | 433 | 1,434 | 546 |
| Jamaica | JAM | 889 | 1 |  |  |  |  |  |  | 1 | 1 | 19 | 203 | 552 | 55 |
| Japón | JPN | 1,340 | 3 |  |  |  |  |  |  | 2 | 9 | 69 | 151 | 330 | 252 |
| Jersey | JEY | 13 |  |  |  |  |  |  |  |  |  | 4 |  | 8 |  |
| Jordania | JOR | 380 |  |  |  |  |  |  |  | 1 | 37 | 18 | 22 | 148 | 27 |
| Kazajistán | KAZ | 150 |  |  |  |  |  |  |  | 1 | 15 | 16 | 10 | 35 | 31 |
| Kenia | KEN | 230 |  |  |  |  |  |  |  |  | 2 | 4 | 2 | 26 | 154 |
| Kirguistán | KGZ | 54 |  |  |  |  |  |  |  |  | 7 | 2 |  | 23 | 11 |
| Kiribati | KIR | 25 |  |  |  |  |  |  |  |  |  |  |  | 15 | 9 |
| Kosovo | KOS | 60 |  |  |  |  |  |  |  |  | 1 | 2 | 2 | 3 | 33 |
| Kuwait | KWT | 78 |  |  |  |  |  |  |  | 3 | 7 | 5 | 12 | 15 | 21 |
| Laos | LAO | 68 |  |  |  |  |  |  |  | 1 | 3 |  |  | 9 | 19 |
| Lesoto | LSO | 91 |  |  |  | 1 |  |  |  |  |  |  | 1 | 12 | 72 |
| Letonia | LVA | 259 | 1 |  |  |  |  |  |  | 2 | 14 | 23 | 24 | 26 | 93 |
| Liberia | LBR | 153 |  |  |  |  |  |  |  |  | 2 | 3 | 5 | 72 | 38 |
| Libia | LBY | 323 | 4 |  |  |  |  |  |  | 6 | 25 | 19 | 16 | 45 | 122 |
| Liechtenstein | LIE | 21 |  |  |  |  |  |  |  | 1 |  | 1 |  | 6 |  |
| Lituania | LTU | 300 |  |  |  |  |  |  |  | 3 | 13 | 15 | 46 | 20 | 50 |
| Luxemburgo | LUX | 382 |  |  |  |  |  |  |  | 1 | 13 | 35 | 63 | 61 | 33 |
| Líbano | LBN | 700 | 2 |  |  | 1 | 1 |  |  | 2 | 17 | 6 | 15 | 454 | 123 |
| Macao | MAC | 90 |  |  |  |  |  |  |  |  |  | 5 | 17 | 19 | 34 |
| Macedonia del Norte | MKD | 119 |  |  |  |  |  |  |  | 2 | 13 | 11 | 5 | 19 | 26 |
| Madagascar | MDG | 242 |  |  |  |  |  |  |  |  | 9 | 19 | 50 | 60 | 42 |
| Malasia | MYS | 246 | 4 |  |  |  |  |  |  |  | 8 | 6 | 10 | 30 | 45 |
| Malaui | MWI | 37 | 1 |  |  |  |  |  |  |  | 1 |  | 2 | 14 | 14 |
| Maldivas | MDV | 68 |  |  |  |  |  |  |  |  | 1 | 8 | 24 | 9 | 14 |
| Malta | MLT | 202 | 1 |  |  |  |  |  | 1 |  | 16 | 17 | 65 | 44 | 11 |
| Malí | MLI | 121 |  |  |  |  |  |  | 3 | 2 | 4 | 5 | 8 | 26 | 20 |
| Marruecos | MAR | 508 | 1 |  |  |  |  | 1 |  | 1 | 14 | 41 | 66 | 120 | 132 |
| Mauricio | MUS | 170 | 2 |  |  | 1 |  |  |  |  | 5 | 16 | 29 | 45 | 14 |
| Mauritania | MRT | 87 |  |  |  |  |  |  |  |  | 10 | 3 | 13 | 15 | 15 |
| Moldavia | MDA | 125 |  |  |  |  |  |  |  | 1 | 5 | 9 | 20 | 25 | 13 |
| Mongolia | MNG | 135 |  |  |  |  |  |  |  |  | 3 | 11 | 7 | 34 | 61 |
| Montenegro | MNE | 139 |  |  |  |  |  |  |  |  | 8 | 9 | 5 | 27 | 24 |
| Montserrat | MSR | 130 |  |  |  |  |  |  |  |  |  |  |  | 105 | 21 |
| Mozambique | MOZ | 227 | 1 |  |  |  |  |  |  |  | 8 | 13 | 28 | 62 | 53 |
| México | MEX | 3,546 | 1 |  |  |  |  | 1 | 1 | 3 | 59 | 116 | 350 | 1,045 | 1,277 |
| Mónaco | MCO | 43 | 1 |  |  |  |  |  |  |  |  | 6 | 9 | 14 | 7 |
| Namibia | NAM | 137 |  |  |  |  |  |  |  |  | 3 |  | 8 | 41 | 29 |
| Nauru | NRU | 17 |  |  |  |  |  |  |  |  |  |  |  | 3 | 11 |
| Nepal | NPL | 85 |  |  |  |  |  |  |  | 1 | 3 | 2 | 1 | 20 | 30 |
| Nicaragua | NIC | 308 |  |  |  |  |  |  |  |  | 2 | 25 | 23 | 158 | 69 |
| Nigeria | NGA | 134 |  |  |  |  |  |  |  |  | 3 | 10 | 8 | 16 | 56 |
| Niue | NIU | 7 |  |  |  |  |  |  |  |  |  |  |  | 1 | 5 |
| Noruega | NOR | 1,160 |  |  |  |  |  |  |  | 2 | 20 | 54 | 96 | 353 | 61 |
| Nueva Caledonia | NCL | 13 |  |  |  |  |  |  |  |  |  |  | 1 | 3 | 6 |
| Nueva Zelanda | NZL | 415 | 2 |  |  | 1 |  |  |  |  | 1 |  | 18 | 229 | 80 |
| Níger | NER | 70 |  |  |  |  |  |  |  |  | 4 | 5 | 3 | 5 | 26 |
| Omán | OMN | 90 |  |  |  |  |  |  |  | 4 | 12 | 8 | 20 | 17 | 10 |
| PSX | PSX | 298 |  |  |  |  |  |  |  | 1 | 17 | 8 | 7 | 106 | 2 |
| Pakistán | PAK | 418 |  |  |  |  |  |  |  |  | 28 | 7 | 11 | 107 | 130 |
| Palaos | PLW | 53 |  |  |  |  |  |  |  |  |  | 1 | 10 | 12 | 20 |
| Palestina | PSE | 1,206 | 4 |  |  |  | 1 | 1 | 1 | 10 | 44 | 37 | 71 | 518 | 194 |
| Panamá | PAN | 344 |  |  |  |  |  |  |  |  | 2 | 42 | 44 | 79 | 110 |
| Papúa Nueva Guinea | PNG | 152 |  |  |  |  |  |  |  |  | 2 | 4 | 4 | 38 | 77 |
| Paraguay | PRY | 288 |  |  |  |  |  |  |  |  | 1 | 14 | 45 | 80 | 56 |
| Países Bajos | NLD | 18,740 | 2 |  | 5 |  |  |  | 1 | 1 | 108 | 469 | 554 | 455 | 1,031 |
| Perú | PER | 918 | 1 |  |  |  |  |  |  |  | 20 | 52 | 78 | 357 | 228 |
| Polinesia Francesa | PYF | 70 |  |  |  |  |  |  |  |  |  | 1 | 35 | 26 | 5 |
| Polonia | POL | 3,185 | 1 |  | 2 | 1 | 1 |  | 1 | 8 | 45 | 70 | 223 | 679 | 524 |
| Portugal | PRT | 2,664 | 3 |  |  |  |  |  |  | 3 | 57 | 137 | 489 | 1,028 | 221 |
| Puerto Rico | PRI | 1,069 |  |  |  |  |  |  |  | 1 | 1 | 18 | 70 | 40 | 905 |
| Reino Unido | GBR | 10,397 | 5 | 1 | 3 | 3 | 3 | 12 |  | 7 | 60 | 468 | 1,333 | 2,651 | 519 |
| República Centroafricana | CAF | 160 |  |  |  |  |  |  |  |  |  | 2 | 3 | 10 | 114 |
| República Checa | CZE | 1,205 | 1 |  |  |  |  |  |  | 1 | 16 | 31 | 64 | 218 | 229 |
| República Democrática del Congo | COD | 225 |  |  |  |  |  |  |  |  | 3 | 6 | 9 | 31 | 128 |
| República Dominicana | DOM | 243 |  |  |  |  |  |  |  |  | 4 | 24 | 66 | 46 | 58 |
| República Turca del Norte de Chipre | CYN | 15 |  |  |  |  |  |  |  |  | 2 | 5 |  |  |  |
| República de China | TWN | 194 |  |  |  |  |  |  |  |  | 2 | 17 | 9 | 49 | 80 |
| República del Congo | COG | 217 | 2 |  |  |  |  |  |  | 1 | 3 | 9 | 29 | 66 | 59 |
| Ruanda | RWA | 42 | 1 |  |  |  |  |  |  |  |  |  |  | 4 | 31 |
| Rumania | ROU | 1,106 |  |  |  |  |  |  |  | 3 | 38 | 26 | 52 | 185 | 199 |
| Rusia | RUS | 4,705 | 4 |  |  |  |  |  | 1 | 6 | 71 | 129 | 276 | 1,733 | 1,245 |
| SAH | SAH | 4 |  |  |  |  |  |  |  |  |  | 2 |  | 1 |  |
| SDS | SDS | 82 |  |  |  |  |  |  |  |  |  | 1 |  | 10 | 19 |
| Sahara Occidental | ESH | 35 |  |  |  |  |  |  | 1 |  |  | 2 | 1 | 16 | 13 |
| Samoa | WSM | 67 | 1 |  |  |  |  |  |  |  |  |  | 6 | 31 | 25 |
| Samoa Estadounidense | ASM | 25 |  |  |  |  |  |  |  |  |  |  |  | 13 | 7 |
| San Bartolomé | BLM | 6 |  |  |  |  |  |  |  |  |  |  | 3 | 2 |  |
| San Cristóbal y Nieves | KNA | 34 |  |  |  |  |  |  |  |  |  | 5 | 17 | 2 | 3 |
| San Marino | SMR | 8 |  |  | 1 |  |  |  |  |  |  | 1 | 1 | 1 | 2 |
| San Martín | MAF | 57 |  |  |  |  |  |  |  |  |  |  | 7 | 32 | 7 |
| San Martín | SXM | 27 |  |  |  |  |  |  |  | 1 |  |  | 6 | 14 | 2 |
| San Pedro y Miquelón | SPM | 8 |  |  |  |  |  |  |  |  |  |  | 1 | 5 | 1 |
| San Vicente y las Granadinas | VCT | 23 | 1 |  |  |  |  |  |  |  |  |  | 6 | 11 | 4 |
| Santa Lucía | LCA | 31 |  |  |  |  |  |  |  |  |  | 1 | 19 | 4 | 5 |
| Santo Tomé y Príncipe | STP | 28 |  |  |  | 1 |  |  |  |  |  | 10 | 10 | 4 | 1 |
| Senegal | SEN | 122 |  |  |  |  |  |  |  |  | 2 | 4 | 42 | 31 | 11 |
| Serbia | SRB | 519 |  |  |  |  |  |  |  | 4 | 26 | 15 | 27 | 142 | 72 |
| Seychelles | SYC | 3 |  |  |  |  |  |  |  |  |  |  |  | 3 |  |
| Sierra Leona | SLE | 155 |  |  |  |  |  |  |  | 1 | 2 | 7 | 18 | 17 | 98 |
| Singapur | SGP | 64 |  |  |  |  |  |  |  | 1 | 2 | 1 | 1 | 23 | 8 |
| Siria | SYR | 899 | 1 |  |  |  | 1 |  |  | 4 | 41 | 31 | 64 | 470 | 95 |
| Somalia | SOM | 189 |  |  |  |  |  |  |  | 1 | 11 | 7 | 6 | 19 | 101 |
| Somalilandia | SOL | 222 |  |  |  |  |  |  |  |  | 2 | 4 |  | 32 | 168 |
| Sri Lanka | LKA | 259 |  |  |  |  |  |  | 2 | 2 | 14 | 39 | 29 | 56 | 23 |
| Suazilandia | SWZ | 45 |  |  |  | 1 |  |  |  |  |  |  |  | 3 | 38 |
| Sudáfrica | ZAF | 699 | 5 |  |  |  |  | 1 |  |  | 5 | 27 | 45 | 261 | 170 |
| Sudán | SDN | 486 | 1 | 3 |  |  |  |  |  | 2 | 9 | 15 | 14 | 81 | 250 |
| Sudán del Sur | SSD | 202 |  |  |  |  |  |  |  |  | 1 | 4 | 2 | 17 | 89 |
| Suecia | SWE | 1,381 | 1 |  |  |  |  |  |  | 3 | 13 | 55 | 68 | 303 | 53 |
| Suiza | CHE | 2,318 | 3 |  |  |  |  |  |  | 4 | 56 | 61 | 135 | 482 | 162 |
| Surinam | SUR | 480 |  |  |  |  |  |  |  |  | 6 | 24 | 41 | 55 | 62 |
| Tailandia | THA | 227 | 1 |  |  |  |  |  | 1 | 1 | 9 | 15 | 22 | 64 | 57 |
| Tanzania | TZA | 214 | 1 |  |  |  |  |  |  |  | 4 | 2 | 3 | 51 | 85 |
| Tayikistán | TJK | 61 |  |  |  |  |  |  |  |  | 6 |  |  | 29 | 15 |
| Territorio Británico del Océano Índico | IOT | 1 |  |  |  |  |  |  |  |  |  |  |  |  | 1 |
| Territorios Australianos del Océano Índico | IOA | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Tierras Australes y Antárticas Francesas | ATF | 4 |  |  |  |  |  |  |  |  |  |  |  | 1 |  |
| Timor Oriental | TLS | 15 |  |  |  |  |  |  |  |  |  |  |  |  | 2 |
| Togo | TGO | 48 |  |  |  |  |  |  |  |  | 1 | 1 | 2 | 7 | 15 |
| Tonga | TON | 44 |  |  |  |  |  |  |  |  |  | 4 | 7 | 13 | 10 |
| Trinidad y Tobago | TTO | 102 |  |  |  |  |  |  |  |  | 1 | 19 | 35 | 12 | 32 |
| Turkmenistán | TKM | 124 |  |  |  |  |  |  |  |  | 14 | 5 | 3 | 49 | 20 |
| Turquía | TUR | 1,942 | 12 |  |  | 1 |  | 1 | 5 | 7 | 73 | 78 | 175 | 717 | 299 |
| Tuvalu | TUV | 14 |  |  |  |  |  |  |  |  |  |  |  | 8 | 4 |
| Túnez | TUN | 525 | 3 |  |  |  |  | 1 | 1 | 2 | 31 | 9 | 18 | 187 | 163 |
| UMI | UMI | 2 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |
| USG | USG | 3 |  |  |  |  |  |  |  |  |  |  | 1 | 1 |  |
| Ucrania | UKR | 753 | 1 |  |  |  |  |  | 4 | 4 | 30 | 58 | 59 | 96 | 97 |
| Uganda | UGA | 248 |  |  |  |  |  |  |  |  | 1 | 3 | 3 | 15 | 192 |
| Uruguay | URY | 313 |  |  |  |  |  |  |  |  | 3 | 22 | 47 | 105 | 69 |
| Uzbekistán | UZB | 121 |  |  |  |  |  |  |  |  | 7 | 4 | 4 | 56 | 31 |
| Vanuatu | VUT | 15 |  |  |  |  |  |  |  |  |  |  |  | 2 | 13 |
| Venezuela | VEN | 498 |  |  |  |  |  |  |  | 1 | 11 | 83 | 115 | 104 | 75 |
| Vietnam | VNM | 331 |  |  |  |  |  |  |  | 2 | 8 | 5 | 17 | 44 | 82 |
| Yemen | YEM | 417 |  |  |  |  |  |  |  | 5 | 17 | 14 | 16 | 39 | 276 |
| Yibuti | DJI | 54 |  |  |  |  |  |  |  |  | 2 | 2 | 3 | 27 | 18 |
| Zambia | ZMB | 105 |  |  |  |  |  |  |  |  | 1 | 3 | 4 | 20 | 45 |
| Zimbabue | ZWE | 110 |  |  |  |  |  |  |  |  | 2 | 1 | 6 | 26 | 43 |
| Åland | ALA | 4 |  |  |  |  |  |  |  |  |  |  |  | 1 |  |
