# Biblioteca de Cartographer

Documento generado por `scripts/comprender.py`. No editar a mano.

- Mapas analizados: **883,524** · con país asignado: **532,339** · sin país: 351,185
  (sobre todo mapamundis, cartas oceánicas o registros sin datos de lugar).
- Países con mapas: **244**.
- Tipos: general 536,146, topográfico 208,980, histórico/temático 79,937, plano urbano 26,229, militar 10,944, mapamundi 7,318, ferroviario/viario 6,588, carta náutica 5,834, ptolemaico 780, portulano 768.
- Escalas: desconocida 613,728, local o ciudad 245,025, provincia o comarca 14,152, región o país 6,100, continente 2,997, mundo 1,522.

Cómo se asigna un país: por **nombre** actual (25+ idiomas, Natural Earth), por **nombre histórico**
(`catalogo/nombres_historicos.json`) o por **coordenadas** de la cobertura del mapa. Cada mapa guarda
la vía en el campo `via`; las asignaciones por coordenadas de mapas grandes pueden incluir países
vecinos. Los siglos salen del año de los metadatos de cada archivo y pueden tener errores puntuales.

Mapas de un país: `catalogo/biblioteca/paises/<ISO3>.jsonl.gz` o
`python scripts/buscar_lugar.py "<país>"`.

| País | ISO | Total | Antes del s. IX | IX | X | XI | XII | XIII | XIV | XV | XVI | XVII | XVIII | XIX | XX |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Afganistán | AFG | 524 | 1 |  |  |  |  |  | 1 |  | 21 | 7 | 12 | 212 | 111 |
| Albania | ALB | 350 | 1 |  |  |  |  | 2 | 2 | 7 | 26 | 31 | 28 | 87 | 61 |
| Alemania | DEU | 15,380 | 9 | 4 | 4 | 2 | 3 | 3 | 2 | 17 | 116 | 290 | 500 | 2,014 | 938 |
| Andorra | AND | 47 | 2 |  |  |  |  |  |  |  |  |  | 2 | 5 | 22 |
| Angola | AGO | 250 |  |  |  |  |  |  |  | 1 | 4 | 13 | 27 | 65 | 91 |
| Anguila | AIA | 10 |  |  |  |  |  |  |  |  |  |  | 6 | 1 | 1 |
| Antigua y Barbuda | ATG | 40 |  |  |  |  |  |  |  |  |  | 2 | 16 | 17 | 1 |
| Antártida | ATA | 110 |  |  |  |  |  |  |  |  |  | 10 | 18 | 10 | 54 |
| Arabia Saudita | SAU | 695 | 1 |  |  |  |  |  |  | 6 | 50 | 41 | 72 | 197 | 147 |
| Argelia | DZA | 750 | 2 |  |  |  |  | 1 | 1 | 3 | 24 | 32 | 39 | 315 | 124 |
| Argentina | ARG | 970 |  |  |  |  |  |  |  |  | 8 | 102 | 110 | 184 | 367 |
| Armenia | ARM | 453 | 2 | 1 |  | 1 |  |  | 1 | 2 | 22 | 18 | 34 | 184 | 103 |
| Aruba | ABW | 23 |  |  |  |  |  |  |  |  |  |  | 3 | 6 | 4 |
| Australia | AUS | 2,505 | 5 |  |  |  |  |  | 1 |  | 8 | 19 | 47 | 420 | 103 |
| Austria | AUT | 2,472 | 4 |  |  |  |  |  | 1 | 4 | 42 | 60 | 119 | 578 | 273 |
| Azerbaiyán | AZE | 140 |  |  |  |  |  |  |  | 1 | 8 | 7 | 10 | 46 | 37 |
| Bahamas | BHS | 203 |  |  |  |  |  | 1 |  |  |  | 7 | 67 | 62 | 33 |
| Bangladés | BGD | 57 |  |  |  |  |  |  |  | 1 | 4 | 5 | 4 | 7 | 8 |
| Barbados | BRB | 129 |  |  |  |  |  |  |  |  |  | 12 | 43 | 15 | 30 |
| Baréin | BHR | 82 |  |  |  |  |  |  |  | 2 | 6 | 6 | 11 | 19 | 27 |
| Belice | BLZ | 73 |  |  |  |  |  |  |  |  |  | 9 | 5 | 17 | 34 |
| Benín | BEN | 70 |  |  |  |  |  |  |  |  | 4 | 7 | 4 | 11 | 16 |
| Bermudas | BMU | 124 |  |  |  |  |  |  |  |  | 1 | 12 | 33 | 28 | 16 |
| Bielorrusia | BLR | 312 | 1 |  |  |  |  |  |  | 3 | 22 | 20 | 33 | 46 | 85 |
| Birmania | MMR | 242 | 1 |  |  |  |  |  |  | 1 | 11 | 9 | 25 | 64 | 70 |
| Bolivia | BOL | 319 |  |  |  |  |  |  |  |  | 5 | 16 | 11 | 92 | 82 |
| Bosnia y Herzegovina | BIH | 464 | 2 |  |  |  |  |  |  | 6 | 37 | 15 | 22 | 113 | 75 |
| Botsuana | BWA | 163 |  |  |  | 2 |  |  |  |  | 2 |  | 5 | 47 | 56 |
| Brasil | BRA | 2,343 | 3 |  |  |  |  |  |  | 3 | 26 | 232 | 265 | 564 | 453 |
| Brunéi | BRN | 30 |  |  |  |  |  |  |  |  | 1 |  | 1 | 11 | 7 |
| Bulgaria | BGR | 547 |  |  |  |  |  |  | 1 | 2 | 26 | 20 | 46 | 141 | 85 |
| Burkina Faso | BFA | 57 |  |  |  |  |  |  |  |  | 2 | 5 | 3 | 7 | 14 |
| Burundi | BDI | 44 | 1 |  |  |  |  |  |  |  |  |  |  | 3 | 34 |
| Bután | BTN | 123 | 1 |  |  |  |  |  |  |  |  |  | 5 | 36 | 55 |
| Bélgica | BEL | 5,742 | 2 |  | 1 |  |  |  | 1 | 3 | 61 | 214 | 444 | 654 | 301 |
| Cabo Verde | CPV | 130 |  |  |  |  |  |  |  |  | 4 | 21 | 50 | 31 | 3 |
| Camboya | KHM | 133 |  |  |  |  |  |  |  |  | 3 | 14 | 6 | 21 | 56 |
| Camerún | CMR | 128 |  |  |  |  |  |  |  |  | 2 | 6 | 8 | 13 | 51 |
| Canadá | CAN | 6,878 | 8 |  |  |  |  |  | 2 |  | 22 | 118 | 1,591 | 1,810 | 1,823 |
| Catar | QAT | 100 |  |  |  |  |  |  |  | 3 | 8 | 7 | 13 | 34 | 32 |
| Chad | TCD | 80 |  |  |  |  |  |  |  |  |  | 3 | 4 | 18 | 30 |
| Chile | CHL | 1,073 |  |  |  |  |  |  |  | 2 | 8 | 128 | 183 | 344 | 146 |
| China | CHN | 4,575 | 2 | 1 |  |  | 9 | 2 | 4 | 5 | 45 | 148 | 452 | 1,679 | 1,271 |
| Chipre | CYP | 271 | 1 |  |  |  |  | 1 |  | 2 | 19 | 18 | 20 | 24 | 95 |
| Ciudad del Vaticano | VAT | 79 |  |  |  |  |  |  |  |  | 1 | 24 | 5 | 10 | 15 |
| Colombia | COL | 692 |  |  |  |  |  |  |  |  | 10 | 55 | 109 | 149 | 149 |
| Comoras | COM | 25 |  |  |  |  |  |  |  |  |  | 1 | 4 | 10 | 8 |
| Corea del Norte | PRK | 136 |  |  |  |  |  |  |  |  | 1 | 9 | 12 | 13 | 54 |
| Corea del Sur | KOR | 850 | 1 |  |  |  |  |  |  |  | 6 | 15 | 69 | 147 | 222 |
| Costa Rica | CRI | 190 |  |  |  |  |  |  |  |  |  | 16 | 17 | 49 | 89 |
| Costa de Marfil | CIV | 106 |  |  |  |  |  |  |  |  | 3 | 5 | 13 | 14 | 39 |
| Croacia | HRV | 939 | 5 |  |  |  |  |  | 2 | 7 | 48 | 36 | 56 | 227 | 87 |
| Cuba | CUB | 1,345 | 17 | 8 | 5 |  |  |  |  | 1 | 7 | 108 | 240 | 289 | 326 |
| Curazao | CUW | 92 |  |  |  |  |  |  |  |  |  | 1 | 20 | 11 | 2 |
| Dinamarca | DNK | 1,511 | 6 |  |  |  |  |  | 3 |  | 11 | 67 | 76 | 417 | 81 |
| Dominica | DMA | 28 |  |  |  |  |  |  |  |  |  | 3 | 17 | 2 |  |
| ESB | ESB | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ecuador | ECU | 388 |  |  |  |  |  |  |  |  | 8 | 22 | 64 | 96 | 89 |
| Egipto | EGY | 2,549 | 8 |  |  | 2 | 1 | 3 | 2 | 5 | 59 | 45 | 162 | 906 | 793 |
| El Salvador | SLV | 192 |  |  |  |  |  | 1 |  |  | 1 | 10 | 5 | 93 | 61 |
| Emiratos Árabes Unidos | ARE | 55 |  |  |  |  |  |  |  | 3 | 7 | 6 | 12 | 13 | 7 |
| Eritrea | ERI | 424 |  |  |  |  |  |  |  |  | 1 | 7 | 7 | 107 | 274 |
| Eslovaquia | SVK | 539 |  |  |  |  |  |  |  | 2 | 17 | 15 | 23 | 103 | 125 |
| Eslovenia | SVN | 325 | 1 |  |  |  |  |  |  | 2 | 22 | 9 | 5 | 18 | 108 |
| España | ESP | 8,493 | 19 |  | 23 | 10 | 16 | 9 | 10 | 22 | 106 | 338 | 1,546 | 2,899 | 1,004 |
| Estados Federados de Micronesia | FSM | 69 |  |  |  |  |  |  |  |  |  | 1 | 4 | 23 | 32 |
| Estados Unidos | USA | 378,521 | 53 |  | 2 |  | 7 | 6 | 1 | 5 | 45 | 682 | 5,464 | 119,967 | 214,139 |
| Estonia | EST | 982 |  |  |  |  |  |  |  |  | 2 | 12 | 18 | 83 | 500 |
| Etiopía | ETH | 581 | 8 |  |  |  |  | 1 | 1 | 1 | 16 | 22 | 26 | 154 | 235 |
| Filipinas | PHL | 676 |  |  |  | 2 |  |  |  |  | 9 | 21 | 95 | 222 | 191 |
| Finlandia | FIN | 267 |  |  |  |  |  |  |  | 1 | 8 | 19 | 28 | 47 | 32 |
| Fiyi | FJI | 77 |  |  |  |  |  |  |  |  |  | 2 | 4 | 43 | 10 |
| Francia | FRA | 19,804 | 26 | 2 | 7 | 4 | 9 | 20 | 25 | 16 | 206 | 957 | 2,667 | 5,643 | 930 |
| GIB | GIB | 5 |  |  |  |  |  |  |  |  |  |  | 5 |  |  |
| Gabón | GAB | 86 |  |  |  |  |  |  |  |  | 2 | 8 | 10 | 18 | 16 |
| Gambia | GMB | 66 |  |  |  |  |  |  |  |  |  | 5 | 29 | 22 | 4 |
| Georgia | GEO | 288 |  |  |  |  |  |  |  | 1 | 12 | 7 | 64 | 65 | 44 |
| Ghana | GHA | 87 |  |  |  |  |  |  | 1 |  | 2 | 8 | 8 | 9 | 20 |
| Granada | GRD | 451 | 1 |  |  |  |  | 3 |  |  | 2 | 22 | 72 | 224 | 30 |
| Grecia | GRC | 2,321 | 19 | 1 | 1 |  |  | 1 | 3 | 5 | 102 | 156 | 165 | 748 | 247 |
| Groenlandia | GRL | 211 | 1 |  |  |  |  |  | 1 |  | 8 | 14 | 41 | 85 | 18 |
| Guam | GUM | 153 |  |  |  |  |  |  |  |  |  | 4 | 15 | 9 | 111 |
| Guatemala | GTM | 245 | 1 | 1 |  |  |  |  |  |  | 3 | 17 | 12 | 57 | 82 |
| Guernsey | GGY | 242 |  |  |  |  |  |  |  |  |  | 4 | 5 | 103 | 110 |
| Guinea | GIN | 164 |  |  |  |  |  |  |  |  | 1 | 11 | 40 | 13 | 16 |
| Guinea Ecuatorial | GNQ | 40 |  |  |  |  |  |  |  |  | 1 | 2 | 2 | 11 | 18 |
| Guinea-Bisáu | GNB | 10 |  |  |  |  |  |  |  |  | 1 |  | 3 | 2 | 2 |
| Guyana | GUY | 392 |  |  |  |  |  |  |  |  | 6 | 32 | 61 | 81 | 57 |
| Haití | HTI | 411 |  |  |  |  |  | 1 |  |  | 5 | 24 | 116 | 64 | 122 |
| Honduras | HND | 278 |  |  |  |  |  |  |  |  |  | 28 | 52 | 66 | 94 |
| Hong Kong | HKG | 61 |  |  |  |  |  |  |  |  |  |  |  | 26 | 22 |
| Hungría | HUN | 1,564 | 1 |  |  |  |  |  | 2 | 4 | 56 | 61 | 112 | 383 | 139 |
| India | IND | 3,002 | 3 |  |  | 7 |  | 8 | 7 | 5 | 80 | 124 | 440 | 912 | 251 |
| Indonesia | IDN | 2,169 | 3 |  |  |  |  |  | 1 | 1 | 25 | 268 | 369 | 187 | 236 |
| Irak | IRQ | 636 | 7 |  |  |  | 1 |  |  | 6 | 46 | 36 | 31 | 119 | 173 |
| Irlanda | IRL | 2,402 | 5 | 1 | 2 | 2 |  |  | 1 | 2 | 79 | 104 | 143 | 730 | 50 |
| Irán | IRN | 994 | 3 |  |  |  |  |  | 3 | 5 | 44 | 38 | 119 | 247 | 89 |
| Isla Norfolk | NFK | 1,359 |  |  |  |  |  |  |  |  |  | 2 | 38 | 1,082 | 206 |
| Isla Santa Elena | SHN | 131 |  |  |  |  |  |  |  |  | 1 | 10 | 8 | 86 | 5 |
| Isla de Man | IMN | 46 |  |  |  |  |  |  |  |  |  |  | 2 | 20 |  |
| Islandia | ISL | 258 | 1 |  |  |  |  |  |  |  | 13 | 18 | 27 | 64 | 27 |
| Islas Caimán | CYM | 9 |  |  |  |  |  |  |  |  |  |  | 1 | 1 | 7 |
| Islas Feroe | FRO | 90 | 1 |  |  |  |  |  | 1 |  |  | 9 | 12 | 30 | 12 |
| Islas Georgias del Sur y Sandwich del Sur | SGS | 2 |  |  |  |  |  |  |  |  |  |  |  |  | 1 |
| Islas Malvinas | FLK | 53 |  |  |  |  |  |  |  |  |  | 11 | 12 | 6 | 4 |
| Islas Marianas del Norte | MNP | 42 |  |  |  |  |  |  |  |  | 2 |  | 7 | 2 | 24 |
| Islas Marshall | MHL | 65 | 2 |  |  |  |  |  |  |  |  |  |  | 21 | 34 |
| Islas Pitcairn | PCN | 11 |  |  |  |  |  |  |  |  |  |  | 1 | 1 | 8 |
| Islas Salomón | SLB | 41 |  |  |  |  |  |  |  |  | 1 | 2 | 2 | 6 | 13 |
| Islas Turcas y Caicos | TCA | 6 |  |  |  |  |  |  |  |  |  |  | 2 | 2 | 2 |
| Islas Vírgenes Británicas | VGB | 9 |  |  |  |  |  |  |  |  |  |  | 3 | 1 | 5 |
| Islas Vírgenes de los Estados Unidos | VIR | 102 |  |  |  |  |  |  |  |  |  | 1 | 49 | 3 | 44 |
| Israel | ISR | 1,595 |  |  | 2 | 2 | 2 | 2 | 4 | 20 | 64 | 75 | 181 | 481 | 162 |
| Italia | ITA | 8,699 | 34 | 5 |  | 4 | 6 | 8 | 3 | 59 | 267 | 454 | 672 | 1,828 | 564 |
| Jamaica | JAM | 958 | 1 |  |  |  |  |  |  | 1 | 1 | 21 | 216 | 558 | 55 |
| Japón | JPN | 1,633 | 3 |  |  |  |  |  | 1 | 2 | 10 | 143 | 184 | 366 | 260 |
| Jersey | JEY | 13 |  |  |  |  |  |  |  |  |  | 4 |  | 8 |  |
| Jordania | JOR | 380 |  |  |  |  |  |  |  | 1 | 37 | 18 | 22 | 148 | 27 |
| Kazajistán | KAZ | 152 |  |  |  |  |  |  |  | 1 | 15 | 17 | 10 | 35 | 31 |
| Kenia | KEN | 231 |  |  |  |  |  |  |  |  | 2 | 4 | 2 | 26 | 155 |
| Kirguistán | KGZ | 54 |  |  |  |  |  |  |  |  | 7 | 2 |  | 23 | 11 |
| Kiribati | KIR | 25 |  |  |  |  |  |  |  |  |  |  |  | 15 | 9 |
| Kosovo | KOS | 60 |  |  |  |  |  |  |  |  | 1 | 2 | 2 | 3 | 33 |
| Kuwait | KWT | 78 |  |  |  |  |  |  |  | 3 | 7 | 5 | 12 | 15 | 21 |
| Laos | LAO | 76 |  |  |  |  |  |  |  | 1 | 3 |  | 1 | 12 | 23 |
| Lesoto | LSO | 91 |  |  |  | 1 |  |  |  |  |  |  | 1 | 12 | 72 |
| Letonia | LVA | 260 | 1 |  |  |  |  |  |  | 2 | 14 | 23 | 24 | 26 | 93 |
| Liberia | LBR | 166 |  |  |  |  |  |  |  |  | 2 | 3 | 5 | 77 | 38 |
| Libia | LBY | 369 | 4 |  |  |  |  |  |  | 8 | 25 | 23 | 23 | 46 | 122 |
| Liechtenstein | LIE | 27 |  |  |  |  |  |  |  | 1 |  | 1 |  | 6 |  |
| Lituania | LTU | 320 |  |  |  |  |  |  |  | 3 | 13 | 15 | 46 | 22 | 50 |
| Luxemburgo | LUX | 430 |  |  |  |  |  |  | 1 | 1 | 14 | 38 | 68 | 69 | 40 |
| Líbano | LBN | 738 | 3 |  |  | 1 | 1 |  |  | 2 | 17 | 6 | 15 | 468 | 132 |
| Macao | MAC | 103 |  |  |  |  |  |  |  |  |  | 5 | 22 | 22 | 36 |
| Macedonia del Norte | MKD | 119 |  |  |  |  |  |  |  | 2 | 13 | 11 | 5 | 19 | 26 |
| Madagascar | MDG | 388 | 1 |  |  |  |  |  |  |  | 14 | 28 | 91 | 88 | 45 |
| Malasia | MYS | 268 | 4 |  |  |  |  |  |  |  | 8 | 9 | 10 | 35 | 45 |
| Malaui | MWI | 37 | 1 |  |  |  |  |  |  |  | 1 |  | 2 | 14 | 14 |
| Maldivas | MDV | 75 |  |  |  |  |  |  |  |  | 1 | 8 | 26 | 9 | 14 |
| Malta | MLT | 317 | 2 |  |  |  |  | 1 | 1 | 1 | 17 | 20 | 82 | 79 | 11 |
| Malí | MLI | 121 |  |  |  |  |  |  | 3 | 2 | 4 | 5 | 8 | 26 | 20 |
| Marruecos | MAR | 618 | 1 |  |  |  |  | 1 |  | 1 | 15 | 44 | 71 | 148 | 152 |
| Mauricio | MUS | 195 | 2 |  |  | 1 |  |  |  | 1 | 5 | 17 | 32 | 53 | 19 |
| Mauritania | MRT | 98 |  |  |  |  |  |  |  |  | 10 | 4 | 13 | 16 | 18 |
| Moldavia | MDA | 135 |  |  |  |  |  |  |  | 1 | 5 | 11 | 23 | 26 | 13 |
| Mongolia | MNG | 145 |  |  |  |  |  |  |  |  | 4 | 11 | 9 | 37 | 62 |
| Montenegro | MNE | 162 |  |  |  |  |  |  |  |  | 8 | 9 | 5 | 34 | 25 |
| Montserrat | MSR | 131 |  |  |  |  |  |  |  |  |  |  |  | 105 | 21 |
| Mozambique | MOZ | 253 | 1 |  |  |  |  |  |  |  | 9 | 15 | 34 | 68 | 53 |
| México | MEX | 4,198 | 3 |  |  |  |  | 1 | 2 | 3 | 60 | 124 | 395 | 1,224 | 1,278 |
| Mónaco | MCO | 64 | 1 |  |  |  |  |  |  |  |  | 6 | 11 | 19 | 7 |
| Namibia | NAM | 137 |  |  |  |  |  |  |  |  | 3 |  | 8 | 41 | 29 |
| Nauru | NRU | 17 |  |  |  |  |  |  |  |  |  |  |  | 3 | 11 |
| Nepal | NPL | 86 |  |  |  |  |  |  |  | 1 | 3 | 2 | 1 | 20 | 30 |
| Nicaragua | NIC | 337 |  |  |  |  |  |  |  |  | 2 | 25 | 26 | 164 | 69 |
| Nigeria | NGA | 135 |  |  |  |  |  |  |  |  | 3 | 10 | 8 | 16 | 57 |
| Niue | NIU | 7 |  |  |  |  |  |  |  |  |  |  |  | 1 | 5 |
| Noruega | NOR | 1,426 | 1 |  |  |  |  |  | 1 | 2 | 20 | 55 | 100 | 411 | 63 |
| Nueva Caledonia | NCL | 25 |  |  |  |  |  |  |  |  |  | 1 | 3 | 5 | 7 |
| Nueva Zelanda | NZL | 475 | 2 |  |  | 1 |  |  |  |  | 1 | 3 | 28 | 241 | 80 |
| Níger | NER | 70 |  |  |  |  |  |  |  |  | 4 | 5 | 3 | 5 | 26 |
| Omán | OMN | 95 |  |  |  |  |  |  |  | 4 | 12 | 9 | 23 | 17 | 10 |
| PSX | PSX | 298 |  |  |  |  |  |  |  | 1 | 17 | 8 | 7 | 106 | 2 |
| Pakistán | PAK | 435 |  |  |  |  |  |  |  |  | 28 | 7 | 11 | 111 | 130 |
| Palaos | PLW | 56 |  |  |  |  |  |  |  |  | 2 | 1 | 10 | 12 | 20 |
| Palestina | PSE | 1,527 | 6 |  |  |  | 2 | 1 | 1 | 10 | 48 | 45 | 82 | 589 | 201 |
| Panamá | PAN | 416 |  |  |  |  |  |  |  |  | 2 | 48 | 55 | 101 | 114 |
| Papúa Nueva Guinea | PNG | 152 |  |  |  |  |  |  |  |  | 2 | 4 | 4 | 38 | 77 |
| Paraguay | PRY | 358 |  |  |  |  |  |  |  |  | 1 | 14 | 55 | 97 | 56 |
| Países Bajos | NLD | 19,714 | 2 |  | 5 |  |  |  | 1 | 1 | 113 | 513 | 673 | 544 | 1,033 |
| Perú | PER | 1,146 | 1 |  |  |  |  |  |  |  | 20 | 54 | 91 | 422 | 229 |
| Polinesia Francesa | PYF | 70 |  |  |  |  |  |  |  |  |  | 1 | 35 | 26 | 5 |
| Polonia | POL | 3,535 | 1 |  | 2 | 1 | 2 |  | 2 | 8 | 49 | 77 | 261 | 753 | 529 |
| Portugal | PRT | 3,212 | 3 |  |  |  |  | 1 | 1 | 10 | 59 | 145 | 524 | 1,189 | 222 |
| Puerto Rico | PRI | 1,082 |  |  |  |  |  |  |  | 1 | 1 | 18 | 71 | 40 | 906 |
| Reino Unido | GBR | 13,864 | 9 | 2 | 3 | 3 | 3 | 13 |  | 8 | 70 | 508 | 1,436 | 3,238 | 523 |
| República Centroafricana | CAF | 160 |  |  |  |  |  |  |  |  |  | 2 | 3 | 10 | 114 |
| República Checa | CZE | 1,313 | 2 |  |  |  |  |  |  | 1 | 18 | 35 | 78 | 231 | 229 |
| República Democrática del Congo | COD | 225 |  |  |  |  |  |  |  |  | 3 | 6 | 9 | 31 | 128 |
| República Dominicana | DOM | 267 |  |  |  |  |  |  |  |  | 4 | 25 | 68 | 46 | 58 |
| República Turca del Norte de Chipre | CYN | 15 |  |  |  |  |  |  |  |  | 2 | 5 |  |  |  |
| República de China | TWN | 195 |  |  |  |  |  |  |  |  | 2 | 17 | 9 | 49 | 80 |
| República del Congo | COG | 298 | 2 |  |  |  |  |  | 1 | 1 | 7 | 11 | 37 | 89 | 67 |
| Ruanda | RWA | 42 | 1 |  |  |  |  |  |  |  |  |  |  | 4 | 31 |
| Rumania | ROU | 1,182 |  |  |  |  |  |  |  | 3 | 42 | 29 | 53 | 194 | 200 |
| Rusia | RUS | 5,641 | 5 |  |  |  |  | 1 | 2 | 6 | 73 | 155 | 340 | 1,899 | 1,251 |
| SAH | SAH | 4 |  |  |  |  |  |  |  |  |  | 2 |  | 1 |  |
| SDS | SDS | 82 |  |  |  |  |  |  |  |  |  | 1 |  | 10 | 19 |
| Sahara Occidental | ESH | 36 |  |  |  |  |  |  | 1 |  |  | 2 | 1 | 17 | 13 |
| Samoa | WSM | 73 | 1 |  |  |  |  |  |  |  |  |  | 6 | 31 | 25 |
| Samoa Estadounidense | ASM | 26 |  |  |  |  |  |  |  |  |  |  |  | 14 | 7 |
| San Bartolomé | BLM | 6 |  |  |  |  |  |  |  |  |  |  | 3 | 2 |  |
| San Cristóbal y Nieves | KNA | 34 |  |  |  |  |  |  |  |  |  | 5 | 17 | 2 | 3 |
| San Marino | SMR | 9 |  |  | 1 |  |  |  |  |  |  | 1 | 1 | 1 | 2 |
| San Martín | MAF | 75 |  |  |  |  |  |  |  |  |  |  | 10 | 36 | 8 |
| San Martín | SXM | 34 |  |  |  |  |  |  |  | 1 |  |  | 6 | 17 | 3 |
| San Pedro y Miquelón | SPM | 8 |  |  |  |  |  |  |  |  |  |  | 1 | 5 | 1 |
| San Vicente y las Granadinas | VCT | 23 | 1 |  |  |  |  |  |  |  |  |  | 6 | 11 | 4 |
| Santa Lucía | LCA | 37 |  |  |  |  |  |  |  |  |  | 1 | 20 | 4 | 5 |
| Santo Tomé y Príncipe | STP | 28 |  |  |  | 1 |  |  |  |  |  | 10 | 10 | 4 | 1 |
| Senegal | SEN | 188 |  |  |  |  |  |  |  |  | 2 | 8 | 65 | 60 | 14 |
| Serbia | SRB | 558 |  |  |  |  |  |  |  | 4 | 27 | 16 | 32 | 144 | 73 |
| Seychelles | SYC | 3 |  |  |  |  |  |  |  |  |  |  |  | 3 |  |
| Sierra Leona | SLE | 177 |  |  |  |  |  |  |  | 1 | 2 | 10 | 21 | 18 | 98 |
| Singapur | SGP | 74 |  |  |  |  |  |  |  | 1 | 2 | 1 | 1 | 29 | 11 |
| Siria | SYR | 1,025 | 2 |  |  | 1 | 1 |  |  | 4 | 47 | 33 | 77 | 505 | 105 |
| Somalia | SOM | 196 |  |  |  |  |  |  |  | 1 | 11 | 7 | 6 | 21 | 105 |
| Somalilandia | SOL | 223 |  |  |  |  |  |  |  |  | 2 | 4 |  | 32 | 169 |
| Sri Lanka | LKA | 289 |  |  |  |  |  |  | 2 | 2 | 14 | 39 | 31 | 61 | 25 |
| Suazilandia | SWZ | 45 |  |  |  | 1 |  |  |  |  |  |  |  | 3 | 38 |
| Sudáfrica | ZAF | 759 | 5 |  |  |  |  | 1 |  |  | 6 | 28 | 46 | 284 | 171 |
| Sudán | SDN | 550 | 1 | 3 |  |  |  |  |  | 2 | 9 | 17 | 15 | 107 | 252 |
| Sudán del Sur | SSD | 202 |  |  |  |  |  |  |  |  | 1 | 4 | 2 | 17 | 89 |
| Suecia | SWE | 1,746 | 2 |  |  |  |  |  | 1 | 3 | 13 | 57 | 85 | 386 | 53 |
| Suiza | CHE | 2,747 | 3 |  |  |  |  | 1 | 1 | 4 | 57 | 69 | 165 | 591 | 175 |
| Surinam | SUR | 490 |  |  |  |  |  |  |  |  | 6 | 24 | 45 | 59 | 62 |
| Tailandia | THA | 260 | 1 |  |  |  |  |  | 2 | 1 | 13 | 20 | 26 | 67 | 59 |
| Tanzania | TZA | 215 | 1 |  |  |  |  |  |  |  | 4 | 2 | 3 | 51 | 85 |
| Tayikistán | TJK | 61 |  |  |  |  |  |  |  |  | 6 |  |  | 29 | 15 |
| Territorio Británico del Océano Índico | IOT | 1 |  |  |  |  |  |  |  |  |  |  |  |  | 1 |
| Territorios Australianos del Océano Índico | IOA | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Tierras Australes y Antárticas Francesas | ATF | 4 |  |  |  |  |  |  |  |  |  |  |  | 1 |  |
| Timor Oriental | TLS | 15 |  |  |  |  |  |  |  |  |  |  |  |  | 2 |
| Togo | TGO | 57 |  |  |  |  |  |  |  |  | 1 | 1 | 2 | 8 | 16 |
| Tonga | TON | 47 |  |  |  |  |  |  |  |  |  | 4 | 7 | 14 | 10 |
| Trinidad y Tobago | TTO | 102 |  |  |  |  |  |  |  |  | 1 | 19 | 35 | 12 | 32 |
| Turkmenistán | TKM | 132 |  |  |  |  |  |  |  |  | 14 | 6 | 4 | 50 | 20 |
| Turquía | TUR | 2,646 | 14 |  |  | 1 |  | 1 | 7 | 8 | 97 | 116 | 249 | 884 | 306 |
| Tuvalu | TUV | 14 |  |  |  |  |  |  |  |  |  |  |  | 8 | 4 |
| Túnez | TUN | 607 | 3 |  |  |  |  | 1 | 1 | 2 | 32 | 11 | 24 | 213 | 172 |
| UMI | UMI | 2 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |
| USG | USG | 3 |  |  |  |  |  |  |  |  |  |  | 1 | 1 |  |
| Ucrania | UKR | 792 | 1 |  |  |  |  |  | 4 | 4 | 32 | 70 | 64 | 98 | 97 |
| Uganda | UGA | 248 |  |  |  |  |  |  |  |  | 1 | 3 | 3 | 15 | 192 |
| Uruguay | URY | 369 |  |  |  |  |  |  |  |  | 4 | 22 | 52 | 123 | 69 |
| Uzbekistán | UZB | 128 |  |  |  |  |  |  |  |  | 7 | 6 | 5 | 59 | 31 |
| Vanuatu | VUT | 15 |  |  |  |  |  |  |  |  |  |  |  | 2 | 13 |
| Venezuela | VEN | 586 |  |  |  |  |  |  |  | 1 | 12 | 83 | 125 | 121 | 76 |
| Vietnam | VNM | 347 |  |  |  |  |  |  |  | 2 | 8 | 5 | 18 | 53 | 85 |
| Yemen | YEM | 433 |  |  |  |  |  |  |  | 5 | 23 | 15 | 18 | 43 | 276 |
| Yibuti | DJI | 57 |  |  |  |  |  |  |  |  | 2 | 2 | 3 | 27 | 20 |
| Zambia | ZMB | 105 |  |  |  |  |  |  |  |  | 1 | 3 | 4 | 20 | 45 |
| Zimbabue | ZWE | 110 |  |  |  |  |  |  |  |  | 2 | 1 | 6 | 26 | 43 |
| Åland | ALA | 6 |  |  |  |  |  |  |  |  |  |  |  | 3 |  |
