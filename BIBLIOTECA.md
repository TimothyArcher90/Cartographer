# Biblioteca de Cartographer

Documento generado por `scripts/comprender.py`. No editar a mano.

- Mapas analizados: **899,255** · con país asignado: **534,703** · sin país: 364,552
  (sobre todo mapamundis, cartas oceánicas o registros sin datos de lugar).
- Países con mapas: **244**.
- Tipos: general 558,624, topográfico 209,360, histórico/temático 62,619, plano urbano 35,520, militar 11,286, mapamundi 7,425, ferroviario/viario 6,886, carta náutica 6,107, portulano 787, ptolemaico 641.
- Escalas: desconocida 629,459, local o ciudad 245,025, provincia o comarca 14,152, región o país 6,100, continente 2,997, mundo 1,522.

Cómo se asigna un país: por **nombre** actual (25+ idiomas, Natural Earth), por **nombre histórico**
(`catalogo/nombres_historicos.json`) o por **coordenadas** de la cobertura del mapa. Cada mapa guarda
la vía en el campo `via`; las asignaciones por coordenadas de mapas grandes pueden incluir países
vecinos. Los siglos salen del año de los metadatos de cada archivo y pueden tener errores puntuales.

Mapas de un país: `catalogo/biblioteca/paises/<ISO3>.jsonl.gz` o
`python scripts/buscar_lugar.py "<país>"`.

| País | ISO | Total | Antes del s. IX | IX | X | XI | XII | XIII | XIV | XV | XVI | XVII | XVIII | XIX | XX |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Afganistán | AFG | 537 | 1 |  |  |  |  |  | 1 |  | 21 | 7 | 12 | 228 | 113 |
| Albania | ALB | 359 | 1 |  |  |  |  | 2 | 2 | 7 | 28 | 35 | 30 | 87 | 65 |
| Alemania | DEU | 15,508 | 6 | 4 | 4 | 2 | 3 | 3 | 2 | 12 | 155 | 403 | 600 | 2,124 | 982 |
| Andorra | AND | 43 | 2 |  |  |  |  |  |  |  |  |  | 2 | 5 | 22 |
| Angola | AGO | 247 |  |  |  |  |  |  |  | 1 | 4 | 16 | 29 | 66 | 92 |
| Anguila | AIA | 14 |  |  |  |  |  |  |  |  |  | 2 | 6 | 2 | 1 |
| Antigua y Barbuda | ATG | 40 |  |  |  |  |  |  |  |  |  | 2 | 16 | 17 | 1 |
| Antártida | ATA | 120 |  |  |  |  |  |  |  |  |  | 13 | 24 | 10 | 55 |
| Arabia Saudita | SAU | 702 | 1 |  |  |  |  |  |  | 6 | 51 | 43 | 87 | 203 | 149 |
| Argelia | DZA | 877 | 2 |  |  |  |  | 1 | 1 | 3 | 26 | 44 | 47 | 385 | 155 |
| Argentina | ARG | 999 |  |  |  |  |  |  |  |  | 8 | 108 | 123 | 207 | 383 |
| Armenia | ARM | 455 | 2 | 1 |  | 1 |  |  | 1 | 2 | 22 | 18 | 36 | 189 | 106 |
| Aruba | ABW | 23 |  |  |  |  |  |  |  |  |  |  | 3 | 6 | 4 |
| Australia | AUS | 2,541 | 5 |  |  |  |  |  | 1 |  | 8 | 19 | 54 | 460 | 112 |
| Austria | AUT | 2,506 | 2 | 1 |  |  |  |  | 1 | 4 | 51 | 73 | 147 | 607 | 294 |
| Azerbaiyán | AZE | 141 |  |  |  |  |  |  |  | 1 | 8 | 7 | 10 | 46 | 38 |
| Bahamas | BHS | 209 |  |  |  |  |  | 1 |  |  |  | 9 | 68 | 65 | 33 |
| Bangladés | BGD | 57 |  |  |  |  |  |  |  | 1 | 4 | 5 | 4 | 7 | 8 |
| Barbados | BRB | 135 |  |  |  |  |  |  |  |  |  | 12 | 47 | 16 | 30 |
| Baréin | BHR | 82 |  |  |  |  |  |  |  | 2 | 6 | 6 | 11 | 19 | 27 |
| Belice | BLZ | 73 |  |  |  |  |  |  |  |  |  | 9 | 5 | 17 | 34 |
| Benín | BEN | 73 |  |  |  |  |  |  |  |  | 4 | 7 | 6 | 11 | 16 |
| Bermudas | BMU | 132 |  |  |  |  |  |  |  |  | 1 | 13 | 36 | 30 | 16 |
| Bielorrusia | BLR | 312 | 1 |  |  |  |  |  |  | 3 | 22 | 20 | 33 | 46 | 85 |
| Birmania | MMR | 245 | 1 |  |  |  |  |  |  | 1 | 11 | 9 | 28 | 64 | 71 |
| Bolivia | BOL | 328 |  |  |  |  |  |  |  |  | 5 | 19 | 11 | 100 | 88 |
| Bosnia y Herzegovina | BIH | 464 | 2 |  |  |  |  |  |  | 6 | 37 | 15 | 22 | 113 | 75 |
| Botsuana | BWA | 163 |  |  |  | 2 |  |  |  |  | 2 |  | 5 | 47 | 56 |
| Brasil | BRA | 2,458 | 3 |  |  |  |  |  |  | 3 | 28 | 251 | 341 | 597 | 478 |
| Brunéi | BRN | 30 |  |  |  |  |  |  |  |  | 1 |  | 1 | 11 | 7 |
| Bulgaria | BGR | 550 |  |  |  |  |  |  | 1 | 2 | 28 | 23 | 50 | 146 | 87 |
| Burkina Faso | BFA | 57 |  |  |  |  |  |  |  |  | 2 | 5 | 3 | 7 | 14 |
| Burundi | BDI | 44 | 1 |  |  |  |  |  |  |  |  |  |  | 3 | 34 |
| Bután | BTN | 123 | 1 |  |  |  |  |  |  |  |  |  | 5 | 36 | 55 |
| Bélgica | BEL | 6,166 | 2 |  | 1 |  |  |  | 1 | 4 | 74 | 262 | 588 | 873 | 340 |
| Cabo Verde | CPV | 132 |  |  |  |  |  |  |  |  | 4 | 22 | 50 | 31 | 3 |
| Camboya | KHM | 142 |  |  |  |  |  |  |  |  | 3 | 13 | 6 | 27 | 58 |
| Camerún | CMR | 135 |  |  |  |  |  |  |  |  | 2 | 6 | 8 | 16 | 55 |
| Canadá | CAN | 6,902 | 8 |  |  |  |  |  | 2 |  | 22 | 145 | 1,641 | 1,833 | 1,861 |
| Catar | QAT | 100 |  |  |  |  |  |  |  | 3 | 8 | 7 | 13 | 34 | 32 |
| Chad | TCD | 85 |  |  |  |  |  |  |  |  |  | 3 | 4 | 18 | 35 |
| Chile | CHL | 1,095 |  |  |  |  |  |  |  | 2 | 8 | 142 | 203 | 347 | 150 |
| China | CHN | 4,641 | 2 | 1 |  |  | 9 | 2 | 4 | 5 | 48 | 159 | 488 | 1,747 | 1,286 |
| Chipre | CYP | 298 | 1 |  |  |  |  | 1 |  | 4 | 35 | 26 | 25 | 25 | 95 |
| Ciudad del Vaticano | VAT | 78 |  |  |  |  |  |  |  |  | 1 | 24 | 5 | 10 | 15 |
| Colombia | COL | 700 |  |  |  |  |  |  |  |  | 10 | 55 | 117 | 160 | 154 |
| Comoras | COM | 27 |  |  |  |  |  |  |  |  |  | 1 | 5 | 10 | 9 |
| Corea del Norte | PRK | 136 |  |  |  |  |  |  |  |  | 1 | 9 | 12 | 13 | 54 |
| Corea del Sur | KOR | 862 | 1 |  |  |  |  |  |  |  | 6 | 15 | 70 | 154 | 226 |
| Costa Rica | CRI | 194 |  |  |  |  |  |  |  |  |  | 16 | 17 | 52 | 91 |
| Costa de Marfil | CIV | 110 |  |  |  |  |  |  |  |  | 3 | 5 | 13 | 15 | 42 |
| Croacia | HRV | 971 | 5 |  |  |  |  |  | 2 | 9 | 59 | 50 | 64 | 231 | 89 |
| Cuba | CUB | 1,395 | 17 | 8 | 5 |  |  |  |  | 1 | 15 | 120 | 262 | 309 | 328 |
| Curazao | CUW | 105 |  |  |  |  |  |  |  |  | 1 | 2 | 27 | 12 | 2 |
| Dinamarca | DNK | 1,513 | 5 |  |  |  |  |  | 3 |  | 14 | 75 | 82 | 431 | 90 |
| Dominica | DMA | 40 |  |  |  |  |  |  |  |  |  | 3 | 26 | 2 |  |
| ESB | ESB | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ecuador | ECU | 424 |  |  |  |  |  |  |  | 1 | 8 | 24 | 81 | 107 | 93 |
| Egipto | EGY | 2,567 | 8 |  |  | 2 | 1 | 3 | 2 | 6 | 65 | 61 | 180 | 929 | 817 |
| El Salvador | SLV | 198 |  |  |  |  |  | 1 |  |  | 2 | 10 | 8 | 96 | 61 |
| Emiratos Árabes Unidos | ARE | 55 |  |  |  |  |  |  |  | 3 | 7 | 6 | 12 | 13 | 7 |
| Eritrea | ERI | 430 |  |  |  |  |  |  |  |  | 1 | 7 | 9 | 109 | 276 |
| Eslovaquia | SVK | 540 |  |  |  |  |  |  |  | 2 | 17 | 15 | 23 | 103 | 126 |
| Eslovenia | SVN | 325 | 1 |  |  |  |  |  |  | 2 | 22 | 9 | 5 | 18 | 108 |
| España | ESP | 8,665 | 18 |  | 23 | 10 | 16 | 9 | 10 | 23 | 125 | 436 | 1,665 | 2,945 | 1,011 |
| Estados Federados de Micronesia | FSM | 69 |  |  |  |  |  |  |  |  |  | 1 | 4 | 23 | 32 |
| Estados Unidos | USA | 376,682 | 49 |  | 2 |  | 1 | 6 | 1 | 4 | 39 | 692 | 5,479 | 119,738 | 214,205 |
| Estonia | EST | 1,098 |  |  |  |  |  |  |  | 1 | 8 | 19 | 28 | 151 | 516 |
| Etiopía | ETH | 600 | 8 |  |  |  |  | 1 | 1 | 1 | 16 | 28 | 34 | 165 | 240 |
| Filipinas | PHL | 737 |  |  |  |  |  |  |  |  | 10 | 25 | 147 | 226 | 192 |
| Finlandia | FIN | 300 |  |  |  |  |  |  |  | 1 | 8 | 24 | 38 | 57 | 36 |
| Fiyi | FJI | 78 |  |  |  |  |  |  |  |  |  | 2 | 4 | 43 | 11 |
| Francia | FRA | 22,126 | 22 | 4 | 7 | 4 | 9 | 20 | 20 | 17 | 293 | 1,384 | 3,411 | 6,718 | 1,265 |
| GIB | GIB | 5 |  |  |  |  |  |  |  |  |  |  | 5 |  |  |
| Gabón | GAB | 92 |  |  |  |  |  |  |  |  | 2 | 8 | 10 | 23 | 17 |
| Gambia | GMB | 89 |  |  |  |  |  |  |  |  | 1 | 6 | 31 | 23 | 5 |
| Georgia | GEO | 286 |  |  |  |  |  |  |  | 1 | 12 | 7 | 68 | 66 | 46 |
| Ghana | GHA | 87 |  |  |  |  |  |  | 1 |  | 2 | 8 | 8 | 9 | 20 |
| Granada | GRD | 490 | 1 |  |  |  |  | 3 |  |  | 2 | 34 | 89 | 229 | 30 |
| Grecia | GRC | 2,365 | 18 | 1 | 1 |  |  | 1 | 3 | 11 | 130 | 226 | 188 | 760 | 255 |
| Groenlandia | GRL | 229 | 2 |  |  |  |  |  | 1 |  | 8 | 15 | 44 | 90 | 29 |
| Guam | GUM | 158 |  |  |  |  |  |  |  |  |  | 4 | 19 | 10 | 111 |
| Guatemala | GTM | 243 | 1 | 1 |  |  |  |  |  |  | 3 | 17 | 12 | 62 | 82 |
| Guernsey | GGY | 247 |  |  |  |  |  |  |  |  |  | 4 | 6 | 104 | 111 |
| Guinea | GIN | 147 |  |  |  |  |  |  |  |  | 1 | 11 | 43 | 15 | 17 |
| Guinea Ecuatorial | GNQ | 40 |  |  |  |  |  |  |  |  | 1 | 2 | 2 | 11 | 18 |
| Guinea-Bisáu | GNB | 10 |  |  |  |  |  |  |  |  | 1 |  | 3 | 2 | 2 |
| Guyana | GUY | 446 |  |  |  |  |  |  |  |  | 8 | 35 | 83 | 100 | 65 |
| Haití | HTI | 410 |  |  |  |  |  | 1 |  |  | 6 | 26 | 123 | 66 | 124 |
| Honduras | HND | 285 |  |  |  |  |  |  |  |  |  | 32 | 52 | 70 | 96 |
| Hong Kong | HKG | 65 |  |  |  |  |  |  |  |  |  |  |  | 27 | 25 |
| Hungría | HUN | 1,617 |  |  |  |  |  |  | 2 | 4 | 60 | 113 | 130 | 389 | 156 |
| India | IND | 3,022 | 3 |  |  |  |  |  | 7 | 7 | 88 | 152 | 505 | 934 | 258 |
| Indonesia | IDN | 2,187 | 4 |  |  |  |  |  | 1 | 2 | 28 | 276 | 470 | 201 | 243 |
| Irak | IRQ | 653 | 7 |  |  |  | 1 |  |  | 6 | 46 | 38 | 34 | 121 | 178 |
| Irlanda | IRL | 2,405 | 5 | 1 | 2 | 2 |  |  | 1 | 4 | 87 | 120 | 179 | 751 | 64 |
| Irán | IRN | 815 | 3 |  |  |  |  |  | 3 | 5 | 48 | 50 | 139 | 259 | 89 |
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
| Israel | ISR | 1,655 |  |  | 2 | 2 | 2 | 2 | 5 | 21 | 81 | 97 | 198 | 499 | 166 |
| Italia | ITA | 8,491 | 30 | 5 |  | 4 | 6 | 8 | 3 | 69 | 422 | 559 | 787 | 1,964 | 603 |
| Jamaica | JAM | 965 | 1 |  |  |  |  |  |  | 1 | 1 | 27 | 224 | 562 | 55 |
| Japón | JPN | 1,618 | 3 |  |  |  |  |  | 1 | 3 | 12 | 100 | 198 | 384 | 289 |
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
| Libia | LBY | 399 | 4 |  |  |  |  |  |  | 9 | 26 | 36 | 35 | 50 | 125 |
| Liechtenstein | LIE | 27 |  |  |  |  |  |  |  | 1 |  | 1 |  | 6 |  |
| Lituania | LTU | 321 |  |  |  |  |  |  |  | 3 | 13 | 17 | 49 | 22 | 50 |
| Luxemburgo | LUX | 541 |  |  |  |  |  |  | 1 | 1 | 15 | 61 | 98 | 104 | 60 |
| Líbano | LBN | 748 | 3 |  |  | 1 | 1 |  |  | 2 | 17 | 7 | 15 | 470 | 136 |
| Macao | MAC | 115 |  |  |  |  |  |  |  |  |  | 7 | 27 | 25 | 36 |
| Macedonia del Norte | MKD | 119 |  |  |  |  |  |  |  | 2 | 13 | 11 | 5 | 19 | 26 |
| Madagascar | MDG | 481 | 1 |  |  |  |  |  |  | 1 | 15 | 32 | 138 | 100 | 53 |
| Malasia | MYS | 264 | 4 |  |  |  |  |  |  |  | 8 | 9 | 12 | 35 | 45 |
| Malaui | MWI | 37 | 1 |  |  |  |  |  |  |  | 1 |  | 2 | 14 | 14 |
| Maldivas | MDV | 77 |  |  |  |  |  |  |  |  | 1 | 8 | 30 | 9 | 14 |
| Malta | MLT | 388 | 2 |  |  |  |  | 1 | 1 | 2 | 30 | 36 | 106 | 90 | 12 |
| Malí | MLI | 121 |  |  |  |  |  |  | 3 | 2 | 4 | 5 | 8 | 26 | 20 |
| Marruecos | MAR | 680 | 1 |  |  |  |  | 1 |  | 2 | 15 | 48 | 75 | 163 | 211 |
| Mauricio | MUS | 234 | 2 |  |  | 1 |  |  |  | 1 | 7 | 20 | 42 | 66 | 27 |
| Mauritania | MRT | 99 |  |  |  |  |  |  |  |  | 10 | 4 | 13 | 16 | 21 |
| Moldavia | MDA | 142 |  |  |  |  |  |  |  | 1 | 5 | 15 | 26 | 26 | 13 |
| Mongolia | MNG | 150 |  |  |  |  |  |  |  |  | 4 | 11 | 10 | 39 | 62 |
| Montenegro | MNE | 170 |  |  |  |  |  |  |  |  | 8 | 9 | 5 | 39 | 27 |
| Montserrat | MSR | 133 |  |  |  |  |  |  |  |  |  |  |  | 106 | 21 |
| Mozambique | MOZ | 270 | 1 |  |  |  |  |  |  |  | 11 | 16 | 38 | 72 | 54 |
| México | MEX | 4,142 | 3 |  |  |  |  | 1 | 2 | 3 | 69 | 141 | 412 | 1,250 | 1,284 |
| Mónaco | MCO | 71 | 1 |  |  |  |  |  |  |  |  | 7 | 12 | 20 | 9 |
| Namibia | NAM | 137 |  |  |  |  |  |  |  |  | 3 |  | 8 | 41 | 29 |
| Nauru | NRU | 17 |  |  |  |  |  |  |  |  |  |  |  | 3 | 11 |
| Nepal | NPL | 87 |  |  |  |  |  |  |  | 1 | 3 | 2 | 1 | 20 | 31 |
| Nicaragua | NIC | 343 |  |  |  |  |  |  |  |  | 2 | 25 | 27 | 173 | 69 |
| Nigeria | NGA | 135 |  |  |  |  |  |  |  |  | 3 | 10 | 8 | 16 | 57 |
| Niue | NIU | 7 |  |  |  |  |  |  |  |  |  |  |  | 1 | 5 |
| Noruega | NOR | 1,407 | 1 |  |  |  |  |  | 1 | 2 | 21 | 56 | 107 | 420 | 65 |
| Nueva Caledonia | NCL | 33 |  |  |  |  |  |  |  |  |  | 1 | 3 | 10 | 10 |
| Nueva Zelanda | NZL | 478 | 2 |  |  | 1 |  |  |  |  | 1 | 3 | 32 | 242 | 83 |
| Níger | NER | 70 |  |  |  |  |  |  |  |  | 4 | 5 | 3 | 5 | 26 |
| Omán | OMN | 107 |  |  |  |  |  |  |  | 4 | 12 | 10 | 31 | 18 | 11 |
| PSX | PSX | 298 |  |  |  |  |  |  |  | 1 | 17 | 8 | 7 | 106 | 2 |
| Pakistán | PAK | 434 |  |  |  |  |  |  |  |  | 28 | 7 | 11 | 112 | 131 |
| Palaos | PLW | 56 |  |  |  |  |  |  |  |  | 2 | 1 | 10 | 12 | 20 |
| Palestina | PSE | 1,545 | 5 |  |  |  | 2 | 1 | 1 | 10 | 49 | 47 | 93 | 598 | 216 |
| Panamá | PAN | 437 |  |  |  |  |  |  |  |  | 3 | 51 | 63 | 106 | 115 |
| Papúa Nueva Guinea | PNG | 152 |  |  |  |  |  |  |  |  | 2 | 4 | 4 | 38 | 77 |
| Paraguay | PRY | 366 |  |  |  |  |  |  |  |  | 1 | 20 | 64 | 104 | 58 |
| Países Bajos | NLD | 19,617 | 1 |  | 5 |  |  |  | 1 | 1 | 128 | 565 | 738 | 572 | 1,039 |
| Perú | PER | 1,237 | 1 |  |  |  |  |  |  |  | 26 | 69 | 131 | 454 | 230 |
| Polinesia Francesa | PYF | 70 |  |  |  |  |  |  |  |  |  | 1 | 35 | 26 | 5 |
| Polonia | POL | 3,595 | 2 |  | 2 | 1 | 3 |  | 2 | 10 | 63 | 103 | 298 | 761 | 552 |
| Portugal | PRT | 3,261 | 2 |  |  |  |  | 1 | 1 | 10 | 63 | 164 | 557 | 1,226 | 228 |
| Puerto Rico | PRI | 1,096 |  |  |  |  |  |  |  | 1 | 2 | 20 | 75 | 41 | 906 |
| Reino Unido | GBR | 13,058 | 8 | 2 | 3 | 3 | 3 | 13 |  | 9 | 75 | 503 | 1,490 | 3,230 | 538 |
| República Centroafricana | CAF | 160 |  |  |  |  |  |  |  |  |  | 2 | 3 | 10 | 114 |
| República Checa | CZE | 1,332 | 2 |  |  |  |  |  |  | 1 | 19 | 42 | 98 | 236 | 232 |
| República Democrática del Congo | COD | 225 |  |  |  |  |  |  |  |  | 3 | 6 | 9 | 31 | 128 |
| República Dominicana | DOM | 260 |  |  |  |  |  |  |  |  | 5 | 27 | 71 | 47 | 59 |
| República Turca del Norte de Chipre | CYN | 15 |  |  |  |  |  |  |  |  | 2 | 5 |  |  |  |
| República de China | TWN | 212 |  |  |  |  |  |  | 1 |  | 2 | 17 | 9 | 50 | 87 |
| República del Congo | COG | 332 | 2 |  |  |  |  |  | 1 | 1 | 8 | 14 | 38 | 121 | 82 |
| Ruanda | RWA | 43 | 1 |  |  |  |  |  |  |  |  |  |  | 4 | 32 |
| Rumania | ROU | 1,191 |  |  |  |  |  |  |  | 3 | 52 | 33 | 55 | 198 | 210 |
| Rusia | RUS | 5,536 | 5 |  |  |  |  | 1 | 2 | 7 | 86 | 169 | 387 | 1,937 | 1,268 |
| SAH | SAH | 4 |  |  |  |  |  |  |  |  |  | 2 |  | 1 |  |
| SDS | SDS | 82 |  |  |  |  |  |  |  |  |  | 1 |  | 10 | 19 |
| Sahara Occidental | ESH | 41 |  |  |  |  |  |  | 1 |  |  | 2 | 1 | 19 | 16 |
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
| Senegal | SEN | 236 |  |  |  |  |  |  |  |  | 2 | 14 | 80 | 79 | 16 |
| Serbia | SRB | 570 |  |  |  |  |  |  |  | 4 | 29 | 20 | 39 | 146 | 77 |
| Seychelles | SYC | 3 |  |  |  |  |  |  |  |  |  |  |  | 3 |  |
| Sierra Leona | SLE | 198 |  |  |  |  |  |  |  | 1 | 2 | 10 | 23 | 20 | 106 |
| Singapur | SGP | 84 |  |  |  |  |  |  |  | 1 | 2 | 1 | 1 | 29 | 19 |
| Siria | SYR | 1,049 | 2 |  |  | 1 | 1 |  | 1 | 4 | 47 | 36 | 84 | 514 | 116 |
| Somalia | SOM | 200 |  |  |  |  |  |  |  | 1 | 11 | 7 | 6 | 22 | 108 |
| Somalilandia | SOL | 225 |  |  |  |  |  |  |  |  | 2 | 4 |  | 33 | 170 |
| Sri Lanka | LKA | 299 |  |  |  |  |  |  | 2 | 2 | 18 | 42 | 38 | 60 | 26 |
| Suazilandia | SWZ | 46 |  |  |  | 1 |  |  |  |  |  |  |  | 3 | 39 |
| Sudáfrica | ZAF | 778 | 5 |  |  |  |  | 1 |  |  | 6 | 28 | 51 | 301 | 176 |
| Sudán | SDN | 569 | 1 | 3 |  |  |  |  |  | 2 | 9 | 19 | 16 | 129 | 256 |
| Sudán del Sur | SSD | 202 |  |  |  |  |  |  |  |  | 1 | 4 | 2 | 17 | 89 |
| Suecia | SWE | 1,744 | 2 |  |  |  |  |  | 1 | 3 | 15 | 70 | 111 | 397 | 57 |
| Suiza | CHE | 2,728 | 3 |  |  |  |  | 1 | 1 | 5 | 61 | 72 | 177 | 602 | 184 |
| Surinam | SUR | 514 |  |  |  |  |  |  |  |  | 6 | 28 | 58 | 63 | 63 |
| Tailandia | THA | 277 | 1 |  |  |  |  |  | 2 | 1 | 13 | 27 | 30 | 71 | 61 |
| Tanzania | TZA | 215 | 1 |  |  |  |  |  |  |  | 4 | 2 | 3 | 51 | 85 |
| Tayikistán | TJK | 61 |  |  |  |  |  |  |  |  | 6 |  |  | 29 | 15 |
| Territorio Británico del Océano Índico | IOT | 1 |  |  |  |  |  |  |  |  |  |  |  |  | 1 |
| Territorios Australianos del Océano Índico | IOA | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Tierras Australes y Antárticas Francesas | ATF | 4 |  |  |  |  |  |  |  |  |  |  |  | 1 |  |
| Timor Oriental | TLS | 15 |  |  |  |  |  |  |  |  |  |  |  |  | 2 |
| Togo | TGO | 59 |  |  |  |  |  |  |  |  | 1 | 1 | 2 | 8 | 18 |
| Tonga | TON | 48 |  |  |  |  |  |  |  |  |  | 4 | 7 | 15 | 10 |
| Trinidad y Tobago | TTO | 102 |  |  |  |  |  |  |  |  | 1 | 19 | 35 | 12 | 32 |
| Turkmenistán | TKM | 134 |  |  |  |  |  |  |  |  | 14 | 6 | 5 | 51 | 20 |
| Turquía | TUR | 2,721 | 14 |  |  | 1 |  | 1 | 7 | 8 | 112 | 156 | 296 | 918 | 341 |
| Tuvalu | TUV | 14 |  |  |  |  |  |  |  |  |  |  |  | 8 | 4 |
| Túnez | TUN | 645 | 3 |  |  |  |  | 1 | 1 | 2 | 33 | 26 | 32 | 227 | 182 |
| UMI | UMI | 2 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |
| USG | USG | 3 |  |  |  |  |  |  |  |  |  |  | 1 | 1 |  |
| Ucrania | UKR | 814 | 1 |  |  |  |  |  | 4 | 4 | 32 | 82 | 76 | 101 | 98 |
| Uganda | UGA | 253 |  |  |  |  |  |  |  |  | 1 | 3 | 3 | 19 | 193 |
| Uruguay | URY | 382 |  |  |  |  |  |  |  |  | 4 | 22 | 55 | 135 | 78 |
| Uzbekistán | UZB | 135 |  |  |  |  |  |  |  |  | 7 | 6 | 6 | 65 | 31 |
| Vanuatu | VUT | 15 |  |  |  |  |  |  |  |  |  |  |  | 2 | 13 |
| Venezuela | VEN | 586 |  |  |  |  |  |  |  | 1 | 12 | 84 | 128 | 125 | 79 |
| Vietnam | VNM | 346 |  |  |  |  |  |  |  | 2 | 8 | 5 | 18 | 53 | 87 |
| Yemen | YEM | 446 |  |  |  |  |  |  |  | 5 | 25 | 16 | 24 | 46 | 276 |
| Yibuti | DJI | 59 |  |  |  |  |  |  |  |  | 2 | 2 | 3 | 28 | 21 |
| Zambia | ZMB | 106 |  |  |  |  |  |  |  |  | 1 | 3 | 4 | 21 | 45 |
| Zimbabue | ZWE | 110 |  |  |  |  |  |  |  |  | 2 | 1 | 6 | 26 | 43 |
| Åland | ALA | 7 |  |  |  |  |  |  |  |  |  |  | 1 | 3 |  |
