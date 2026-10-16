# Biblioteca de Cartographer

Documento generado por `scripts/comprender.py`. No editar a mano.

- Mapas analizados: **732,122** · con país asignado: **461,977** · sin país: 270,145
  (sobre todo mapamundis, cartas oceánicas o registros sin datos de lugar).
- Países con mapas: **243**.
- Tipos: general 478,876, topográfico 201,695, plano urbano 23,364, militar 8,366, histórico/temático 6,728, mapamundi 4,758, ferroviario/viario 4,398, carta náutica 3,322, portulano 448, ptolemaico 167.
- Escalas: desconocida 462,326, local o ciudad 245,025, provincia o comarca 14,152, región o país 6,100, continente 2,997, mundo 1,522.

Cómo se asigna un país: por **nombre** actual (25+ idiomas, Natural Earth), por **nombre histórico**
(`catalogo/nombres_historicos.json`) o por **coordenadas** de la cobertura del mapa. Cada mapa guarda
la vía en el campo `via`; las asignaciones por coordenadas de mapas grandes pueden incluir países
vecinos. Los siglos salen del año de los metadatos de cada archivo y pueden tener errores puntuales.

Mapas de un país: `catalogo/biblioteca/paises/<ISO3>.jsonl.gz` o
`python scripts/buscar_lugar.py "<país>"`.

| País | ISO | Total | Antes del s. IX | IX | X | XI | XII | XIII | XIV | XV | XVI | XVII | XVIII | XIX | XX |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Afganistán | AFG | 367 |  |  |  |  |  |  |  |  | 21 | 6 | 9 | 142 | 100 |
| Albania | ALB | 262 |  |  |  |  |  |  | 1 | 3 | 23 | 22 | 19 | 63 | 48 |
| Alemania | DEU | 12,799 | 1 |  |  |  |  |  |  | 4 | 96 | 208 | 334 | 1,341 | 814 |
| Andorra | AND | 27 |  |  |  |  |  |  |  |  |  |  | 1 | 2 | 18 |
| Angola | AGO | 189 |  |  |  |  |  |  |  |  | 3 | 9 | 13 | 48 | 88 |
| Anguila | AIA | 7 |  |  |  |  |  |  |  |  |  |  | 6 | 1 |  |
| Antigua y Barbuda | ATG | 26 |  |  |  |  |  |  |  |  |  | 1 | 13 | 10 | 1 |
| Antártida | ATA | 87 |  |  |  |  |  |  |  |  |  | 8 | 11 | 9 | 49 |
| Arabia Saudita | SAU | 490 |  |  |  |  |  |  |  | 6 | 45 | 32 | 51 | 145 | 118 |
| Argelia | DZA | 390 |  |  |  |  |  |  |  | 2 | 20 | 21 | 33 | 100 | 102 |
| Argentina | ARG | 753 |  |  |  |  |  |  |  |  | 7 | 98 | 95 | 124 | 355 |
| Armenia | ARM | 141 |  |  |  |  |  |  | 1 | 1 | 11 | 7 | 15 | 61 | 21 |
| Aruba | ABW | 22 |  |  |  |  |  |  |  |  |  |  | 2 | 6 | 4 |
| Australia | AUS | 1,948 |  |  |  |  |  |  |  |  | 1 | 7 | 18 | 273 | 61 |
| Austria | AUT | 1,582 | 1 |  |  |  |  |  |  | 2 | 38 | 36 | 63 | 384 | 254 |
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
| Bolivia | BOL | 194 |  |  |  |  |  |  |  |  | 5 | 15 | 9 | 66 | 73 |
| Bosnia y Herzegovina | BIH | 433 |  |  |  |  |  |  |  | 6 | 37 | 13 | 21 | 101 | 64 |
| Botsuana | BWA | 158 |  |  |  |  |  |  |  |  | 2 |  | 5 | 46 | 55 |
| Brasil | BRA | 1,550 |  |  |  |  |  |  |  | 3 | 16 | 191 | 239 | 460 | 420 |
| Brunéi | BRN | 17 |  |  |  |  |  |  |  |  |  |  |  | 6 | 4 |
| Bulgaria | BGR | 442 |  |  |  |  |  |  | 1 | 2 | 22 | 19 | 42 | 123 | 71 |
| Burkina Faso | BFA | 55 |  |  |  |  |  |  |  |  | 2 | 5 | 3 | 7 | 13 |
| Burundi | BDI | 37 |  |  |  |  |  |  |  |  |  |  |  | 3 | 30 |
| Bután | BTN | 38 |  |  |  |  |  |  |  |  |  |  | 1 | 9 | 11 |
| Bélgica | BEL | 4,650 |  |  |  |  |  |  |  | 2 | 52 | 136 | 339 | 360 | 271 |
| Cabo Verde | CPV | 93 |  |  |  |  |  |  |  |  | 3 | 15 | 37 | 21 | 3 |
| Camboya | KHM | 92 |  |  |  |  |  |  |  |  | 1 | 1 | 1 | 10 | 47 |
| Camerún | CMR | 98 |  |  |  |  |  |  |  |  | 2 | 4 | 8 | 9 | 43 |
| Canadá | CAN | 5,293 |  |  |  |  |  |  |  |  | 13 | 81 | 1,306 | 1,531 | 1,551 |
| Catar | QAT | 55 |  |  |  |  |  |  |  | 3 | 8 | 7 | 11 | 13 | 10 |
| Chad | TCD | 67 |  |  |  |  |  |  |  |  |  | 3 | 4 | 10 | 29 |
| Chile | CHL | 656 |  |  |  |  |  |  |  | 2 | 6 | 108 | 134 | 221 | 128 |
| China | CHN | 3,449 |  |  |  |  | 8 | 1 | 2 | 4 | 35 | 96 | 335 | 1,389 | 1,102 |
| Chipre | CYP | 178 |  |  |  |  |  |  |  | 1 | 10 | 13 | 11 | 18 | 91 |
| Ciudad del Vaticano | VAT | 40 |  |  |  |  |  |  |  |  | 1 | 24 | 1 | 3 | 3 |
| Colombia | COL | 492 |  |  |  |  |  |  |  |  | 10 | 55 | 101 | 103 | 141 |
| Comoras | COM | 9 |  |  |  |  |  |  |  |  |  |  |  | 2 | 7 |
| Corea del Norte | PRK | 134 |  |  |  |  |  |  |  |  | 1 | 9 | 11 | 13 | 54 |
| Corea del Sur | KOR | 723 |  |  |  |  |  |  |  |  | 2 | 12 | 50 | 117 | 195 |
| Costa Rica | CRI | 169 |  |  |  |  |  |  |  |  |  | 14 | 15 | 39 | 89 |
| Costa de Marfil | CIV | 84 |  |  |  |  |  |  |  |  | 3 | 5 | 9 | 10 | 25 |
| Croacia | HRV | 734 |  |  |  |  |  |  |  | 6 | 41 | 18 | 34 | 188 | 69 |
| Cuba | CUB | 961 |  |  |  |  |  |  |  | 1 | 7 | 99 | 215 | 261 | 241 |
| Curazao | CUW | 81 |  |  |  |  |  |  |  |  |  |  | 19 | 10 | 2 |
| Dinamarca | DNK | 1,040 |  |  |  |  |  |  | 1 |  | 10 | 47 | 47 | 275 | 69 |
| Dominica | DMA | 15 |  |  |  |  |  |  |  |  |  |  | 12 | 2 |  |
| ESB | ESB | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ecuador | ECU | 253 |  |  |  |  |  |  |  |  | 8 | 19 | 36 | 65 | 85 |
| Egipto | EGY | 1,899 |  |  |  |  | 1 | 1 |  | 3 | 44 | 39 | 114 | 759 | 750 |
| El Salvador | SLV | 112 |  |  |  |  |  |  |  |  |  | 2 | 4 | 44 | 54 |
| Emiratos Árabes Unidos | ARE | 53 |  |  |  |  |  |  |  | 3 | 7 | 6 | 12 | 13 | 6 |
| Eritrea | ERI | 398 |  |  |  |  |  |  |  |  | 1 | 6 | 7 | 99 | 260 |
| Eslovaquia | SVK | 490 |  |  |  |  |  |  |  | 2 | 16 | 13 | 19 | 94 | 97 |
| Eslovenia | SVN | 301 |  |  |  |  |  |  |  | 2 | 20 | 7 | 3 | 15 | 106 |
| España | ESP | 6,890 | 6 |  |  |  | 1 | 1 | 6 | 13 | 95 | 285 | 1,364 | 2,639 | 890 |
| Estados Federados de Micronesia | FSM | 44 |  |  |  |  |  |  |  |  |  | 1 | 1 | 11 | 25 |
| Estados Unidos | USA | 356,992 | 3 |  |  |  |  |  |  | 4 | 29 | 516 | 4,965 | 110,893 | 209,122 |
| Estonia | EST | 954 |  |  |  |  |  |  |  |  | 2 | 11 | 14 | 79 | 489 |
| Etiopía | ETH | 421 |  |  |  |  |  | 1 |  | 1 | 11 | 15 | 12 | 104 | 202 |
| Filipinas | PHL | 366 |  |  |  |  |  |  |  |  | 5 | 5 | 56 | 72 | 179 |
| Finlandia | FIN | 201 |  |  |  |  |  |  |  | 1 | 8 | 15 | 18 | 32 | 29 |
| Fiyi | FJI | 43 |  |  |  |  |  |  |  |  |  | 1 |  | 29 | 10 |
| Francia | FRA | 11,964 |  |  | 1 |  | 1 | 1 | 1 | 3 | 138 | 468 | 1,488 | 3,949 | 619 |
| GIB | GIB | 5 |  |  |  |  |  |  |  |  |  |  | 5 |  |  |
| Gabón | GAB | 56 |  |  |  |  |  |  |  |  | 2 | 5 | 7 | 6 | 12 |
| Gambia | GMB | 27 |  |  |  |  |  |  |  |  |  | 2 | 11 | 9 | 4 |
| Georgia | GEO | 230 |  |  |  |  |  |  |  | 1 | 11 | 4 | 48 | 60 | 40 |
| Ghana | GHA | 81 |  |  |  |  |  |  |  |  | 2 | 7 | 7 | 8 | 19 |
| Granada | GRD | 334 |  |  |  |  |  |  |  |  |  | 19 | 59 | 207 | 27 |
| Grecia | GRC | 1,276 |  |  |  |  |  |  |  | 3 | 75 | 92 | 89 | 506 | 177 |
| Groenlandia | GRL | 150 |  |  |  |  |  |  | 1 |  | 6 | 11 | 31 | 74 | 13 |
| Guam | GUM | 24 |  |  |  |  |  |  |  |  |  |  | 4 | 6 | 3 |
| Guatemala | GTM | 152 |  |  |  |  |  |  |  |  | 2 | 15 | 10 | 38 | 72 |
| Guernsey | GGY | 217 |  |  |  |  |  |  |  |  |  | 4 |  | 102 | 109 |
| Guinea | GIN | 84 |  |  |  |  |  |  |  |  | 1 | 11 | 32 | 10 | 12 |
| Guinea Ecuatorial | GNQ | 38 |  |  |  |  |  |  |  |  | 1 |  | 2 | 11 | 18 |
| Guinea-Bisáu | GNB | 6 |  |  |  |  |  |  |  |  |  |  | 2 | 2 | 2 |
| Guyana | GUY | 238 |  |  |  |  |  |  |  |  | 3 | 20 | 30 | 44 | 51 |
| Haití | HTI | 342 |  |  |  |  |  |  |  |  | 4 | 17 | 102 | 60 | 118 |
| Honduras | HND | 231 |  |  |  |  |  |  |  |  |  | 26 | 47 | 60 | 81 |
| Hong Kong | HKG | 43 |  |  |  |  |  |  |  |  |  |  |  | 21 | 12 |
| Hungría | HUN | 995 |  |  |  |  |  |  |  | 3 | 39 | 28 | 66 | 283 | 102 |
| India | IND | 1,433 |  |  |  |  |  |  | 5 | 2 | 61 | 40 | 159 | 558 | 149 |
| Indonesia | IDN | 1,430 | 1 |  |  |  |  |  | 1 |  | 14 | 117 | 74 | 174 | 213 |
| Irak | IRQ | 486 |  |  |  |  | 1 |  |  | 3 | 31 | 24 | 25 | 92 | 139 |
| Irlanda | IRL | 1,563 |  |  |  |  |  |  |  | 1 | 30 | 65 | 99 | 573 | 31 |
| Irán | IRN | 437 |  |  |  |  |  |  |  | 5 | 40 | 17 | 61 | 158 | 68 |
| Isla Norfolk | NFK | 1,193 |  |  |  |  |  |  |  |  |  | 1 | 33 | 957 | 196 |
| Isla Santa Elena | SHN | 100 |  |  |  |  |  |  |  |  | 1 | 2 | 5 | 80 | 5 |
| Isla de Man | IMN | 29 |  |  |  |  |  |  |  |  |  |  | 2 | 19 |  |
| Islandia | ISL | 105 |  |  |  |  |  |  |  |  | 5 | 8 | 10 | 38 | 18 |
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
| Israel | ISR | 1,232 |  |  |  |  |  | 1 | 1 | 9 | 51 | 61 | 154 | 426 | 110 |
| Italia | ITA | 5,101 | 2 |  |  | 2 | 4 | 1 |  | 12 | 204 | 340 | 306 | 1,290 | 461 |
| Jamaica | JAM | 744 |  |  |  |  |  |  |  | 1 | 1 | 15 | 115 | 543 | 46 |
| Japón | JPN | 1,104 |  |  |  |  |  |  |  | 1 | 5 | 41 | 129 | 291 | 225 |
| Jersey | JEY | 13 |  |  |  |  |  |  |  |  |  | 4 |  | 8 |  |
| Jordania | JOR | 380 |  |  |  |  |  |  |  | 1 | 37 | 18 | 22 | 148 | 27 |
| Kazajistán | KAZ | 111 |  |  |  |  |  |  |  | 1 | 15 | 15 | 4 | 22 | 22 |
| Kenia | KEN | 214 |  |  |  |  |  |  |  |  | 2 | 4 | 1 | 21 | 147 |
| Kirguistán | KGZ | 42 |  |  |  |  |  |  |  |  | 7 | 2 |  | 15 | 10 |
| Kiribati | KIR | 22 |  |  |  |  |  |  |  |  |  |  |  | 14 | 8 |
| Kosovo | KOS | 47 |  |  |  |  |  |  |  |  | 1 | 2 | 2 |  | 24 |
| Kuwait | KWT | 67 |  |  |  |  |  |  |  | 3 | 7 | 5 | 12 | 12 | 13 |
| Laos | LAO | 63 |  |  |  |  |  |  |  | 1 | 3 |  |  | 8 | 16 |
| Lesoto | LSO | 90 |  |  |  |  |  |  |  |  |  |  | 1 | 12 | 72 |
| Letonia | LVA | 192 |  |  |  |  |  |  |  | 2 | 12 | 11 | 11 | 18 | 75 |
| Liberia | LBR | 130 |  |  |  |  |  |  |  |  | 2 | 2 | 4 | 66 | 38 |
| Libia | LBY | 264 |  |  |  |  |  |  |  | 6 | 22 | 17 | 11 | 32 | 103 |
| Liechtenstein | LIE | 13 |  |  |  |  |  |  |  | 1 |  | 1 |  | 3 |  |
| Lituania | LTU | 278 |  |  |  |  |  |  |  | 2 | 12 | 14 | 41 | 20 | 48 |
| Luxemburgo | LUX | 273 |  |  |  |  |  |  |  |  | 6 | 22 | 44 | 35 | 19 |
| Líbano | LBN | 653 |  |  |  |  |  |  |  | 1 | 17 | 6 | 15 | 444 | 105 |
| Macao | MAC | 69 |  |  |  |  |  |  |  |  |  | 1 | 13 | 14 | 31 |
| Macedonia del Norte | MKD | 115 |  |  |  |  |  |  |  | 2 | 13 | 11 | 5 | 19 | 24 |
| Madagascar | MDG | 155 |  |  |  |  |  |  |  |  | 5 | 9 | 25 | 41 | 36 |
| Malasia | MYS | 202 |  |  |  |  |  |  |  |  | 4 | 5 | 5 | 22 | 33 |
| Malaui | MWI | 34 |  |  |  |  |  |  |  |  | 1 |  | 2 | 13 | 14 |
| Maldivas | MDV | 12 |  |  |  |  |  |  |  |  |  |  | 4 |  | 7 |
| Malta | MLT | 151 |  |  |  |  |  |  |  |  | 10 | 15 | 64 | 31 | 8 |
| Malí | MLI | 96 |  |  |  |  |  |  | 1 |  | 4 | 5 | 7 | 12 | 17 |
| Marruecos | MAR | 413 |  |  |  |  |  |  |  | 1 | 11 | 32 | 55 | 96 | 115 |
| Mauricio | MUS | 71 |  |  |  |  |  |  |  |  |  | 1 | 8 | 21 | 9 |
| Mauritania | MRT | 74 |  |  |  |  |  |  |  |  | 6 | 3 | 12 | 12 | 14 |
| Moldavia | MDA | 109 |  |  |  |  |  |  |  | 1 | 5 | 8 | 18 | 25 | 10 |
| Mongolia | MNG | 93 |  |  |  |  |  |  |  |  | 1 | 9 | 4 | 29 | 36 |
| Montenegro | MNE | 92 |  |  |  |  |  |  |  |  | 8 | 8 | 5 | 21 | 13 |
| Montserrat | MSR | 130 |  |  |  |  |  |  |  |  |  |  |  | 105 | 21 |
| Mozambique | MOZ | 175 |  |  |  |  |  |  |  |  | 6 | 6 | 15 | 52 | 43 |
| México | MEX | 3,104 |  |  |  |  |  |  |  | 3 | 54 | 103 | 305 | 890 | 1,258 |
| Mónaco | MCO | 8 |  |  |  |  |  |  |  |  |  |  | 3 | 1 | 3 |
| Namibia | NAM | 132 |  |  |  |  |  |  |  |  | 3 |  | 6 | 41 | 28 |
| Nauru | NRU | 6 |  |  |  |  |  |  |  |  |  |  |  |  | 5 |
| Nepal | NPL | 46 |  |  |  |  |  |  |  | 1 | 3 | 2 |  | 8 | 14 |
| Nicaragua | NIC | 238 |  |  |  |  |  |  |  |  |  | 24 | 22 | 110 | 67 |
| Nigeria | NGA | 118 |  |  |  |  |  |  |  |  | 3 | 8 | 7 | 8 | 52 |
| Noruega | NOR | 830 |  |  |  |  |  |  |  | 2 | 5 | 19 | 24 | 265 | 26 |
| Nueva Caledonia | NCL | 9 |  |  |  |  |  |  |  |  |  |  | 1 | 3 | 5 |
| Nueva Zelanda | NZL | 193 |  |  |  |  |  |  |  |  |  |  | 3 | 132 | 19 |
| Níger | NER | 70 |  |  |  |  |  |  |  |  | 4 | 5 | 3 | 5 | 26 |
| Omán | OMN | 75 |  |  |  |  |  |  |  | 4 | 12 | 6 | 13 | 16 | 9 |
| PSX | PSX | 298 |  |  |  |  |  |  |  | 1 | 17 | 8 | 7 | 106 | 2 |
| Pakistán | PAK | 380 |  |  |  |  |  |  |  |  | 28 | 7 | 10 | 99 | 116 |
| Palaos | PLW | 40 |  |  |  |  |  |  |  |  |  | 1 | 2 | 9 | 19 |
| Palestina | PSE | 998 |  |  |  |  |  |  |  | 6 | 40 | 31 | 65 | 489 | 116 |
| Panamá | PAN | 304 |  |  |  |  |  |  |  |  | 2 | 42 | 44 | 73 | 99 |
| Papúa Nueva Guinea | PNG | 65 |  |  |  |  |  |  |  |  | 1 | 4 | 2 | 14 | 33 |
| Paraguay | PRY | 190 |  |  |  |  |  |  |  |  |  | 12 | 38 | 64 | 56 |
| Países Bajos | NLD | 18,107 |  |  | 1 |  |  |  |  | 1 | 94 | 351 | 451 | 402 | 962 |
| Perú | PER | 691 |  |  |  |  |  |  |  |  | 19 | 45 | 65 | 287 | 216 |
| Polinesia Francesa | PYF | 69 |  |  |  |  |  |  |  |  |  | 1 | 35 | 26 | 5 |
| Polonia | POL | 2,692 |  |  |  |  |  |  | 1 | 6 | 41 | 52 | 155 | 525 | 448 |
| Portugal | PRT | 2,419 | 1 |  |  |  |  |  |  | 2 | 50 | 129 | 461 | 971 | 204 |
| Puerto Rico | PRI | 1,041 |  |  |  |  |  |  |  | 1 | 1 | 10 | 70 | 38 | 897 |
| Reino Unido | GBR | 8,319 |  |  |  |  | 2 | 8 |  | 1 | 55 | 429 | 644 | 2,231 | 466 |
| República Centroafricana | CAF | 155 |  |  |  |  |  |  |  |  |  | 2 | 3 | 8 | 112 |
| República Checa | CZE | 1,089 |  |  |  |  |  |  |  | 1 | 16 | 31 | 57 | 189 | 213 |
| República Democrática del Congo | COD | 224 |  |  |  |  |  |  |  |  | 3 | 6 | 9 | 31 | 128 |
| República Dominicana | DOM | 223 |  |  |  |  |  |  |  |  | 4 | 21 | 65 | 45 | 49 |
| República Turca del Norte de Chipre | CYN | 15 |  |  |  |  |  |  |  |  | 2 | 5 |  |  |  |
| República de China | TWN | 138 |  |  |  |  |  |  |  |  | 1 | 8 | 2 | 41 | 53 |
| República del Congo | COG | 151 |  |  |  |  |  |  |  | 1 | 2 | 5 | 16 | 43 | 49 |
| Ruanda | RWA | 24 |  |  |  |  |  |  |  |  |  |  |  | 3 | 17 |
| Rumania | ROU | 1,020 |  |  |  |  |  |  |  | 3 | 37 | 21 | 41 | 161 | 172 |
| Rusia | RUS | 4,008 |  |  |  |  |  |  |  | 5 | 63 | 106 | 229 | 1,561 | 1,098 |
| SAH | SAH | 4 |  |  |  |  |  |  |  |  |  | 2 |  | 1 |  |
| SDS | SDS | 82 |  |  |  |  |  |  |  |  |  | 1 |  | 10 | 19 |
| Sahara Occidental | ESH | 18 |  |  |  |  |  |  | 1 |  |  | 2 |  | 9 | 5 |
| Samoa | WSM | 33 |  |  |  |  |  |  |  |  |  |  | 3 | 21 | 9 |
| Samoa Estadounidense | ASM | 24 |  |  |  |  |  |  |  |  |  |  |  | 13 | 6 |
| San Bartolomé | BLM | 5 |  |  |  |  |  |  |  |  |  |  | 3 | 2 |  |
| San Cristóbal y Nieves | KNA | 18 |  |  |  |  |  |  |  |  |  | 2 | 12 | 1 | 3 |
| San Marino | SMR | 2 |  |  |  |  |  |  |  |  |  |  |  | 1 | 1 |
| San Martín | MAF | 42 |  |  |  |  |  |  |  |  |  |  | 5 | 26 | 6 |
| San Martín | SXM | 17 |  |  |  |  |  |  |  | 1 |  |  | 4 | 8 | 1 |
| San Pedro y Miquelón | SPM | 7 |  |  |  |  |  |  |  |  |  |  | 1 | 5 | 1 |
| San Vicente y las Granadinas | VCT | 19 |  |  |  |  |  |  |  |  |  |  | 6 | 10 | 3 |
| Santa Lucía | LCA | 26 |  |  |  |  |  |  |  |  |  | 1 | 17 | 4 | 4 |
| Santo Tomé y Príncipe | STP | 10 |  |  |  |  |  |  |  |  |  | 1 | 8 |  | 1 |
| Senegal | SEN | 80 |  |  |  |  |  |  |  |  | 2 | 3 | 27 | 19 | 10 |
| Serbia | SRB | 470 |  |  |  |  |  |  |  | 4 | 26 | 14 | 27 | 127 | 58 |
| Seychelles | SYC | 2 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |
| Sierra Leona | SLE | 70 |  |  |  |  |  |  |  |  | 2 | 3 | 9 | 14 | 37 |
| Singapur | SGP | 34 |  |  |  |  |  |  |  |  |  |  | 1 | 19 | 4 |
| Siria | SYR | 724 |  |  |  |  |  |  |  | 4 | 41 | 31 | 57 | 367 | 79 |
| Somalia | SOM | 155 |  |  |  |  |  |  |  |  | 8 | 7 | 4 | 14 | 96 |
| Somalilandia | SOL | 72 |  |  |  |  |  |  |  |  | 2 | 4 |  | 31 | 22 |
| Sri Lanka | LKA | 166 |  |  |  |  |  |  | 2 | 2 | 10 | 13 | 16 | 48 | 18 |
| Suazilandia | SWZ | 38 |  |  |  |  |  |  |  |  |  |  |  | 3 | 33 |
| Sudáfrica | ZAF | 530 |  |  |  |  |  |  |  |  | 4 | 3 | 22 | 218 | 149 |
| Sudán | SDN | 345 |  |  |  |  |  |  |  | 2 | 9 | 15 | 12 | 78 | 138 |
| Sudán del Sur | SSD | 200 |  |  |  |  |  |  |  |  | 1 | 4 | 2 | 17 | 89 |
| Suecia | SWE | 1,148 |  |  |  |  |  |  |  | 2 | 13 | 31 | 45 | 245 | 35 |
| Suiza | CHE | 1,960 | 1 |  |  |  |  |  |  | 3 | 48 | 49 | 89 | 372 | 139 |
| Surinam | SUR | 361 |  |  |  |  |  |  |  |  | 3 | 14 | 23 | 17 | 28 |
| Tailandia | THA | 138 |  |  |  |  |  |  |  |  | 5 | 3 | 11 | 48 | 32 |
| Tanzania | TZA | 196 |  |  |  |  |  |  |  |  | 3 | 2 | 2 | 48 | 79 |
| Tayikistán | TJK | 45 |  |  |  |  |  |  |  |  | 6 |  |  | 20 | 11 |
| Territorio Británico del Océano Índico | IOT | 1 |  |  |  |  |  |  |  |  |  |  |  |  | 1 |
| Territorios Australianos del Océano Índico | IOA | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Tierras Australes y Antárticas Francesas | ATF | 4 |  |  |  |  |  |  |  |  |  |  |  | 1 |  |
| Timor Oriental | TLS | 15 |  |  |  |  |  |  |  |  |  |  |  |  | 2 |
| Togo | TGO | 26 |  |  |  |  |  |  |  |  |  | 1 | 2 | 2 | 8 |
| Tonga | TON | 10 |  |  |  |  |  |  |  |  |  | 1 | 1 | 5 | 2 |
| Trinidad y Tobago | TTO | 58 |  |  |  |  |  |  |  |  |  | 12 | 21 | 6 | 18 |
| Turkmenistán | TKM | 102 |  |  |  |  |  |  |  |  | 14 | 5 | 3 | 46 | 16 |
| Turquía | TUR | 1,345 |  |  |  |  |  |  | 1 | 3 | 59 | 56 | 119 | 549 | 222 |
| Tuvalu | TUV | 6 |  |  |  |  |  |  |  |  |  |  |  | 5 | 1 |
| Túnez | TUN | 414 |  |  |  |  |  |  |  | 2 | 26 | 7 | 14 | 163 | 138 |
| UMI | UMI | 2 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |
| USG | USG | 3 |  |  |  |  |  |  |  |  |  |  | 1 | 1 |  |
| Ucrania | UKR | 672 |  |  |  |  |  |  | 2 | 4 | 29 | 48 | 48 | 85 | 76 |
| Uganda | UGA | 186 |  |  |  |  |  |  |  |  | 1 | 3 | 3 | 14 | 138 |
| Uruguay | URY | 251 |  |  |  |  |  |  |  |  | 1 | 22 | 44 | 90 | 64 |
| Uzbekistán | UZB | 92 |  |  |  |  |  |  |  |  | 7 | 4 | 2 | 48 | 16 |
| Vanuatu | VUT | 6 |  |  |  |  |  |  |  |  |  |  |  | 2 | 4 |
| Venezuela | VEN | 405 |  |  |  |  |  |  |  |  | 9 | 67 | 104 | 82 | 72 |
| Vietnam | VNM | 228 |  |  |  |  |  |  |  | 1 | 4 | 3 | 4 | 25 | 43 |
| Yemen | YEM | 354 |  |  |  |  |  |  |  | 4 | 16 | 11 | 14 | 35 | 238 |
| Yibuti | DJI | 49 |  |  |  |  |  |  |  |  | 2 | 2 | 3 | 26 | 14 |
| Zambia | ZMB | 97 |  |  |  |  |  |  |  |  | 1 | 3 | 4 | 19 | 45 |
| Zimbabue | ZWE | 103 |  |  |  |  |  |  |  |  | 2 | 1 | 5 | 25 | 43 |
| Åland | ALA | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |
