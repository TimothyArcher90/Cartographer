# Biblioteca de Cartographer

Documento generado por `scripts/comprender.py`. No editar a mano.

- Mapas analizados: **391,440** · con país asignado: **339,146** · sin país: 52,294
  (sobre todo mapamundis, cartas oceánicas o registros sin datos de lugar).
- Países con mapas: **243**.
- Tipos: topográfico 197,185, general 168,111, plano urbano 8,437, militar 4,954, histórico/temático 3,951, mapamundi 3,856, ferroviario/viario 2,395, carta náutica 2,248, portulano 162, ptolemaico 141.
- Escalas: local o ciudad 241,434, desconocida 118,659, provincia o comarca 17,234, región o país 8,454, continente 3,931, mundo 1,728.

Cómo se asigna un país: por **nombre** actual (25+ idiomas, Natural Earth), por **nombre histórico**
(`catalogo/nombres_historicos.json`) o por **coordenadas** de la cobertura del mapa. Cada mapa guarda
la vía en el campo `via`; las asignaciones por coordenadas de mapas grandes pueden incluir países
vecinos. Los siglos salen del año de los metadatos de cada archivo y pueden tener errores puntuales.

Mapas de un país: `catalogo/biblioteca/paises/<ISO3>.jsonl.gz` o
`python scripts/buscar_lugar.py "<país>"`.

| País | ISO | Total | Antes del s. IX | IX | X | XI | XII | XIII | XIV | XV | XVI | XVII | XVIII | XIX | XX |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Afganistán | AFG | 374 |  |  |  |  |  |  |  |  | 19 | 5 | 6 | 107 | 71 |
| Albania | ALB | 283 |  |  |  |  |  |  |  | 2 | 21 | 22 | 14 | 55 | 40 |
| Alemania | DEU | 8,083 | 1 |  |  |  |  |  |  | 2 | 86 | 146 | 214 | 889 | 466 |
| Andorra | AND | 11 |  |  |  |  |  |  |  |  |  |  |  |  | 3 |
| Angola | AGO | 112 |  |  |  |  |  |  |  |  | 2 | 6 | 11 | 23 | 41 |
| Anguila | AIA | 6 |  |  |  |  |  |  |  |  |  |  | 5 | 1 |  |
| Antigua y Barbuda | ATG | 24 |  |  |  |  |  |  |  |  |  | 1 | 12 | 6 | 1 |
| Antártida | ATA | 63 |  |  |  |  |  |  |  |  |  | 3 | 2 | 8 | 40 |
| Arabia Saudita | SAU | 543 |  |  |  |  |  |  |  | 6 | 42 | 28 | 53 | 142 | 117 |
| Argelia | DZA | 329 |  |  |  |  |  |  |  | 2 | 19 | 17 | 19 | 72 | 46 |
| Argentina | ARG | 696 |  |  |  |  |  |  |  |  | 3 | 71 | 48 | 151 | 300 |
| Armenia | ARM | 108 |  |  |  |  |  |  |  | 1 | 10 | 5 | 11 | 33 | 14 |
| Aruba | ABW | 17 |  |  |  |  |  |  |  |  |  |  | 2 | 6 | 1 |
| Australia | AUS | 1,921 |  |  |  |  |  |  |  |  |  | 6 | 13 | 208 | 51 |
| Austria | AUT | 1,800 | 1 |  |  |  |  |  |  | 2 | 35 | 29 | 40 | 280 | 218 |
| Azerbaiyán | AZE | 124 |  |  |  |  |  |  |  | 1 | 8 | 3 | 3 | 27 | 19 |
| Bahamas | BHS | 103 |  |  |  |  |  |  |  |  |  | 1 | 41 | 43 | 13 |
| Bangladés | BGD | 64 |  |  |  |  |  |  |  | 1 | 2 | 4 | 3 | 6 | 8 |
| Barbados | BRB | 73 |  |  |  |  |  |  |  |  |  | 5 | 22 | 6 | 20 |
| Baréin | BHR | 44 |  |  |  |  |  |  |  | 2 | 4 | 4 | 6 | 7 | 13 |
| Belice | BLZ | 50 |  |  |  |  |  |  |  |  |  | 7 | 5 | 9 | 23 |
| Benín | BEN | 46 |  |  |  |  |  |  |  |  | 3 | 6 |  | 2 | 13 |
| Bermudas | BMU | 68 |  |  |  |  |  |  |  |  |  | 11 | 24 | 19 | 5 |
| Bielorrusia | BLR | 362 |  |  |  |  |  |  |  | 3 | 22 | 18 | 23 | 21 | 52 |
| Birmania | MMR | 204 |  |  |  |  |  |  |  |  | 8 | 4 | 16 | 36 | 37 |
| Bolivia | BOL | 197 |  |  |  |  |  |  |  |  | 4 | 13 | 7 | 51 | 56 |
| Bosnia y Herzegovina | BIH | 626 |  |  |  |  |  |  |  | 6 | 36 | 13 | 20 | 100 | 55 |
| Botsuana | BWA | 161 |  |  |  |  |  |  |  |  | 1 |  | 6 | 46 | 51 |
| Brasil | BRA | 1,226 |  |  |  |  |  |  |  |  | 11 | 106 | 123 | 375 | 315 |
| Brunéi | BRN | 15 |  |  |  |  |  |  |  |  |  |  |  | 4 | 4 |
| Bulgaria | BGR | 517 |  |  |  |  |  |  | 1 | 2 | 19 | 17 | 38 | 101 | 62 |
| Burkina Faso | BFA | 62 |  |  |  |  |  |  |  |  | 1 | 5 | 3 | 7 | 11 |
| Burundi | BDI | 29 |  |  |  |  |  |  |  |  |  |  |  | 3 | 22 |
| Bután | BTN | 39 |  |  |  |  |  |  |  |  |  |  | 1 | 6 | 11 |
| Bélgica | BEL | 4,211 |  |  |  |  |  |  |  | 1 | 48 | 92 | 248 | 307 | 104 |
| Cabo Verde | CPV | 79 |  |  |  |  |  |  |  |  | 2 | 14 | 35 | 14 | 2 |
| Camboya | KHM | 98 |  |  |  |  |  |  |  |  | 1 | 1 | 1 | 10 | 42 |
| Camerún | CMR | 103 |  |  |  |  |  |  |  |  | 1 | 4 | 8 | 9 | 42 |
| Canadá | CAN | 5,329 |  |  |  |  |  |  |  |  | 10 | 80 | 1,135 | 1,162 | 1,575 |
| Catar | QAT | 31 |  |  |  |  |  |  |  | 3 | 5 | 3 | 8 | 5 | 4 |
| Chad | TCD | 72 |  |  |  |  |  |  |  |  |  | 3 | 5 | 10 | 29 |
| Chile | CHL | 450 |  |  |  |  |  |  |  | 1 | 2 | 70 | 45 | 134 | 91 |
| China | CHN | 2,329 |  |  |  |  | 7 | 1 | 1 | 4 | 30 | 81 | 246 | 698 | 691 |
| Chipre | CYP | 71 |  |  |  |  |  |  |  | 1 | 10 | 11 | 7 | 15 | 5 |
| Ciudad del Vaticano | VAT | 8 |  |  |  |  |  |  |  |  |  |  | 1 | 3 | 2 |
| Colombia | COL | 358 |  |  |  |  |  |  |  |  | 5 | 24 | 55 | 71 | 113 |
| Comoras | COM | 4 |  |  |  |  |  |  |  |  |  |  |  | 2 | 2 |
| Corea del Norte | PRK | 127 |  |  |  |  |  |  |  |  | 1 | 9 | 11 | 13 | 47 |
| Corea del Sur | KOR | 300 |  |  |  |  |  |  |  |  | 2 | 12 | 51 | 118 | 61 |
| Costa Rica | CRI | 117 |  |  |  |  |  |  |  |  |  | 14 | 10 | 31 | 47 |
| Costa de Marfil | CIV | 77 |  |  |  |  |  |  |  |  | 2 | 5 | 9 | 10 | 14 |
| Croacia | HRV | 921 |  |  |  |  |  |  |  | 6 | 40 | 15 | 29 | 175 | 62 |
| Cuba | CUB | 577 |  |  |  |  |  |  |  |  | 5 | 36 | 122 | 142 | 152 |
| Curazao | CUW | 71 |  |  |  |  |  |  |  |  |  |  | 13 | 8 | 1 |
| Dinamarca | DNK | 1,002 |  |  |  |  |  |  | 1 |  | 7 | 42 | 20 | 259 | 15 |
| Dominica | DMA | 14 |  |  |  |  |  |  |  |  |  |  | 9 | 2 |  |
| ESB | ESB | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ecuador | ECU | 188 |  |  |  |  |  |  |  |  | 5 | 11 | 16 | 48 | 51 |
| Egipto | EGY | 935 |  |  |  |  |  |  |  | 3 | 41 | 33 | 91 | 404 | 127 |
| El Salvador | SLV | 67 |  |  |  |  |  |  |  |  |  | 1 | 2 | 19 | 38 |
| Emiratos Árabes Unidos | ARE | 42 |  |  |  |  |  |  |  | 3 | 6 | 4 | 10 | 9 | 4 |
| Eritrea | ERI | 343 |  |  |  |  |  |  |  |  | 1 | 6 | 4 | 94 | 210 |
| Eslovaquia | SVK | 720 |  |  |  |  |  |  |  | 2 | 16 | 10 | 19 | 93 | 73 |
| Eslovenia | SVN | 364 |  |  |  |  |  |  |  | 2 | 18 | 4 | 3 | 12 | 106 |
| España | ESP | 2,827 |  |  |  |  |  |  |  | 4 | 66 | 81 | 421 | 1,001 | 75 |
| Estados Federados de Micronesia | FSM | 40 |  |  |  |  |  |  |  |  |  | 1 |  | 9 | 25 |
| Estados Unidos | USA | 265,312 | 2 |  |  |  |  |  |  | 1 | 21 | 417 | 4,248 | 33,811 | 193,533 |
| Estonia | EST | 288 |  |  |  |  |  |  |  |  | 1 | 8 | 3 | 7 | 181 |
| Etiopía | ETH | 376 |  |  |  |  |  |  |  | 1 | 8 | 14 | 11 | 109 | 144 |
| Filipinas | PHL | 277 |  |  |  |  |  |  |  |  | 3 | 5 | 27 | 47 | 161 |
| Finlandia | FIN | 237 |  |  |  |  |  |  |  | 1 | 8 | 13 | 13 | 30 | 16 |
| Fiyi | FJI | 39 |  |  |  |  |  |  |  |  |  |  |  | 28 | 7 |
| Francia | FRA | 11,344 |  |  |  |  |  |  |  | 1 | 128 | 294 | 1,002 | 3,120 | 323 |
| GIB | GIB | 6 |  |  |  |  |  |  |  |  |  |  | 5 |  |  |
| Gabón | GAB | 50 |  |  |  |  |  |  |  |  | 1 | 5 | 6 | 6 | 12 |
| Gambia | GMB | 20 |  |  |  |  |  |  |  |  |  | 1 | 8 | 7 | 4 |
| Georgia | GEO | 164 |  |  |  |  |  |  |  | 1 | 11 | 3 | 26 | 29 | 31 |
| Ghana | GHA | 73 |  |  |  |  |  |  |  |  | 2 | 6 | 7 | 8 | 9 |
| Granada | GRD | 88 |  |  |  |  |  |  |  |  |  | 9 | 27 | 33 | 5 |
| Grecia | GRC | 1,077 |  |  |  |  |  |  |  | 3 | 69 | 80 | 76 | 351 | 78 |
| Groenlandia | GRL | 113 |  |  |  |  |  |  | 1 |  | 4 | 10 | 22 | 56 | 9 |
| Guam | GUM | 19 |  |  |  |  |  |  |  |  |  |  | 2 | 3 | 3 |
| Guatemala | GTM | 118 |  |  |  |  |  |  |  |  | 1 | 15 | 10 | 22 | 45 |
| Guernsey | GGY | 77 |  |  |  |  |  |  |  |  |  | 4 |  | 57 | 14 |
| Guinea | GIN | 76 |  |  |  |  |  |  |  |  | 1 | 5 | 23 | 9 | 12 |
| Guinea Ecuatorial | GNQ | 16 |  |  |  |  |  |  |  |  | 1 |  |  | 3 | 6 |
| Guinea-Bisáu | GNB | 9 |  |  |  |  |  |  |  |  |  |  | 2 | 2 | 2 |
| Guyana | GUY | 232 |  |  |  |  |  |  |  |  | 2 | 18 | 27 | 38 | 30 |
| Haití | HTI | 249 |  |  |  |  |  |  |  |  | 3 | 22 | 94 | 55 | 27 |
| Honduras | HND | 162 |  |  |  |  |  |  |  |  |  | 21 | 33 | 31 | 53 |
| Hong Kong | HKG | 34 |  |  |  |  |  |  |  |  |  |  |  | 16 | 8 |
| Hungría | HUN | 1,241 |  |  |  |  |  |  |  | 3 | 36 | 18 | 47 | 254 | 97 |
| India | IND | 1,121 |  |  |  |  |  |  |  | 1 | 51 | 28 | 107 | 367 | 75 |
| Indonesia | IDN | 1,197 | 1 |  |  |  |  |  | 1 |  | 12 | 117 | 61 | 112 | 120 |
| Irak | IRQ | 455 |  |  |  |  |  |  |  | 3 | 29 | 18 | 26 | 112 | 54 |
| Irlanda | IRL | 1,495 |  |  |  |  |  |  |  | 1 | 23 | 48 | 67 | 530 | 43 |
| Irán | IRN | 427 |  |  |  |  |  |  |  | 5 | 36 | 14 | 36 | 139 | 40 |
| Isla Norfolk | NFK | 352 |  |  |  |  |  |  |  |  |  | 1 | 26 | 223 | 100 |
| Isla Santa Elena | SHN | 34 |  |  |  |  |  |  |  |  | 1 | 1 | 5 | 20 | 1 |
| Isla de Man | IMN | 30 |  |  |  |  |  |  |  |  |  |  | 1 | 19 |  |
| Islandia | ISL | 82 |  |  |  |  |  |  |  |  | 2 | 6 | 5 | 27 | 5 |
| Islas Caimán | CYM | 8 |  |  |  |  |  |  |  |  |  |  | 1 | 1 | 6 |
| Islas Feroe | FRO | 5 |  |  |  |  |  |  |  |  |  | 1 | 1 | 2 |  |
| Islas Georgias del Sur y Sandwich del Sur | SGS | 3 |  |  |  |  |  |  |  |  |  |  |  |  | 1 |
| Islas Malvinas | FLK | 20 |  |  |  |  |  |  |  |  |  | 6 | 4 | 4 | 3 |
| Islas Marianas del Norte | MNP | 22 |  |  |  |  |  |  |  |  |  |  |  | 2 | 17 |
| Islas Marshall | MHL | 14 |  |  |  |  |  |  |  |  |  |  |  | 3 | 11 |
| Islas Pitcairn | PCN | 7 |  |  |  |  |  |  |  |  |  |  | 1 | 1 | 5 |
| Islas Salomón | SLB | 18 |  |  |  |  |  |  |  |  | 1 | 2 | 1 | 3 | 10 |
| Islas Turcas y Caicos | TCA | 6 |  |  |  |  |  |  |  |  |  |  | 2 | 2 | 2 |
| Islas Vírgenes Británicas | VGB | 7 |  |  |  |  |  |  |  |  |  |  | 2 | 1 | 4 |
| Islas Vírgenes de los Estados Unidos | VIR | 101 |  |  |  |  |  |  |  |  |  | 1 | 48 | 2 | 43 |
| Israel | ISR | 1,570 |  |  |  |  |  |  |  | 9 | 51 | 59 | 169 | 643 | 141 |
| Italia | ITA | 4,058 | 1 |  |  |  |  |  |  | 8 | 177 | 171 | 172 | 774 | 274 |
| Jamaica | JAM | 238 |  |  |  |  |  |  |  |  | 1 | 14 | 78 | 80 | 36 |
| Japón | JPN | 963 |  |  |  |  |  |  |  | 1 | 4 | 31 | 41 | 247 | 209 |
| Jersey | JEY | 14 |  |  |  |  |  |  |  |  |  | 4 |  | 8 |  |
| Jordania | JOR | 442 |  |  |  |  |  |  |  | 1 | 37 | 16 | 22 | 148 | 28 |
| Kazajistán | KAZ | 144 |  |  |  |  |  |  |  | 1 | 15 | 15 | 4 | 21 | 11 |
| Kenia | KEN | 168 |  |  |  |  |  |  |  |  | 1 | 4 | 1 | 21 | 103 |
| Kirguistán | KGZ | 57 |  |  |  |  |  |  |  |  | 7 | 2 |  | 15 | 8 |
| Kiribati | KIR | 19 |  |  |  |  |  |  |  |  |  |  |  | 14 | 5 |
| Kosovo | KOS | 48 |  |  |  |  |  |  |  |  | 1 | 2 | 2 |  | 12 |
| Kuwait | KWT | 42 |  |  |  |  |  |  |  | 3 | 6 | 3 | 10 | 6 | 8 |
| Laos | LAO | 63 |  |  |  |  |  |  |  | 1 | 3 |  |  | 8 | 15 |
| Lesoto | LSO | 87 |  |  |  |  |  |  |  |  |  |  | 1 | 12 | 67 |
| Letonia | LVA | 190 |  |  |  |  |  |  |  | 2 | 10 | 9 | 9 | 17 | 17 |
| Liberia | LBR | 84 |  |  |  |  |  |  |  |  | 1 | 2 | 4 | 32 | 29 |
| Libia | LBY | 259 |  |  |  |  |  |  |  | 6 | 21 | 17 | 13 | 30 | 80 |
| Liechtenstein | LIE | 11 |  |  |  |  |  |  |  | 1 |  |  |  | 2 |  |
| Lituania | LTU | 337 |  |  |  |  |  |  |  | 2 | 10 | 9 | 15 | 18 | 33 |
| Luxemburgo | LUX | 274 |  |  |  |  |  |  |  |  | 6 | 16 | 27 | 24 | 19 |
| Líbano | LBN | 325 |  |  |  |  |  |  |  | 1 | 17 | 6 | 12 | 156 | 53 |
| Macao | MAC | 30 |  |  |  |  |  |  |  |  |  |  | 4 | 7 | 14 |
| Macedonia del Norte | MKD | 149 |  |  |  |  |  |  |  | 2 | 13 | 11 | 5 | 19 | 22 |
| Madagascar | MDG | 134 |  |  |  |  |  |  |  |  | 3 | 5 | 14 | 39 | 36 |
| Malasia | MYS | 203 |  |  |  |  |  |  |  |  | 4 | 5 | 3 | 22 | 28 |
| Malaui | MWI | 35 |  |  |  |  |  |  |  |  | 1 |  | 2 | 13 | 14 |
| Maldivas | MDV | 4 |  |  |  |  |  |  |  |  |  |  | 1 |  | 3 |
| Malta | MLT | 75 |  |  |  |  |  |  |  |  | 9 | 12 | 10 | 18 | 6 |
| Malí | MLI | 101 |  |  |  |  |  |  |  |  | 2 | 5 | 7 | 12 | 9 |
| Marruecos | MAR | 264 |  |  |  |  |  |  |  | 1 | 10 | 17 | 22 | 65 | 36 |
| Mauricio | MUS | 34 |  |  |  |  |  |  |  |  |  | 1 | 6 | 19 | 3 |
| Mauritania | MRT | 78 |  |  |  |  |  |  |  |  | 4 | 3 | 11 | 10 | 8 |
| Moldavia | MDA | 121 |  |  |  |  |  |  |  | 1 | 3 | 5 | 11 | 21 | 10 |
| Mongolia | MNG | 85 |  |  |  |  |  |  |  |  | 1 | 8 | 3 | 22 | 28 |
| Montenegro | MNE | 104 |  |  |  |  |  |  |  |  | 6 | 7 | 4 | 13 | 13 |
| Montserrat | MSR | 7 |  |  |  |  |  |  |  |  |  |  |  | 6 | 1 |
| Mozambique | MOZ | 164 |  |  |  |  |  |  |  |  | 3 | 5 | 11 | 51 | 36 |
| México | MEX | 2,549 |  |  |  |  |  |  |  | 2 | 30 | 78 | 217 | 549 | 1,066 |
| Mónaco | MCO | 3 |  |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| Namibia | NAM | 126 |  |  |  |  |  |  |  |  | 2 |  | 7 | 41 | 24 |
| Nauru | NRU | 3 |  |  |  |  |  |  |  |  |  |  |  |  | 3 |
| Nepal | NPL | 55 |  |  |  |  |  |  |  | 1 | 2 | 2 |  | 5 | 7 |
| Nicaragua | NIC | 149 |  |  |  |  |  |  |  |  |  | 21 | 17 | 51 | 39 |
| Nigeria | NGA | 112 |  |  |  |  |  |  |  |  | 2 | 8 | 7 | 8 | 36 |
| Noruega | NOR | 759 |  |  |  |  |  |  |  | 2 | 3 | 15 | 15 | 172 | 19 |
| Nueva Caledonia | NCL | 9 |  |  |  |  |  |  |  |  |  |  | 1 | 2 | 5 |
| Nueva Zelanda | NZL | 161 |  |  |  |  |  |  |  |  |  |  | 3 | 99 | 16 |
| Níger | NER | 79 |  |  |  |  |  |  |  |  | 4 | 5 | 3 | 5 | 26 |
| Omán | OMN | 70 |  |  |  |  |  |  |  | 4 | 10 | 4 | 11 | 10 | 7 |
| PSX | PSX | 327 |  |  |  |  |  |  |  | 1 | 17 | 8 | 7 | 106 | 2 |
| Pakistán | PAK | 329 |  |  |  |  |  |  |  |  | 24 | 5 | 9 | 95 | 27 |
| Palaos | PLW | 24 |  |  |  |  |  |  |  |  |  |  |  | 5 | 15 |
| Palestina | PSE | 857 |  |  |  |  |  |  |  | 6 | 38 | 29 | 48 | 384 | 82 |
| Panamá | PAN | 249 |  |  |  |  |  |  |  |  | 1 | 34 | 33 | 53 | 78 |
| Papúa Nueva Guinea | PNG | 64 |  |  |  |  |  |  |  |  | 1 | 4 | 2 | 14 | 27 |
| Paraguay | PRY | 174 |  |  |  |  |  |  |  |  |  | 11 | 12 | 49 | 33 |
| Países Bajos | NLD | 13,082 |  |  |  |  |  |  |  |  | 50 | 203 | 282 | 291 | 51 |
| Perú | PER | 392 |  |  |  |  |  |  |  |  | 13 | 26 | 25 | 138 | 98 |
| Polinesia Francesa | PYF | 38 |  |  |  |  |  |  |  |  |  |  | 6 | 25 | 3 |
| Polonia | POL | 2,430 |  |  |  |  |  |  |  | 6 | 40 | 36 | 70 | 305 | 167 |
| Portugal | PRT | 1,205 |  |  |  |  |  |  |  | 2 | 28 | 37 | 84 | 412 | 52 |
| Puerto Rico | PRI | 973 |  |  |  |  |  |  |  |  |  | 10 | 40 | 22 | 877 |
| Reino Unido | GBR | 8,421 |  |  |  |  |  |  |  | 1 | 54 | 295 | 476 | 1,814 | 275 |
| República Centroafricana | CAF | 157 |  |  |  |  |  |  |  |  |  | 2 | 4 | 8 | 112 |
| República Checa | CZE | 1,399 |  |  |  |  |  |  |  | 1 | 16 | 27 | 33 | 161 | 176 |
| República Democrática del Congo | COD | 271 |  |  |  |  |  |  |  | 1 | 3 | 6 | 13 | 56 | 137 |
| República Dominicana | DOM | 189 |  |  |  |  |  |  |  |  | 3 | 20 | 63 | 35 | 30 |
| República Turca del Norte de Chipre | CYN | 18 |  |  |  |  |  |  |  |  | 2 | 5 |  |  |  |
| República de China | TWN | 93 |  |  |  |  |  |  |  |  |  | 6 |  | 11 | 45 |
| República del Congo | COG | 113 |  |  |  |  |  |  |  | 1 | 1 | 5 | 14 | 33 | 31 |
| Ruanda | RWA | 17 |  |  |  |  |  |  |  |  |  |  |  | 3 | 10 |
| Rumania | ROU | 1,163 |  |  |  |  |  |  |  | 2 | 36 | 19 | 42 | 145 | 145 |
| Rusia | RUS | 3,318 |  |  |  |  |  |  |  | 5 | 55 | 98 | 162 | 989 | 701 |
| SAH | SAH | 4 |  |  |  |  |  |  |  |  |  | 2 |  | 1 |  |
| SDS | SDS | 84 |  |  |  |  |  |  |  |  |  | 1 |  | 10 | 19 |
| Sahara Occidental | ESH | 11 |  |  |  |  |  |  |  |  |  | 2 |  | 5 | 3 |
| Samoa | WSM | 28 |  |  |  |  |  |  |  |  |  |  |  | 20 | 6 |
| Samoa Estadounidense | ASM | 24 |  |  |  |  |  |  |  |  |  |  |  | 13 | 6 |
| San Bartolomé | BLM | 5 |  |  |  |  |  |  |  |  |  |  | 3 | 2 |  |
| San Cristóbal y Nieves | KNA | 18 |  |  |  |  |  |  |  |  |  | 2 | 12 | 1 |  |
| San Marino | SMR | 1 |  |  |  |  |  |  |  |  |  |  |  | 1 |  |
| San Martín | MAF | 24 |  |  |  |  |  |  |  |  |  |  | 5 | 11 | 5 |
| San Martín | SXM | 15 |  |  |  |  |  |  |  | 1 |  |  | 4 | 7 |  |
| San Pedro y Miquelón | SPM | 7 |  |  |  |  |  |  |  |  |  |  | 1 | 5 | 1 |
| San Vicente y las Granadinas | VCT | 14 |  |  |  |  |  |  |  |  |  |  | 3 | 9 | 1 |
| Santa Lucía | LCA | 16 |  |  |  |  |  |  |  |  |  | 1 | 10 | 2 | 2 |
| Santo Tomé y Príncipe | STP | 2 |  |  |  |  |  |  |  |  |  | 1 |  |  | 1 |
| Senegal | SEN | 74 |  |  |  |  |  |  |  |  | 1 | 3 | 20 | 14 | 10 |
| Serbia | SRB | 617 |  |  |  |  |  |  |  | 4 | 23 | 11 | 23 | 118 | 56 |
| Seychelles | SYC | 2 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |
| Sierra Leona | SLE | 69 |  |  |  |  |  |  |  |  | 1 | 2 | 9 | 11 | 35 |
| Singapur | SGP | 28 |  |  |  |  |  |  |  |  |  |  |  | 14 | 4 |
| Siria | SYR | 698 |  |  |  |  |  |  |  | 4 | 40 | 29 | 53 | 278 | 60 |
| Somalia | SOM | 143 |  |  |  |  |  |  |  |  | 7 | 6 | 3 | 10 | 87 |
| Somalilandia | SOL | 59 |  |  |  |  |  |  |  |  | 2 | 4 |  | 13 | 21 |
| Sri Lanka | LKA | 167 |  |  |  |  |  |  |  | 1 | 6 | 9 | 12 | 59 | 17 |
| Suazilandia | SWZ | 38 |  |  |  |  |  |  |  |  |  |  |  | 3 | 33 |
| Sudáfrica | ZAF | 483 |  |  |  |  |  |  |  |  | 2 | 1 | 19 | 181 | 146 |
| Sudán | SDN | 361 |  |  |  |  |  |  |  | 2 | 8 | 16 | 16 | 76 | 135 |
| Sudán del Sur | SSD | 210 |  |  |  |  |  |  |  |  | 1 | 4 | 3 | 17 | 89 |
| Suecia | SWE | 1,016 |  |  |  |  |  |  |  | 2 | 10 | 30 | 23 | 152 | 22 |
| Suiza | CHE | 1,969 | 1 |  |  |  |  |  |  | 2 | 41 | 41 | 68 | 286 | 101 |
| Surinam | SUR | 345 |  |  |  |  |  |  |  |  | 2 | 12 | 16 | 13 | 18 |
| Tailandia | THA | 134 |  |  |  |  |  |  |  |  | 5 | 6 | 11 | 29 | 29 |
| Tanzania | TZA | 187 |  |  |  |  |  |  |  |  | 2 | 2 | 2 | 46 | 71 |
| Tayikistán | TJK | 69 |  |  |  |  |  |  |  |  | 6 |  |  | 18 | 11 |
| Territorio Británico del Océano Índico | IOT | 1 |  |  |  |  |  |  |  |  |  |  |  |  | 1 |
| Territorios Australianos del Océano Índico | IOA | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Tierras Australes y Antárticas Francesas | ATF | 4 |  |  |  |  |  |  |  |  |  |  |  | 1 |  |
| Timor Oriental | TLS | 9 |  |  |  |  |  |  |  |  |  |  |  |  | 2 |
| Togo | TGO | 22 |  |  |  |  |  |  |  |  |  |  | 2 | 1 | 6 |
| Tonga | TON | 6 |  |  |  |  |  |  |  |  |  |  | 1 | 4 | 1 |
| Trinidad y Tobago | TTO | 34 |  |  |  |  |  |  |  |  |  | 4 | 11 | 5 | 11 |
| Turkmenistán | TKM | 163 |  |  |  |  |  |  |  |  | 14 | 5 | 2 | 48 | 19 |
| Turquía | TUR | 1,127 |  |  |  |  |  |  |  | 3 | 57 | 49 | 96 | 376 | 137 |
| Tuvalu | TUV | 6 |  |  |  |  |  |  |  |  |  |  |  | 5 | 1 |
| Túnez | TUN | 294 |  |  |  |  |  |  |  | 2 | 23 | 5 | 12 | 61 | 82 |
| UMI | UMI | 2 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |
| USG | USG | 3 |  |  |  |  |  |  |  |  |  |  | 1 | 1 |  |
| Ucrania | UKR | 779 |  |  |  |  |  |  | 2 | 4 | 28 | 39 | 37 | 73 | 70 |
| Uganda | UGA | 170 |  |  |  |  |  |  |  |  | 1 | 3 | 3 | 13 | 124 |
| Uruguay | URY | 142 |  |  |  |  |  |  |  |  | 1 | 12 | 11 | 55 | 34 |
| Uzbekistán | UZB | 127 |  |  |  |  |  |  |  |  | 7 | 4 | 3 | 42 | 12 |
| Vanuatu | VUT | 5 |  |  |  |  |  |  |  |  |  |  |  | 1 | 3 |
| Venezuela | VEN | 323 |  |  |  |  |  |  |  |  | 6 | 40 | 45 | 60 | 54 |
| Vietnam | VNM | 272 |  |  |  |  |  |  |  | 1 | 4 | 3 | 5 | 28 | 36 |
| Yemen | YEM | 351 |  |  |  |  |  |  |  | 4 | 13 | 6 | 11 | 31 | 231 |
| Yibuti | DJI | 17 |  |  |  |  |  |  |  |  | 1 | 1 | 2 | 6 | 5 |
| Zambia | ZMB | 102 |  |  |  |  |  |  |  |  | 1 | 3 | 5 | 19 | 45 |
| Zimbabue | ZWE | 111 |  |  |  |  |  |  |  |  | 2 |  | 6 | 25 | 43 |
| Åland | ALA | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |
