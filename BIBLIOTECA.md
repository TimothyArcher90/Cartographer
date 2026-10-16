# Biblioteca de Cartographer

Documento generado por `scripts/comprender.py`. No editar a mano.

- Mapas analizados: **690,064** · con país asignado: **446,818** · sin país: 243,246
  (sobre todo mapamundis, cartas oceánicas o registros sin datos de lugar).
- Países con mapas: **243**.
- Tipos: general 437,390, topográfico 201,676, plano urbano 23,300, militar 8,358, histórico/temático 6,634, mapamundi 4,440, ferroviario/viario 4,397, carta náutica 3,262, portulano 446, ptolemaico 161.
- Escalas: desconocida 420,268, local o ciudad 245,025, provincia o comarca 14,152, región o país 6,100, continente 2,997, mundo 1,522.

Cómo se asigna un país: por **nombre** actual (25+ idiomas, Natural Earth), por **nombre histórico**
(`catalogo/nombres_historicos.json`) o por **coordenadas** de la cobertura del mapa. Cada mapa guarda
la vía en el campo `via`; las asignaciones por coordenadas de mapas grandes pueden incluir países
vecinos. Los siglos salen del año de los metadatos de cada archivo y pueden tener errores puntuales.

Mapas de un país: `catalogo/biblioteca/paises/<ISO3>.jsonl.gz` o
`python scripts/buscar_lugar.py "<país>"`.

| País | ISO | Total | Antes del s. IX | IX | X | XI | XII | XIII | XIV | XV | XVI | XVII | XVIII | XIX | XX |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Afganistán | AFG | 365 |  |  |  |  |  |  |  |  | 19 | 6 | 9 | 142 | 100 |
| Albania | ALB | 259 |  |  |  |  |  |  | 1 | 3 | 21 | 22 | 19 | 63 | 47 |
| Alemania | DEU | 12,784 | 1 |  |  |  |  |  |  | 4 | 95 | 207 | 334 | 1,340 | 814 |
| Andorra | AND | 27 |  |  |  |  |  |  |  |  |  |  | 1 | 2 | 18 |
| Angola | AGO | 188 |  |  |  |  |  |  |  |  | 2 | 9 | 13 | 48 | 88 |
| Anguila | AIA | 7 |  |  |  |  |  |  |  |  |  |  | 6 | 1 |  |
| Antigua y Barbuda | ATG | 26 |  |  |  |  |  |  |  |  |  | 1 | 13 | 10 | 1 |
| Antártida | ATA | 86 |  |  |  |  |  |  |  |  |  | 8 | 11 | 9 | 48 |
| Arabia Saudita | SAU | 474 |  |  |  |  |  |  |  | 6 | 44 | 31 | 51 | 134 | 115 |
| Argelia | DZA | 387 |  |  |  |  |  |  |  | 2 | 19 | 21 | 33 | 99 | 101 |
| Argentina | ARG | 746 |  |  |  |  |  |  |  |  | 5 | 98 | 95 | 124 | 351 |
| Armenia | ARM | 139 |  |  |  |  |  |  | 1 | 1 | 10 | 7 | 14 | 61 | 21 |
| Aruba | ABW | 22 |  |  |  |  |  |  |  |  |  |  | 2 | 6 | 4 |
| Australia | AUS | 1,944 |  |  |  |  |  |  |  |  | 1 | 7 | 18 | 270 | 60 |
| Austria | AUT | 1,563 | 1 |  |  |  |  |  |  | 2 | 36 | 36 | 63 | 373 | 248 |
| Azerbaiyán | AZE | 94 |  |  |  |  |  |  |  | 1 | 8 | 4 | 5 | 30 | 22 |
| Bahamas | BHS | 125 |  |  |  |  |  |  |  |  |  | 4 | 51 | 49 | 16 |
| Bangladés | BGD | 53 |  |  |  |  |  |  |  | 1 | 3 | 5 | 4 | 7 | 8 |
| Barbados | BRB | 84 |  |  |  |  |  |  |  |  |  | 6 | 33 | 6 | 23 |
| Baréin | BHR | 63 |  |  |  |  |  |  |  | 2 | 6 | 6 | 9 | 14 | 16 |
| Belice | BLZ | 67 |  |  |  |  |  |  |  |  |  | 9 | 5 | 15 | 34 |
| Benín | BEN | 47 |  |  |  |  |  |  |  |  | 3 | 6 |  | 2 | 16 |
| Bermudas | BMU | 78 |  |  |  |  |  |  |  |  |  | 11 | 30 | 22 | 8 |
| Bielorrusia | BLR | 243 |  |  |  |  |  |  |  | 3 | 22 | 19 | 25 | 22 | 54 |
| Birmania | MMR | 151 |  |  |  |  |  |  |  |  | 8 | 5 | 14 | 38 | 37 |
| Bolivia | BOL | 192 |  |  |  |  |  |  |  |  | 4 | 15 | 9 | 66 | 72 |
| Bosnia y Herzegovina | BIH | 433 |  |  |  |  |  |  |  | 6 | 37 | 13 | 21 | 101 | 64 |
| Botsuana | BWA | 157 |  |  |  |  |  |  |  |  | 1 |  | 5 | 46 | 55 |
| Brasil | BRA | 1,544 |  |  |  |  |  |  |  | 3 | 15 | 191 | 239 | 459 | 417 |
| Brunéi | BRN | 17 |  |  |  |  |  |  |  |  |  |  |  | 6 | 4 |
| Bulgaria | BGR | 400 |  |  |  |  |  |  | 1 | 2 | 21 | 19 | 42 | 121 | 70 |
| Burkina Faso | BFA | 54 |  |  |  |  |  |  |  |  | 1 | 5 | 3 | 7 | 13 |
| Burundi | BDI | 37 |  |  |  |  |  |  |  |  |  |  |  | 3 | 30 |
| Bután | BTN | 38 |  |  |  |  |  |  |  |  |  |  | 1 | 9 | 11 |
| Bélgica | BEL | 4,648 |  |  |  |  |  |  |  | 2 | 51 | 136 | 339 | 360 | 270 |
| Cabo Verde | CPV | 93 |  |  |  |  |  |  |  |  | 3 | 15 | 37 | 21 | 3 |
| Camboya | KHM | 92 |  |  |  |  |  |  |  |  | 1 | 1 | 1 | 10 | 47 |
| Camerún | CMR | 97 |  |  |  |  |  |  |  |  | 1 | 4 | 8 | 9 | 43 |
| Canadá | CAN | 5,285 |  |  |  |  |  |  |  |  | 12 | 80 | 1,305 | 1,530 | 1,550 |
| Catar | QAT | 55 |  |  |  |  |  |  |  | 3 | 8 | 7 | 11 | 13 | 10 |
| Chad | TCD | 67 |  |  |  |  |  |  |  |  |  | 3 | 4 | 10 | 29 |
| Chile | CHL | 589 |  |  |  |  |  |  |  | 2 | 4 | 108 | 134 | 157 | 127 |
| China | CHN | 3,439 |  |  |  |  | 8 | 1 | 2 | 4 | 33 | 96 | 334 | 1,385 | 1,100 |
| Chipre | CYP | 177 |  |  |  |  |  |  |  | 1 | 10 | 13 | 11 | 18 | 91 |
| Ciudad del Vaticano | VAT | 38 |  |  |  |  |  |  |  |  |  | 24 | 1 | 3 | 3 |
| Colombia | COL | 492 |  |  |  |  |  |  |  |  | 10 | 55 | 101 | 103 | 141 |
| Comoras | COM | 9 |  |  |  |  |  |  |  |  |  |  |  | 2 | 7 |
| Corea del Norte | PRK | 134 |  |  |  |  |  |  |  |  | 1 | 9 | 11 | 13 | 54 |
| Corea del Sur | KOR | 722 |  |  |  |  |  |  |  |  | 2 | 12 | 50 | 116 | 195 |
| Costa Rica | CRI | 169 |  |  |  |  |  |  |  |  |  | 14 | 15 | 39 | 89 |
| Costa de Marfil | CIV | 83 |  |  |  |  |  |  |  |  | 2 | 5 | 9 | 10 | 25 |
| Croacia | HRV | 734 |  |  |  |  |  |  |  | 6 | 41 | 18 | 34 | 188 | 69 |
| Cuba | CUB | 960 |  |  |  |  |  |  |  | 1 | 6 | 99 | 215 | 261 | 241 |
| Curazao | CUW | 81 |  |  |  |  |  |  |  |  |  |  | 19 | 10 | 2 |
| Dinamarca | DNK | 1,039 |  |  |  |  |  |  | 1 |  | 9 | 47 | 47 | 275 | 69 |
| Dominica | DMA | 15 |  |  |  |  |  |  |  |  |  |  | 12 | 2 |  |
| ESB | ESB | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ecuador | ECU | 251 |  |  |  |  |  |  |  |  | 7 | 19 | 36 | 65 | 85 |
| Egipto | EGY | 1,892 |  |  |  |  | 1 | 1 |  | 3 | 43 | 39 | 114 | 758 | 748 |
| El Salvador | SLV | 109 |  |  |  |  |  |  |  |  |  | 1 | 3 | 44 | 54 |
| Emiratos Árabes Unidos | ARE | 53 |  |  |  |  |  |  |  | 3 | 7 | 6 | 12 | 13 | 6 |
| Eritrea | ERI | 398 |  |  |  |  |  |  |  |  | 1 | 6 | 7 | 99 | 260 |
| Eslovaquia | SVK | 490 |  |  |  |  |  |  |  | 2 | 16 | 13 | 19 | 94 | 97 |
| Eslovenia | SVN | 300 |  |  |  |  |  |  |  | 2 | 20 | 6 | 3 | 15 | 106 |
| España | ESP | 6,888 | 6 |  |  |  | 1 | 1 | 6 | 13 | 94 | 285 | 1,364 | 2,638 | 890 |
| Estados Federados de Micronesia | FSM | 44 |  |  |  |  |  |  |  |  |  | 1 | 1 | 11 | 25 |
| Estados Unidos | USA | 342,956 | 2 |  |  |  |  |  |  | 2 | 26 | 516 | 4,940 | 97,832 | 208,185 |
| Estonia | EST | 954 |  |  |  |  |  |  |  |  | 2 | 11 | 14 | 79 | 489 |
| Etiopía | ETH | 420 |  |  |  |  |  | 1 |  | 1 | 10 | 15 | 12 | 104 | 202 |
| Filipinas | PHL | 365 |  |  |  |  |  |  |  |  | 4 | 5 | 56 | 72 | 179 |
| Finlandia | FIN | 201 |  |  |  |  |  |  |  | 1 | 8 | 15 | 18 | 32 | 29 |
| Fiyi | FJI | 43 |  |  |  |  |  |  |  |  |  | 1 |  | 29 | 10 |
| Francia | FRA | 11,907 |  |  |  |  | 1 | 1 | 1 | 2 | 135 | 468 | 1,487 | 3,923 | 613 |
| GIB | GIB | 5 |  |  |  |  |  |  |  |  |  |  | 5 |  |  |
| Gabón | GAB | 55 |  |  |  |  |  |  |  |  | 1 | 5 | 7 | 6 | 12 |
| Gambia | GMB | 27 |  |  |  |  |  |  |  |  |  | 2 | 11 | 9 | 4 |
| Georgia | GEO | 230 |  |  |  |  |  |  |  | 1 | 11 | 4 | 48 | 60 | 40 |
| Ghana | GHA | 81 |  |  |  |  |  |  |  |  | 2 | 7 | 7 | 8 | 19 |
| Granada | GRD | 333 |  |  |  |  |  |  |  |  |  | 19 | 59 | 207 | 27 |
| Grecia | GRC | 1,269 |  |  |  |  |  |  |  | 3 | 72 | 92 | 88 | 505 | 176 |
| Groenlandia | GRL | 148 |  |  |  |  |  |  | 1 |  | 4 | 11 | 31 | 74 | 13 |
| Guam | GUM | 24 |  |  |  |  |  |  |  |  |  |  | 4 | 6 | 3 |
| Guatemala | GTM | 152 |  |  |  |  |  |  |  |  | 2 | 15 | 10 | 38 | 72 |
| Guernsey | GGY | 217 |  |  |  |  |  |  |  |  |  | 4 |  | 102 | 109 |
| Guinea | GIN | 84 |  |  |  |  |  |  |  |  | 1 | 11 | 32 | 10 | 12 |
| Guinea Ecuatorial | GNQ | 38 |  |  |  |  |  |  |  |  | 1 |  | 2 | 11 | 18 |
| Guinea-Bisáu | GNB | 6 |  |  |  |  |  |  |  |  |  |  | 2 | 2 | 2 |
| Guyana | GUY | 237 |  |  |  |  |  |  |  |  | 3 | 20 | 30 | 44 | 50 |
| Haití | HTI | 341 |  |  |  |  |  |  |  |  | 3 | 17 | 102 | 60 | 118 |
| Honduras | HND | 231 |  |  |  |  |  |  |  |  |  | 26 | 47 | 60 | 81 |
| Hong Kong | HKG | 43 |  |  |  |  |  |  |  |  |  |  |  | 21 | 12 |
| Hungría | HUN | 993 |  |  |  |  |  |  |  | 3 | 38 | 28 | 66 | 282 | 102 |
| India | IND | 1,423 |  |  |  |  |  |  | 5 | 2 | 59 | 40 | 155 | 555 | 148 |
| Indonesia | IDN | 1,426 | 1 |  |  |  |  |  | 1 |  | 13 | 117 | 71 | 174 | 213 |
| Irak | IRQ | 484 |  |  |  |  | 1 |  |  | 3 | 30 | 23 | 25 | 92 | 139 |
| Irlanda | IRL | 1,561 |  |  |  |  |  |  |  | 1 | 28 | 65 | 99 | 573 | 31 |
| Irán | IRN | 435 |  |  |  |  |  |  |  | 5 | 38 | 17 | 61 | 158 | 68 |
| Isla Norfolk | NFK | 1,151 |  |  |  |  |  |  |  |  |  | 1 | 33 | 915 | 196 |
| Isla Santa Elena | SHN | 50 |  |  |  |  |  |  |  |  | 1 | 2 | 5 | 30 | 5 |
| Isla de Man | IMN | 29 |  |  |  |  |  |  |  |  |  |  | 2 | 19 |  |
| Islandia | ISL | 103 |  |  |  |  |  |  |  |  | 3 | 8 | 10 | 38 | 18 |
| Islas Caimán | CYM | 9 |  |  |  |  |  |  |  |  |  |  | 1 | 1 | 7 |
| Islas Feroe | FRO | 4 |  |  |  |  |  |  |  |  |  | 1 | 1 | 2 |  |
| Islas Georgias del Sur y Sandwich del Sur | SGS | 2 |  |  |  |  |  |  |  |  |  |  |  |  | 1 |
| Islas Malvinas | FLK | 33 |  |  |  |  |  |  |  |  |  | 11 | 10 | 6 | 3 |
| Islas Marianas del Norte | MNP | 25 |  |  |  |  |  |  |  |  |  |  |  | 2 | 20 |
| Islas Marshall | MHL | 17 |  |  |  |  |  |  |  |  |  |  |  | 3 | 14 |
| Islas Pitcairn | PCN | 10 |  |  |  |  |  |  |  |  |  |  | 1 | 1 | 8 |
| Islas Salomón | SLB | 33 |  |  |  |  |  |  |  |  | 1 | 2 | 1 | 5 | 10 |
| Islas Turcas y Caicos | TCA | 6 |  |  |  |  |  |  |  |  |  |  | 2 | 2 | 2 |
| Islas Vírgenes Británicas | VGB | 9 |  |  |  |  |  |  |  |  |  |  | 3 | 1 | 5 |
| Islas Vírgenes de los Estados Unidos | VIR | 101 |  |  |  |  |  |  |  |  |  | 1 | 49 | 2 | 44 |
| Israel | ISR | 1,230 |  |  |  |  |  | 1 | 1 | 9 | 51 | 61 | 154 | 426 | 109 |
| Italia | ITA | 4,614 | 2 |  |  |  | 1 | 1 |  | 10 | 189 | 337 | 305 | 1,168 | 357 |
| Jamaica | JAM | 744 |  |  |  |  |  |  |  | 1 | 1 | 15 | 115 | 543 | 46 |
| Japón | JPN | 1,103 |  |  |  |  |  |  |  | 1 | 4 | 41 | 129 | 291 | 225 |
| Jersey | JEY | 13 |  |  |  |  |  |  |  |  |  | 4 |  | 8 |  |
| Jordania | JOR | 380 |  |  |  |  |  |  |  | 1 | 37 | 18 | 22 | 148 | 27 |
| Kazajistán | KAZ | 111 |  |  |  |  |  |  |  | 1 | 15 | 15 | 4 | 22 | 22 |
| Kenia | KEN | 213 |  |  |  |  |  |  |  |  | 1 | 4 | 1 | 21 | 147 |
| Kirguistán | KGZ | 42 |  |  |  |  |  |  |  |  | 7 | 2 |  | 15 | 10 |
| Kiribati | KIR | 22 |  |  |  |  |  |  |  |  |  |  |  | 14 | 8 |
| Kosovo | KOS | 47 |  |  |  |  |  |  |  |  | 1 | 2 | 2 |  | 24 |
| Kuwait | KWT | 67 |  |  |  |  |  |  |  | 3 | 7 | 5 | 12 | 12 | 13 |
| Laos | LAO | 63 |  |  |  |  |  |  |  | 1 | 3 |  |  | 8 | 16 |
| Lesoto | LSO | 90 |  |  |  |  |  |  |  |  |  |  | 1 | 12 | 72 |
| Letonia | LVA | 191 |  |  |  |  |  |  |  | 2 | 11 | 11 | 11 | 18 | 75 |
| Liberia | LBR | 129 |  |  |  |  |  |  |  |  | 1 | 2 | 4 | 66 | 38 |
| Libia | LBY | 258 |  |  |  |  |  |  |  | 6 | 21 | 17 | 11 | 32 | 98 |
| Liechtenstein | LIE | 12 |  |  |  |  |  |  |  | 1 |  | 1 |  | 2 |  |
| Lituania | LTU | 276 |  |  |  |  |  |  |  | 2 | 11 | 14 | 41 | 20 | 48 |
| Luxemburgo | LUX | 272 |  |  |  |  |  |  |  |  | 6 | 22 | 43 | 35 | 19 |
| Líbano | LBN | 652 |  |  |  |  |  |  |  | 1 | 17 | 6 | 14 | 444 | 105 |
| Macao | MAC | 69 |  |  |  |  |  |  |  |  |  | 1 | 13 | 14 | 31 |
| Macedonia del Norte | MKD | 115 |  |  |  |  |  |  |  | 2 | 13 | 11 | 5 | 19 | 24 |
| Madagascar | MDG | 152 |  |  |  |  |  |  |  |  | 3 | 9 | 25 | 41 | 36 |
| Malasia | MYS | 202 |  |  |  |  |  |  |  |  | 4 | 5 | 5 | 22 | 33 |
| Malaui | MWI | 34 |  |  |  |  |  |  |  |  | 1 |  | 2 | 13 | 14 |
| Maldivas | MDV | 12 |  |  |  |  |  |  |  |  |  |  | 4 |  | 7 |
| Malta | MLT | 147 |  |  |  |  |  |  |  |  | 10 | 15 | 64 | 30 | 6 |
| Malí | MLI | 94 |  |  |  |  |  |  | 1 |  | 2 | 5 | 7 | 12 | 17 |
| Marruecos | MAR | 411 |  |  |  |  |  |  |  | 1 | 10 | 32 | 55 | 96 | 114 |
| Mauricio | MUS | 71 |  |  |  |  |  |  |  |  |  | 1 | 8 | 21 | 9 |
| Mauritania | MRT | 73 |  |  |  |  |  |  |  |  | 5 | 3 | 12 | 12 | 14 |
| Moldavia | MDA | 109 |  |  |  |  |  |  |  | 1 | 5 | 8 | 18 | 25 | 10 |
| Mongolia | MNG | 93 |  |  |  |  |  |  |  |  | 1 | 9 | 4 | 29 | 36 |
| Montenegro | MNE | 92 |  |  |  |  |  |  |  |  | 8 | 8 | 5 | 21 | 13 |
| Montserrat | MSR | 130 |  |  |  |  |  |  |  |  |  |  |  | 105 | 21 |
| Mozambique | MOZ | 173 |  |  |  |  |  |  |  |  | 4 | 6 | 15 | 52 | 43 |
| México | MEX | 3,023 |  |  |  |  |  |  |  | 3 | 52 | 103 | 305 | 868 | 1,202 |
| Mónaco | MCO | 8 |  |  |  |  |  |  |  |  |  |  | 3 | 1 | 3 |
| Namibia | NAM | 131 |  |  |  |  |  |  |  |  | 2 |  | 6 | 41 | 28 |
| Nauru | NRU | 5 |  |  |  |  |  |  |  |  |  |  |  |  | 5 |
| Nepal | NPL | 45 |  |  |  |  |  |  |  | 1 | 2 | 2 |  | 8 | 14 |
| Nicaragua | NIC | 238 |  |  |  |  |  |  |  |  |  | 24 | 22 | 110 | 67 |
| Nigeria | NGA | 117 |  |  |  |  |  |  |  |  | 2 | 8 | 7 | 8 | 52 |
| Noruega | NOR | 830 |  |  |  |  |  |  |  | 2 | 5 | 19 | 24 | 265 | 26 |
| Nueva Caledonia | NCL | 9 |  |  |  |  |  |  |  |  |  |  | 1 | 3 | 5 |
| Nueva Zelanda | NZL | 193 |  |  |  |  |  |  |  |  |  |  | 3 | 132 | 19 |
| Níger | NER | 70 |  |  |  |  |  |  |  |  | 4 | 5 | 3 | 5 | 26 |
| Omán | OMN | 75 |  |  |  |  |  |  |  | 4 | 12 | 6 | 13 | 16 | 9 |
| PSX | PSX | 298 |  |  |  |  |  |  |  | 1 | 17 | 8 | 7 | 106 | 2 |
| Pakistán | PAK | 378 |  |  |  |  |  |  |  |  | 26 | 7 | 10 | 99 | 116 |
| Palaos | PLW | 40 |  |  |  |  |  |  |  |  |  | 1 | 2 | 9 | 19 |
| Palestina | PSE | 992 |  |  |  |  |  |  |  | 6 | 40 | 31 | 64 | 487 | 114 |
| Panamá | PAN | 304 |  |  |  |  |  |  |  |  | 2 | 42 | 44 | 73 | 99 |
| Papúa Nueva Guinea | PNG | 65 |  |  |  |  |  |  |  |  | 1 | 4 | 2 | 14 | 33 |
| Paraguay | PRY | 190 |  |  |  |  |  |  |  |  |  | 12 | 38 | 64 | 56 |
| Países Bajos | NLD | 18,102 |  |  | 1 |  |  |  |  | 1 | 93 | 349 | 450 | 401 | 962 |
| Perú | PER | 688 |  |  |  |  |  |  |  |  | 17 | 45 | 65 | 287 | 216 |
| Polinesia Francesa | PYF | 69 |  |  |  |  |  |  |  |  |  | 1 | 35 | 26 | 5 |
| Polonia | POL | 2,689 |  |  |  |  |  |  | 1 | 6 | 40 | 52 | 155 | 525 | 448 |
| Portugal | PRT | 2,416 | 1 |  |  |  |  |  |  | 2 | 48 | 129 | 461 | 970 | 204 |
| Puerto Rico | PRI | 1,040 |  |  |  |  |  |  |  | 1 |  | 10 | 70 | 38 | 897 |
| Reino Unido | GBR | 8,231 |  |  |  |  | 2 | 8 |  | 1 | 54 | 428 | 644 | 2,185 | 432 |
| República Centroafricana | CAF | 155 |  |  |  |  |  |  |  |  |  | 2 | 3 | 8 | 112 |
| República Checa | CZE | 1,089 |  |  |  |  |  |  |  | 1 | 16 | 31 | 57 | 189 | 213 |
| República Democrática del Congo | COD | 224 |  |  |  |  |  |  |  |  | 3 | 6 | 9 | 31 | 128 |
| República Dominicana | DOM | 222 |  |  |  |  |  |  |  |  | 3 | 21 | 65 | 45 | 49 |
| República Turca del Norte de Chipre | CYN | 15 |  |  |  |  |  |  |  |  | 2 | 5 |  |  |  |
| República de China | TWN | 138 |  |  |  |  |  |  |  |  | 1 | 8 | 2 | 41 | 53 |
| República del Congo | COG | 150 |  |  |  |  |  |  |  | 1 | 1 | 5 | 16 | 43 | 49 |
| Ruanda | RWA | 24 |  |  |  |  |  |  |  |  |  |  |  | 3 | 17 |
| Rumania | ROU | 1,017 |  |  |  |  |  |  |  | 3 | 37 | 21 | 41 | 160 | 172 |
| Rusia | RUS | 3,991 |  |  |  |  |  |  |  | 5 | 59 | 106 | 229 | 1,551 | 1,096 |
| SAH | SAH | 4 |  |  |  |  |  |  |  |  |  | 2 |  | 1 |  |
| SDS | SDS | 82 |  |  |  |  |  |  |  |  |  | 1 |  | 10 | 19 |
| Sahara Occidental | ESH | 18 |  |  |  |  |  |  | 1 |  |  | 2 |  | 9 | 5 |
| Samoa | WSM | 33 |  |  |  |  |  |  |  |  |  |  | 3 | 21 | 9 |
| Samoa Estadounidense | ASM | 24 |  |  |  |  |  |  |  |  |  |  |  | 13 | 6 |
| San Bartolomé | BLM | 5 |  |  |  |  |  |  |  |  |  |  | 3 | 2 |  |
| San Cristóbal y Nieves | KNA | 18 |  |  |  |  |  |  |  |  |  | 2 | 12 | 1 | 3 |
| San Marino | SMR | 2 |  |  |  |  |  |  |  |  |  |  |  | 1 | 1 |
| San Martín | MAF | 30 |  |  |  |  |  |  |  |  |  |  | 5 | 16 | 6 |
| San Martín | SXM | 17 |  |  |  |  |  |  |  | 1 |  |  | 4 | 8 | 1 |
| San Pedro y Miquelón | SPM | 7 |  |  |  |  |  |  |  |  |  |  | 1 | 5 | 1 |
| San Vicente y las Granadinas | VCT | 19 |  |  |  |  |  |  |  |  |  |  | 6 | 10 | 3 |
| Santa Lucía | LCA | 26 |  |  |  |  |  |  |  |  |  | 1 | 17 | 4 | 4 |
| Santo Tomé y Príncipe | STP | 10 |  |  |  |  |  |  |  |  |  | 1 | 8 |  | 1 |
| Senegal | SEN | 79 |  |  |  |  |  |  |  |  | 1 | 3 | 27 | 19 | 10 |
| Serbia | SRB | 468 |  |  |  |  |  |  |  | 4 | 26 | 14 | 27 | 126 | 58 |
| Seychelles | SYC | 2 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |
| Sierra Leona | SLE | 69 |  |  |  |  |  |  |  |  | 1 | 3 | 9 | 14 | 37 |
| Singapur | SGP | 33 |  |  |  |  |  |  |  |  |  |  | 1 | 18 | 4 |
| Siria | SYR | 723 |  |  |  |  |  |  |  | 4 | 41 | 31 | 57 | 366 | 79 |
| Somalia | SOM | 154 |  |  |  |  |  |  |  |  | 7 | 7 | 4 | 14 | 96 |
| Somalilandia | SOL | 72 |  |  |  |  |  |  |  |  | 2 | 4 |  | 31 | 22 |
| Sri Lanka | LKA | 162 |  |  |  |  |  |  | 2 | 1 | 8 | 12 | 16 | 48 | 18 |
| Suazilandia | SWZ | 38 |  |  |  |  |  |  |  |  |  |  |  | 3 | 33 |
| Sudáfrica | ZAF | 526 |  |  |  |  |  |  |  |  | 2 | 3 | 22 | 217 | 148 |
| Sudán | SDN | 344 |  |  |  |  |  |  |  | 2 | 8 | 15 | 12 | 78 | 138 |
| Sudán del Sur | SSD | 200 |  |  |  |  |  |  |  |  | 1 | 4 | 2 | 17 | 89 |
| Suecia | SWE | 1,147 |  |  |  |  |  |  |  | 2 | 13 | 31 | 44 | 245 | 35 |
| Suiza | CHE | 1,922 | 1 |  |  |  |  |  |  | 3 | 41 | 49 | 89 | 347 | 136 |
| Surinam | SUR | 361 |  |  |  |  |  |  |  |  | 3 | 14 | 23 | 17 | 28 |
| Tailandia | THA | 137 |  |  |  |  |  |  |  |  | 5 | 3 | 11 | 47 | 32 |
| Tanzania | TZA | 195 |  |  |  |  |  |  |  |  | 2 | 2 | 2 | 48 | 79 |
| Tayikistán | TJK | 45 |  |  |  |  |  |  |  |  | 6 |  |  | 20 | 11 |
| Territorio Británico del Océano Índico | IOT | 1 |  |  |  |  |  |  |  |  |  |  |  |  | 1 |
| Territorios Australianos del Océano Índico | IOA | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Tierras Australes y Antárticas Francesas | ATF | 4 |  |  |  |  |  |  |  |  |  |  |  | 1 |  |
| Timor Oriental | TLS | 15 |  |  |  |  |  |  |  |  |  |  |  |  | 2 |
| Togo | TGO | 26 |  |  |  |  |  |  |  |  |  | 1 | 2 | 2 | 8 |
| Tonga | TON | 10 |  |  |  |  |  |  |  |  |  | 1 | 1 | 5 | 2 |
| Trinidad y Tobago | TTO | 58 |  |  |  |  |  |  |  |  |  | 12 | 21 | 6 | 18 |
| Turkmenistán | TKM | 102 |  |  |  |  |  |  |  |  | 14 | 5 | 3 | 46 | 16 |
| Turquía | TUR | 1,285 |  |  |  |  |  |  | 1 | 3 | 59 | 56 | 119 | 525 | 186 |
| Tuvalu | TUV | 6 |  |  |  |  |  |  |  |  |  |  |  | 5 | 1 |
| Túnez | TUN | 410 |  |  |  |  |  |  |  | 2 | 25 | 6 | 14 | 163 | 136 |
| UMI | UMI | 2 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |
| USG | USG | 3 |  |  |  |  |  |  |  |  |  |  | 1 | 1 |  |
| Ucrania | UKR | 672 |  |  |  |  |  |  | 2 | 4 | 29 | 48 | 48 | 85 | 76 |
| Uganda | UGA | 186 |  |  |  |  |  |  |  |  | 1 | 3 | 3 | 14 | 138 |
| Uruguay | URY | 250 |  |  |  |  |  |  |  |  | 1 | 22 | 44 | 90 | 63 |
| Uzbekistán | UZB | 92 |  |  |  |  |  |  |  |  | 7 | 4 | 2 | 48 | 16 |
| Vanuatu | VUT | 6 |  |  |  |  |  |  |  |  |  |  |  | 2 | 4 |
| Venezuela | VEN | 405 |  |  |  |  |  |  |  |  | 9 | 67 | 104 | 82 | 72 |
| Vietnam | VNM | 227 |  |  |  |  |  |  |  | 1 | 4 | 3 | 4 | 24 | 43 |
| Yemen | YEM | 354 |  |  |  |  |  |  |  | 4 | 16 | 11 | 14 | 35 | 238 |
| Yibuti | DJI | 49 |  |  |  |  |  |  |  |  | 2 | 2 | 3 | 26 | 14 |
| Zambia | ZMB | 97 |  |  |  |  |  |  |  |  | 1 | 3 | 4 | 19 | 45 |
| Zimbabue | ZWE | 103 |  |  |  |  |  |  |  |  | 2 | 1 | 5 | 25 | 43 |
| Åland | ALA | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |
