## Граф
[map.png](map.png)
## Приклад роботи:
### Завдання 1
```
Кількість вузлів: 24
Кількість ребер:  37



Граф незвʼязний



Ступінь вузла "Вінниця" = 5
Ступінь вузла "Дніпро" = 4
Ступінь вузла "Донецьк" = 1
Ступінь вузла "Житомир" = 3
Ступінь вузла "Запоріжжя" = 2
Ступінь вузла "Івано-Франківськ" = 4
Ступінь вузла "Київ" = 6
Ступінь вузла "Кропивницький" = 4
Ступінь вузла "Луганськ" = 1
Ступінь вузла "Луцьк" = 2
Ступінь вузла "Львів" = 4
Ступінь вузла "Миколаїв" = 4
Ступінь вузла "Одеса" = 3
Ступінь вузла "Полтава" = 5
Ступінь вузла "Рівне" = 3
Ступінь вузла "Суми" = 3
Ступінь вузла "Тернопіль" = 4
Ступінь вузла "Ужгород" = 2
Ступінь вузла "Харків" = 3
Ступінь вузла "Херсон" = 1
Ступінь вузла "Хмельницький" = 3
Ступінь вузла "Черкаси" = 3
Ступінь вузла "Чернівці" = 3
Ступінь вузла "Чернігів" = 1
```

### Завдання 2
```
DFS:
Київ Житомир Вінниця Кропивницький Черкаси Полтава Дніпро Запоріжжя Миколаїв Херсон Одеса Харків Суми Хмельницький Тернопіль Івано-Франківськ Львів Луцьк Рівне Ужгород Чернівці Чернігів 


BFS:
Київ Чернігів Черкаси Житомир Одеса Полтава Суми Кропивницький Рівне Вінниця Миколаїв Дніпро Харків Луцьк Хмельницький Чернівці Херсон Запоріжжя Львів Тернопіль Івано-Франківськ Ужгород 
```

#### Висновок
По результату роботи видно, що DFS обходить граф в глибину, в той час як BFS йде в ширину.

### Завдання 3
```
Dijkstra:
Найкоротша відстань від Вінниця до Дніпро: 663
Найкоротша відстань від Вінниця до Донецьк: inf
Найкоротша відстань від Вінниця до Житомир: 103
Найкоротша відстань від Вінниця до Запоріжжя: 726
Найкоротша відстань від Вінниця до Івано-Франківськ: 396
Найкоротша відстань від Вінниця до Київ: 290
Найкоротша відстань від Вінниця до Кропивницький: 385
Найкоротша відстань від Вінниця до Луганськ: inf
Найкоротша відстань від Вінниця до Луцьк: 380
Найкоротша відстань від Вінниця до Львів: 447
Найкоротша відстань від Вінниця до Миколаїв: 491
Найкоротша відстань від Вінниця до Одеса: 355
Найкоротша відстань від Вінниця до Полтава: 701
Найкоротша відстань від Вінниця до Рівне: 289
Найкоротша відстань від Вінниця до Суми: 719
Найкоротша відстань від Вінниця до Тернопіль: 288
Найкоротша відстань від Вінниця до Ужгород: 640
Найкоротша відстань від Вінниця до Харків: 856
Найкоротша відстань від Вінниця до Херсон: 561
Найкоротша відстань від Вінниця до Хмельницький: 149
Найкоротша відстань від Вінниця до Черкаси: 473
Найкоротша відстань від Вінниця до Чернівці: 270
Найкоротша відстань від Вінниця до Чернігів: 419
Найкоротша відстань від Дніпро до Вінниця: 663
Найкоротша відстань від Дніпро до Донецьк: inf
Найкоротша відстань від Дніпро до Житомир: 720
Найкоротша відстань від Дніпро до Запоріжжя: 63
Найкоротша відстань від Дніпро до Івано-Франківськ: 1059
Найкоротша відстань від Дніпро до Київ: 533
Найкоротша відстань від Дніпро до Кропивницький: 278
Найкоротша відстань від Дніпро до Луганськ: inf
Найкоротша відстань від Дніпро до Луцьк: 1043
Найкоротша відстань від Дніпро до Львів: 1110
Найкоротша відстань від Дніпро до Миколаїв: 389
Найкоротша відстань від Дніпро до Одеса: 525
Найкоротша відстань від Дніпро до Полтава: 122
Найкоротша відстань від Дніпро до Рівне: 952
Найкоротша відстань від Дніпро до Суми: 256
Найкоротша відстань від Дніпро до Тернопіль: 951
Найкоротша відстань від Дніпро до Ужгород: 1303
Найкоротша відстань від Дніпро до Харків: 193
Найкоротша відстань від Дніпро до Херсон: 459
Найкоротша відстань від Дніпро до Хмельницький: 812
Найкоротша відстань від Дніпро до Черкаси: 371
Найкоротша відстань від Дніпро до Чернівці: 933
Найкоротша відстань від Дніпро до Чернігів: 662
Найкоротша відстань від Донецьк до Вінниця: inf
Найкоротша відстань від Донецьк до Дніпро: inf
Найкоротша відстань від Донецьк до Житомир: inf
Найкоротша відстань від Донецьк до Запоріжжя: inf
Найкоротша відстань від Донецьк до Івано-Франківськ: inf
Найкоротша відстань від Донецьк до Київ: inf
Найкоротша відстань від Донецьк до Кропивницький: inf
Найкоротша відстань від Донецьк до Луганськ: 160
Найкоротша відстань від Донецьк до Луцьк: inf
Найкоротша відстань від Донецьк до Львів: inf
Найкоротша відстань від Донецьк до Миколаїв: inf
Найкоротша відстань від Донецьк до Одеса: inf
Найкоротша відстань від Донецьк до Полтава: inf
Найкоротша відстань від Донецьк до Рівне: inf
Найкоротша відстань від Донецьк до Суми: inf
Найкоротша відстань від Донецьк до Тернопіль: inf
Найкоротша відстань від Донецьк до Ужгород: inf
Найкоротша відстань від Донецьк до Харків: inf
Найкоротша відстань від Донецьк до Херсон: inf
Найкоротша відстань від Донецьк до Хмельницький: inf
Найкоротша відстань від Донецьк до Черкаси: inf
Найкоротша відстань від Донецьк до Чернівці: inf
Найкоротша відстань від Донецьк до Чернігів: inf
Найкоротша відстань від Житомир до Вінниця: 103
Найкоротша відстань від Житомир до Дніпро: 720
Найкоротша відстань від Житомир до Донецьк: inf
Найкоротша відстань від Житомир до Запоріжжя: 783
Найкоротша відстань від Житомир до Івано-Франківськ: 499
Найкоротша відстань від Житомир до Київ: 187
Найкоротша відстань від Житомир до Кропивницький: 465
Найкоротша відстань від Житомир до Луганськ: inf
Найкоротша відстань від Житомир до Луцьк: 334
Найкоротша відстань від Житомир до Львів: 494
Найкоротша відстань від Житомир до Миколаїв: 594
Найкоротша відстань від Житомир до Одеса: 458
Найкоротша відстань від Житомир до Полтава: 598
Найкоротша відстань від Житомир до Рівне: 243
Найкоротша відстань від Житомир до Суми: 616
Найкоротша відстань від Житомир до Тернопіль: 391
Найкоротша відстань від Житомир до Ужгород: 706
Найкоротша відстань від Житомир до Харків: 770
Найкоротша відстань від Житомир до Херсон: 664
Найкоротша відстань від Житомир до Хмельницький: 252
Найкоротша відстань від Житомир до Черкаси: 370
Найкоротша відстань від Житомир до Чернівці: 373
Найкоротша відстань від Житомир до Чернігів: 316
Найкоротша відстань від Запоріжжя до Вінниця: 726
Найкоротша відстань від Запоріжжя до Дніпро: 63
Найкоротша відстань від Запоріжжя до Донецьк: inf
Найкоротша відстань від Запоріжжя до Житомир: 783
Найкоротша відстань від Запоріжжя до Івано-Франківськ: 1122
Найкоротша відстань від Запоріжжя до Київ: 596
Найкоротша відстань від Запоріжжя до Кропивницький: 341
Найкоротша відстань від Запоріжжя до Луганськ: inf
Найкоротша відстань від Запоріжжя до Луцьк: 1106
Найкоротша відстань від Запоріжжя до Львів: 1173
Найкоротша відстань від Запоріжжя до Миколаїв: 326
Найкоротша відстань від Запоріжжя до Одеса: 462
Найкоротша відстань від Запоріжжя до Полтава: 185
Найкоротша відстань від Запоріжжя до Рівне: 1015
Найкоротша відстань від Запоріжжя до Суми: 319
Найкоротша відстань від Запоріжжя до Тернопіль: 1014
Найкоротша відстань від Запоріжжя до Ужгород: 1366
Найкоротша відстань від Запоріжжя до Харків: 256
Найкоротша відстань від Запоріжжя до Херсон: 396
Найкоротша відстань від Запоріжжя до Хмельницький: 875
Найкоротша відстань від Запоріжжя до Черкаси: 434
Найкоротша відстань від Запоріжжя до Чернівці: 996
Найкоротша відстань від Запоріжжя до Чернігів: 725
Найкоротша відстань від Івано-Франківськ до Вінниця: 396
Найкоротша відстань від Івано-Франківськ до Дніпро: 1059
Найкоротша відстань від Івано-Франківськ до Донецьк: inf
Найкоротша відстань від Івано-Франківськ до Житомир: 499
Найкоротша відстань від Івано-Франківськ до Запоріжжя: 1122
Найкоротша відстань від Івано-Франківськ до Київ: 686
Найкоротша відстань від Івано-Франківськ до Кропивницький: 781
Найкоротша відстань від Івано-Франківськ до Луганськ: inf
Найкоротша відстань від Івано-Франківськ до Луцьк: 274
Найкоротша відстань від Івано-Франківськ до Львів: 114
Найкоротша відстань від Івано-Франківськ до Миколаїв: 887
Найкоротша відстань від Івано-Франківськ до Одеса: 751
Найкоротша відстань від Івано-Франківськ до Полтава: 1097
Найкоротша відстань від Івано-Франківськ до Рівне: 365
Найкоротша відстань від Івано-Франківськ до Суми: 1115
Найкоротша відстань від Івано-Франківськ до Тернопіль: 108
Найкоротша відстань від Івано-Франківськ до Ужгород: 244
Найкоротша відстань від Івано-Франківськ до Харків: 1252
Найкоротша відстань від Івано-Франківськ до Херсон: 957
Найкоротша відстань від Івано-Франківськ до Хмельницький: 247
Найкоротша відстань від Івано-Франківськ до Черкаси: 869
Найкоротша відстань від Івано-Франківськ до Чернівці: 137
Найкоротша відстань від Івано-Франківськ до Чернігів: 815
Найкоротша відстань від Київ до Вінниця: 290
Найкоротша відстань від Київ до Дніпро: 533
Найкоротша відстань від Київ до Донецьк: inf
Найкоротша відстань від Київ до Житомир: 187
Найкоротша відстань від Київ до Запоріжжя: 596
Найкоротша відстань від Київ до Івано-Франківськ: 686
Найкоротша відстань від Київ до Кропивницький: 278
Найкоротша відстань від Київ до Луганськ: inf
Найкоротша відстань від Київ до Луцьк: 521
Найкоротша відстань від Київ до Львів: 681
Найкоротша відстань від Київ до Миколаїв: 434
Найкоротша відстань від Київ до Одеса: 397
Найкоротша відстань від Київ до Полтава: 411
Найкоротша відстань від Київ до Рівне: 430
Найкоротша відстань від Київ до Суми: 429
Найкоротша відстань від Київ до Тернопіль: 578
Найкоротша відстань від Київ до Ужгород: 893
Найкоротша відстань від Київ до Харків: 583
Найкоротша відстань від Київ до Херсон: 504
Найкоротша відстань від Київ до Хмельницький: 439
Найкоротша відстань від Київ до Черкаси: 183
Найкоротша відстань від Київ до Чернівці: 560
Найкоротша відстань від Київ до Чернігів: 129
Найкоротша відстань від Кропивницький до Вінниця: 385
Найкоротша відстань від Кропивницький до Дніпро: 278
Найкоротша відстань від Кропивницький до Донецьк: inf
Найкоротша відстань від Кропивницький до Житомир: 465
Найкоротша відстань від Кропивницький до Запоріжжя: 341
Найкоротша відстань від Кропивницький до Івано-Франківськ: 781
Найкоротша відстань від Кропивницький до Київ: 278
Найкоротша відстань від Кропивницький до Луганськ: inf
Найкоротша відстань від Кропивницький до Луцьк: 765
Найкоротша відстань від Кропивницький до Львів: 832
Найкоротша відстань від Кропивницький до Миколаїв: 156
Найкоротша відстань від Кропивницький до Одеса: 292
Найкоротша відстань від Кропивницький до Полтава: 344
Найкоротша відстань від Кропивницький до Рівне: 674
Найкоротша відстань від Кропивницький до Суми: 478
Найкоротша відстань від Кропивницький до Тернопіль: 673
Найкоротша відстань від Кропивницький до Ужгород: 1025
Найкоротша відстань від Кропивницький до Харків: 471
Найкоротша відстань від Кропивницький до Херсон: 226
Найкоротша відстань від Кропивницький до Хмельницький: 534
Найкоротша відстань від Кропивницький до Черкаси: 95
Найкоротша відстань від Кропивницький до Чернівці: 655
Найкоротша відстань від Кропивницький до Чернігів: 407
Найкоротша відстань від Луганськ до Вінниця: inf
Найкоротша відстань від Луганськ до Дніпро: inf
Найкоротша відстань від Луганськ до Донецьк: 160
Найкоротша відстань від Луганськ до Житомир: inf
Найкоротша відстань від Луганськ до Запоріжжя: inf
Найкоротша відстань від Луганськ до Івано-Франківськ: inf
Найкоротша відстань від Луганськ до Київ: inf
Найкоротша відстань від Луганськ до Кропивницький: inf
Найкоротша відстань від Луганськ до Луцьк: inf
Найкоротша відстань від Луганськ до Львів: inf
Найкоротша відстань від Луганськ до Миколаїв: inf
Найкоротша відстань від Луганськ до Одеса: inf
Найкоротша відстань від Луганськ до Полтава: inf
Найкоротша відстань від Луганськ до Рівне: inf
Найкоротша відстань від Луганськ до Суми: inf
Найкоротша відстань від Луганськ до Тернопіль: inf
Найкоротша відстань від Луганськ до Ужгород: inf
Найкоротша відстань від Луганськ до Харків: inf
Найкоротша відстань від Луганськ до Херсон: inf
Найкоротша відстань від Луганськ до Хмельницький: inf
Найкоротша відстань від Луганськ до Черкаси: inf
Найкоротша відстань від Луганськ до Чернівці: inf
Найкоротша відстань від Луганськ до Чернігів: inf
Найкоротша відстань від Луцьк до Вінниця: 380
Найкоротша відстань від Луцьк до Дніпро: 1043
Найкоротша відстань від Луцьк до Донецьк: inf
Найкоротша відстань від Луцьк до Житомир: 334
Найкоротша відстань від Луцьк до Запоріжжя: 1106
Найкоротша відстань від Луцьк до Івано-Франківськ: 274
Найкоротша відстань від Луцьк до Київ: 521
Найкоротша відстань від Луцьк до Кропивницький: 765
Найкоротша відстань від Луцьк до Луганськ: inf
Найкоротша відстань від Луцьк до Львів: 160
Найкоротша відстань від Луцьк до Миколаїв: 871
Найкоротша відстань від Луцьк до Одеса: 735
Найкоротша відстань від Луцьк до Полтава: 932
Найкоротша відстань від Луцьк до Рівне: 91
Найкоротша відстань від Луцьк до Суми: 950
Найкоротша відстань від Луцьк до Тернопіль: 319
Найкоротша відстань від Луцьк до Ужгород: 372
Найкоротша відстань від Луцьк до Харків: 1104
Найкоротша відстань від Луцьк до Херсон: 941
Найкоротша відстань від Луцьк до Хмельницький: 231
Найкоротша відстань від Луцьк до Черкаси: 704
Найкоротша відстань від Луцьк до Чернівці: 411
Найкоротша відстань від Луцьк до Чернігів: 650
Найкоротша відстань від Львів до Вінниця: 447
Найкоротша відстань від Львів до Дніпро: 1110
Найкоротша відстань від Львів до Донецьк: inf
Найкоротша відстань від Львів до Житомир: 494
Найкоротша відстань від Львів до Запоріжжя: 1173
Найкоротша відстань від Львів до Івано-Франківськ: 114
Найкоротша відстань від Львів до Київ: 681
Найкоротша відстань від Львів до Кропивницький: 832
Найкоротша відстань від Львів до Луганськ: inf
Найкоротша відстань від Львів до Луцьк: 160
Найкоротша відстань від Львів до Миколаїв: 938
Найкоротша відстань від Львів до Одеса: 802
Найкоротша відстань від Львів до Полтава: 1092
Найкоротша відстань від Львів до Рівне: 251
Найкоротша відстань від Львів до Суми: 1110
Найкоротша відстань від Львів до Тернопіль: 159
Найкоротша відстань від Львів до Ужгород: 212
Найкоротша відстань від Львів до Харків: 1264
Найкоротша відстань від Львів до Херсон: 1008
Найкоротша відстань від Львів до Хмельницький: 298
Найкоротша відстань від Львів до Черкаси: 864
Найкоротша відстань від Львів до Чернівці: 251
Найкоротша відстань від Львів до Чернігів: 810
Найкоротша відстань від Миколаїв до Вінниця: 491
Найкоротша відстань від Миколаїв до Дніпро: 389
Найкоротша відстань від Миколаїв до Донецьк: inf
Найкоротша відстань від Миколаїв до Житомир: 594
Найкоротша відстань від Миколаїв до Запоріжжя: 326
Найкоротша відстань від Миколаїв до Івано-Франківськ: 887
Найкоротша відстань від Миколаїв до Київ: 434
Найкоротша відстань від Миколаїв до Кропивницький: 156
Найкоротша відстань від Миколаїв до Луганськ: inf
Найкоротша відстань від Миколаїв до Луцьк: 871
Найкоротша відстань від Миколаїв до Львів: 938
Найкоротша відстань від Миколаїв до Одеса: 136
Найкоротша відстань від Миколаїв до Полтава: 500
Найкоротша відстань від Миколаїв до Рівне: 780
Найкоротша відстань від Миколаїв до Суми: 634
Найкоротша відстань від Миколаїв до Тернопіль: 779
Найкоротша відстань від Миколаїв до Ужгород: 1131
Найкоротша відстань від Миколаїв до Харків: 582
Найкоротша відстань від Миколаїв до Херсон: 70
Найкоротша відстань від Миколаїв до Хмельницький: 640
Найкоротша відстань від Миколаїв до Черкаси: 251
Найкоротша відстань від Миколаїв до Чернівці: 761
Найкоротша відстань від Миколаїв до Чернігів: 563
Найкоротша відстань від Одеса до Вінниця: 355
Найкоротша відстань від Одеса до Дніпро: 525
Найкоротша відстань від Одеса до Донецьк: inf
Найкоротша відстань від Одеса до Житомир: 458
Найкоротша відстань від Одеса до Запоріжжя: 462
Найкоротша відстань від Одеса до Івано-Франківськ: 751
Найкоротша відстань від Одеса до Київ: 397
Найкоротша відстань від Одеса до Кропивницький: 292
Найкоротша відстань від Одеса до Луганськ: inf
Найкоротша відстань від Одеса до Луцьк: 735
Найкоротша відстань від Одеса до Львів: 802
Найкоротша відстань від Одеса до Миколаїв: 136
Найкоротша відстань від Одеса до Полтава: 636
Найкоротша відстань від Одеса до Рівне: 644
Найкоротша відстань від Одеса до Суми: 770
Найкоротша відстань від Одеса до Тернопіль: 643
Найкоротша відстань від Одеса до Ужгород: 995
Найкоротша відстань від Одеса до Харків: 718
Найкоротша відстань від Одеса до Херсон: 206
Найкоротша відстань від Одеса до Хмельницький: 504
Найкоротша відстань від Одеса до Черкаси: 387
Найкоротша відстань від Одеса до Чернівці: 625
Найкоротша відстань від Одеса до Чернігів: 526
Найкоротша відстань від Полтава до Вінниця: 701
Найкоротша відстань від Полтава до Дніпро: 122
Найкоротша відстань від Полтава до Донецьк: inf
Найкоротша відстань від Полтава до Житомир: 598
Найкоротша відстань від Полтава до Запоріжжя: 185
Найкоротша відстань від Полтава до Івано-Франківськ: 1097
Найкоротша відстань від Полтава до Київ: 411
Найкоротша відстань від Полтава до Кропивницький: 344
Найкоротша відстань від Полтава до Луганськ: inf
Найкоротша відстань від Полтава до Луцьк: 932
Найкоротша відстань від Полтава до Львів: 1092
Найкоротша відстань від Полтава до Миколаїв: 500
Найкоротша відстань від Полтава до Одеса: 636
Найкоротша відстань від Полтава до Рівне: 841
Найкоротша відстань від Полтава до Суми: 134
Найкоротша відстань від Полтава до Тернопіль: 989
Найкоротша відстань від Полтава до Ужгород: 1304
Найкоротша відстань від Полтава до Харків: 172
Найкоротша відстань від Полтава до Херсон: 570
Найкоротша відстань від Полтава до Хмельницький: 850
Найкоротша відстань від Полтава до Черкаси: 249
Найкоротша відстань від Полтава до Чернівці: 971
Найкоротша відстань від Полтава до Чернігів: 540
Найкоротша відстань від Рівне до Вінниця: 289
Найкоротша відстань від Рівне до Дніпро: 952
Найкоротша відстань від Рівне до Донецьк: inf
Найкоротша відстань від Рівне до Житомир: 243
Найкоротша відстань від Рівне до Запоріжжя: 1015
Найкоротша відстань від Рівне до Івано-Франківськ: 365
Найкоротша відстань від Рівне до Київ: 430
Найкоротша відстань від Рівне до Кропивницький: 674
Найкоротша відстань від Рівне до Луганськ: inf
Найкоротша відстань від Рівне до Луцьк: 91
Найкоротша відстань від Рівне до Львів: 251
Найкоротша відстань від Рівне до Миколаїв: 780
Найкоротша відстань від Рівне до Одеса: 644
Найкоротша відстань від Рівне до Полтава: 841
Найкоротша відстань від Рівне до Суми: 859
Найкоротша відстань від Рівне до Тернопіль: 279
Найкоротша відстань від Рівне до Ужгород: 463
Найкоротша відстань від Рівне до Харків: 1013
Найкоротша відстань від Рівне до Херсон: 850
Найкоротша відстань від Рівне до Хмельницький: 140
Найкоротша відстань від Рівне до Черкаси: 613
Найкоротша відстань від Рівне до Чернівці: 409
Найкоротша відстань від Рівне до Чернігів: 559
Найкоротша відстань від Суми до Вінниця: 719
Найкоротша відстань від Суми до Дніпро: 256
Найкоротша відстань від Суми до Донецьк: inf
Найкоротша відстань від Суми до Житомир: 616
Найкоротша відстань від Суми до Запоріжжя: 319
Найкоротша відстань від Суми до Івано-Франківськ: 1115
Найкоротша відстань від Суми до Київ: 429
Найкоротша відстань від Суми до Кропивницький: 478
Найкоротша відстань від Суми до Луганськ: inf
Найкоротша відстань від Суми до Луцьк: 950
Найкоротша відстань від Суми до Львів: 1110
Найкоротша відстань від Суми до Миколаїв: 634
Найкоротша відстань від Суми до Одеса: 770
Найкоротша відстань від Суми до Полтава: 134
Найкоротша відстань від Суми до Рівне: 859
Найкоротша відстань від Суми до Тернопіль: 1007
Найкоротша відстань від Суми до Ужгород: 1322
Найкоротша відстань від Суми до Харків: 169
Найкоротша відстань від Суми до Херсон: 704
Найкоротша відстань від Суми до Хмельницький: 868
Найкоротша відстань від Суми до Черкаси: 383
Найкоротша відстань від Суми до Чернівці: 989
Найкоротша відстань від Суми до Чернігів: 558
Найкоротша відстань від Тернопіль до Вінниця: 288
Найкоротша відстань від Тернопіль до Дніпро: 951
Найкоротша відстань від Тернопіль до Донецьк: inf
Найкоротша відстань від Тернопіль до Житомир: 391
Найкоротша відстань від Тернопіль до Запоріжжя: 1014
Найкоротша відстань від Тернопіль до Івано-Франківськ: 108
Найкоротша відстань від Тернопіль до Київ: 578
Найкоротша відстань від Тернопіль до Кропивницький: 673
Найкоротша відстань від Тернопіль до Луганськ: inf
Найкоротша відстань від Тернопіль до Луцьк: 319
Найкоротша відстань від Тернопіль до Львів: 159
Найкоротша відстань від Тернопіль до Миколаїв: 779
Найкоротша відстань від Тернопіль до Одеса: 643
Найкоротша відстань від Тернопіль до Полтава: 989
Найкоротша відстань від Тернопіль до Рівне: 279
Найкоротша відстань від Тернопіль до Суми: 1007
Найкоротша відстань від Тернопіль до Ужгород: 352
Найкоротша відстань від Тернопіль до Харків: 1144
Найкоротша відстань від Тернопіль до Херсон: 849
Найкоротша відстань від Тернопіль до Хмельницький: 139
Найкоротша відстань від Тернопіль до Черкаси: 761
Найкоротша відстань від Тернопіль до Чернівці: 130
Найкоротша відстань від Тернопіль до Чернігів: 707
Найкоротша відстань від Ужгород до Вінниця: 640
Найкоротша відстань від Ужгород до Дніпро: 1303
Найкоротша відстань від Ужгород до Донецьк: inf
Найкоротша відстань від Ужгород до Житомир: 706
Найкоротша відстань від Ужгород до Запоріжжя: 1366
Найкоротша відстань від Ужгород до Івано-Франківськ: 244
Найкоротша відстань від Ужгород до Київ: 893
Найкоротша відстань від Ужгород до Кропивницький: 1025
Найкоротша відстань від Ужгород до Луганськ: inf
Найкоротша відстань від Ужгород до Луцьк: 372
Найкоротша відстань від Ужгород до Львів: 212
Найкоротша відстань від Ужгород до Миколаїв: 1131
Найкоротша відстань від Ужгород до Одеса: 995
Найкоротша відстань від Ужгород до Полтава: 1304
Найкоротша відстань від Ужгород до Рівне: 463
Найкоротша відстань від Ужгород до Суми: 1322
Найкоротша відстань від Ужгород до Тернопіль: 352
Найкоротша відстань від Ужгород до Харків: 1476
Найкоротша відстань від Ужгород до Херсон: 1201
Найкоротша відстань від Ужгород до Хмельницький: 491
Найкоротша відстань від Ужгород до Черкаси: 1076
Найкоротша відстань від Ужгород до Чернівці: 381
Найкоротша відстань від Ужгород до Чернігів: 1022
Найкоротша відстань від Харків до Вінниця: 856
Найкоротша відстань від Харків до Дніпро: 193
Найкоротша відстань від Харків до Донецьк: inf
Найкоротша відстань від Харків до Житомир: 770
Найкоротша відстань від Харків до Запоріжжя: 256
Найкоротша відстань від Харків до Івано-Франківськ: 1252
Найкоротша відстань від Харків до Київ: 583
Найкоротша відстань від Харків до Кропивницький: 471
Найкоротша відстань від Харків до Луганськ: inf
Найкоротша відстань від Харків до Луцьк: 1104
Найкоротша відстань від Харків до Львів: 1264
Найкоротша відстань від Харків до Миколаїв: 582
Найкоротша відстань від Харків до Одеса: 718
Найкоротша відстань від Харків до Полтава: 172
Найкоротша відстань від Харків до Рівне: 1013
Найкоротша відстань від Харків до Суми: 169
Найкоротша відстань від Харків до Тернопіль: 1144
Найкоротша відстань від Харків до Ужгород: 1476
Найкоротша відстань від Харків до Херсон: 652
Найкоротша відстань від Харків до Хмельницький: 1005
Найкоротша відстань від Харків до Черкаси: 421
Найкоротша відстань від Харків до Чернівці: 1126
Найкоротша відстань від Харків до Чернігів: 712
Найкоротша відстань від Херсон до Вінниця: 561
Найкоротша відстань від Херсон до Дніпро: 459
Найкоротша відстань від Херсон до Донецьк: inf
Найкоротша відстань від Херсон до Житомир: 664
Найкоротша відстань від Херсон до Запоріжжя: 396
Найкоротша відстань від Херсон до Івано-Франківськ: 957
Найкоротша відстань від Херсон до Київ: 504
Найкоротша відстань від Херсон до Кропивницький: 226
Найкоротша відстань від Херсон до Луганськ: inf
Найкоротша відстань від Херсон до Луцьк: 941
Найкоротша відстань від Херсон до Львів: 1008
Найкоротша відстань від Херсон до Миколаїв: 70
Найкоротша відстань від Херсон до Одеса: 206
Найкоротша відстань від Херсон до Полтава: 570
Найкоротша відстань від Херсон до Рівне: 850
Найкоротша відстань від Херсон до Суми: 704
Найкоротша відстань від Херсон до Тернопіль: 849
Найкоротша відстань від Херсон до Ужгород: 1201
Найкоротша відстань від Херсон до Харків: 652
Найкоротша відстань від Херсон до Хмельницький: 710
Найкоротша відстань від Херсон до Черкаси: 321
Найкоротша відстань від Херсон до Чернівці: 831
Найкоротша відстань від Херсон до Чернігів: 633
Найкоротша відстань від Хмельницький до Вінниця: 149
Найкоротша відстань від Хмельницький до Дніпро: 812
Найкоротша відстань від Хмельницький до Донецьк: inf
Найкоротша відстань від Хмельницький до Житомир: 252
Найкоротша відстань від Хмельницький до Запоріжжя: 875
Найкоротша відстань від Хмельницький до Івано-Франківськ: 247
Найкоротша відстань від Хмельницький до Київ: 439
Найкоротша відстань від Хмельницький до Кропивницький: 534
Найкоротша відстань від Хмельницький до Луганськ: inf
Найкоротша відстань від Хмельницький до Луцьк: 231
Найкоротша відстань від Хмельницький до Львів: 298
Найкоротша відстань від Хмельницький до Миколаїв: 640
Найкоротша відстань від Хмельницький до Одеса: 504
Найкоротша відстань від Хмельницький до Полтава: 850
Найкоротша відстань від Хмельницький до Рівне: 140
Найкоротша відстань від Хмельницький до Суми: 868
Найкоротша відстань від Хмельницький до Тернопіль: 139
Найкоротша відстань від Хмельницький до Ужгород: 491
Найкоротша відстань від Хмельницький до Харків: 1005
Найкоротша відстань від Хмельницький до Херсон: 710
Найкоротша відстань від Хмельницький до Черкаси: 622
Найкоротша відстань від Хмельницький до Чернівці: 269
Найкоротша відстань від Хмельницький до Чернігів: 568
Найкоротша відстань від Черкаси до Вінниця: 473
Найкоротша відстань від Черкаси до Дніпро: 371
Найкоротша відстань від Черкаси до Донецьк: inf
Найкоротша відстань від Черкаси до Житомир: 370
Найкоротша відстань від Черкаси до Запоріжжя: 434
Найкоротша відстань від Черкаси до Івано-Франківськ: 869
Найкоротша відстань від Черкаси до Київ: 183
Найкоротша відстань від Черкаси до Кропивницький: 95
Найкоротша відстань від Черкаси до Луганськ: inf
Найкоротша відстань від Черкаси до Луцьк: 704
Найкоротша відстань від Черкаси до Львів: 864
Найкоротша відстань від Черкаси до Миколаїв: 251
Найкоротша відстань від Черкаси до Одеса: 387
Найкоротша відстань від Черкаси до Полтава: 249
Найкоротша відстань від Черкаси до Рівне: 613
Найкоротша відстань від Черкаси до Суми: 383
Найкоротша відстань від Черкаси до Тернопіль: 761
Найкоротша відстань від Черкаси до Ужгород: 1076
Найкоротша відстань від Черкаси до Харків: 421
Найкоротша відстань від Черкаси до Херсон: 321
Найкоротша відстань від Черкаси до Хмельницький: 622
Найкоротша відстань від Черкаси до Чернівці: 743
Найкоротша відстань від Черкаси до Чернігів: 312
Найкоротша відстань від Чернівці до Вінниця: 270
Найкоротша відстань від Чернівці до Дніпро: 933
Найкоротша відстань від Чернівці до Донецьк: inf
Найкоротша відстань від Чернівці до Житомир: 373
Найкоротша відстань від Чернівці до Запоріжжя: 996
Найкоротша відстань від Чернівці до Івано-Франківськ: 137
Найкоротша відстань від Чернівці до Київ: 560
Найкоротша відстань від Чернівці до Кропивницький: 655
Найкоротша відстань від Чернівці до Луганськ: inf
Найкоротша відстань від Чернівці до Луцьк: 411
Найкоротша відстань від Чернівці до Львів: 251
Найкоротша відстань від Чернівці до Миколаїв: 761
Найкоротша відстань від Чернівці до Одеса: 625
Найкоротша відстань від Чернівці до Полтава: 971
Найкоротша відстань від Чернівці до Рівне: 409
Найкоротша відстань від Чернівці до Суми: 989
Найкоротша відстань від Чернівці до Тернопіль: 130
Найкоротша відстань від Чернівці до Ужгород: 381
Найкоротша відстань від Чернівці до Харків: 1126
Найкоротша відстань від Чернівці до Херсон: 831
Найкоротша відстань від Чернівці до Хмельницький: 269
Найкоротша відстань від Чернівці до Черкаси: 743
Найкоротша відстань від Чернівці до Чернігів: 689
Найкоротша відстань від Чернігів до Вінниця: 419
Найкоротша відстань від Чернігів до Дніпро: 662
Найкоротша відстань від Чернігів до Донецьк: inf
Найкоротша відстань від Чернігів до Житомир: 316
Найкоротша відстань від Чернігів до Запоріжжя: 725
Найкоротша відстань від Чернігів до Івано-Франківськ: 815
Найкоротша відстань від Чернігів до Київ: 129
Найкоротша відстань від Чернігів до Кропивницький: 407
Найкоротша відстань від Чернігів до Луганськ: inf
Найкоротша відстань від Чернігів до Луцьк: 650
Найкоротша відстань від Чернігів до Львів: 810
Найкоротша відстань від Чернігів до Миколаїв: 563
Найкоротша відстань від Чернігів до Одеса: 526
Найкоротша відстань від Чернігів до Полтава: 540
Найкоротша відстань від Чернігів до Рівне: 559
Найкоротша відстань від Чернігів до Суми: 558
Найкоротша відстань від Чернігів до Тернопіль: 707
Найкоротша відстань від Чернігів до Ужгород: 1022
Найкоротша відстань від Чернігів до Харків: 712
Найкоротша відстань від Чернігів до Херсон: 633
Найкоротша відстань від Чернігів до Хмельницький: 568
Найкоротша відстань від Чернігів до Черкаси: 312
Найкоротша відстань від Чернігів до Чернівці: 689
```