# Biblioteca de Cartographer

Documento generado por `scripts/comprender.py`. No editar a mano.

- Mapas analizados: **566,754** · con país asignado: **403,382** · sin país: 163,372
  (sobre todo mapamundis, cartas oceánicas o registros sin datos de lugar).
- Países con mapas: **243**.
- Tipos: general 314,805, topográfico 201,529, plano urbano 23,211, militar 8,258, histórico/temático 6,522, ferroviario/viario 4,345, mapamundi 4,229, carta náutica 3,249, portulano 445, ptolemaico 161.
- Escalas: desconocida 296,958, local o ciudad 245,025, provincia o comarca 14,152, región o país 6,100, continente 2,997, mundo 1,522.

Cómo se asigna un país: por **nombre** actual (25+ idiomas, Natural Earth), por **nombre histórico**
(`catalogo/nombres_historicos.json`) o por **coordenadas** de la cobertura del mapa. Cada mapa guarda
la vía en el campo `via`; las asignaciones por coordenadas de mapas grandes pueden incluir países
vecinos. Los siglos salen del año de los metadatos de cada archivo y pueden tener errores puntuales.

Mapas de un país: `catalogo/biblioteca/paises/<ISO3>.jsonl.gz` o
`python scripts/buscar_lugar.py "<país>"`.

| País | ISO | Total | Antes del s. IX | IX | X | XI | XII | XIII | XIV | XV | XVI | XVII | XVIII | XIX | XX |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Afganistán | AFG | 357 |  |  |  |  |  |  |  |  | 19 | 6 | 9 | 142 | 94 |
| Albania | ALB | 256 |  |  |  |  |  |  |  | 2 | 21 | 22 | 19 | 63 | 46 |
| Alemania | DEU | 12,661 | 1 |  |  |  |  |  |  | 4 | 95 | 207 | 334 | 1,272 | 761 |
| Andorra | AND | 27 |  |  |  |  |  |  |  |  |  |  | 1 | 2 | 18 |
| Angola | AGO | 184 |  |  |  |  |  |  |  |  | 2 | 9 | 13 | 48 | 84 |
| Anguila | AIA | 7 |  |  |  |  |  |  |  |  |  |  | 6 | 1 |  |
| Antigua y Barbuda | ATG | 26 |  |  |  |  |  |  |  |  |  | 1 | 13 | 10 | 1 |
| Antártida | ATA | 81 |  |  |  |  |  |  |  |  |  | 8 | 11 | 9 | 45 |
| Arabia Saudita | SAU | 453 |  |  |  |  |  |  |  | 6 | 44 | 31 | 51 | 116 | 113 |
| Argelia | DZA | 324 |  |  |  |  |  |  |  | 2 | 19 | 21 | 33 | 87 | 50 |
| Argentina | ARG | 713 |  |  |  |  |  |  |  |  | 5 | 98 | 95 | 124 | 318 |
| Armenia | ARM | 134 |  |  |  |  |  |  |  | 1 | 10 | 7 | 14 | 61 | 18 |
| Aruba | ABW | 22 |  |  |  |  |  |  |  |  |  |  | 2 | 6 | 4 |
| Australia | AUS | 1,938 |  |  |  |  |  |  |  |  | 1 | 7 | 18 | 268 | 56 |
| Austria | AUT | 1,555 | 1 |  |  |  |  |  |  | 2 | 36 | 36 | 63 | 369 | 244 |
| Azerbaiyán | AZE | 92 |  |  |  |  |  |  |  | 1 | 8 | 4 | 5 | 30 | 20 |
| Bahamas | BHS | 122 |  |  |  |  |  |  |  |  |  | 4 | 51 | 49 | 13 |
| Bangladés | BGD | 52 |  |  |  |  |  |  |  | 1 | 3 | 5 | 4 | 7 | 8 |
| Barbados | BRB | 81 |  |  |  |  |  |  |  |  |  | 6 | 33 | 6 | 20 |
| Baréin | BHR | 62 |  |  |  |  |  |  |  | 2 | 6 | 6 | 9 | 14 | 15 |
| Belice | BLZ | 57 |  |  |  |  |  |  |  |  |  | 9 | 5 | 15 | 25 |
| Benín | BEN | 42 |  |  |  |  |  |  |  |  | 3 | 6 |  | 2 | 13 |
| Bermudas | BMU | 77 |  |  |  |  |  |  |  |  |  | 11 | 30 | 22 | 7 |
| Bielorrusia | BLR | 242 |  |  |  |  |  |  |  | 3 | 22 | 19 | 25 | 22 | 54 |
| Birmania | MMR | 149 |  |  |  |  |  |  |  |  | 8 | 5 | 14 | 38 | 36 |
| Bolivia | BOL | 168 |  |  |  |  |  |  |  |  | 4 | 15 | 9 | 58 | 58 |
| Bosnia y Herzegovina | BIH | 430 |  |  |  |  |  |  |  | 6 | 37 | 13 | 21 | 101 | 62 |
| Botsuana | BWA | 153 |  |  |  |  |  |  |  |  | 1 |  | 5 | 46 | 51 |
| Brasil | BRA | 1,463 |  |  |  |  |  |  |  | 1 | 15 | 191 | 239 | 459 | 338 |
| Brunéi | BRN | 17 |  |  |  |  |  |  |  |  |  |  |  | 6 | 4 |
| Bulgaria | BGR | 398 |  |  |  |  |  |  | 1 | 2 | 21 | 19 | 42 | 121 | 68 |
| Burkina Faso | BFA | 52 |  |  |  |  |  |  |  |  | 1 | 5 | 3 | 7 | 11 |
| Burundi | BDI | 37 |  |  |  |  |  |  |  |  |  |  |  | 3 | 30 |
| Bután | BTN | 36 |  |  |  |  |  |  |  |  |  |  | 1 | 9 | 11 |
| Bélgica | BEL | 4,645 |  |  |  |  |  |  |  | 2 | 51 | 136 | 339 | 360 | 267 |
| Cabo Verde | CPV | 91 |  |  |  |  |  |  |  |  | 3 | 15 | 37 | 21 | 2 |
| Camboya | KHM | 89 |  |  |  |  |  |  |  |  | 1 | 1 | 1 | 10 | 44 |
| Camerún | CMR | 96 |  |  |  |  |  |  |  |  | 1 | 4 | 8 | 9 | 42 |
| Canadá | CAN | 5,240 |  |  |  |  |  |  |  |  | 12 | 80 | 1,305 | 1,492 | 1,543 |
| Catar | QAT | 53 |  |  |  |  |  |  |  | 3 | 8 | 7 | 11 | 13 | 8 |
| Chad | TCD | 67 |  |  |  |  |  |  |  |  |  | 3 | 4 | 10 | 29 |
| Chile | CHL | 566 |  |  |  |  |  |  |  | 2 | 4 | 108 | 134 | 157 | 105 |
| China | CHN | 3,150 |  |  |  |  | 8 | 1 | 1 | 4 | 33 | 96 | 334 | 1,314 | 886 |
| Chipre | CYP | 175 |  |  |  |  |  |  |  | 1 | 10 | 13 | 11 | 18 | 90 |
| Ciudad del Vaticano | VAT | 38 |  |  |  |  |  |  |  |  |  | 24 | 1 | 3 | 3 |
| Colombia | COL | 466 |  |  |  |  |  |  |  |  | 10 | 55 | 101 | 103 | 115 |
| Comoras | COM | 8 |  |  |  |  |  |  |  |  |  |  |  | 2 | 6 |
| Corea del Norte | PRK | 131 |  |  |  |  |  |  |  |  | 1 | 9 | 11 | 13 | 54 |
| Corea del Sur | KOR | 719 |  |  |  |  |  |  |  |  | 2 | 12 | 50 | 116 | 192 |
| Costa Rica | CRI | 152 |  |  |  |  |  |  |  |  |  | 14 | 15 | 39 | 73 |
| Costa de Marfil | CIV | 78 |  |  |  |  |  |  |  |  | 2 | 5 | 9 | 10 | 22 |
| Croacia | HRV | 732 |  |  |  |  |  |  |  | 6 | 41 | 18 | 34 | 187 | 69 |
| Cuba | CUB | 895 |  |  |  |  |  |  |  | 1 | 6 | 99 | 215 | 235 | 203 |
| Curazao | CUW | 81 |  |  |  |  |  |  |  |  |  |  | 19 | 10 | 2 |
| Dinamarca | DNK | 1,034 |  |  |  |  |  |  | 1 |  | 9 | 47 | 47 | 275 | 64 |
| Dominica | DMA | 15 |  |  |  |  |  |  |  |  |  |  | 12 | 2 |  |
| ESB | ESB | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ecuador | ECU | 234 |  |  |  |  |  |  |  |  | 7 | 19 | 36 | 65 | 69 |
| Egipto | EGY | 1,874 |  |  |  |  |  |  |  | 3 | 43 | 39 | 114 | 756 | 734 |
| El Salvador | SLV | 101 |  |  |  |  |  |  |  |  |  | 1 | 3 | 44 | 46 |
| Emiratos Árabes Unidos | ARE | 52 |  |  |  |  |  |  |  | 3 | 7 | 6 | 12 | 13 | 6 |
| Eritrea | ERI | 389 |  |  |  |  |  |  |  |  | 1 | 6 | 7 | 99 | 254 |
| Eslovaquia | SVK | 489 |  |  |  |  |  |  |  | 2 | 16 | 13 | 19 | 94 | 97 |
| Eslovenia | SVN | 297 |  |  |  |  |  |  |  | 2 | 20 | 6 | 3 | 15 | 106 |
| España | ESP | 6,786 | 6 |  |  |  |  |  | 1 | 12 | 94 | 285 | 1,364 | 2,552 | 886 |
| Estados Federados de Micronesia | FSM | 44 |  |  |  |  |  |  |  |  |  | 1 | 1 | 11 | 25 |
| Estados Unidos | USA | 303,467 | 2 |  |  |  |  |  |  | 2 | 26 | 516 | 4,940 | 64,246 | 202,529 |
| Estonia | EST | 951 |  |  |  |  |  |  |  |  | 2 | 11 | 14 | 79 | 486 |
| Etiopía | ETH | 411 |  |  |  |  |  |  |  | 1 | 10 | 15 | 12 | 104 | 195 |
| Filipinas | PHL | 361 |  |  |  |  |  |  |  |  | 4 | 5 | 56 | 72 | 175 |
| Finlandia | FIN | 200 |  |  |  |  |  |  |  | 1 | 8 | 15 | 18 | 32 | 28 |
| Fiyi | FJI | 43 |  |  |  |  |  |  |  |  |  | 1 |  | 29 | 10 |
| Francia | FRA | 11,465 |  |  |  |  | 1 |  | 1 | 2 | 135 | 468 | 1,487 | 3,633 | 463 |
| GIB | GIB | 5 |  |  |  |  |  |  |  |  |  |  | 5 |  |  |
| Gabón | GAB | 52 |  |  |  |  |  |  |  |  | 1 | 5 | 7 | 6 | 12 |
| Gambia | GMB | 27 |  |  |  |  |  |  |  |  |  | 2 | 11 | 9 | 4 |
| Georgia | GEO | 230 |  |  |  |  |  |  |  | 1 | 11 | 4 | 48 | 60 | 40 |
| Ghana | GHA | 78 |  |  |  |  |  |  |  |  | 2 | 7 | 7 | 8 | 17 |
| Granada | GRD | 314 |  |  |  |  |  |  |  |  |  | 19 | 59 | 193 | 22 |
| Grecia | GRC | 1,266 |  |  |  |  |  |  |  | 3 | 72 | 92 | 88 | 505 | 174 |
| Groenlandia | GRL | 147 |  |  |  |  |  |  | 1 |  | 4 | 11 | 31 | 74 | 13 |
| Guam | GUM | 24 |  |  |  |  |  |  |  |  |  |  | 4 | 6 | 3 |
| Guatemala | GTM | 134 |  |  |  |  |  |  |  |  | 2 | 15 | 10 | 38 | 54 |
| Guernsey | GGY | 204 |  |  |  |  |  |  |  |  |  | 4 |  | 102 | 96 |
| Guinea | GIN | 84 |  |  |  |  |  |  |  |  | 1 | 11 | 32 | 10 | 12 |
| Guinea Ecuatorial | GNQ | 38 |  |  |  |  |  |  |  |  | 1 |  | 2 | 11 | 18 |
| Guinea-Bisáu | GNB | 6 |  |  |  |  |  |  |  |  |  |  | 2 | 2 | 2 |
| Guyana | GUY | 227 |  |  |  |  |  |  |  |  | 3 | 20 | 30 | 44 | 40 |
| Haití | HTI | 333 |  |  |  |  |  |  |  |  | 3 | 17 | 102 | 60 | 111 |
| Honduras | HND | 219 |  |  |  |  |  |  |  |  |  | 26 | 47 | 60 | 69 |
| Hong Kong | HKG | 43 |  |  |  |  |  |  |  |  |  |  |  | 21 | 12 |
| Hungría | HUN | 993 |  |  |  |  |  |  |  | 3 | 38 | 28 | 66 | 282 | 102 |
| India | IND | 1,412 |  |  |  |  |  |  |  | 1 | 59 | 40 | 155 | 555 | 147 |
| Indonesia | IDN | 1,421 | 1 |  |  |  |  |  | 1 |  | 13 | 117 | 71 | 174 | 209 |
| Irak | IRQ | 465 |  |  |  |  |  |  |  | 3 | 30 | 23 | 25 | 92 | 131 |
| Irlanda | IRL | 1,560 |  |  |  |  |  |  |  | 1 | 28 | 65 | 99 | 573 | 30 |
| Irán | IRN | 423 |  |  |  |  |  |  |  | 5 | 38 | 17 | 61 | 158 | 61 |
| Isla Norfolk | NFK | 560 |  |  |  |  |  |  |  |  |  | 1 | 33 | 402 | 118 |
| Isla Santa Elena | SHN | 48 |  |  |  |  |  |  |  |  | 1 | 2 | 5 | 30 | 3 |
| Isla de Man | IMN | 29 |  |  |  |  |  |  |  |  |  |  | 2 | 19 |  |
| Islandia | ISL | 101 |  |  |  |  |  |  |  |  | 3 | 8 | 10 | 38 | 16 |
| Islas Caimán | CYM | 8 |  |  |  |  |  |  |  |  |  |  | 1 | 1 | 6 |
| Islas Feroe | FRO | 4 |  |  |  |  |  |  |  |  |  | 1 | 1 | 2 |  |
| Islas Georgias del Sur y Sandwich del Sur | SGS | 2 |  |  |  |  |  |  |  |  |  |  |  |  | 1 |
| Islas Malvinas | FLK | 33 |  |  |  |  |  |  |  |  |  | 11 | 10 | 6 | 3 |
| Islas Marianas del Norte | MNP | 24 |  |  |  |  |  |  |  |  |  |  |  | 2 | 19 |
| Islas Marshall | MHL | 16 |  |  |  |  |  |  |  |  |  |  |  | 3 | 13 |
| Islas Pitcairn | PCN | 9 |  |  |  |  |  |  |  |  |  |  | 1 | 1 | 7 |
| Islas Salomón | SLB | 33 |  |  |  |  |  |  |  |  | 1 | 2 | 1 | 5 | 10 |
| Islas Turcas y Caicos | TCA | 6 |  |  |  |  |  |  |  |  |  |  | 2 | 2 | 2 |
| Islas Vírgenes Británicas | VGB | 9 |  |  |  |  |  |  |  |  |  |  | 3 | 1 | 5 |
| Islas Vírgenes de los Estados Unidos | VIR | 100 |  |  |  |  |  |  |  |  |  | 1 | 49 | 2 | 43 |
| Israel | ISR | 1,216 |  |  |  |  |  |  | 1 | 9 | 51 | 61 | 154 | 418 | 105 |
| Italia | ITA | 4,254 | 2 |  |  |  |  |  |  | 9 | 189 | 337 | 304 | 918 | 261 |
| Jamaica | JAM | 684 |  |  |  |  |  |  |  | 1 | 1 | 15 | 115 | 490 | 39 |
| Japón | JPN | 1,099 |  |  |  |  |  |  |  | 1 | 4 | 41 | 129 | 291 | 221 |
| Jersey | JEY | 13 |  |  |  |  |  |  |  |  |  | 4 |  | 8 |  |
| Jordania | JOR | 380 |  |  |  |  |  |  |  | 1 | 37 | 18 | 22 | 148 | 27 |
| Kazajistán | KAZ | 110 |  |  |  |  |  |  |  | 1 | 15 | 15 | 4 | 22 | 21 |
| Kenia | KEN | 206 |  |  |  |  |  |  |  |  | 1 | 4 | 1 | 21 | 140 |
| Kirguistán | KGZ | 42 |  |  |  |  |  |  |  |  | 7 | 2 |  | 15 | 10 |
| Kiribati | KIR | 21 |  |  |  |  |  |  |  |  |  |  |  | 14 | 7 |
| Kosovo | KOS | 44 |  |  |  |  |  |  |  |  | 1 | 2 | 2 |  | 21 |
| Kuwait | KWT | 65 |  |  |  |  |  |  |  | 3 | 7 | 5 | 12 | 12 | 12 |
| Laos | LAO | 60 |  |  |  |  |  |  |  | 1 | 3 |  |  | 8 | 16 |
| Lesoto | LSO | 89 |  |  |  |  |  |  |  |  |  |  | 1 | 12 | 71 |
| Letonia | LVA | 191 |  |  |  |  |  |  |  | 2 | 11 | 11 | 11 | 18 | 75 |
| Liberia | LBR | 128 |  |  |  |  |  |  |  |  | 1 | 2 | 4 | 66 | 37 |
| Libia | LBY | 252 |  |  |  |  |  |  |  | 6 | 21 | 17 | 11 | 32 | 93 |
| Liechtenstein | LIE | 12 |  |  |  |  |  |  |  | 1 |  | 1 |  | 2 |  |
| Lituania | LTU | 275 |  |  |  |  |  |  |  | 2 | 11 | 14 | 41 | 20 | 47 |
| Luxemburgo | LUX | 272 |  |  |  |  |  |  |  |  | 6 | 22 | 43 | 35 | 19 |
| Líbano | LBN | 362 |  |  |  |  |  |  |  | 1 | 17 | 6 | 14 | 190 | 71 |
| Macao | MAC | 67 |  |  |  |  |  |  |  |  |  | 1 | 13 | 14 | 29 |
| Macedonia del Norte | MKD | 114 |  |  |  |  |  |  |  | 2 | 13 | 11 | 5 | 19 | 23 |
| Madagascar | MDG | 151 |  |  |  |  |  |  |  |  | 3 | 9 | 25 | 41 | 36 |
| Malasia | MYS | 201 |  |  |  |  |  |  |  |  | 4 | 5 | 5 | 22 | 32 |
| Malaui | MWI | 34 |  |  |  |  |  |  |  |  | 1 |  | 2 | 13 | 14 |
| Maldivas | MDV | 12 |  |  |  |  |  |  |  |  |  |  | 4 |  | 7 |
| Malta | MLT | 147 |  |  |  |  |  |  |  |  | 10 | 15 | 64 | 30 | 6 |
| Malí | MLI | 91 |  |  |  |  |  |  |  |  | 2 | 5 | 7 | 12 | 15 |
| Marruecos | MAR | 411 |  |  |  |  |  |  |  | 1 | 10 | 32 | 55 | 96 | 114 |
| Mauricio | MUS | 69 |  |  |  |  |  |  |  |  |  | 1 | 8 | 21 | 7 |
| Mauritania | MRT | 71 |  |  |  |  |  |  |  |  | 5 | 3 | 12 | 12 | 12 |
| Moldavia | MDA | 109 |  |  |  |  |  |  |  | 1 | 5 | 8 | 18 | 25 | 10 |
| Mongolia | MNG | 92 |  |  |  |  |  |  |  |  | 1 | 9 | 4 | 29 | 35 |
| Montenegro | MNE | 92 |  |  |  |  |  |  |  |  | 8 | 8 | 5 | 21 | 13 |
| Montserrat | MSR | 130 |  |  |  |  |  |  |  |  |  |  |  | 105 | 21 |
| Mozambique | MOZ | 173 |  |  |  |  |  |  |  |  | 4 | 6 | 15 | 52 | 43 |
| México | MEX | 2,857 |  |  |  |  |  |  |  | 3 | 52 | 103 | 305 | 808 | 1,097 |
| Mónaco | MCO | 8 |  |  |  |  |  |  |  |  |  |  | 3 | 1 | 3 |
| Namibia | NAM | 131 |  |  |  |  |  |  |  |  | 2 |  | 6 | 41 | 28 |
| Nauru | NRU | 5 |  |  |  |  |  |  |  |  |  |  |  |  | 5 |
| Nepal | NPL | 44 |  |  |  |  |  |  |  | 1 | 2 | 2 |  | 8 | 13 |
| Nicaragua | NIC | 229 |  |  |  |  |  |  |  |  |  | 24 | 22 | 110 | 58 |
| Nigeria | NGA | 116 |  |  |  |  |  |  |  |  | 2 | 8 | 7 | 8 | 51 |
| Noruega | NOR | 774 |  |  |  |  |  |  |  | 2 | 5 | 19 | 24 | 209 | 26 |
| Nueva Caledonia | NCL | 9 |  |  |  |  |  |  |  |  |  |  | 1 | 3 | 5 |
| Nueva Zelanda | NZL | 190 |  |  |  |  |  |  |  |  |  |  | 3 | 132 | 18 |
| Níger | NER | 70 |  |  |  |  |  |  |  |  | 4 | 5 | 3 | 5 | 26 |
| Omán | OMN | 74 |  |  |  |  |  |  |  | 4 | 12 | 6 | 13 | 16 | 9 |
| PSX | PSX | 298 |  |  |  |  |  |  |  | 1 | 17 | 8 | 7 | 106 | 2 |
| Pakistán | PAK | 374 |  |  |  |  |  |  |  |  | 26 | 7 | 10 | 99 | 114 |
| Palaos | PLW | 40 |  |  |  |  |  |  |  |  |  | 1 | 2 | 9 | 19 |
| Palestina | PSE | 939 |  |  |  |  |  |  |  | 6 | 40 | 31 | 64 | 451 | 98 |
| Panamá | PAN | 295 |  |  |  |  |  |  |  |  | 2 | 42 | 44 | 73 | 90 |
| Papúa Nueva Guinea | PNG | 64 |  |  |  |  |  |  |  |  | 1 | 4 | 2 | 14 | 32 |
| Paraguay | PRY | 176 |  |  |  |  |  |  |  |  |  | 12 | 38 | 64 | 42 |
| Países Bajos | NLD | 18,098 |  |  | 1 |  |  |  |  | 1 | 93 | 349 | 450 | 401 | 959 |
| Perú | PER | 473 |  |  |  |  |  |  |  |  | 17 | 45 | 65 | 176 | 114 |
| Polinesia Francesa | PYF | 69 |  |  |  |  |  |  |  |  |  | 1 | 35 | 26 | 5 |
| Polonia | POL | 2,685 |  |  |  |  |  |  |  | 6 | 40 | 52 | 155 | 525 | 445 |
| Portugal | PRT | 2,267 | 1 |  |  |  |  |  |  | 2 | 48 | 129 | 461 | 909 | 116 |
| Puerto Rico | PRI | 1,034 |  |  |  |  |  |  |  | 1 |  | 10 | 70 | 38 | 892 |
| Reino Unido | GBR | 7,708 |  |  |  |  |  |  |  | 1 | 54 | 428 | 644 | 1,723 | 386 |
| República Centroafricana | CAF | 153 |  |  |  |  |  |  |  |  |  | 2 | 3 | 8 | 112 |
| República Checa | CZE | 1,035 |  |  |  |  |  |  |  | 1 | 16 | 31 | 57 | 173 | 175 |
| República Democrática del Congo | COD | 218 |  |  |  |  |  |  |  |  | 3 | 6 | 9 | 31 | 126 |
| República Dominicana | DOM | 209 |  |  |  |  |  |  |  |  | 3 | 21 | 65 | 45 | 38 |
| República Turca del Norte de Chipre | CYN | 15 |  |  |  |  |  |  |  |  | 2 | 5 |  |  |  |
| República de China | TWN | 132 |  |  |  |  |  |  |  |  | 1 | 8 | 2 | 41 | 48 |
| República del Congo | COG | 142 |  |  |  |  |  |  |  | 1 | 1 | 5 | 16 | 43 | 45 |
| Ruanda | RWA | 24 |  |  |  |  |  |  |  |  |  |  |  | 3 | 17 |
| Rumania | ROU | 1,013 |  |  |  |  |  |  |  | 3 | 37 | 21 | 41 | 160 | 169 |
| Rusia | RUS | 3,519 |  |  |  |  |  |  |  | 5 | 59 | 106 | 229 | 1,354 | 826 |
| SAH | SAH | 4 |  |  |  |  |  |  |  |  |  | 2 |  | 1 |  |
| SDS | SDS | 82 |  |  |  |  |  |  |  |  |  | 1 |  | 10 | 19 |
| Sahara Occidental | ESH | 16 |  |  |  |  |  |  |  |  |  | 2 |  | 9 | 4 |
| Samoa | WSM | 32 |  |  |  |  |  |  |  |  |  |  | 3 | 21 | 8 |
| Samoa Estadounidense | ASM | 24 |  |  |  |  |  |  |  |  |  |  |  | 13 | 6 |
| San Bartolomé | BLM | 5 |  |  |  |  |  |  |  |  |  |  | 3 | 2 |  |
| San Cristóbal y Nieves | KNA | 17 |  |  |  |  |  |  |  |  |  | 2 | 12 | 1 | 2 |
| San Marino | SMR | 1 |  |  |  |  |  |  |  |  |  |  |  | 1 |  |
| San Martín | MAF | 30 |  |  |  |  |  |  |  |  |  |  | 5 | 16 | 6 |
| San Martín | SXM | 17 |  |  |  |  |  |  |  | 1 |  |  | 4 | 8 | 1 |
| San Pedro y Miquelón | SPM | 7 |  |  |  |  |  |  |  |  |  |  | 1 | 5 | 1 |
| San Vicente y las Granadinas | VCT | 19 |  |  |  |  |  |  |  |  |  |  | 6 | 10 | 3 |
| Santa Lucía | LCA | 26 |  |  |  |  |  |  |  |  |  | 1 | 17 | 4 | 4 |
| Santo Tomé y Príncipe | STP | 10 |  |  |  |  |  |  |  |  |  | 1 | 8 |  | 1 |
| Senegal | SEN | 79 |  |  |  |  |  |  |  |  | 1 | 3 | 27 | 19 | 10 |
| Serbia | SRB | 468 |  |  |  |  |  |  |  | 4 | 26 | 14 | 27 | 126 | 58 |
| Seychelles | SYC | 2 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |
| Sierra Leona | SLE | 66 |  |  |  |  |  |  |  |  | 1 | 3 | 9 | 14 | 35 |
| Singapur | SGP | 33 |  |  |  |  |  |  |  |  |  |  | 1 | 18 | 4 |
| Siria | SYR | 678 |  |  |  |  |  |  |  | 4 | 41 | 31 | 57 | 342 | 59 |
| Somalia | SOM | 152 |  |  |  |  |  |  |  |  | 7 | 7 | 4 | 14 | 95 |
| Somalilandia | SOL | 71 |  |  |  |  |  |  |  |  | 2 | 4 |  | 31 | 21 |
| Sri Lanka | LKA | 160 |  |  |  |  |  |  |  | 1 | 8 | 12 | 16 | 48 | 18 |
| Suazilandia | SWZ | 38 |  |  |  |  |  |  |  |  |  |  |  | 3 | 33 |
| Sudáfrica | ZAF | 524 |  |  |  |  |  |  |  |  | 2 | 3 | 22 | 217 | 147 |
| Sudán | SDN | 339 |  |  |  |  |  |  |  | 2 | 8 | 15 | 12 | 78 | 134 |
| Sudán del Sur | SSD | 200 |  |  |  |  |  |  |  |  | 1 | 4 | 2 | 17 | 89 |
| Suecia | SWE | 1,146 |  |  |  |  |  |  |  | 2 | 13 | 31 | 44 | 245 | 34 |
| Suiza | CHE | 1,906 | 1 |  |  |  |  |  |  | 3 | 41 | 49 | 89 | 347 | 122 |
| Surinam | SUR | 353 |  |  |  |  |  |  |  |  | 3 | 14 | 23 | 17 | 20 |
| Tailandia | THA | 137 |  |  |  |  |  |  |  |  | 5 | 3 | 11 | 47 | 32 |
| Tanzania | TZA | 192 |  |  |  |  |  |  |  |  | 2 | 2 | 2 | 48 | 77 |
| Tayikistán | TJK | 45 |  |  |  |  |  |  |  |  | 6 |  |  | 20 | 11 |
| Territorio Británico del Océano Índico | IOT | 1 |  |  |  |  |  |  |  |  |  |  |  |  | 1 |
| Territorios Australianos del Océano Índico | IOA | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Tierras Australes y Antárticas Francesas | ATF | 4 |  |  |  |  |  |  |  |  |  |  |  | 1 |  |
| Timor Oriental | TLS | 15 |  |  |  |  |  |  |  |  |  |  |  |  | 2 |
| Togo | TGO | 25 |  |  |  |  |  |  |  |  |  | 1 | 2 | 2 | 8 |
| Tonga | TON | 9 |  |  |  |  |  |  |  |  |  | 1 | 1 | 5 | 1 |
| Trinidad y Tobago | TTO | 53 |  |  |  |  |  |  |  |  |  | 12 | 21 | 6 | 13 |
| Turkmenistán | TKM | 101 |  |  |  |  |  |  |  |  | 14 | 5 | 3 | 46 | 16 |
| Turquía | TUR | 1,259 |  |  |  |  |  |  |  | 3 | 59 | 56 | 119 | 519 | 177 |
| Tuvalu | TUV | 6 |  |  |  |  |  |  |  |  |  |  |  | 5 | 1 |
| Túnez | TUN | 407 |  |  |  |  |  |  |  | 2 | 25 | 6 | 14 | 163 | 135 |
| UMI | UMI | 2 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |
| USG | USG | 3 |  |  |  |  |  |  |  |  |  |  | 1 | 1 |  |
| Ucrania | UKR | 670 |  |  |  |  |  |  | 2 | 4 | 29 | 48 | 48 | 85 | 76 |
| Uganda | UGA | 175 |  |  |  |  |  |  |  |  | 1 | 3 | 3 | 14 | 128 |
| Uruguay | URY | 199 |  |  |  |  |  |  |  |  | 1 | 22 | 44 | 66 | 36 |
| Uzbekistán | UZB | 91 |  |  |  |  |  |  |  |  | 7 | 4 | 2 | 48 | 15 |
| Vanuatu | VUT | 5 |  |  |  |  |  |  |  |  |  |  |  | 2 | 3 |
| Venezuela | VEN | 388 |  |  |  |  |  |  |  |  | 9 | 67 | 104 | 82 | 55 |
| Vietnam | VNM | 226 |  |  |  |  |  |  |  | 1 | 4 | 3 | 4 | 24 | 42 |
| Yemen | YEM | 349 |  |  |  |  |  |  |  | 4 | 16 | 11 | 14 | 35 | 233 |
| Yibuti | DJI | 48 |  |  |  |  |  |  |  |  | 2 | 2 | 3 | 26 | 13 |
| Zambia | ZMB | 97 |  |  |  |  |  |  |  |  | 1 | 3 | 4 | 19 | 45 |
| Zimbabue | ZWE | 103 |  |  |  |  |  |  |  |  | 2 | 1 | 5 | 25 | 43 |
| Åland | ALA | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |
