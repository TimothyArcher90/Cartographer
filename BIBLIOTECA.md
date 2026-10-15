# Biblioteca de Cartographer

Documento generado por `scripts/comprender.py`. No editar a mano.

- Mapas analizados: **381,791** · con país asignado: **331,188** · sin país: 50,603
  (sobre todo mapamundis, cartas oceánicas o registros sin datos de lugar).
- Países con mapas: **243**.
- Tipos: topográfico 197,075, general 158,651, plano urbano 8,470, militar 4,996, histórico/temático 3,956, mapamundi 3,663, ferroviario/viario 2,417, carta náutica 2,258, portulano 164, ptolemaico 141.
- Escalas: local o ciudad 236,396, desconocida 120,624, provincia o comarca 14,152, región o país 6,100, continente 2,997, mundo 1,522.

Cómo se asigna un país: por **nombre** actual (25+ idiomas, Natural Earth), por **nombre histórico**
(`catalogo/nombres_historicos.json`) o por **coordenadas** de la cobertura del mapa. Cada mapa guarda
la vía en el campo `via`; las asignaciones por coordenadas de mapas grandes pueden incluir países
vecinos. Los siglos salen del año de los metadatos de cada archivo y pueden tener errores puntuales.

Mapas de un país: `catalogo/biblioteca/paises/<ISO3>.jsonl.gz` o
`python scripts/buscar_lugar.py "<país>"`.

| País | ISO | Total | Antes del s. IX | IX | X | XI | XII | XIII | XIV | XV | XVI | XVII | XVIII | XIX | XX |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Afganistán | AFG | 296 |  |  |  |  |  |  |  |  | 19 | 5 | 7 | 108 | 72 |
| Albania | ALB | 236 |  |  |  |  |  |  |  | 2 | 21 | 22 | 14 | 55 | 40 |
| Alemania | DEU | 6,462 | 1 |  |  |  |  |  |  | 2 | 85 | 145 | 202 | 807 | 410 |
| Andorra | AND | 4 |  |  |  |  |  |  |  |  |  |  |  |  | 3 |
| Angola | AGO | 109 |  |  |  |  |  |  |  |  | 2 | 6 | 10 | 23 | 41 |
| Anguila | AIA | 6 |  |  |  |  |  |  |  |  |  |  | 5 | 1 |  |
| Antigua y Barbuda | ATG | 23 |  |  |  |  |  |  |  |  |  | 1 | 13 | 7 | 1 |
| Antártida | ATA | 63 |  |  |  |  |  |  |  |  |  | 3 | 2 | 8 | 42 |
| Arabia Saudita | SAU | 391 |  |  |  |  |  |  |  | 6 | 41 | 27 | 43 | 85 | 102 |
| Argelia | DZA | 269 |  |  |  |  |  |  |  | 2 | 19 | 16 | 17 | 68 | 43 |
| Argentina | ARG | 567 |  |  |  |  |  |  |  |  | 3 | 69 | 47 | 98 | 302 |
| Armenia | ARM | 98 |  |  |  |  |  |  |  | 1 | 10 | 5 | 11 | 33 | 15 |
| Aruba | ABW | 18 |  |  |  |  |  |  |  |  |  |  | 2 | 6 | 2 |
| Australia | AUS | 1,834 |  |  |  |  |  |  |  |  |  | 6 | 13 | 201 | 48 |
| Austria | AUT | 1,278 | 1 |  |  |  |  |  |  | 2 | 36 | 29 | 39 | 259 | 209 |
| Azerbaiyán | AZE | 85 |  |  |  |  |  |  |  | 1 | 8 | 3 | 3 | 27 | 19 |
| Bahamas | BHS | 102 |  |  |  |  |  |  |  |  |  | 1 | 41 | 43 | 13 |
| Bangladés | BGD | 47 |  |  |  |  |  |  |  | 1 | 2 | 4 | 3 | 6 | 8 |
| Barbados | BRB | 69 |  |  |  |  |  |  |  |  |  | 5 | 23 | 6 | 20 |
| Baréin | BHR | 44 |  |  |  |  |  |  |  | 2 | 4 | 4 | 6 | 7 | 13 |
| Belice | BLZ | 49 |  |  |  |  |  |  |  |  |  | 7 | 5 | 9 | 25 |
| Benín | BEN | 42 |  |  |  |  |  |  |  |  | 3 | 6 |  | 2 | 13 |
| Bermudas | BMU | 65 |  |  |  |  |  |  |  |  |  | 11 | 25 | 19 | 5 |
| Bielorrusia | BLR | 236 |  |  |  |  |  |  |  | 3 | 22 | 18 | 23 | 21 | 52 |
| Birmania | MMR | 143 |  |  |  |  |  |  |  |  | 8 | 4 | 14 | 33 | 36 |
| Bolivia | BOL | 147 |  |  |  |  |  |  |  |  | 4 | 13 | 8 | 47 | 51 |
| Bosnia y Herzegovina | BIH | 422 |  |  |  |  |  |  |  | 6 | 36 | 13 | 20 | 100 | 58 |
| Botsuana | BWA | 153 |  |  |  |  |  |  |  |  | 1 |  | 5 | 46 | 51 |
| Brasil | BRA | 977 |  |  |  |  |  |  |  |  | 11 | 92 | 95 | 306 | 320 |
| Brunéi | BRN | 15 |  |  |  |  |  |  |  |  |  |  |  | 4 | 4 |
| Bulgaria | BGR | 360 |  |  |  |  |  |  | 1 | 2 | 19 | 17 | 38 | 101 | 62 |
| Burkina Faso | BFA | 52 |  |  |  |  |  |  |  |  | 1 | 5 | 3 | 7 | 11 |
| Burundi | BDI | 31 |  |  |  |  |  |  |  |  |  |  |  | 3 | 24 |
| Bután | BTN | 32 |  |  |  |  |  |  |  |  |  |  | 1 | 6 | 11 |
| Bélgica | BEL | 3,829 |  |  |  |  |  |  |  | 1 | 47 | 92 | 231 | 288 | 101 |
| Cabo Verde | CPV | 79 |  |  |  |  |  |  |  |  | 2 | 14 | 35 | 14 | 2 |
| Camboya | KHM | 88 |  |  |  |  |  |  |  |  | 1 | 1 | 1 | 10 | 43 |
| Camerún | CMR | 94 |  |  |  |  |  |  |  |  | 1 | 4 | 8 | 9 | 42 |
| Canadá | CAN | 4,628 |  |  |  |  |  |  |  |  | 8 | 73 | 1,095 | 1,133 | 1,529 |
| Catar | QAT | 31 |  |  |  |  |  |  |  | 3 | 5 | 3 | 8 | 5 | 4 |
| Chad | TCD | 67 |  |  |  |  |  |  |  |  |  | 3 | 4 | 10 | 29 |
| Chile | CHL | 384 |  |  |  |  |  |  |  | 1 | 2 | 70 | 45 | 128 | 93 |
| China | CHN | 2,075 |  |  |  |  | 7 | 1 | 1 | 4 | 30 | 83 | 241 | 669 | 664 |
| Chipre | CYP | 68 |  |  |  |  |  |  |  | 1 | 10 | 11 | 7 | 15 | 5 |
| Ciudad del Vaticano | VAT | 8 |  |  |  |  |  |  |  |  |  |  | 1 | 3 | 2 |
| Colombia | COL | 296 |  |  |  |  |  |  |  |  | 5 | 22 | 50 | 61 | 102 |
| Comoras | COM | 4 |  |  |  |  |  |  |  |  |  |  |  | 2 | 2 |
| Corea del Norte | PRK | 117 |  |  |  |  |  |  |  |  | 1 | 9 | 11 | 13 | 48 |
| Corea del Sur | KOR | 252 |  |  |  |  |  |  |  |  | 2 | 11 | 44 | 99 | 57 |
| Costa Rica | CRI | 115 |  |  |  |  |  |  |  |  |  | 14 | 11 | 31 | 50 |
| Costa de Marfil | CIV | 66 |  |  |  |  |  |  |  |  | 2 | 5 | 9 | 10 | 14 |
| Croacia | HRV | 639 |  |  |  |  |  |  |  | 6 | 40 | 15 | 28 | 174 | 63 |
| Cuba | CUB | 558 |  |  |  |  |  |  |  |  | 5 | 36 | 123 | 139 | 149 |
| Curazao | CUW | 71 |  |  |  |  |  |  |  |  |  |  | 13 | 8 | 1 |
| Dinamarca | DNK | 885 |  |  |  |  |  |  | 1 |  | 8 | 42 | 19 | 251 | 15 |
| Dominica | DMA | 13 |  |  |  |  |  |  |  |  |  |  | 10 | 2 |  |
| ESB | ESB | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ecuador | ECU | 164 |  |  |  |  |  |  |  |  | 5 | 11 | 16 | 48 | 56 |
| Egipto | EGY | 753 |  |  |  |  |  |  |  | 3 | 41 | 33 | 87 | 336 | 95 |
| El Salvador | SLV | 66 |  |  |  |  |  |  |  |  |  | 1 | 2 | 19 | 38 |
| Emiratos Árabes Unidos | ARE | 41 |  |  |  |  |  |  |  | 3 | 6 | 4 | 10 | 9 | 4 |
| Eritrea | ERI | 334 |  |  |  |  |  |  |  |  | 1 | 6 | 5 | 94 | 210 |
| Eslovaquia | SVK | 450 |  |  |  |  |  |  |  | 2 | 16 | 10 | 19 | 93 | 73 |
| Eslovenia | SVN | 287 |  |  |  |  |  |  |  | 2 | 18 | 4 | 3 | 12 | 106 |
| España | ESP | 2,499 |  |  |  |  |  |  |  | 4 | 66 | 78 | 419 | 993 | 60 |
| Estados Federados de Micronesia | FSM | 40 |  |  |  |  |  |  |  |  |  | 1 |  | 9 | 25 |
| Estados Unidos | USA | 264,061 | 2 |  |  |  |  |  |  | 1 | 21 | 421 | 4,221 | 34,418 | 194,403 |
| Estonia | EST | 263 |  |  |  |  |  |  |  |  | 1 | 8 | 3 | 7 | 181 |
| Etiopía | ETH | 343 |  |  |  |  |  |  |  | 1 | 8 | 14 | 10 | 99 | 143 |
| Filipinas | PHL | 268 |  |  |  |  |  |  |  |  | 3 | 5 | 27 | 47 | 160 |
| Finlandia | FIN | 158 |  |  |  |  |  |  |  | 1 | 8 | 13 | 13 | 28 | 16 |
| Fiyi | FJI | 38 |  |  |  |  |  |  |  |  |  |  |  | 28 | 7 |
| Francia | FRA | 9,372 |  |  |  |  |  |  |  | 1 | 126 | 292 | 951 | 3,063 | 293 |
| GIB | GIB | 5 |  |  |  |  |  |  |  |  |  |  | 5 |  |  |
| Gabón | GAB | 47 |  |  |  |  |  |  |  |  | 1 | 5 | 6 | 6 | 12 |
| Gambia | GMB | 20 |  |  |  |  |  |  |  |  |  | 1 | 8 | 7 | 4 |
| Georgia | GEO | 131 |  |  |  |  |  |  |  | 1 | 11 | 3 | 26 | 29 | 31 |
| Ghana | GHA | 63 |  |  |  |  |  |  |  |  | 2 | 6 | 7 | 8 | 9 |
| Granada | GRD | 89 |  |  |  |  |  |  |  |  |  | 9 | 28 | 34 | 6 |
| Grecia | GRC | 900 |  |  |  |  |  |  |  | 3 | 70 | 81 | 74 | 331 | 66 |
| Groenlandia | GRL | 113 |  |  |  |  |  |  | 1 |  | 4 | 10 | 22 | 56 | 9 |
| Guam | GUM | 19 |  |  |  |  |  |  |  |  |  |  | 2 | 3 | 3 |
| Guatemala | GTM | 106 |  |  |  |  |  |  |  |  | 1 | 15 | 10 | 23 | 46 |
| Guernsey | GGY | 77 |  |  |  |  |  |  |  |  |  | 4 |  | 57 | 14 |
| Guinea | GIN | 67 |  |  |  |  |  |  |  |  | 1 | 5 | 23 | 9 | 12 |
| Guinea Ecuatorial | GNQ | 16 |  |  |  |  |  |  |  |  | 1 |  |  | 3 | 6 |
| Guinea-Bisáu | GNB | 6 |  |  |  |  |  |  |  |  |  |  | 2 | 2 | 2 |
| Guyana | GUY | 195 |  |  |  |  |  |  |  |  | 2 | 18 | 25 | 37 | 28 |
| Haití | HTI | 190 |  |  |  |  |  |  |  |  | 3 | 10 | 70 | 51 | 21 |
| Honduras | HND | 156 |  |  |  |  |  |  |  |  |  | 21 | 34 | 31 | 55 |
| Hong Kong | HKG | 32 |  |  |  |  |  |  |  |  |  |  |  | 16 | 8 |
| Hungría | HUN | 869 |  |  |  |  |  |  |  | 3 | 37 | 18 | 47 | 254 | 97 |
| India | IND | 973 |  |  |  |  |  |  |  | 1 | 52 | 28 | 108 | 357 | 63 |
| Indonesia | IDN | 1,105 | 1 |  |  |  |  |  | 1 |  | 11 | 114 | 50 | 80 | 112 |
| Irak | IRQ | 329 |  |  |  |  |  |  |  | 3 | 29 | 18 | 24 | 81 | 53 |
| Irlanda | IRL | 1,339 |  |  |  |  |  |  |  | 1 | 24 | 46 | 63 | 503 | 21 |
| Irán | IRN | 301 |  |  |  |  |  |  |  | 5 | 36 | 14 | 34 | 110 | 34 |
| Isla Norfolk | NFK | 358 |  |  |  |  |  |  |  |  |  | 1 | 26 | 225 | 104 |
| Isla Santa Elena | SHN | 34 |  |  |  |  |  |  |  |  | 1 | 1 | 5 | 21 | 1 |
| Isla de Man | IMN | 25 |  |  |  |  |  |  |  |  |  |  | 1 | 19 |  |
| Islandia | ISL | 70 |  |  |  |  |  |  |  |  | 2 | 6 | 5 | 27 | 5 |
| Islas Caimán | CYM | 8 |  |  |  |  |  |  |  |  |  |  | 1 | 1 | 6 |
| Islas Feroe | FRO | 4 |  |  |  |  |  |  |  |  |  | 1 | 1 | 2 |  |
| Islas Georgias del Sur y Sandwich del Sur | SGS | 2 |  |  |  |  |  |  |  |  |  |  |  |  | 1 |
| Islas Malvinas | FLK | 20 |  |  |  |  |  |  |  |  |  | 6 | 4 | 4 | 3 |
| Islas Marianas del Norte | MNP | 22 |  |  |  |  |  |  |  |  |  |  |  | 2 | 17 |
| Islas Marshall | MHL | 14 |  |  |  |  |  |  |  |  |  |  |  | 3 | 11 |
| Islas Pitcairn | PCN | 7 |  |  |  |  |  |  |  |  |  |  | 1 | 1 | 5 |
| Islas Salomón | SLB | 18 |  |  |  |  |  |  |  |  | 1 | 2 | 1 | 3 | 10 |
| Islas Turcas y Caicos | TCA | 6 |  |  |  |  |  |  |  |  |  |  | 2 | 2 | 2 |
| Islas Vírgenes Británicas | VGB | 8 |  |  |  |  |  |  |  |  |  |  | 2 | 1 | 5 |
| Islas Vírgenes de los Estados Unidos | VIR | 99 |  |  |  |  |  |  |  |  |  | 1 | 48 | 2 | 43 |
| Israel | ISR | 1,109 |  |  |  |  |  |  |  | 8 | 50 | 54 | 137 | 389 | 74 |
| Italia | ITA | 3,327 | 1 |  |  |  |  |  |  | 8 | 174 | 171 | 158 | 724 | 220 |
| Jamaica | JAM | 227 |  |  |  |  |  |  |  |  | 1 | 14 | 79 | 81 | 36 |
| Japón | JPN | 940 |  |  |  |  |  |  |  | 1 | 4 | 31 | 41 | 248 | 209 |
| Jersey | JEY | 13 |  |  |  |  |  |  |  |  |  | 4 |  | 8 |  |
| Jordania | JOR | 378 |  |  |  |  |  |  |  | 1 | 37 | 16 | 22 | 148 | 27 |
| Kazajistán | KAZ | 95 |  |  |  |  |  |  |  | 1 | 15 | 15 | 4 | 21 | 11 |
| Kenia | KEN | 165 |  |  |  |  |  |  |  |  | 1 | 4 | 1 | 21 | 105 |
| Kirguistán | KGZ | 36 |  |  |  |  |  |  |  |  | 7 | 2 |  | 15 | 8 |
| Kiribati | KIR | 19 |  |  |  |  |  |  |  |  |  |  |  | 14 | 5 |
| Kosovo | KOS | 31 |  |  |  |  |  |  |  |  | 1 | 2 | 2 |  | 12 |
| Kuwait | KWT | 42 |  |  |  |  |  |  |  | 3 | 6 | 3 | 10 | 6 | 8 |
| Laos | LAO | 55 |  |  |  |  |  |  |  | 1 | 3 |  |  | 8 | 15 |
| Lesoto | LSO | 85 |  |  |  |  |  |  |  |  |  |  | 1 | 12 | 67 |
| Letonia | LVA | 123 |  |  |  |  |  |  |  | 2 | 10 | 9 | 9 | 17 | 17 |
| Liberia | LBR | 80 |  |  |  |  |  |  |  |  | 1 | 2 | 4 | 32 | 29 |
| Libia | LBY | 233 |  |  |  |  |  |  |  | 6 | 21 | 17 | 9 | 28 | 81 |
| Liechtenstein | LIE | 11 |  |  |  |  |  |  |  | 1 |  |  |  | 2 |  |
| Lituania | LTU | 209 |  |  |  |  |  |  |  | 2 | 10 | 9 | 15 | 18 | 34 |
| Luxemburgo | LUX | 224 |  |  |  |  |  |  |  |  | 6 | 16 | 27 | 24 | 19 |
| Líbano | LBN | 301 |  |  |  |  |  |  |  | 1 | 17 | 6 | 12 | 155 | 54 |
| Macao | MAC | 27 |  |  |  |  |  |  |  |  |  |  | 4 | 7 | 14 |
| Macedonia del Norte | MKD | 113 |  |  |  |  |  |  |  | 2 | 13 | 11 | 5 | 19 | 22 |
| Madagascar | MDG | 127 |  |  |  |  |  |  |  |  | 3 | 5 | 14 | 39 | 36 |
| Malasia | MYS | 194 |  |  |  |  |  |  |  |  | 4 | 5 | 3 | 22 | 28 |
| Malaui | MWI | 34 |  |  |  |  |  |  |  |  | 1 |  | 2 | 13 | 14 |
| Maldivas | MDV | 4 |  |  |  |  |  |  |  |  |  |  | 1 |  | 3 |
| Malta | MLT | 73 |  |  |  |  |  |  |  |  | 9 | 12 | 10 | 18 | 6 |
| Malí | MLI | 85 |  |  |  |  |  |  |  |  | 2 | 5 | 7 | 12 | 9 |
| Marruecos | MAR | 225 |  |  |  |  |  |  |  | 1 | 10 | 17 | 19 | 64 | 36 |
| Mauricio | MUS | 31 |  |  |  |  |  |  |  |  |  | 1 | 6 | 19 | 3 |
| Mauritania | MRT | 63 |  |  |  |  |  |  |  |  | 4 | 3 | 11 | 10 | 8 |
| Moldavia | MDA | 81 |  |  |  |  |  |  |  | 1 | 3 | 5 | 11 | 21 | 10 |
| Mongolia | MNG | 73 |  |  |  |  |  |  |  |  | 1 | 8 | 3 | 22 | 29 |
| Montenegro | MNE | 81 |  |  |  |  |  |  |  |  | 6 | 7 | 5 | 13 | 13 |
| Montserrat | MSR | 7 |  |  |  |  |  |  |  |  |  |  |  | 6 | 1 |
| Mozambique | MOZ | 154 |  |  |  |  |  |  |  |  | 3 | 5 | 11 | 51 | 36 |
| México | MEX | 2,372 |  |  |  |  |  |  |  | 2 | 29 | 75 | 204 | 548 | 1,069 |
| Mónaco | MCO | 3 |  |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| Namibia | NAM | 117 |  |  |  |  |  |  |  |  | 2 |  | 6 | 41 | 24 |
| Nauru | NRU | 3 |  |  |  |  |  |  |  |  |  |  |  |  | 3 |
| Nepal | NPL | 32 |  |  |  |  |  |  |  | 1 | 2 | 2 |  | 5 | 7 |
| Nicaragua | NIC | 144 |  |  |  |  |  |  |  |  |  | 21 | 18 | 51 | 41 |
| Nigeria | NGA | 103 |  |  |  |  |  |  |  |  | 2 | 8 | 7 | 8 | 38 |
| Noruega | NOR | 675 |  |  |  |  |  |  |  | 2 | 3 | 15 | 15 | 172 | 19 |
| Nueva Caledonia | NCL | 8 |  |  |  |  |  |  |  |  |  |  | 1 | 2 | 5 |
| Nueva Zelanda | NZL | 148 |  |  |  |  |  |  |  |  |  |  | 3 | 99 | 16 |
| Níger | NER | 70 |  |  |  |  |  |  |  |  | 4 | 5 | 3 | 5 | 26 |
| Omán | OMN | 60 |  |  |  |  |  |  |  | 4 | 10 | 4 | 11 | 10 | 7 |
| PSX | PSX | 298 |  |  |  |  |  |  |  | 1 | 17 | 8 | 7 | 106 | 2 |
| Pakistán | PAK | 225 |  |  |  |  |  |  |  |  | 24 | 5 | 7 | 91 | 26 |
| Palaos | PLW | 24 |  |  |  |  |  |  |  |  |  |  |  | 5 | 15 |
| Palestina | PSE | 821 |  |  |  |  |  |  |  | 6 | 38 | 29 | 47 | 382 | 81 |
| Panamá | PAN | 240 |  |  |  |  |  |  |  |  | 1 | 34 | 33 | 52 | 79 |
| Papúa Nueva Guinea | PNG | 59 |  |  |  |  |  |  |  |  | 1 | 4 | 2 | 14 | 27 |
| Paraguay | PRY | 121 |  |  |  |  |  |  |  |  |  | 11 | 11 | 49 | 34 |
| Países Bajos | NLD | 12,937 |  |  |  |  |  |  |  |  | 50 | 201 | 276 | 274 | 48 |
| Perú | PER | 339 |  |  |  |  |  |  |  |  | 13 | 26 | 25 | 141 | 99 |
| Polinesia Francesa | PYF | 36 |  |  |  |  |  |  |  |  |  |  | 6 | 25 | 3 |
| Polonia | POL | 1,807 |  |  |  |  |  |  |  | 6 | 40 | 35 | 67 | 292 | 160 |
| Portugal | PRT | 1,043 |  |  |  |  |  |  |  | 2 | 29 | 37 | 83 | 394 | 31 |
| Puerto Rico | PRI | 970 |  |  |  |  |  |  |  |  |  | 10 | 40 | 22 | 878 |
| Reino Unido | GBR | 6,460 |  |  |  |  |  |  |  | 1 | 53 | 282 | 373 | 1,439 | 106 |
| República Centroafricana | CAF | 153 |  |  |  |  |  |  |  |  |  | 2 | 3 | 8 | 112 |
| República Checa | CZE | 932 |  |  |  |  |  |  |  | 1 | 16 | 27 | 29 | 155 | 169 |
| República Democrática del Congo | COD | 216 |  |  |  |  |  |  |  |  | 3 | 6 | 9 | 31 | 124 |
| República Dominicana | DOM | 138 |  |  |  |  |  |  |  |  | 3 | 10 | 36 | 34 | 29 |
| República Turca del Norte de Chipre | CYN | 15 |  |  |  |  |  |  |  |  | 2 | 5 |  |  |  |
| República de China | TWN | 91 |  |  |  |  |  |  |  |  |  | 6 |  | 11 | 45 |
| República del Congo | COG | 111 |  |  |  |  |  |  |  | 1 | 1 | 5 | 14 | 33 | 31 |
| Ruanda | RWA | 18 |  |  |  |  |  |  |  |  |  |  |  | 3 | 11 |
| Rumania | ROU | 897 |  |  |  |  |  |  |  | 2 | 36 | 19 | 36 | 135 | 142 |
| Rusia | RUS | 2,692 |  |  |  |  |  |  |  | 5 | 55 | 97 | 149 | 930 | 670 |
| SAH | SAH | 4 |  |  |  |  |  |  |  |  |  | 2 |  | 1 |  |
| SDS | SDS | 82 |  |  |  |  |  |  |  |  |  | 1 |  | 10 | 19 |
| Sahara Occidental | ESH | 11 |  |  |  |  |  |  |  |  |  | 2 |  | 5 | 3 |
| Samoa | WSM | 26 |  |  |  |  |  |  |  |  |  |  |  | 20 | 6 |
| Samoa Estadounidense | ASM | 24 |  |  |  |  |  |  |  |  |  |  |  | 13 | 6 |
| San Bartolomé | BLM | 5 |  |  |  |  |  |  |  |  |  |  | 3 | 2 |  |
| San Cristóbal y Nieves | KNA | 15 |  |  |  |  |  |  |  |  |  | 2 | 12 | 1 |  |
| San Marino | SMR | 1 |  |  |  |  |  |  |  |  |  |  |  | 1 |  |
| San Martín | MAF | 25 |  |  |  |  |  |  |  |  |  |  | 5 | 12 | 5 |
| San Martín | SXM | 15 |  |  |  |  |  |  |  | 1 |  |  | 4 | 7 |  |
| San Pedro y Miquelón | SPM | 7 |  |  |  |  |  |  |  |  |  |  | 1 | 5 | 1 |
| San Vicente y las Granadinas | VCT | 13 |  |  |  |  |  |  |  |  |  |  | 3 | 9 | 1 |
| Santa Lucía | LCA | 15 |  |  |  |  |  |  |  |  |  | 1 | 10 | 2 | 2 |
| Santo Tomé y Príncipe | STP | 2 |  |  |  |  |  |  |  |  |  | 1 |  |  | 1 |
| Senegal | SEN | 66 |  |  |  |  |  |  |  |  | 1 | 3 | 20 | 14 | 10 |
| Serbia | SRB | 435 |  |  |  |  |  |  |  | 4 | 24 | 11 | 23 | 118 | 56 |
| Seychelles | SYC | 2 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |
| Sierra Leona | SLE | 62 |  |  |  |  |  |  |  |  | 1 | 2 | 9 | 11 | 35 |
| Singapur | SGP | 27 |  |  |  |  |  |  |  |  |  |  |  | 14 | 4 |
| Siria | SYR | 565 |  |  |  |  |  |  |  | 4 | 40 | 27 | 53 | 257 | 47 |
| Somalia | SOM | 137 |  |  |  |  |  |  |  |  | 7 | 6 | 3 | 10 | 87 |
| Somalilandia | SOL | 53 |  |  |  |  |  |  |  |  | 2 | 4 |  | 13 | 21 |
| Sri Lanka | LKA | 144 |  |  |  |  |  |  |  | 1 | 6 | 9 | 12 | 46 | 17 |
| Suazilandia | SWZ | 38 |  |  |  |  |  |  |  |  |  |  |  | 3 | 33 |
| Sudáfrica | ZAF | 461 |  |  |  |  |  |  |  |  | 2 | 1 | 19 | 177 | 146 |
| Sudán | SDN | 319 |  |  |  |  |  |  |  | 2 | 8 | 15 | 10 | 66 | 134 |
| Sudán del Sur | SSD | 198 |  |  |  |  |  |  |  |  | 1 | 4 | 2 | 17 | 89 |
| Suecia | SWE | 873 |  |  |  |  |  |  |  | 2 | 10 | 30 | 23 | 151 | 21 |
| Suiza | CHE | 1,487 | 1 |  |  |  |  |  |  | 2 | 41 | 41 | 69 | 286 | 105 |
| Surinam | SUR | 333 |  |  |  |  |  |  |  |  | 2 | 12 | 16 | 13 | 18 |
| Tailandia | THA | 103 |  |  |  |  |  |  |  |  | 5 | 3 | 9 | 19 | 30 |
| Tanzania | TZA | 184 |  |  |  |  |  |  |  |  | 2 | 2 | 2 | 46 | 73 |
| Tayikistán | TJK | 43 |  |  |  |  |  |  |  |  | 6 |  |  | 18 | 11 |
| Territorio Británico del Océano Índico | IOT | 1 |  |  |  |  |  |  |  |  |  |  |  |  | 1 |
| Territorios Australianos del Océano Índico | IOA | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Tierras Australes y Antárticas Francesas | ATF | 4 |  |  |  |  |  |  |  |  |  |  |  | 1 |  |
| Timor Oriental | TLS | 9 |  |  |  |  |  |  |  |  |  |  |  |  | 2 |
| Togo | TGO | 20 |  |  |  |  |  |  |  |  |  |  | 2 | 1 | 6 |
| Tonga | TON | 6 |  |  |  |  |  |  |  |  |  |  | 1 | 4 | 1 |
| Trinidad y Tobago | TTO | 36 |  |  |  |  |  |  |  |  |  | 5 | 12 | 5 | 13 |
| Turkmenistán | TKM | 94 |  |  |  |  |  |  |  |  | 14 | 5 | 2 | 41 | 15 |
| Turquía | TUR | 907 |  |  |  |  |  |  |  | 3 | 56 | 49 | 91 | 333 | 119 |
| Tuvalu | TUV | 6 |  |  |  |  |  |  |  |  |  |  |  | 5 | 1 |
| Túnez | TUN | 222 |  |  |  |  |  |  |  | 2 | 24 | 5 | 10 | 52 | 71 |
| UMI | UMI | 2 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |
| USG | USG | 3 |  |  |  |  |  |  |  |  |  |  | 1 | 1 |  |
| Ucrania | UKR | 586 |  |  |  |  |  |  | 2 | 4 | 28 | 39 | 35 | 63 | 70 |
| Uganda | UGA | 168 |  |  |  |  |  |  |  |  | 1 | 3 | 3 | 13 | 124 |
| Uruguay | URY | 121 |  |  |  |  |  |  |  |  | 1 | 12 | 11 | 52 | 35 |
| Uzbekistán | UZB | 82 |  |  |  |  |  |  |  |  | 7 | 4 | 2 | 41 | 13 |
| Vanuatu | VUT | 4 |  |  |  |  |  |  |  |  |  |  |  | 1 | 3 |
| Venezuela | VEN | 262 |  |  |  |  |  |  |  |  | 6 | 40 | 46 | 59 | 53 |
| Vietnam | VNM | 213 |  |  |  |  |  |  |  | 1 | 4 | 3 | 3 | 18 | 37 |
| Yemen | YEM | 332 |  |  |  |  |  |  |  | 4 | 13 | 6 | 11 | 30 | 232 |
| Yibuti | DJI | 17 |  |  |  |  |  |  |  |  | 1 | 1 | 2 | 6 | 5 |
| Zambia | ZMB | 97 |  |  |  |  |  |  |  |  | 1 | 3 | 4 | 19 | 45 |
| Zimbabue | ZWE | 102 |  |  |  |  |  |  |  |  | 2 |  | 5 | 25 | 43 |
| Åland | ALA | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |
