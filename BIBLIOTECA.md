# Biblioteca de Cartographer

Documento generado por `scripts/comprender.py`. No editar a mano.

- Mapas analizados: **849,491** · con país asignado: **518,669** · sin país: 330,822
  (sobre todo mapamundis, cartas oceánicas o registros sin datos de lugar).
- Países con mapas: **244**.
- Tipos: general 530,363, topográfico 207,913, histórico/temático 55,644, plano urbano 25,698, militar 10,679, mapamundi 6,676, ferroviario/viario 5,977, carta náutica 5,289, portulano 766, ptolemaico 486.
- Escalas: desconocida 579,695, local o ciudad 245,025, provincia o comarca 14,152, región o país 6,100, continente 2,997, mundo 1,522.

Cómo se asigna un país: por **nombre** actual (25+ idiomas, Natural Earth), por **nombre histórico**
(`catalogo/nombres_historicos.json`) o por **coordenadas** de la cobertura del mapa. Cada mapa guarda
la vía en el campo `via`; las asignaciones por coordenadas de mapas grandes pueden incluir países
vecinos. Los siglos salen del año de los metadatos de cada archivo y pueden tener errores puntuales.

Mapas de un país: `catalogo/biblioteca/paises/<ISO3>.jsonl.gz` o
`python scripts/buscar_lugar.py "<país>"`.

| País | ISO | Total | Antes del s. IX | IX | X | XI | XII | XIII | XIV | XV | XVI | XVII | XVIII | XIX | XX |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Afganistán | AFG | 504 | 1 |  |  |  |  |  | 1 |  | 21 | 7 | 12 | 211 | 111 |
| Albania | ALB | 339 | 1 |  |  |  |  | 2 | 2 | 7 | 26 | 28 | 27 | 87 | 61 |
| Alemania | DEU | 14,812 | 8 | 4 | 4 | 2 | 3 | 3 | 2 | 9 | 106 | 274 | 484 | 1,935 | 936 |
| Andorra | AND | 43 | 2 |  |  |  |  |  |  |  |  |  | 2 | 5 | 22 |
| Angola | AGO | 231 |  |  |  |  |  |  |  | 1 | 4 | 13 | 23 | 64 | 90 |
| Anguila | AIA | 10 |  |  |  |  |  |  |  |  |  |  | 6 | 1 | 1 |
| Antigua y Barbuda | ATG | 40 |  |  |  |  |  |  |  |  |  | 2 | 16 | 17 | 1 |
| Antártida | ATA | 101 |  |  |  |  |  |  |  |  |  | 10 | 11 | 10 | 54 |
| Arabia Saudita | SAU | 658 | 1 |  |  |  |  |  |  | 6 | 50 | 39 | 71 | 188 | 147 |
| Argelia | DZA | 678 | 2 |  |  |  |  | 1 | 1 | 3 | 24 | 29 | 39 | 274 | 117 |
| Argentina | ARG | 945 |  |  |  |  |  |  |  |  | 7 | 102 | 107 | 179 | 367 |
| Armenia | ARM | 435 | 2 | 1 |  | 1 |  |  | 1 | 2 | 22 | 17 | 31 | 184 | 102 |
| Aruba | ABW | 23 |  |  |  |  |  |  |  |  |  |  | 3 | 6 | 4 |
| Australia | AUS | 2,439 | 5 |  |  |  |  |  | 1 |  | 8 | 19 | 46 | 411 | 102 |
| Austria | AUT | 2,300 | 4 |  |  |  |  |  | 1 | 4 | 42 | 60 | 113 | 554 | 270 |
| Azerbaiyán | AZE | 139 |  |  |  |  |  |  |  | 1 | 8 | 7 | 10 | 46 | 37 |
| Bahamas | BHS | 191 |  |  |  |  |  | 1 |  |  |  | 6 | 65 | 61 | 33 |
| Bangladés | BGD | 57 |  |  |  |  |  |  |  | 1 | 4 | 5 | 4 | 7 | 8 |
| Barbados | BRB | 127 |  |  |  |  |  |  |  |  |  | 12 | 43 | 14 | 30 |
| Baréin | BHR | 82 |  |  |  |  |  |  |  | 2 | 6 | 6 | 11 | 19 | 27 |
| Belice | BLZ | 73 |  |  |  |  |  |  |  |  |  | 9 | 5 | 17 | 34 |
| Benín | BEN | 60 |  |  |  |  |  |  |  |  | 4 | 7 | 4 | 5 | 16 |
| Bermudas | BMU | 117 |  |  |  |  |  |  |  |  | 1 | 12 | 33 | 26 | 16 |
| Bielorrusia | BLR | 312 | 1 |  |  |  |  |  |  | 3 | 22 | 20 | 33 | 46 | 85 |
| Birmania | MMR | 239 | 1 |  |  |  |  |  |  | 1 | 11 | 9 | 23 | 64 | 70 |
| Bolivia | BOL | 297 |  |  |  |  |  |  |  |  | 5 | 15 | 11 | 89 | 82 |
| Bosnia y Herzegovina | BIH | 464 | 2 |  |  |  |  |  |  | 6 | 37 | 15 | 22 | 113 | 75 |
| Botsuana | BWA | 163 |  |  |  | 2 |  |  |  |  | 2 |  | 5 | 47 | 56 |
| Brasil | BRA | 2,220 | 3 |  |  |  |  |  |  | 3 | 26 | 229 | 259 | 544 | 452 |
| Brunéi | BRN | 30 |  |  |  |  |  |  |  |  | 1 |  | 1 | 11 | 7 |
| Bulgaria | BGR | 520 |  |  |  |  |  |  | 1 | 2 | 25 | 20 | 46 | 141 | 85 |
| Burkina Faso | BFA | 57 |  |  |  |  |  |  |  |  | 2 | 5 | 3 | 7 | 14 |
| Burundi | BDI | 44 | 1 |  |  |  |  |  |  |  |  |  |  | 3 | 34 |
| Bután | BTN | 123 | 1 |  |  |  |  |  |  |  |  |  | 5 | 36 | 55 |
| Bélgica | BEL | 5,467 | 2 |  | 1 |  |  |  | 1 | 3 | 61 | 162 | 418 | 571 | 297 |
| Cabo Verde | CPV | 128 |  |  |  |  |  |  |  |  | 4 | 21 | 49 | 30 | 3 |
| Camboya | KHM | 118 |  |  |  |  |  |  |  |  | 2 | 8 | 5 | 17 | 53 |
| Camerún | CMR | 122 |  |  |  |  |  |  |  |  | 2 | 6 | 8 | 12 | 50 |
| Canadá | CAN | 6,655 | 8 |  |  |  |  |  | 2 |  | 22 | 111 | 1,538 | 1,784 | 1,819 |
| Catar | QAT | 100 |  |  |  |  |  |  |  | 3 | 8 | 7 | 13 | 34 | 32 |
| Chad | TCD | 74 |  |  |  |  |  |  |  |  |  | 3 | 4 | 13 | 29 |
| Chile | CHL | 997 |  |  |  |  |  |  |  | 2 | 8 | 126 | 175 | 327 | 145 |
| China | CHN | 4,354 | 2 | 1 |  |  | 9 | 2 | 4 | 5 | 42 | 144 | 438 | 1,605 | 1,264 |
| Chipre | CYP | 255 | 1 |  |  |  |  | 1 |  | 2 | 18 | 17 | 18 | 24 | 95 |
| Ciudad del Vaticano | VAT | 79 |  |  |  |  |  |  |  |  | 1 | 24 | 5 | 10 | 15 |
| Colombia | COL | 632 |  |  |  |  |  |  |  |  | 10 | 55 | 106 | 140 | 148 |
| Comoras | COM | 24 |  |  |  |  |  |  |  |  |  | 1 | 3 | 10 | 8 |
| Corea del Norte | PRK | 136 |  |  |  |  |  |  |  |  | 1 | 9 | 12 | 13 | 54 |
| Corea del Sur | KOR | 844 | 1 |  |  |  |  |  |  |  | 6 | 15 | 67 | 145 | 221 |
| Costa Rica | CRI | 187 |  |  |  |  |  |  |  |  |  | 16 | 16 | 49 | 89 |
| Costa de Marfil | CIV | 104 |  |  |  |  |  |  |  |  | 3 | 5 | 13 | 13 | 38 |
| Croacia | HRV | 901 | 5 |  |  |  |  |  | 2 | 7 | 48 | 35 | 47 | 226 | 87 |
| Cuba | CUB | 1,306 | 17 | 8 | 5 |  |  |  |  | 1 | 7 | 107 | 237 | 288 | 326 |
| Curazao | CUW | 91 |  |  |  |  |  |  |  |  |  | 1 | 20 | 11 | 2 |
| Dinamarca | DNK | 1,420 | 6 |  |  |  |  |  | 3 |  | 11 | 66 | 74 | 408 | 81 |
| Dominica | DMA | 27 |  |  |  |  |  |  |  |  |  | 3 | 17 | 2 |  |
| ESB | ESB | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ecuador | ECU | 340 |  |  |  |  |  |  |  |  | 8 | 21 | 50 | 85 | 88 |
| Egipto | EGY | 2,425 | 8 |  |  | 2 | 1 | 3 | 2 | 5 | 57 | 43 | 152 | 888 | 793 |
| El Salvador | SLV | 189 |  |  |  |  |  | 1 |  |  | 1 | 10 | 5 | 93 | 61 |
| Emiratos Árabes Unidos | ARE | 55 |  |  |  |  |  |  |  | 3 | 7 | 6 | 12 | 13 | 7 |
| Eritrea | ERI | 421 |  |  |  |  |  |  |  |  | 1 | 6 | 7 | 105 | 274 |
| Eslovaquia | SVK | 539 |  |  |  |  |  |  |  | 2 | 17 | 15 | 23 | 103 | 125 |
| Eslovenia | SVN | 324 | 1 |  |  |  |  |  |  | 2 | 22 | 9 | 5 | 18 | 108 |
| España | ESP | 7,927 | 19 |  | 23 | 10 | 16 | 9 | 10 | 22 | 106 | 320 | 1,507 | 2,774 | 1,002 |
| Estados Federados de Micronesia | FSM | 68 |  |  |  |  |  |  |  |  |  | 1 | 4 | 23 | 32 |
| Estados Unidos | USA | 376,043 | 52 |  | 2 |  | 4 | 6 | 1 | 4 | 41 | 679 | 5,404 | 119,356 | 214,123 |
| Estonia | EST | 981 |  |  |  |  |  |  |  |  | 2 | 12 | 18 | 83 | 500 |
| Etiopía | ETH | 560 | 8 |  |  |  |  | 1 | 1 | 1 | 16 | 22 | 26 | 149 | 235 |
| Filipinas | PHL | 651 |  |  |  | 1 |  |  |  |  | 8 | 16 | 88 | 222 | 191 |
| Finlandia | FIN | 239 |  |  |  |  |  |  |  | 1 | 8 | 19 | 23 | 40 | 32 |
| Fiyi | FJI | 77 |  |  |  |  |  |  |  |  |  | 2 | 4 | 43 | 10 |
| Francia | FRA | 17,748 | 23 | 2 | 7 | 4 | 9 | 19 | 20 | 14 | 186 | 783 | 2,374 | 5,038 | 867 |
| GIB | GIB | 5 |  |  |  |  |  |  |  |  |  |  | 5 |  |  |
| Gabón | GAB | 80 |  |  |  |  |  |  |  |  | 2 | 8 | 10 | 14 | 16 |
| Gambia | GMB | 49 |  |  |  |  |  |  |  |  |  | 4 | 20 | 16 | 4 |
| Georgia | GEO | 273 |  |  |  |  |  |  |  | 1 | 11 | 6 | 62 | 65 | 44 |
| Ghana | GHA | 87 |  |  |  |  |  |  | 1 |  | 2 | 8 | 8 | 9 | 20 |
| Granada | GRD | 412 | 1 |  |  |  |  | 3 |  |  | 1 | 21 | 68 | 214 | 30 |
| Grecia | GRC | 2,169 | 18 | 1 | 1 |  |  | 1 | 2 | 5 | 102 | 153 | 157 | 732 | 247 |
| Groenlandia | GRL | 201 | 1 |  |  |  |  |  | 1 |  | 8 | 14 | 38 | 83 | 18 |
| Guam | GUM | 153 |  |  |  |  |  |  |  |  |  | 4 | 15 | 9 | 111 |
| Guatemala | GTM | 233 | 1 | 1 |  |  |  |  |  |  | 3 | 17 | 12 | 56 | 82 |
| Guernsey | GGY | 241 |  |  |  |  |  |  |  |  |  | 4 | 5 | 103 | 110 |
| Guinea | GIN | 134 |  |  |  |  |  |  |  |  | 1 | 11 | 38 | 13 | 16 |
| Guinea Ecuatorial | GNQ | 40 |  |  |  |  |  |  |  |  | 1 | 2 | 2 | 11 | 18 |
| Guinea-Bisáu | GNB | 10 |  |  |  |  |  |  |  |  | 1 |  | 3 | 2 | 2 |
| Guyana | GUY | 373 |  |  |  |  |  |  |  |  | 6 | 31 | 56 | 77 | 56 |
| Haití | HTI | 390 |  |  |  |  |  | 1 |  |  | 5 | 24 | 114 | 63 | 122 |
| Honduras | HND | 270 |  |  |  |  |  |  |  |  |  | 28 | 50 | 66 | 94 |
| Hong Kong | HKG | 61 |  |  |  |  |  |  |  |  |  |  |  | 26 | 22 |
| Hungría | HUN | 1,409 | 1 |  |  |  |  |  | 1 | 4 | 54 | 61 | 101 | 369 | 137 |
| India | IND | 2,716 | 3 |  |  |  |  |  | 7 | 5 | 74 | 111 | 413 | 879 | 251 |
| Indonesia | IDN | 1,980 | 3 |  |  |  |  |  | 1 | 1 | 22 | 257 | 344 | 185 | 234 |
| Irak | IRQ | 632 | 7 |  |  |  | 1 |  |  | 6 | 46 | 36 | 30 | 119 | 173 |
| Irlanda | IRL | 2,222 | 5 | 1 | 2 | 2 |  |  | 1 | 2 | 79 | 97 | 132 | 715 | 48 |
| Irán | IRN | 750 | 3 |  |  |  |  |  | 3 | 5 | 44 | 35 | 112 | 243 | 89 |
| Isla Norfolk | NFK | 1,353 |  |  |  |  |  |  |  |  |  | 2 | 38 | 1,082 | 206 |
| Isla Santa Elena | SHN | 126 |  |  |  |  |  |  |  |  | 1 | 9 | 7 | 85 | 5 |
| Isla de Man | IMN | 38 |  |  |  |  |  |  |  |  |  |  | 2 | 19 |  |
| Islandia | ISL | 217 | 1 |  |  |  |  |  |  |  | 13 | 16 | 21 | 60 | 26 |
| Islas Caimán | CYM | 9 |  |  |  |  |  |  |  |  |  |  | 1 | 1 | 7 |
| Islas Feroe | FRO | 84 | 1 |  |  |  |  |  | 1 |  |  | 9 | 12 | 27 | 12 |
| Islas Georgias del Sur y Sandwich del Sur | SGS | 2 |  |  |  |  |  |  |  |  |  |  |  |  | 1 |
| Islas Malvinas | FLK | 48 |  |  |  |  |  |  |  |  |  | 11 | 11 | 6 | 4 |
| Islas Marianas del Norte | MNP | 42 |  |  |  |  |  |  |  |  | 2 |  | 7 | 2 | 24 |
| Islas Marshall | MHL | 64 | 2 |  |  |  |  |  |  |  |  |  |  | 21 | 34 |
| Islas Pitcairn | PCN | 11 |  |  |  |  |  |  |  |  |  |  | 1 | 1 | 8 |
| Islas Salomón | SLB | 41 |  |  |  |  |  |  |  |  | 1 | 2 | 2 | 6 | 13 |
| Islas Turcas y Caicos | TCA | 6 |  |  |  |  |  |  |  |  |  |  | 2 | 2 | 2 |
| Islas Vírgenes Británicas | VGB | 9 |  |  |  |  |  |  |  |  |  |  | 3 | 1 | 5 |
| Islas Vírgenes de los Estados Unidos | VIR | 102 |  |  |  |  |  |  |  |  |  | 1 | 49 | 3 | 44 |
| Israel | ISR | 1,524 |  |  | 2 | 2 | 2 | 2 | 4 | 20 | 64 | 74 | 180 | 478 | 161 |
| Italia | ITA | 7,447 | 29 | 4 |  | 3 | 6 | 8 | 3 | 55 | 264 | 431 | 622 | 1,736 | 560 |
| Jamaica | JAM | 928 | 1 |  |  |  |  |  |  | 1 | 1 | 21 | 213 | 557 | 55 |
| Japón | JPN | 1,483 | 3 |  |  |  |  |  | 1 | 2 | 9 | 83 | 170 | 358 | 259 |
| Jersey | JEY | 13 |  |  |  |  |  |  |  |  |  | 4 |  | 8 |  |
| Jordania | JOR | 380 |  |  |  |  |  |  |  | 1 | 37 | 18 | 22 | 148 | 27 |
| Kazajistán | KAZ | 151 |  |  |  |  |  |  |  | 1 | 15 | 17 | 10 | 35 | 31 |
| Kenia | KEN | 231 |  |  |  |  |  |  |  |  | 2 | 4 | 2 | 26 | 155 |
| Kirguistán | KGZ | 54 |  |  |  |  |  |  |  |  | 7 | 2 |  | 23 | 11 |
| Kiribati | KIR | 25 |  |  |  |  |  |  |  |  |  |  |  | 15 | 9 |
| Kosovo | KOS | 60 |  |  |  |  |  |  |  |  | 1 | 2 | 2 | 3 | 33 |
| Kuwait | KWT | 78 |  |  |  |  |  |  |  | 3 | 7 | 5 | 12 | 15 | 21 |
| Laos | LAO | 71 |  |  |  |  |  |  |  | 1 | 3 |  | 1 | 11 | 19 |
| Lesoto | LSO | 91 |  |  |  | 1 |  |  |  |  |  |  | 1 | 12 | 72 |
| Letonia | LVA | 259 | 1 |  |  |  |  |  |  | 2 | 14 | 23 | 24 | 26 | 93 |
| Liberia | LBR | 164 |  |  |  |  |  |  |  |  | 2 | 3 | 5 | 77 | 38 |
| Libia | LBY | 348 | 4 |  |  |  |  |  |  | 8 | 25 | 22 | 23 | 45 | 122 |
| Liechtenstein | LIE | 24 |  |  |  |  |  |  |  | 1 |  | 1 |  | 6 |  |
| Lituania | LTU | 315 |  |  |  |  |  |  |  | 3 | 13 | 15 | 46 | 22 | 50 |
| Luxemburgo | LUX | 410 |  |  |  |  |  |  | 1 | 1 | 13 | 37 | 66 | 66 | 34 |
| Líbano | LBN | 725 | 3 |  |  | 1 | 1 |  |  | 2 | 17 | 6 | 15 | 464 | 125 |
| Macao | MAC | 98 |  |  |  |  |  |  |  |  |  | 5 | 20 | 20 | 36 |
| Macedonia del Norte | MKD | 119 |  |  |  |  |  |  |  | 2 | 13 | 11 | 5 | 19 | 26 |
| Madagascar | MDG | 319 |  |  |  |  |  |  |  |  | 12 | 23 | 70 | 82 | 44 |
| Malasia | MYS | 260 | 4 |  |  |  |  |  |  |  | 8 | 7 | 10 | 35 | 45 |
| Malaui | MWI | 37 | 1 |  |  |  |  |  |  |  | 1 |  | 2 | 14 | 14 |
| Maldivas | MDV | 71 |  |  |  |  |  |  |  |  | 1 | 8 | 25 | 9 | 14 |
| Malta | MLT | 263 | 1 |  |  |  |  | 1 | 1 | 1 | 17 | 20 | 74 | 60 | 11 |
| Malí | MLI | 121 |  |  |  |  |  |  | 3 | 2 | 4 | 5 | 8 | 26 | 20 |
| Marruecos | MAR | 559 | 1 |  |  |  |  | 1 |  | 1 | 14 | 44 | 69 | 138 | 135 |
| Mauricio | MUS | 181 | 2 |  |  | 1 |  |  |  |  | 5 | 17 | 31 | 48 | 17 |
| Mauritania | MRT | 94 |  |  |  |  |  |  |  |  | 10 | 4 | 13 | 16 | 16 |
| Moldavia | MDA | 131 |  |  |  |  |  |  |  | 1 | 5 | 11 | 22 | 26 | 13 |
| Mongolia | MNG | 139 |  |  |  |  |  |  |  |  | 3 | 11 | 8 | 35 | 62 |
| Montenegro | MNE | 153 |  |  |  |  |  |  |  |  | 8 | 9 | 5 | 32 | 24 |
| Montserrat | MSR | 131 |  |  |  |  |  |  |  |  |  |  |  | 105 | 21 |
| Mozambique | MOZ | 243 | 1 |  |  |  |  |  |  |  | 9 | 13 | 32 | 64 | 53 |
| México | MEX | 3,979 | 3 |  |  |  |  | 1 | 2 | 3 | 60 | 120 | 375 | 1,181 | 1,278 |
| Mónaco | MCO | 59 | 1 |  |  |  |  |  |  |  |  | 6 | 10 | 18 | 7 |
| Namibia | NAM | 137 |  |  |  |  |  |  |  |  | 3 |  | 8 | 41 | 29 |
| Nauru | NRU | 17 |  |  |  |  |  |  |  |  |  |  |  | 3 | 11 |
| Nepal | NPL | 86 |  |  |  |  |  |  |  | 1 | 3 | 2 | 1 | 20 | 30 |
| Nicaragua | NIC | 327 |  |  |  |  |  |  |  |  | 2 | 25 | 23 | 163 | 69 |
| Nigeria | NGA | 135 |  |  |  |  |  |  |  |  | 3 | 10 | 8 | 16 | 57 |
| Niue | NIU | 7 |  |  |  |  |  |  |  |  |  |  |  | 1 | 5 |
| Noruega | NOR | 1,268 | 1 |  |  |  |  |  | 1 | 2 | 20 | 54 | 99 | 377 | 63 |
| Nueva Caledonia | NCL | 21 |  |  |  |  |  |  |  |  |  |  | 3 | 5 | 6 |
| Nueva Zelanda | NZL | 452 | 2 |  |  | 1 |  |  |  |  | 1 | 3 | 24 | 236 | 80 |
| Níger | NER | 70 |  |  |  |  |  |  |  |  | 4 | 5 | 3 | 5 | 26 |
| Omán | OMN | 92 |  |  |  |  |  |  |  | 4 | 12 | 9 | 20 | 17 | 10 |
| PSX | PSX | 298 |  |  |  |  |  |  |  | 1 | 17 | 8 | 7 | 106 | 2 |
| Pakistán | PAK | 426 |  |  |  |  |  |  |  |  | 28 | 7 | 11 | 110 | 130 |
| Palaos | PLW | 55 |  |  |  |  |  |  |  |  | 1 | 1 | 10 | 12 | 20 |
| Palestina | PSE | 1,471 | 6 |  |  |  | 2 | 1 | 1 | 10 | 48 | 42 | 77 | 581 | 201 |
| Panamá | PAN | 391 |  |  |  |  |  |  |  |  | 2 | 48 | 50 | 87 | 114 |
| Papúa Nueva Guinea | PNG | 152 |  |  |  |  |  |  |  |  | 2 | 4 | 4 | 38 | 77 |
| Paraguay | PRY | 330 |  |  |  |  |  |  |  |  | 1 | 14 | 47 | 95 | 56 |
| Países Bajos | NLD | 19,272 | 2 |  | 5 |  |  |  | 1 | 1 | 110 | 497 | 639 | 515 | 1,033 |
| Perú | PER | 1,073 | 1 |  |  |  |  |  |  |  | 20 | 53 | 87 | 408 | 229 |
| Polinesia Francesa | PYF | 70 |  |  |  |  |  |  |  |  |  | 1 | 35 | 26 | 5 |
| Polonia | POL | 3,426 | 1 |  | 2 | 1 | 2 |  | 2 | 8 | 49 | 73 | 251 | 733 | 528 |
| Portugal | PRT | 2,861 | 3 |  |  |  |  | 1 | 1 | 9 | 59 | 140 | 505 | 1,079 | 222 |
| Puerto Rico | PRI | 1,079 |  |  |  |  |  |  |  | 1 | 1 | 18 | 71 | 40 | 906 |
| Reino Unido | GBR | 12,264 | 7 | 1 | 3 | 3 | 3 | 13 |  | 8 | 69 | 480 | 1,385 | 3,084 | 521 |
| República Centroafricana | CAF | 160 |  |  |  |  |  |  |  |  |  | 2 | 3 | 10 | 114 |
| República Checa | CZE | 1,285 | 2 |  |  |  |  |  |  | 1 | 18 | 35 | 77 | 230 | 229 |
| República Democrática del Congo | COD | 225 |  |  |  |  |  |  |  |  | 3 | 6 | 9 | 31 | 128 |
| República Dominicana | DOM | 249 |  |  |  |  |  |  |  |  | 4 | 25 | 67 | 46 | 58 |
| República Turca del Norte de Chipre | CYN | 15 |  |  |  |  |  |  |  |  | 2 | 5 |  |  |  |
| República de China | TWN | 195 |  |  |  |  |  |  |  |  | 2 | 17 | 9 | 49 | 80 |
| República del Congo | COG | 245 | 2 |  |  |  |  |  | 1 | 1 | 5 | 10 | 33 | 77 | 62 |
| Ruanda | RWA | 42 | 1 |  |  |  |  |  |  |  |  |  |  | 4 | 31 |
| Rumania | ROU | 1,142 |  |  |  |  |  |  |  | 3 | 42 | 29 | 52 | 191 | 200 |
| Rusia | RUS | 5,286 | 5 |  |  |  |  | 1 | 2 | 6 | 73 | 150 | 327 | 1,864 | 1,251 |
| SAH | SAH | 4 |  |  |  |  |  |  |  |  |  | 2 |  | 1 |  |
| SDS | SDS | 82 |  |  |  |  |  |  |  |  |  | 1 |  | 10 | 19 |
| Sahara Occidental | ESH | 35 |  |  |  |  |  |  | 1 |  |  | 2 | 1 | 16 | 13 |
| Samoa | WSM | 71 | 1 |  |  |  |  |  |  |  |  |  | 6 | 31 | 25 |
| Samoa Estadounidense | ASM | 26 |  |  |  |  |  |  |  |  |  |  |  | 14 | 7 |
| San Bartolomé | BLM | 6 |  |  |  |  |  |  |  |  |  |  | 3 | 2 |  |
| San Cristóbal y Nieves | KNA | 34 |  |  |  |  |  |  |  |  |  | 5 | 17 | 2 | 3 |
| San Marino | SMR | 8 |  |  | 1 |  |  |  |  |  |  | 1 | 1 | 1 | 2 |
| San Martín | MAF | 68 |  |  |  |  |  |  |  |  |  |  | 8 | 35 | 8 |
| San Martín | SXM | 33 |  |  |  |  |  |  |  | 1 |  |  | 6 | 17 | 3 |
| San Pedro y Miquelón | SPM | 8 |  |  |  |  |  |  |  |  |  |  | 1 | 5 | 1 |
| San Vicente y las Granadinas | VCT | 23 | 1 |  |  |  |  |  |  |  |  |  | 6 | 11 | 4 |
| Santa Lucía | LCA | 34 |  |  |  |  |  |  |  |  |  | 1 | 20 | 4 | 5 |
| Santo Tomé y Príncipe | STP | 28 |  |  |  | 1 |  |  |  |  |  | 10 | 10 | 4 | 1 |
| Senegal | SEN | 144 |  |  |  |  |  |  |  |  | 2 | 5 | 53 | 37 | 11 |
| Serbia | SRB | 535 |  |  |  |  |  |  |  | 4 | 26 | 16 | 32 | 143 | 73 |
| Seychelles | SYC | 3 |  |  |  |  |  |  |  |  |  |  |  | 3 |  |
| Sierra Leona | SLE | 169 |  |  |  |  |  |  |  | 1 | 2 | 10 | 20 | 17 | 98 |
| Singapur | SGP | 72 |  |  |  |  |  |  |  | 1 | 2 | 1 | 1 | 28 | 11 |
| Siria | SYR | 966 | 2 |  |  |  | 1 |  |  | 4 | 47 | 32 | 73 | 488 | 102 |
| Somalia | SOM | 192 |  |  |  |  |  |  |  | 1 | 11 | 7 | 6 | 20 | 103 |
| Somalilandia | SOL | 223 |  |  |  |  |  |  |  |  | 2 | 4 |  | 32 | 169 |
| Sri Lanka | LKA | 275 |  |  |  |  |  |  | 2 | 2 | 14 | 39 | 31 | 61 | 23 |
| Suazilandia | SWZ | 45 |  |  |  | 1 |  |  |  |  |  |  |  | 3 | 38 |
| Sudáfrica | ZAF | 738 | 5 |  |  |  |  | 1 |  |  | 6 | 28 | 45 | 280 | 170 |
| Sudán | SDN | 516 | 1 | 3 |  |  |  |  |  | 2 | 9 | 16 | 15 | 95 | 252 |
| Sudán del Sur | SSD | 202 |  |  |  |  |  |  |  |  | 1 | 4 | 2 | 17 | 89 |
| Suecia | SWE | 1,544 | 2 |  |  |  |  |  | 1 | 3 | 13 | 56 | 81 | 343 | 53 |
| Suiza | CHE | 2,480 | 3 |  |  |  |  | 1 | 1 | 4 | 57 | 62 | 150 | 509 | 163 |
| Surinam | SUR | 487 |  |  |  |  |  |  |  |  | 6 | 24 | 45 | 56 | 62 |
| Tailandia | THA | 236 | 1 |  |  |  |  |  | 2 | 1 | 9 | 15 | 22 | 66 | 58 |
| Tanzania | TZA | 215 | 1 |  |  |  |  |  |  |  | 4 | 2 | 3 | 51 | 85 |
| Tayikistán | TJK | 61 |  |  |  |  |  |  |  |  | 6 |  |  | 29 | 15 |
| Territorio Británico del Océano Índico | IOT | 1 |  |  |  |  |  |  |  |  |  |  |  |  | 1 |
| Territorios Australianos del Océano Índico | IOA | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Tierras Australes y Antárticas Francesas | ATF | 4 |  |  |  |  |  |  |  |  |  |  |  | 1 |  |
| Timor Oriental | TLS | 15 |  |  |  |  |  |  |  |  |  |  |  |  | 2 |
| Togo | TGO | 52 |  |  |  |  |  |  |  |  | 1 | 1 | 2 | 7 | 15 |
| Tonga | TON | 46 |  |  |  |  |  |  |  |  |  | 4 | 7 | 13 | 10 |
| Trinidad y Tobago | TTO | 102 |  |  |  |  |  |  |  |  | 1 | 19 | 35 | 12 | 32 |
| Turkmenistán | TKM | 128 |  |  |  |  |  |  |  |  | 14 | 6 | 4 | 49 | 20 |
| Turquía | TUR | 2,283 | 13 |  |  | 1 |  | 1 | 7 | 8 | 97 | 111 | 232 | 818 | 304 |
| Tuvalu | TUV | 14 |  |  |  |  |  |  |  |  |  |  |  | 8 | 4 |
| Túnez | TUN | 568 | 3 |  |  |  |  | 1 | 1 | 2 | 32 | 10 | 23 | 202 | 169 |
| UMI | UMI | 2 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |
| USG | USG | 3 |  |  |  |  |  |  |  |  |  |  | 1 | 1 |  |
| Ucrania | UKR | 780 | 1 |  |  |  |  |  | 4 | 4 | 32 | 70 | 64 | 98 | 97 |
| Uganda | UGA | 248 |  |  |  |  |  |  |  |  | 1 | 3 | 3 | 15 | 192 |
| Uruguay | URY | 354 |  |  |  |  |  |  |  |  | 3 | 22 | 52 | 121 | 69 |
| Uzbekistán | UZB | 125 |  |  |  |  |  |  |  |  | 7 | 6 | 5 | 57 | 31 |
| Vanuatu | VUT | 15 |  |  |  |  |  |  |  |  |  |  |  | 2 | 13 |
| Venezuela | VEN | 535 |  |  |  |  |  |  |  | 1 | 11 | 83 | 115 | 112 | 76 |
| Vietnam | VNM | 338 |  |  |  |  |  |  |  | 2 | 8 | 5 | 17 | 50 | 83 |
| Yemen | YEM | 426 |  |  |  |  |  |  |  | 5 | 23 | 14 | 16 | 42 | 276 |
| Yibuti | DJI | 57 |  |  |  |  |  |  |  |  | 2 | 2 | 3 | 27 | 20 |
| Zambia | ZMB | 105 |  |  |  |  |  |  |  |  | 1 | 3 | 4 | 20 | 45 |
| Zimbabue | ZWE | 110 |  |  |  |  |  |  |  |  | 2 | 1 | 6 | 26 | 43 |
| Åland | ALA | 6 |  |  |  |  |  |  |  |  |  |  |  | 3 |  |
