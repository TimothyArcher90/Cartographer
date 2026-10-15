# Biblioteca de Cartographer

Documento generado por `scripts/comprender.py`. No editar a mano.

- Mapas analizados: **478,803** · con país asignado: **372,407** · sin país: 106,396
  (sobre todo mapamundis, cartas oceánicas o registros sin datos de lugar).
- Países con mapas: **243**.
- Tipos: general 230,570, topográfico 200,995, plano urbano 21,502, militar 7,521, histórico/temático 6,316, mapamundi 4,161, ferroviario/viario 4,144, carta náutica 3,117, portulano 329, ptolemaico 148.
- Escalas: local o ciudad 245,025, desconocida 209,007, provincia o comarca 14,152, región o país 6,100, continente 2,997, mundo 1,522.

Cómo se asigna un país: por **nombre** actual (25+ idiomas, Natural Earth), por **nombre histórico**
(`catalogo/nombres_historicos.json`) o por **coordenadas** de la cobertura del mapa. Cada mapa guarda
la vía en el campo `via`; las asignaciones por coordenadas de mapas grandes pueden incluir países
vecinos. Los siglos salen del año de los metadatos de cada archivo y pueden tener errores puntuales.

Mapas de un país: `catalogo/biblioteca/paises/<ISO3>.jsonl.gz` o
`python scripts/buscar_lugar.py "<país>"`.

| País | ISO | Total | Antes del s. IX | IX | X | XI | XII | XIII | XIV | XV | XVI | XVII | XVIII | XIX | XX |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Afganistán | AFG | 348 |  |  |  |  |  |  |  |  | 19 | 6 | 8 | 135 | 93 |
| Albania | ALB | 251 |  |  |  |  |  |  |  | 2 | 21 | 22 | 18 | 59 | 46 |
| Alemania | DEU | 12,344 | 1 |  |  |  |  |  |  | 2 | 88 | 197 | 304 | 1,063 | 708 |
| Andorra | AND | 16 |  |  |  |  |  |  |  |  |  |  |  | 1 | 11 |
| Angola | AGO | 180 |  |  |  |  |  |  |  |  | 2 | 9 | 12 | 47 | 82 |
| Anguila | AIA | 7 |  |  |  |  |  |  |  |  |  |  | 6 | 1 |  |
| Antigua y Barbuda | ATG | 23 |  |  |  |  |  |  |  |  |  | 1 | 13 | 7 | 1 |
| Antártida | ATA | 80 |  |  |  |  |  |  |  |  |  | 8 | 11 | 8 | 45 |
| Arabia Saudita | SAU | 433 |  |  |  |  |  |  |  | 6 | 41 | 27 | 46 | 109 | 113 |
| Argelia | DZA | 309 |  |  |  |  |  |  |  | 2 | 19 | 20 | 29 | 81 | 48 |
| Argentina | ARG | 663 |  |  |  |  |  |  |  |  | 3 | 91 | 84 | 114 | 309 |
| Armenia | ARM | 102 |  |  |  |  |  |  |  | 1 | 10 | 5 | 13 | 33 | 17 |
| Aruba | ABW | 22 |  |  |  |  |  |  |  |  |  |  | 2 | 6 | 4 |
| Australia | AUS | 1,928 |  |  |  |  |  |  |  |  |  | 6 | 16 | 263 | 55 |
| Austria | AUT | 1,528 | 1 |  |  |  |  |  |  | 2 | 36 | 36 | 60 | 358 | 240 |
| Azerbaiyán | AZE | 88 |  |  |  |  |  |  |  | 1 | 8 | 3 | 5 | 28 | 19 |
| Bahamas | BHS | 110 |  |  |  |  |  |  |  |  |  | 3 | 43 | 46 | 13 |
| Bangladés | BGD | 51 |  |  |  |  |  |  |  | 1 | 2 | 5 | 4 | 7 | 8 |
| Barbados | BRB | 78 |  |  |  |  |  |  |  |  |  | 5 | 31 | 6 | 20 |
| Baréin | BHR | 48 |  |  |  |  |  |  |  | 2 | 4 | 4 | 6 | 7 | 15 |
| Belice | BLZ | 54 |  |  |  |  |  |  |  |  |  | 9 | 5 | 12 | 25 |
| Benín | BEN | 42 |  |  |  |  |  |  |  |  | 3 | 6 |  | 2 | 13 |
| Bermudas | BMU | 75 |  |  |  |  |  |  |  |  |  | 11 | 29 | 21 | 7 |
| Bielorrusia | BLR | 241 |  |  |  |  |  |  |  | 3 | 22 | 19 | 25 | 21 | 54 |
| Birmania | MMR | 149 |  |  |  |  |  |  |  |  | 8 | 5 | 14 | 38 | 36 |
| Bolivia | BOL | 159 |  |  |  |  |  |  |  |  | 4 | 14 | 8 | 53 | 56 |
| Bosnia y Herzegovina | BIH | 427 |  |  |  |  |  |  |  | 6 | 36 | 13 | 20 | 100 | 62 |
| Botsuana | BWA | 153 |  |  |  |  |  |  |  |  | 1 |  | 5 | 46 | 51 |
| Brasil | BRA | 1,317 |  |  |  |  |  |  |  |  | 11 | 156 | 213 | 389 | 336 |
| Brunéi | BRN | 17 |  |  |  |  |  |  |  |  |  |  |  | 6 | 4 |
| Bulgaria | BGR | 382 |  |  |  |  |  |  | 1 | 2 | 19 | 18 | 40 | 113 | 65 |
| Burkina Faso | BFA | 52 |  |  |  |  |  |  |  |  | 1 | 5 | 3 | 7 | 11 |
| Burundi | BDI | 37 |  |  |  |  |  |  |  |  |  |  |  | 3 | 30 |
| Bután | BTN | 36 |  |  |  |  |  |  |  |  |  |  | 1 | 9 | 11 |
| Bélgica | BEL | 4,604 |  |  |  |  |  |  |  | 2 | 47 | 123 | 333 | 353 | 264 |
| Cabo Verde | CPV | 87 |  |  |  |  |  |  |  |  | 2 | 14 | 36 | 21 | 2 |
| Camboya | KHM | 89 |  |  |  |  |  |  |  |  | 1 | 1 | 1 | 10 | 44 |
| Camerún | CMR | 96 |  |  |  |  |  |  |  |  | 1 | 4 | 8 | 9 | 42 |
| Canadá | CAN | 5,116 |  |  |  |  |  |  |  |  | 10 | 75 | 1,231 | 1,455 | 1,540 |
| Catar | QAT | 35 |  |  |  |  |  |  |  | 3 | 5 | 3 | 8 | 5 | 8 |
| Chad | TCD | 67 |  |  |  |  |  |  |  |  |  | 3 | 4 | 10 | 29 |
| Chile | CHL | 523 |  |  |  |  |  |  |  | 1 | 2 | 101 | 121 | 148 | 97 |
| China | CHN | 2,723 |  |  |  |  | 7 | 1 | 1 | 4 | 31 | 91 | 309 | 964 | 846 |
| Chipre | CYP | 173 |  |  |  |  |  |  |  | 1 | 10 | 13 | 9 | 18 | 90 |
| Ciudad del Vaticano | VAT | 38 |  |  |  |  |  |  |  |  |  | 24 | 1 | 3 | 3 |
| Colombia | COL | 423 |  |  |  |  |  |  |  |  | 6 | 52 | 92 | 87 | 111 |
| Comoras | COM | 8 |  |  |  |  |  |  |  |  |  |  |  | 2 | 6 |
| Corea del Norte | PRK | 130 |  |  |  |  |  |  |  |  | 1 | 9 | 11 | 13 | 54 |
| Corea del Sur | KOR | 697 |  |  |  |  |  |  |  |  | 2 | 11 | 44 | 101 | 192 |
| Costa Rica | CRI | 147 |  |  |  |  |  |  |  |  |  | 14 | 13 | 38 | 72 |
| Costa de Marfil | CIV | 78 |  |  |  |  |  |  |  |  | 2 | 5 | 9 | 10 | 22 |
| Croacia | HRV | 726 |  |  |  |  |  |  |  | 6 | 40 | 17 | 32 | 187 | 69 |
| Cuba | CUB | 744 |  |  |  |  |  |  |  |  | 5 | 89 | 186 | 171 | 168 |
| Curazao | CUW | 81 |  |  |  |  |  |  |  |  |  |  | 19 | 10 | 2 |
| Dinamarca | DNK | 1,020 |  |  |  |  |  |  | 1 |  | 8 | 46 | 44 | 270 | 63 |
| Dominica | DMA | 15 |  |  |  |  |  |  |  |  |  |  | 12 | 2 |  |
| ESB | ESB | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ecuador | ECU | 216 |  |  |  |  |  |  |  |  | 6 | 18 | 30 | 58 | 67 |
| Egipto | EGY | 1,483 |  |  |  |  |  |  |  | 3 | 41 | 37 | 108 | 659 | 452 |
| El Salvador | SLV | 95 |  |  |  |  |  |  |  |  |  | 1 | 3 | 40 | 44 |
| Emiratos Árabes Unidos | ARE | 43 |  |  |  |  |  |  |  | 3 | 6 | 4 | 10 | 9 | 6 |
| Eritrea | ERI | 383 |  |  |  |  |  |  |  |  | 1 | 6 | 5 | 95 | 254 |
| Eslovaquia | SVK | 488 |  |  |  |  |  |  |  | 2 | 16 | 13 | 19 | 93 | 97 |
| Eslovenia | SVN | 292 |  |  |  |  |  |  |  | 2 | 18 | 5 | 3 | 14 | 106 |
| España | ESP | 5,164 |  |  |  |  |  |  | 1 | 5 | 82 | 204 | 959 | 2,058 | 522 |
| Estados Federados de Micronesia | FSM | 44 |  |  |  |  |  |  |  |  |  | 1 | 1 | 11 | 25 |
| Estados Unidos | USA | 277,837 | 2 |  |  |  |  |  |  | 1 | 23 | 442 | 4,550 | 42,613 | 199,005 |
| Estonia | EST | 948 |  |  |  |  |  |  |  |  | 1 | 11 | 13 | 78 | 486 |
| Etiopía | ETH | 404 |  |  |  |  |  |  |  | 1 | 8 | 15 | 10 | 104 | 193 |
| Filipinas | PHL | 331 |  |  |  |  |  |  |  |  | 3 | 5 | 48 | 61 | 174 |
| Finlandia | FIN | 197 |  |  |  |  |  |  |  | 1 | 8 | 15 | 17 | 30 | 28 |
| Fiyi | FJI | 43 |  |  |  |  |  |  |  |  |  | 1 |  | 29 | 10 |
| Francia | FRA | 10,936 |  |  |  |  | 1 |  | 1 | 2 | 128 | 408 | 1,319 | 3,450 | 441 |
| GIB | GIB | 5 |  |  |  |  |  |  |  |  |  |  | 5 |  |  |
| Gabón | GAB | 52 |  |  |  |  |  |  |  |  | 1 | 5 | 7 | 6 | 12 |
| Gambia | GMB | 24 |  |  |  |  |  |  |  |  |  | 1 | 10 | 8 | 4 |
| Georgia | GEO | 228 |  |  |  |  |  |  |  | 1 | 11 | 4 | 47 | 59 | 40 |
| Ghana | GHA | 78 |  |  |  |  |  |  |  |  | 2 | 7 | 7 | 8 | 17 |
| Granada | GRD | 276 |  |  |  |  |  |  |  |  |  | 18 | 50 | 179 | 13 |
| Grecia | GRC | 1,136 |  |  |  |  |  |  |  | 3 | 70 | 91 | 84 | 463 | 94 |
| Groenlandia | GRL | 141 |  |  |  |  |  |  | 1 |  | 4 | 10 | 26 | 74 | 13 |
| Guam | GUM | 24 |  |  |  |  |  |  |  |  |  |  | 4 | 6 | 3 |
| Guatemala | GTM | 131 |  |  |  |  |  |  |  |  | 1 | 15 | 10 | 36 | 54 |
| Guernsey | GGY | 161 |  |  |  |  |  |  |  |  |  | 4 |  | 61 | 94 |
| Guinea | GIN | 78 |  |  |  |  |  |  |  |  | 1 | 8 | 29 | 10 | 12 |
| Guinea Ecuatorial | GNQ | 32 |  |  |  |  |  |  |  |  | 1 |  | 2 | 8 | 15 |
| Guinea-Bisáu | GNB | 6 |  |  |  |  |  |  |  |  |  |  | 2 | 2 | 2 |
| Guyana | GUY | 219 |  |  |  |  |  |  |  |  | 2 | 19 | 28 | 40 | 40 |
| Haití | HTI | 313 |  |  |  |  |  |  |  |  | 3 | 16 | 87 | 59 | 108 |
| Honduras | HND | 211 |  |  |  |  |  |  |  |  |  | 26 | 44 | 55 | 69 |
| Hong Kong | HKG | 41 |  |  |  |  |  |  |  |  |  |  |  | 19 | 12 |
| Hungría | HUN | 973 |  |  |  |  |  |  |  | 3 | 37 | 25 | 57 | 278 | 102 |
| India | IND | 1,363 |  |  |  |  |  |  |  | 1 | 55 | 36 | 140 | 542 | 147 |
| Indonesia | IDN | 1,277 | 1 |  |  |  |  |  | 1 |  | 11 | 117 | 66 | 106 | 142 |
| Irak | IRQ | 445 |  |  |  |  |  |  |  | 3 | 29 | 19 | 24 | 83 | 127 |
| Irlanda | IRL | 1,520 |  |  |  |  |  |  |  | 1 | 24 | 63 | 97 | 546 | 30 |
| Irán | IRN | 387 |  |  |  |  |  |  |  | 5 | 36 | 15 | 41 | 147 | 60 |
| Isla Norfolk | NFK | 424 |  |  |  |  |  |  |  |  |  | 1 | 32 | 277 | 108 |
| Isla Santa Elena | SHN | 47 |  |  |  |  |  |  |  |  | 1 | 2 | 5 | 30 | 3 |
| Isla de Man | IMN | 29 |  |  |  |  |  |  |  |  |  |  | 2 | 19 |  |
| Islandia | ISL | 98 |  |  |  |  |  |  |  |  | 2 | 8 | 8 | 38 | 16 |
| Islas Caimán | CYM | 8 |  |  |  |  |  |  |  |  |  |  | 1 | 1 | 6 |
| Islas Feroe | FRO | 4 |  |  |  |  |  |  |  |  |  | 1 | 1 | 2 |  |
| Islas Georgias del Sur y Sandwich del Sur | SGS | 2 |  |  |  |  |  |  |  |  |  |  |  |  | 1 |
| Islas Malvinas | FLK | 32 |  |  |  |  |  |  |  |  |  | 11 | 10 | 5 | 3 |
| Islas Marianas del Norte | MNP | 24 |  |  |  |  |  |  |  |  |  |  |  | 2 | 19 |
| Islas Marshall | MHL | 16 |  |  |  |  |  |  |  |  |  |  |  | 3 | 13 |
| Islas Pitcairn | PCN | 9 |  |  |  |  |  |  |  |  |  |  | 1 | 1 | 7 |
| Islas Salomón | SLB | 31 |  |  |  |  |  |  |  |  | 1 | 2 | 1 | 3 | 10 |
| Islas Turcas y Caicos | TCA | 6 |  |  |  |  |  |  |  |  |  |  | 2 | 2 | 2 |
| Islas Vírgenes Británicas | VGB | 8 |  |  |  |  |  |  |  |  |  |  | 2 | 1 | 5 |
| Islas Vírgenes de los Estados Unidos | VIR | 99 |  |  |  |  |  |  |  |  |  | 1 | 48 | 2 | 43 |
| Israel | ISR | 1,190 |  |  |  |  |  |  |  | 9 | 51 | 58 | 151 | 407 | 98 |
| Italia | ITA | 4,120 | 1 |  |  |  |  |  |  | 8 | 182 | 319 | 269 | 887 | 253 |
| Jamaica | JAM | 661 |  |  |  |  |  |  |  |  | 1 | 14 | 103 | 482 | 38 |
| Japón | JPN | 1,071 |  |  |  |  |  |  |  | 1 | 4 | 34 | 126 | 277 | 219 |
| Jersey | JEY | 13 |  |  |  |  |  |  |  |  |  | 4 |  | 8 |  |
| Jordania | JOR | 380 |  |  |  |  |  |  |  | 1 | 37 | 18 | 22 | 148 | 27 |
| Kazajistán | KAZ | 105 |  |  |  |  |  |  |  | 1 | 15 | 15 | 4 | 21 | 17 |
| Kenia | KEN | 204 |  |  |  |  |  |  |  |  | 1 | 4 | 1 | 21 | 139 |
| Kirguistán | KGZ | 42 |  |  |  |  |  |  |  |  | 7 | 2 |  | 15 | 10 |
| Kiribati | KIR | 21 |  |  |  |  |  |  |  |  |  |  |  | 14 | 7 |
| Kosovo | KOS | 44 |  |  |  |  |  |  |  |  | 1 | 2 | 2 |  | 21 |
| Kuwait | KWT | 54 |  |  |  |  |  |  |  | 3 | 6 | 3 | 10 | 6 | 12 |
| Laos | LAO | 60 |  |  |  |  |  |  |  | 1 | 3 |  |  | 8 | 16 |
| Lesoto | LSO | 89 |  |  |  |  |  |  |  |  |  |  | 1 | 12 | 71 |
| Letonia | LVA | 190 |  |  |  |  |  |  |  | 2 | 10 | 11 | 11 | 18 | 75 |
| Liberia | LBR | 124 |  |  |  |  |  |  |  |  | 1 | 2 | 4 | 63 | 36 |
| Libia | LBY | 250 |  |  |  |  |  |  |  | 6 | 21 | 17 | 10 | 31 | 93 |
| Liechtenstein | LIE | 12 |  |  |  |  |  |  |  | 1 |  | 1 |  | 2 |  |
| Lituania | LTU | 268 |  |  |  |  |  |  |  | 2 | 10 | 12 | 39 | 18 | 47 |
| Luxemburgo | LUX | 270 |  |  |  |  |  |  |  |  | 6 | 21 | 42 | 35 | 19 |
| Líbano | LBN | 343 |  |  |  |  |  |  |  | 1 | 17 | 6 | 12 | 178 | 66 |
| Macao | MAC | 61 |  |  |  |  |  |  |  |  |  |  | 9 | 13 | 29 |
| Macedonia del Norte | MKD | 114 |  |  |  |  |  |  |  | 2 | 13 | 11 | 5 | 19 | 23 |
| Madagascar | MDG | 143 |  |  |  |  |  |  |  |  | 3 | 8 | 19 | 41 | 36 |
| Malasia | MYS | 201 |  |  |  |  |  |  |  |  | 4 | 5 | 5 | 22 | 32 |
| Malaui | MWI | 34 |  |  |  |  |  |  |  |  | 1 |  | 2 | 13 | 14 |
| Maldivas | MDV | 11 |  |  |  |  |  |  |  |  |  |  | 3 |  | 7 |
| Malta | MLT | 124 |  |  |  |  |  |  |  |  | 9 | 15 | 47 | 25 | 6 |
| Malí | MLI | 91 |  |  |  |  |  |  |  |  | 2 | 5 | 7 | 12 | 15 |
| Marruecos | MAR | 354 |  |  |  |  |  |  |  | 1 | 10 | 30 | 49 | 86 | 87 |
| Mauricio | MUS | 68 |  |  |  |  |  |  |  |  |  | 1 | 8 | 21 | 7 |
| Mauritania | MRT | 70 |  |  |  |  |  |  |  |  | 4 | 3 | 12 | 12 | 12 |
| Moldavia | MDA | 102 |  |  |  |  |  |  |  | 1 | 3 | 6 | 17 | 23 | 10 |
| Mongolia | MNG | 91 |  |  |  |  |  |  |  |  | 1 | 9 | 4 | 29 | 35 |
| Montenegro | MNE | 87 |  |  |  |  |  |  |  |  | 6 | 7 | 5 | 19 | 13 |
| Montserrat | MSR | 116 |  |  |  |  |  |  |  |  |  |  |  | 103 | 11 |
| Mozambique | MOZ | 167 |  |  |  |  |  |  |  |  | 3 | 5 | 11 | 52 | 43 |
| México | MEX | 2,665 |  |  |  |  |  |  |  | 2 | 40 | 98 | 253 | 701 | 1,096 |
| Mónaco | MCO | 8 |  |  |  |  |  |  |  |  |  |  | 3 | 1 | 3 |
| Namibia | NAM | 126 |  |  |  |  |  |  |  |  | 2 |  | 6 | 41 | 28 |
| Nauru | NRU | 5 |  |  |  |  |  |  |  |  |  |  |  |  | 5 |
| Nepal | NPL | 44 |  |  |  |  |  |  |  | 1 | 2 | 2 |  | 8 | 13 |
| Nicaragua | NIC | 218 |  |  |  |  |  |  |  |  |  | 24 | 20 | 101 | 58 |
| Nigeria | NGA | 116 |  |  |  |  |  |  |  |  | 2 | 8 | 7 | 8 | 51 |
| Noruega | NOR | 759 |  |  |  |  |  |  |  | 2 | 3 | 16 | 23 | 204 | 25 |
| Nueva Caledonia | NCL | 8 |  |  |  |  |  |  |  |  |  |  | 1 | 2 | 5 |
| Nueva Zelanda | NZL | 189 |  |  |  |  |  |  |  |  |  |  | 3 | 131 | 18 |
| Níger | NER | 70 |  |  |  |  |  |  |  |  | 4 | 5 | 3 | 5 | 26 |
| Omán | OMN | 62 |  |  |  |  |  |  |  | 4 | 10 | 4 | 11 | 10 | 9 |
| PSX | PSX | 298 |  |  |  |  |  |  |  | 1 | 17 | 8 | 7 | 106 | 2 |
| Pakistán | PAK | 368 |  |  |  |  |  |  |  |  | 24 | 6 | 10 | 97 | 113 |
| Palaos | PLW | 36 |  |  |  |  |  |  |  |  |  | 1 | 2 | 7 | 17 |
| Palestina | PSE | 911 |  |  |  |  |  |  |  | 6 | 38 | 31 | 60 | 434 | 93 |
| Panamá | PAN | 273 |  |  |  |  |  |  |  |  | 1 | 37 | 39 | 66 | 87 |
| Papúa Nueva Guinea | PNG | 63 |  |  |  |  |  |  |  |  | 1 | 4 | 2 | 14 | 31 |
| Paraguay | PRY | 156 |  |  |  |  |  |  |  |  |  | 12 | 27 | 57 | 41 |
| Países Bajos | NLD | 18,040 |  |  | 1 |  |  |  |  | 1 | 90 | 335 | 422 | 395 | 956 |
| Perú | PER | 440 |  |  |  |  |  |  |  |  | 15 | 43 | 50 | 168 | 110 |
| Polinesia Francesa | PYF | 69 |  |  |  |  |  |  |  |  |  | 1 | 35 | 26 | 5 |
| Polonia | POL | 2,661 |  |  |  |  |  |  |  | 6 | 40 | 50 | 147 | 520 | 440 |
| Portugal | PRT | 1,873 |  |  |  |  |  |  |  | 2 | 43 | 88 | 308 | 781 | 86 |
| Puerto Rico | PRI | 1,021 |  |  |  |  |  |  |  |  |  | 10 | 66 | 32 | 891 |
| Reino Unido | GBR | 7,544 |  |  |  |  |  |  |  | 1 | 53 | 426 | 611 | 1,651 | 338 |
| República Centroafricana | CAF | 153 |  |  |  |  |  |  |  |  |  | 2 | 3 | 8 | 112 |
| República Checa | CZE | 1,030 |  |  |  |  |  |  |  | 1 | 16 | 31 | 52 | 173 | 175 |
| República Democrática del Congo | COD | 218 |  |  |  |  |  |  |  |  | 3 | 6 | 9 | 31 | 126 |
| República Dominicana | DOM | 186 |  |  |  |  |  |  |  |  | 3 | 17 | 53 | 41 | 35 |
| República Turca del Norte de Chipre | CYN | 15 |  |  |  |  |  |  |  |  | 2 | 5 |  |  |  |
| República de China | TWN | 121 |  |  |  |  |  |  |  |  |  | 7 |  | 36 | 47 |
| República del Congo | COG | 136 |  |  |  |  |  |  |  | 1 | 1 | 5 | 15 | 39 | 45 |
| Ruanda | RWA | 24 |  |  |  |  |  |  |  |  |  |  |  | 3 | 17 |
| Rumania | ROU | 998 |  |  |  |  |  |  |  | 3 | 36 | 21 | 40 | 150 | 166 |
| Rusia | RUS | 3,275 |  |  |  |  |  |  |  | 5 | 56 | 102 | 213 | 1,147 | 816 |
| SAH | SAH | 4 |  |  |  |  |  |  |  |  |  | 2 |  | 1 |  |
| SDS | SDS | 82 |  |  |  |  |  |  |  |  |  | 1 |  | 10 | 19 |
| Sahara Occidental | ESH | 15 |  |  |  |  |  |  |  |  |  | 2 |  | 9 | 3 |
| Samoa | WSM | 32 |  |  |  |  |  |  |  |  |  |  | 3 | 21 | 8 |
| Samoa Estadounidense | ASM | 24 |  |  |  |  |  |  |  |  |  |  |  | 13 | 6 |
| San Bartolomé | BLM | 5 |  |  |  |  |  |  |  |  |  |  | 3 | 2 |  |
| San Cristóbal y Nieves | KNA | 17 |  |  |  |  |  |  |  |  |  | 2 | 12 | 1 | 2 |
| San Marino | SMR | 1 |  |  |  |  |  |  |  |  |  |  |  | 1 |  |
| San Martín | MAF | 27 |  |  |  |  |  |  |  |  |  |  | 5 | 13 | 6 |
| San Martín | SXM | 17 |  |  |  |  |  |  |  | 1 |  |  | 4 | 8 | 1 |
| San Pedro y Miquelón | SPM | 7 |  |  |  |  |  |  |  |  |  |  | 1 | 5 | 1 |
| San Vicente y las Granadinas | VCT | 15 |  |  |  |  |  |  |  |  |  |  | 3 | 9 | 3 |
| Santa Lucía | LCA | 22 |  |  |  |  |  |  |  |  |  | 1 | 15 | 2 | 4 |
| Santo Tomé y Príncipe | STP | 10 |  |  |  |  |  |  |  |  |  | 1 | 8 |  | 1 |
| Senegal | SEN | 75 |  |  |  |  |  |  |  |  | 1 | 3 | 25 | 17 | 10 |
| Serbia | SRB | 456 |  |  |  |  |  |  |  | 4 | 24 | 13 | 25 | 122 | 57 |
| Seychelles | SYC | 2 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |
| Sierra Leona | SLE | 65 |  |  |  |  |  |  |  |  | 1 | 3 | 9 | 13 | 35 |
| Singapur | SGP | 32 |  |  |  |  |  |  |  |  |  |  | 1 | 17 | 4 |
| Siria | SYR | 636 |  |  |  |  |  |  |  | 4 | 40 | 30 | 54 | 308 | 56 |
| Somalia | SOM | 147 |  |  |  |  |  |  |  |  | 7 | 7 | 3 | 10 | 95 |
| Somalilandia | SOL | 71 |  |  |  |  |  |  |  |  | 2 | 4 |  | 31 | 21 |
| Sri Lanka | LKA | 156 |  |  |  |  |  |  |  | 1 | 6 | 12 | 15 | 48 | 18 |
| Suazilandia | SWZ | 38 |  |  |  |  |  |  |  |  |  |  |  | 3 | 33 |
| Sudáfrica | ZAF | 518 |  |  |  |  |  |  |  |  | 2 | 2 | 20 | 216 | 147 |
| Sudán | SDN | 329 |  |  |  |  |  |  |  | 2 | 8 | 15 | 10 | 71 | 134 |
| Sudán del Sur | SSD | 200 |  |  |  |  |  |  |  |  | 1 | 4 | 2 | 17 | 89 |
| Suecia | SWE | 1,137 |  |  |  |  |  |  |  | 2 | 11 | 31 | 42 | 242 | 33 |
| Suiza | CHE | 1,870 | 1 |  |  |  |  |  |  | 3 | 41 | 47 | 85 | 338 | 116 |
| Surinam | SUR | 349 |  |  |  |  |  |  |  |  | 2 | 13 | 21 | 17 | 20 |
| Tailandia | THA | 136 |  |  |  |  |  |  |  |  | 5 | 3 | 10 | 47 | 32 |
| Tanzania | TZA | 192 |  |  |  |  |  |  |  |  | 2 | 2 | 2 | 48 | 77 |
| Tayikistán | TJK | 43 |  |  |  |  |  |  |  |  | 6 |  |  | 18 | 11 |
| Territorio Británico del Océano Índico | IOT | 1 |  |  |  |  |  |  |  |  |  |  |  |  | 1 |
| Territorios Australianos del Océano Índico | IOA | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Tierras Australes y Antárticas Francesas | ATF | 4 |  |  |  |  |  |  |  |  |  |  |  | 1 |  |
| Timor Oriental | TLS | 15 |  |  |  |  |  |  |  |  |  |  |  |  | 2 |
| Togo | TGO | 24 |  |  |  |  |  |  |  |  |  | 1 | 2 | 1 | 8 |
| Tonga | TON | 9 |  |  |  |  |  |  |  |  |  | 1 | 1 | 5 | 1 |
| Trinidad y Tobago | TTO | 49 |  |  |  |  |  |  |  |  |  | 10 | 19 | 6 | 13 |
| Turkmenistán | TKM | 96 |  |  |  |  |  |  |  |  | 14 | 5 | 3 | 41 | 16 |
| Turquía | TUR | 1,171 |  |  |  |  |  |  |  | 3 | 56 | 52 | 112 | 456 | 170 |
| Tuvalu | TUV | 6 |  |  |  |  |  |  |  |  |  |  |  | 5 | 1 |
| Túnez | TUN | 241 |  |  |  |  |  |  |  | 2 | 25 | 6 | 13 | 59 | 74 |
| UMI | UMI | 2 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |
| USG | USG | 3 |  |  |  |  |  |  |  |  |  |  | 1 | 1 |  |
| Ucrania | UKR | 656 |  |  |  |  |  |  | 2 | 4 | 28 | 47 | 47 | 74 | 76 |
| Uganda | UGA | 175 |  |  |  |  |  |  |  |  | 1 | 3 | 3 | 14 | 128 |
| Uruguay | URY | 178 |  |  |  |  |  |  |  |  | 1 | 21 | 37 | 62 | 36 |
| Uzbekistán | UZB | 86 |  |  |  |  |  |  |  |  | 7 | 4 | 2 | 43 | 15 |
| Vanuatu | VUT | 4 |  |  |  |  |  |  |  |  |  |  |  | 1 | 3 |
| Venezuela | VEN | 371 |  |  |  |  |  |  |  |  | 7 | 63 | 99 | 78 | 54 |
| Vietnam | VNM | 223 |  |  |  |  |  |  |  | 1 | 4 | 3 | 4 | 21 | 42 |
| Yemen | YEM | 335 |  |  |  |  |  |  |  | 4 | 13 | 7 | 12 | 30 | 233 |
| Yibuti | DJI | 43 |  |  |  |  |  |  |  |  | 1 | 1 | 2 | 24 | 13 |
| Zambia | ZMB | 97 |  |  |  |  |  |  |  |  | 1 | 3 | 4 | 19 | 45 |
| Zimbabue | ZWE | 103 |  |  |  |  |  |  |  |  | 2 | 1 | 5 | 25 | 43 |
| Åland | ALA | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |
