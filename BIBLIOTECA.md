# Biblioteca de Cartographer

Documento generado por `scripts/comprender.py`. No editar a mano.

- Mapas analizados: **873,165** · con país asignado: **527,545** · sin país: 345,620
  (sobre todo mapamundis, cartas oceánicas o registros sin datos de lugar).
- Países con mapas: **244**.
- Tipos: general 544,007, topográfico 208,898, histórico/temático 62,445, plano urbano 26,354, militar 10,917, mapamundi 6,965, ferroviario/viario 6,384, carta náutica 5,797, portulano 770, ptolemaico 628.
- Escalas: desconocida 603,369, local o ciudad 245,025, provincia o comarca 14,152, región o país 6,100, continente 2,997, mundo 1,522.

Cómo se asigna un país: por **nombre** actual (25+ idiomas, Natural Earth), por **nombre histórico**
(`catalogo/nombres_historicos.json`) o por **coordenadas** de la cobertura del mapa. Cada mapa guarda
la vía en el campo `via`; las asignaciones por coordenadas de mapas grandes pueden incluir países
vecinos. Los siglos salen del año de los metadatos de cada archivo y pueden tener errores puntuales.

Mapas de un país: `catalogo/biblioteca/paises/<ISO3>.jsonl.gz` o
`python scripts/buscar_lugar.py "<país>"`.

| País | ISO | Total | Antes del s. IX | IX | X | XI | XII | XIII | XIV | XV | XVI | XVII | XVIII | XIX | XX |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Afganistán | AFG | 520 | 1 |  |  |  |  |  | 1 |  | 21 | 7 | 12 | 214 | 111 |
| Albania | ALB | 352 | 1 |  |  |  |  | 2 | 2 | 7 | 27 | 33 | 29 | 87 | 64 |
| Alemania | DEU | 15,292 | 6 | 4 | 4 | 2 | 3 | 3 | 2 | 12 | 140 | 345 | 545 | 2,052 | 966 |
| Andorra | AND | 43 | 2 |  |  |  |  |  |  |  |  |  | 2 | 5 | 22 |
| Angola | AGO | 241 |  |  |  |  |  |  |  | 1 | 4 | 13 | 27 | 66 | 92 |
| Anguila | AIA | 10 |  |  |  |  |  |  |  |  |  |  | 6 | 1 | 1 |
| Antigua y Barbuda | ATG | 40 |  |  |  |  |  |  |  |  |  | 2 | 16 | 17 | 1 |
| Antártida | ATA | 117 |  |  |  |  |  |  |  |  |  | 12 | 23 | 10 | 54 |
| Arabia Saudita | SAU | 673 | 1 |  |  |  |  |  |  | 6 | 51 | 41 | 72 | 195 | 147 |
| Argelia | DZA | 782 | 2 |  |  |  |  | 1 | 1 | 3 | 24 | 33 | 40 | 336 | 142 |
| Argentina | ARG | 952 |  |  |  |  |  |  |  |  | 8 | 107 | 110 | 185 | 371 |
| Armenia | ARM | 445 | 2 | 1 |  | 1 |  |  | 1 | 2 | 22 | 18 | 34 | 184 | 103 |
| Aruba | ABW | 23 |  |  |  |  |  |  |  |  |  |  | 3 | 6 | 4 |
| Australia | AUS | 2,494 | 5 |  |  |  |  |  | 1 |  | 8 | 19 | 50 | 423 | 106 |
| Austria | AUT | 2,431 | 2 |  |  |  |  |  | 1 | 4 | 49 | 67 | 122 | 590 | 281 |
| Azerbaiyán | AZE | 140 |  |  |  |  |  |  |  | 1 | 8 | 7 | 10 | 46 | 37 |
| Bahamas | BHS | 202 |  |  |  |  |  | 1 |  |  |  | 7 | 68 | 62 | 33 |
| Bangladés | BGD | 57 |  |  |  |  |  |  |  | 1 | 4 | 5 | 4 | 7 | 8 |
| Barbados | BRB | 130 |  |  |  |  |  |  |  |  |  | 12 | 43 | 15 | 30 |
| Baréin | BHR | 82 |  |  |  |  |  |  |  | 2 | 6 | 6 | 11 | 19 | 27 |
| Belice | BLZ | 73 |  |  |  |  |  |  |  |  |  | 9 | 5 | 17 | 34 |
| Benín | BEN | 70 |  |  |  |  |  |  |  |  | 4 | 7 | 4 | 11 | 16 |
| Bermudas | BMU | 123 |  |  |  |  |  |  |  |  | 1 | 12 | 33 | 28 | 16 |
| Bielorrusia | BLR | 312 | 1 |  |  |  |  |  |  | 3 | 22 | 20 | 33 | 46 | 85 |
| Birmania | MMR | 241 | 1 |  |  |  |  |  |  | 1 | 11 | 9 | 25 | 64 | 70 |
| Bolivia | BOL | 310 |  |  |  |  |  |  |  |  | 5 | 18 | 11 | 92 | 83 |
| Bosnia y Herzegovina | BIH | 464 | 2 |  |  |  |  |  |  | 6 | 37 | 15 | 22 | 113 | 75 |
| Botsuana | BWA | 163 |  |  |  | 2 |  |  |  |  | 2 |  | 5 | 47 | 56 |
| Brasil | BRA | 2,328 | 3 |  |  |  |  |  |  | 3 | 26 | 238 | 279 | 566 | 464 |
| Brunéi | BRN | 30 |  |  |  |  |  |  |  |  | 1 |  | 1 | 11 | 7 |
| Bulgaria | BGR | 536 |  |  |  |  |  |  | 1 | 2 | 27 | 20 | 48 | 140 | 87 |
| Burkina Faso | BFA | 57 |  |  |  |  |  |  |  |  | 2 | 5 | 3 | 7 | 14 |
| Burundi | BDI | 44 | 1 |  |  |  |  |  |  |  |  |  |  | 3 | 34 |
| Bután | BTN | 123 | 1 |  |  |  |  |  |  |  |  |  | 5 | 36 | 55 |
| Bélgica | BEL | 5,953 | 1 |  | 1 |  |  |  | 1 | 3 | 70 | 235 | 542 | 788 | 320 |
| Cabo Verde | CPV | 132 |  |  |  |  |  |  |  |  | 4 | 22 | 50 | 31 | 3 |
| Camboya | KHM | 134 |  |  |  |  |  |  |  |  | 3 | 13 | 6 | 22 | 56 |
| Camerún | CMR | 129 |  |  |  |  |  |  |  |  | 2 | 6 | 8 | 14 | 51 |
| Canadá | CAN | 6,789 | 8 |  |  |  |  |  | 2 |  | 22 | 124 | 1,598 | 1,813 | 1,843 |
| Catar | QAT | 100 |  |  |  |  |  |  |  | 3 | 8 | 7 | 13 | 34 | 32 |
| Chad | TCD | 80 |  |  |  |  |  |  |  |  |  | 3 | 4 | 18 | 30 |
| Chile | CHL | 1,050 |  |  |  |  |  |  |  | 2 | 8 | 135 | 186 | 337 | 148 |
| China | CHN | 4,519 | 2 | 1 |  |  | 9 | 2 | 4 | 5 | 45 | 150 | 463 | 1,686 | 1,277 |
| Chipre | CYP | 290 | 1 |  |  |  |  | 1 |  | 4 | 35 | 19 | 25 | 25 | 95 |
| Ciudad del Vaticano | VAT | 78 |  |  |  |  |  |  |  |  | 1 | 24 | 5 | 10 | 15 |
| Colombia | COL | 674 |  |  |  |  |  |  |  |  | 10 | 55 | 111 | 149 | 149 |
| Comoras | COM | 25 |  |  |  |  |  |  |  |  |  | 1 | 4 | 10 | 8 |
| Corea del Norte | PRK | 136 |  |  |  |  |  |  |  |  | 1 | 9 | 12 | 13 | 54 |
| Corea del Sur | KOR | 856 | 1 |  |  |  |  |  |  |  | 6 | 15 | 69 | 152 | 223 |
| Costa Rica | CRI | 191 |  |  |  |  |  |  |  |  |  | 16 | 17 | 49 | 91 |
| Costa de Marfil | CIV | 109 |  |  |  |  |  |  |  |  | 3 | 5 | 13 | 14 | 42 |
| Croacia | HRV | 933 | 5 |  |  |  |  |  | 2 | 7 | 51 | 42 | 57 | 227 | 88 |
| Cuba | CUB | 1,331 | 17 | 8 | 5 |  |  |  |  | 1 | 9 | 108 | 244 | 291 | 328 |
| Curazao | CUW | 103 |  |  |  |  |  |  |  |  | 1 | 2 | 25 | 12 | 2 |
| Dinamarca | DNK | 1,486 | 5 |  |  |  |  |  | 3 |  | 11 | 69 | 77 | 417 | 89 |
| Dominica | DMA | 28 |  |  |  |  |  |  |  |  |  | 3 | 17 | 2 |  |
| ESB | ESB | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ecuador | ECU | 393 |  |  |  |  |  |  |  | 1 | 8 | 24 | 67 | 97 | 90 |
| Egipto | EGY | 2,508 | 8 |  |  | 2 | 1 | 3 | 2 | 5 | 60 | 48 | 176 | 909 | 803 |
| El Salvador | SLV | 191 |  |  |  |  |  | 1 |  |  | 1 | 10 | 5 | 93 | 61 |
| Emiratos Árabes Unidos | ARE | 55 |  |  |  |  |  |  |  | 3 | 7 | 6 | 12 | 13 | 7 |
| Eritrea | ERI | 425 |  |  |  |  |  |  |  |  | 1 | 7 | 7 | 107 | 275 |
| Eslovaquia | SVK | 539 |  |  |  |  |  |  |  | 2 | 17 | 15 | 23 | 103 | 125 |
| Eslovenia | SVN | 325 | 1 |  |  |  |  |  |  | 2 | 22 | 9 | 5 | 18 | 108 |
| España | ESP | 8,389 | 18 |  | 23 | 10 | 16 | 9 | 10 | 22 | 119 | 351 | 1,578 | 2,902 | 1,004 |
| Estados Federados de Micronesia | FSM | 69 |  |  |  |  |  |  |  |  |  | 1 | 4 | 23 | 32 |
| Estados Unidos | USA | 376,511 | 50 |  | 2 |  | 1 | 6 | 1 | 4 | 38 | 681 | 5,452 | 119,653 | 214,151 |
| Estonia | EST | 1,096 |  |  |  |  |  |  |  | 1 | 8 | 19 | 28 | 149 | 516 |
| Etiopía | ETH | 582 | 8 |  |  |  |  | 1 | 1 | 1 | 16 | 28 | 27 | 155 | 239 |
| Filipinas | PHL | 669 |  |  |  |  |  |  |  |  | 10 | 21 | 95 | 222 | 191 |
| Finlandia | FIN | 280 |  |  |  |  |  |  |  | 1 | 8 | 23 | 33 | 49 | 34 |
| Fiyi | FJI | 78 |  |  |  |  |  |  |  |  |  | 2 | 4 | 43 | 11 |
| Francia | FRA | 19,759 | 22 | 4 | 7 | 4 | 9 | 20 | 20 | 16 | 228 | 1,046 | 2,813 | 5,811 | 1,040 |
| GIB | GIB | 5 |  |  |  |  |  |  |  |  |  |  | 5 |  |  |
| Gabón | GAB | 90 |  |  |  |  |  |  |  |  | 2 | 8 | 10 | 21 | 17 |
| Gambia | GMB | 77 |  |  |  |  |  |  |  |  |  | 6 | 30 | 22 | 4 |
| Georgia | GEO | 280 |  |  |  |  |  |  |  | 1 | 12 | 7 | 64 | 65 | 45 |
| Ghana | GHA | 87 |  |  |  |  |  |  | 1 |  | 2 | 8 | 8 | 9 | 20 |
| Granada | GRD | 450 | 1 |  |  |  |  | 3 |  |  | 2 | 22 | 74 | 224 | 30 |
| Grecia | GRC | 2,280 | 18 | 1 | 1 |  |  | 1 | 3 | 7 | 118 | 187 | 167 | 755 | 253 |
| Groenlandia | GRL | 218 | 1 |  |  |  |  |  | 1 |  | 8 | 14 | 41 | 86 | 28 |
| Guam | GUM | 153 |  |  |  |  |  |  |  |  |  | 4 | 15 | 9 | 111 |
| Guatemala | GTM | 237 | 1 | 1 |  |  |  |  |  |  | 3 | 17 | 12 | 57 | 82 |
| Guernsey | GGY | 244 |  |  |  |  |  |  |  |  |  | 4 | 6 | 104 | 110 |
| Guinea | GIN | 144 |  |  |  |  |  |  |  |  | 1 | 11 | 40 | 15 | 17 |
| Guinea Ecuatorial | GNQ | 40 |  |  |  |  |  |  |  |  | 1 | 2 | 2 | 11 | 18 |
| Guinea-Bisáu | GNB | 10 |  |  |  |  |  |  |  |  | 1 |  | 3 | 2 | 2 |
| Guyana | GUY | 427 |  |  |  |  |  |  |  |  | 6 | 34 | 78 | 93 | 61 |
| Haití | HTI | 404 |  |  |  |  |  | 1 |  |  | 6 | 26 | 119 | 64 | 124 |
| Honduras | HND | 275 |  |  |  |  |  |  |  |  |  | 29 | 52 | 66 | 94 |
| Hong Kong | HKG | 63 |  |  |  |  |  |  |  |  |  |  |  | 26 | 24 |
| Hungría | HUN | 1,537 |  |  |  |  |  |  | 2 | 4 | 59 | 77 | 115 | 382 | 143 |
| India | IND | 2,898 | 3 |  |  |  |  |  | 7 | 6 | 84 | 129 | 457 | 915 | 256 |
| Indonesia | IDN | 2,065 | 3 |  |  |  |  |  | 1 | 1 | 26 | 268 | 379 | 191 | 237 |
| Irak | IRQ | 640 | 7 |  |  |  | 1 |  |  | 6 | 46 | 36 | 31 | 119 | 175 |
| Irlanda | IRL | 2,338 | 5 | 1 | 2 | 2 |  |  | 1 | 4 | 87 | 108 | 154 | 737 | 56 |
| Irán | IRN | 770 | 3 |  |  |  |  |  | 3 | 5 | 48 | 38 | 122 | 250 | 89 |
| Isla Norfolk | NFK | 1,358 |  |  |  |  |  |  |  |  |  | 2 | 38 | 1,082 | 206 |
| Isla Santa Elena | SHN | 134 |  |  |  |  |  |  |  |  | 2 | 9 | 8 | 89 | 5 |
| Isla de Man | IMN | 46 |  |  |  |  |  |  |  |  |  |  | 3 | 22 |  |
| Islandia | ISL | 265 | 1 |  |  |  |  |  |  | 1 | 22 | 23 | 28 | 64 | 28 |
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
| Israel | ISR | 1,580 |  |  | 2 | 2 | 2 | 2 | 4 | 21 | 68 | 78 | 182 | 484 | 163 |
| Italia | ITA | 7,952 | 29 | 5 |  | 4 | 6 | 8 | 3 | 56 | 305 | 485 | 663 | 1,842 | 572 |
| Jamaica | JAM | 947 | 1 |  |  |  |  |  |  | 1 | 1 | 22 | 217 | 558 | 55 |
| Japón | JPN | 1,548 | 3 |  |  |  |  |  | 1 | 2 | 11 | 92 | 186 | 367 | 263 |
| Jersey | JEY | 13 |  |  |  |  |  |  |  |  |  | 4 |  | 8 |  |
| Jordania | JOR | 380 |  |  |  |  |  |  |  | 1 | 37 | 18 | 22 | 148 | 27 |
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
| Libia | LBY | 365 | 4 |  |  |  |  |  |  | 9 | 25 | 23 | 26 | 46 | 123 |
| Liechtenstein | LIE | 27 |  |  |  |  |  |  |  | 1 |  | 1 |  | 6 |  |
| Lituania | LTU | 316 |  |  |  |  |  |  |  | 3 | 13 | 15 | 46 | 22 | 50 |
| Luxemburgo | LUX | 437 |  |  |  |  |  |  | 1 | 1 | 14 | 40 | 69 | 72 | 44 |
| Líbano | LBN | 738 | 3 |  |  | 1 | 1 |  |  | 2 | 17 | 6 | 15 | 468 | 132 |
| Macao | MAC | 103 |  |  |  |  |  |  |  |  |  | 5 | 22 | 22 | 36 |
| Macedonia del Norte | MKD | 119 |  |  |  |  |  |  |  | 2 | 13 | 11 | 5 | 19 | 26 |
| Madagascar | MDG | 394 | 1 |  |  |  |  |  |  |  | 15 | 31 | 96 | 93 | 49 |
| Malasia | MYS | 264 | 4 |  |  |  |  |  |  |  | 8 | 9 | 12 | 35 | 45 |
| Malaui | MWI | 37 | 1 |  |  |  |  |  |  |  | 1 |  | 2 | 14 | 14 |
| Maldivas | MDV | 72 |  |  |  |  |  |  |  |  | 1 | 8 | 26 | 9 | 14 |
| Malta | MLT | 318 | 2 |  |  |  |  | 1 | 1 | 2 | 21 | 24 | 85 | 85 | 10 |
| Malí | MLI | 121 |  |  |  |  |  |  | 3 | 2 | 4 | 5 | 8 | 26 | 20 |
| Marruecos | MAR | 610 | 1 |  |  |  |  | 1 |  | 2 | 15 | 47 | 71 | 151 | 158 |
| Mauricio | MUS | 198 | 2 |  |  | 1 |  |  |  | 1 | 5 | 17 | 32 | 55 | 21 |
| Mauritania | MRT | 96 |  |  |  |  |  |  |  |  | 10 | 4 | 13 | 16 | 18 |
| Moldavia | MDA | 140 |  |  |  |  |  |  |  | 1 | 5 | 14 | 25 | 26 | 13 |
| Mongolia | MNG | 145 |  |  |  |  |  |  |  |  | 4 | 11 | 9 | 37 | 62 |
| Montenegro | MNE | 163 |  |  |  |  |  |  |  |  | 8 | 9 | 5 | 34 | 26 |
| Montserrat | MSR | 131 |  |  |  |  |  |  |  |  |  |  |  | 105 | 21 |
| Mozambique | MOZ | 256 | 1 |  |  |  |  |  |  |  | 10 | 16 | 34 | 69 | 54 |
| México | MEX | 4,072 | 3 |  |  |  |  | 1 | 2 | 3 | 64 | 128 | 398 | 1,223 | 1,280 |
| Mónaco | MCO | 65 | 1 |  |  |  |  |  |  |  |  | 6 | 11 | 20 | 7 |
| Namibia | NAM | 137 |  |  |  |  |  |  |  |  | 3 |  | 8 | 41 | 29 |
| Nauru | NRU | 17 |  |  |  |  |  |  |  |  |  |  |  | 3 | 11 |
| Nepal | NPL | 86 |  |  |  |  |  |  |  | 1 | 3 | 2 | 1 | 20 | 30 |
| Nicaragua | NIC | 335 |  |  |  |  |  |  |  |  | 2 | 25 | 26 | 167 | 69 |
| Nigeria | NGA | 135 |  |  |  |  |  |  |  |  | 3 | 10 | 8 | 16 | 57 |
| Niue | NIU | 7 |  |  |  |  |  |  |  |  |  |  |  | 1 | 5 |
| Noruega | NOR | 1,391 | 1 |  |  |  |  |  | 1 | 2 | 21 | 55 | 104 | 411 | 63 |
| Nueva Caledonia | NCL | 25 |  |  |  |  |  |  |  |  |  | 1 | 3 | 6 | 7 |
| Nueva Zelanda | NZL | 468 | 2 |  |  | 1 |  |  |  |  | 1 | 3 | 28 | 239 | 80 |
| Níger | NER | 70 |  |  |  |  |  |  |  |  | 4 | 5 | 3 | 5 | 26 |
| Omán | OMN | 99 |  |  |  |  |  |  |  | 4 | 12 | 10 | 24 | 17 | 11 |
| PSX | PSX | 298 |  |  |  |  |  |  |  | 1 | 17 | 8 | 7 | 106 | 2 |
| Pakistán | PAK | 432 |  |  |  |  |  |  |  |  | 28 | 7 | 11 | 111 | 130 |
| Palaos | PLW | 56 |  |  |  |  |  |  |  |  | 2 | 1 | 10 | 12 | 20 |
| Palestina | PSE | 1,506 | 5 |  |  |  | 2 | 1 | 1 | 10 | 48 | 45 | 84 | 585 | 205 |
| Panamá | PAN | 417 |  |  |  |  |  |  |  |  | 3 | 51 | 57 | 97 | 115 |
| Papúa Nueva Guinea | PNG | 152 |  |  |  |  |  |  |  |  | 2 | 4 | 4 | 38 | 77 |
| Paraguay | PRY | 342 |  |  |  |  |  |  |  |  | 1 | 14 | 55 | 97 | 56 |
| Países Bajos | NLD | 19,490 | 1 |  | 5 |  |  |  | 1 | 1 | 122 | 529 | 690 | 556 | 1,036 |
| Perú | PER | 1,120 | 1 |  |  |  |  |  |  |  | 20 | 59 | 96 | 424 | 229 |
| Polinesia Francesa | PYF | 70 |  |  |  |  |  |  |  |  |  | 1 | 35 | 26 | 5 |
| Polonia | POL | 3,527 | 2 |  | 2 | 1 | 2 |  | 2 | 8 | 57 | 98 | 267 | 758 | 533 |
| Portugal | PRT | 3,174 | 2 |  |  |  |  | 1 | 1 | 10 | 62 | 148 | 533 | 1,190 | 224 |
| Puerto Rico | PRI | 1,082 |  |  |  |  |  |  |  | 1 | 2 | 19 | 71 | 40 | 906 |
| Reino Unido | GBR | 12,963 | 8 | 2 | 3 | 3 | 3 | 13 |  | 8 | 73 | 491 | 1,444 | 3,210 | 529 |
| República Centroafricana | CAF | 160 |  |  |  |  |  |  |  |  |  | 2 | 3 | 10 | 114 |
| República Checa | CZE | 1,301 | 2 |  |  |  |  |  |  | 1 | 18 | 35 | 83 | 232 | 230 |
| República Democrática del Congo | COD | 225 |  |  |  |  |  |  |  |  | 3 | 6 | 9 | 31 | 128 |
| República Dominicana | DOM | 257 |  |  |  |  |  |  |  |  | 5 | 27 | 69 | 46 | 59 |
| República Turca del Norte de Chipre | CYN | 15 |  |  |  |  |  |  |  |  | 2 | 5 |  |  |  |
| República de China | TWN | 212 |  |  |  |  |  |  | 1 |  | 2 | 17 | 9 | 50 | 87 |
| República del Congo | COG | 313 | 2 |  |  |  |  |  | 1 | 1 | 8 | 11 | 37 | 113 | 76 |
| Ruanda | RWA | 43 | 1 |  |  |  |  |  |  |  |  |  |  | 4 | 32 |
| Rumania | ROU | 1,163 |  |  |  |  |  |  |  | 3 | 43 | 29 | 54 | 193 | 202 |
| Rusia | RUS | 5,429 | 5 |  |  |  |  | 1 | 2 | 6 | 74 | 155 | 347 | 1,906 | 1,259 |
| SAH | SAH | 4 |  |  |  |  |  |  |  |  |  | 2 |  | 1 |  |
| SDS | SDS | 82 |  |  |  |  |  |  |  |  |  | 1 |  | 10 | 19 |
| Sahara Occidental | ESH | 37 |  |  |  |  |  |  | 1 |  |  | 2 | 1 | 17 | 14 |
| Samoa | WSM | 72 | 1 |  |  |  |  |  |  |  |  |  | 6 | 31 | 25 |
| Samoa Estadounidense | ASM | 26 |  |  |  |  |  |  |  |  |  |  |  | 14 | 7 |
| San Bartolomé | BLM | 6 |  |  |  |  |  |  |  |  |  |  | 3 | 2 |  |
| San Cristóbal y Nieves | KNA | 34 |  |  |  |  |  |  |  |  |  | 5 | 17 | 2 | 3 |
| San Marino | SMR | 8 |  |  | 1 |  |  |  |  |  |  | 1 | 1 | 1 | 2 |
| San Martín | MAF | 74 |  |  |  |  |  |  |  |  |  |  | 10 | 36 | 8 |
| San Martín | SXM | 34 |  |  |  |  |  |  |  | 1 |  |  | 6 | 17 | 3 |
| San Pedro y Miquelón | SPM | 8 |  |  |  |  |  |  |  |  |  |  | 1 | 5 | 1 |
| San Vicente y las Granadinas | VCT | 23 | 1 |  |  |  |  |  |  |  |  |  | 6 | 11 | 4 |
| Santa Lucía | LCA | 37 |  |  |  |  |  |  |  |  |  | 1 | 20 | 4 | 5 |
| Santo Tomé y Príncipe | STP | 28 |  |  |  | 1 |  |  |  |  |  | 10 | 10 | 4 | 1 |
| Senegal | SEN | 210 |  |  |  |  |  |  |  |  | 2 | 10 | 71 | 69 | 15 |
| Serbia | SRB | 556 |  |  |  |  |  |  |  | 4 | 28 | 18 | 35 | 144 | 74 |
| Seychelles | SYC | 3 |  |  |  |  |  |  |  |  |  |  |  | 3 |  |
| Sierra Leona | SLE | 184 |  |  |  |  |  |  |  | 1 | 2 | 10 | 22 | 18 | 98 |
| Singapur | SGP | 76 |  |  |  |  |  |  |  | 1 | 2 | 1 | 1 | 29 | 11 |
| Siria | SYR | 1,027 | 2 |  |  | 1 | 1 |  |  | 4 | 47 | 34 | 81 | 507 | 110 |
| Somalia | SOM | 196 |  |  |  |  |  |  |  | 1 | 11 | 7 | 6 | 21 | 105 |
| Somalilandia | SOL | 223 |  |  |  |  |  |  |  |  | 2 | 4 |  | 32 | 169 |
| Sri Lanka | LKA | 289 |  |  |  |  |  |  | 2 | 2 | 18 | 41 | 32 | 60 | 25 |
| Suazilandia | SWZ | 45 |  |  |  | 1 |  |  |  |  |  |  |  | 3 | 38 |
| Sudáfrica | ZAF | 757 | 5 |  |  |  |  | 1 |  |  | 6 | 28 | 46 | 286 | 175 |
| Sudán | SDN | 546 | 1 | 3 |  |  |  |  |  | 2 | 9 | 18 | 15 | 112 | 255 |
| Sudán del Sur | SSD | 202 |  |  |  |  |  |  |  |  | 1 | 4 | 2 | 17 | 89 |
| Suecia | SWE | 1,682 | 2 |  |  |  |  |  | 1 | 3 | 13 | 57 | 85 | 384 | 54 |
| Suiza | CHE | 2,697 | 3 |  |  |  |  | 1 | 1 | 5 | 58 | 71 | 176 | 583 | 179 |
| Surinam | SUR | 494 |  |  |  |  |  |  |  |  | 6 | 24 | 48 | 60 | 62 |
| Tailandia | THA | 260 | 1 |  |  |  |  |  | 2 | 1 | 13 | 20 | 26 | 68 | 60 |
| Tanzania | TZA | 215 | 1 |  |  |  |  |  |  |  | 4 | 2 | 3 | 51 | 85 |
| Tayikistán | TJK | 61 |  |  |  |  |  |  |  |  | 6 |  |  | 29 | 15 |
| Territorio Británico del Océano Índico | IOT | 1 |  |  |  |  |  |  |  |  |  |  |  |  | 1 |
| Territorios Australianos del Océano Índico | IOA | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Tierras Australes y Antárticas Francesas | ATF | 4 |  |  |  |  |  |  |  |  |  |  |  | 1 |  |
| Timor Oriental | TLS | 15 |  |  |  |  |  |  |  |  |  |  |  |  | 2 |
| Togo | TGO | 58 |  |  |  |  |  |  |  |  | 1 | 1 | 2 | 8 | 17 |
| Tonga | TON | 47 |  |  |  |  |  |  |  |  |  | 4 | 7 | 14 | 10 |
| Trinidad y Tobago | TTO | 102 |  |  |  |  |  |  |  |  | 1 | 19 | 35 | 12 | 32 |
| Turkmenistán | TKM | 130 |  |  |  |  |  |  |  |  | 14 | 6 | 4 | 50 | 20 |
| Turquía | TUR | 2,581 | 14 |  |  | 1 |  | 1 | 7 | 8 | 108 | 123 | 267 | 890 | 319 |
| Tuvalu | TUV | 14 |  |  |  |  |  |  |  |  |  |  |  | 8 | 4 |
| Túnez | TUN | 606 | 3 |  |  |  |  | 1 | 1 | 2 | 32 | 11 | 26 | 220 | 174 |
| UMI | UMI | 2 |  |  |  |  |  |  |  |  |  |  |  | 2 |  |
| USG | USG | 3 |  |  |  |  |  |  |  |  |  |  | 1 | 1 |  |
| Ucrania | UKR | 793 | 1 |  |  |  |  |  | 4 | 4 | 32 | 76 | 65 | 98 | 97 |
| Uganda | UGA | 248 |  |  |  |  |  |  |  |  | 1 | 3 | 3 | 15 | 192 |
| Uruguay | URY | 361 |  |  |  |  |  |  |  |  | 4 | 22 | 52 | 125 | 69 |
| Uzbekistán | UZB | 130 |  |  |  |  |  |  |  |  | 7 | 6 | 6 | 60 | 31 |
| Vanuatu | VUT | 15 |  |  |  |  |  |  |  |  |  |  |  | 2 | 13 |
| Venezuela | VEN | 575 |  |  |  |  |  |  |  | 1 | 12 | 83 | 125 | 121 | 77 |
| Vietnam | VNM | 346 |  |  |  |  |  |  |  | 2 | 8 | 5 | 18 | 53 | 87 |
| Yemen | YEM | 439 |  |  |  |  |  |  |  | 5 | 24 | 15 | 19 | 46 | 276 |
| Yibuti | DJI | 58 |  |  |  |  |  |  |  |  | 2 | 2 | 3 | 28 | 20 |
| Zambia | ZMB | 105 |  |  |  |  |  |  |  |  | 1 | 3 | 4 | 20 | 45 |
| Zimbabue | ZWE | 110 |  |  |  |  |  |  |  |  | 2 | 1 | 6 | 26 | 43 |
| Åland | ALA | 6 |  |  |  |  |  |  |  |  |  |  |  | 3 |  |
