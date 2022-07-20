# easy.math v.3.x.x

Библиотека математических функций easy.math.

Разрабатывалась для плееров версий 5.8.0 — это: классический плеер [версии 5.8.0](http://qsp.su/attachments/qsp570.zip), [qSpider](https://aleksversus.github.io/howdo_faq/articles/00000004.html). Не гарантируется правильная работа на плеерах иных версий. Некоторые функции имеют ограничения на значение числовых аргументов, это связано с используемыми плеером библиотеками. Для разных версий плеера могут быть разные ограничения, поэтому внимательно читайте документацию к плееру, под который разрабатываете игру.

Для плееров версии 5.7.0. существует ветка версий [2.x.x](https://github.com/AleksVersus/easy.math).

По всем вопросам и предложениям обращаться:

* aleksversus@mail.ru
* Вконтакте: [id40090736](https://vk.com/id40090736)

## Подключение и использование
Предполагается, что Вы читали справку по QSP, пробовали писать игры и уже знаете, что такое локации, подпрограммы (процедуры) и функции, чем отличаются текстовые и числовые переменные, что такое аргументы и для чего они нужны.

Чтобы использовать функции библиотеки при написании своей игры, сделайте следующее:

скачайте архив с библиотекой отсюда, и распакуйте в папку, где лежит ваша игра. В папке с вашей игрой должна появиться папка "lib".

В своей игре на самой первой локации, в поле "выполнить при посещении" введите
```qsp
inclib 'lib\easy.math.qsp'
```

Теперь Вы можете пользоваться функциями библиотеки.

Все функции библиотеки вызываются с помощью ключевого слова `FUNC( )` - для получения числовых значений, и `$FUNC( )` - для получения текстовых значений.

Исключением являются функции, результат которых записывается в массив. Такие функции вызываются оператором `GOSUB`, или `GS`.

```qsp
$FUNC('foo,$args[0],$args[1],$args[2],$args[3],$args[4],$args[5],$args[6],$args[7],$args[8])
```

Можно использовать неявный вызов функции, если вам удобно:

```qsp
@foo($args[0],$args[1],$args[2],$args[3],$args[4],$args[5],$args[6],$args[7],$args[8])
```

Аргументы могут быть текстовыми или числовыми в зависимости от требований и назначения функции.

Все переменные, использующиеся функциями, являются локальными, т.е. уничтожаются после использования, кроме переменных/массивов, в который может быть возвращён результат.

Если результат работы функции помещается в массив, одним из параметров функции указывается имя массива, в который должен быть помещён результат. Имена массивов, передаваемые в аргументах функций, должны записываться по общим правилам записи имён переменных для плеера: текстовые массивы - с символом `$` перед именем, числовые - без символа `$` перед именем. Само имя не должно содержать символа `$`, и других запрещённых символов.

Функции могут принимать или возвращать кортежи значений. Имена переменных, которые хранят кортежи, должны начинаться с символа `$`.

## История версий

[Просмотреть историю версий](https://github.com/AleksVersus/easy.math.3/blob/main/%5Bdisdocs%5D/vhistory.md)

## Функции
1. Операции над целыми числами
	* `em.even` - округление целых чисел до указанной разрядности
	* `em.summ` - подсчёт суммы всех элементов массива.
	* `em.digs` - получение разрядности целого числа
	* `em.exp` - возведение целого числа в степень.
	* `em.abs` - модуль от разности. c=|a-b|
	* `em.random` — случайное число из указанных промежутков
	* `em.log` — логарифмирование по указанному основанию
2. Логические операции
	* `em.byte.add` - "логическое" сложение
	* `em.byte.dev` - "логическое" вычитание
3. Операции над текстом
	* `em.zero` - генерирует строку одинаковых символов
	* `#rndstr#` - генерирует строку случайных символов
	* `#chk.obj.word#` - производит поиск предмета в "инвентаре"
	* `#chk.array.word#` - производит поиск элемента массива, содержащего строку, соответствующую регулярному выражению.
	* `#str.inArray# `- из блока текста выбирает все строки между указанными разделителями и помещает их в указанный массив.
	* `#widetrim#` - удаление прилегающих пробелов, символов табуляции и переводов строк, или символов преформатирования.
	* `#str.thin#` - разрежение строки строкой-разделителем.
4. Операции над вещественными (дробными) числами
	* `#dz#` - отсечение нулей в дробной части числа
	* `#indiv#` - рациональное частное от деления двух целых чисел
	* `#undiv#` - превращает рациональное число в целое
	* `#razdiv#` - получает разрядность дробной части числа
	* `#rounddiv#` - округляет рациональное число.
	* `#+#` - вычисление суммы рациональных чисел.
	* `#*#` - вычисление произведения рациональных чисел.
	* `#:#` - вычисление частного от деления рациональных чисел.
	* `#sim#` - сравнение рациональных чисел.
	* `#sqrt#` - вычисление корня квадратного.
	* `#invert#` - инвертирование числа.
5. Операции над шестнадцатеричными числами
	* `#hex-dec#` - перевод из шестнадцатеричной системы в десятеричную
	* `#dec-hex#` - перевод из десятеричной системы в шестнадцатеричную
	* `#dec-col#` - превращает десятеричное число в шестнадцатеричное
	* `#+col#` - изменение цвета, записанного в шестнадцатеричном RGB.
	* `#col-rgb#` - преобразование цвета из формата RRGGBB в формат rgb понятный QSP.
	* `#col-inv#` - инвертирование цвета в формате RRGGBB, т.е. преобразование цвета к совершенно противоположному.
6. Операции над массивами
	* `#array.rand#` - заполнение элементов массива случайными числами
	* `#array.strt#` - заполнение элементов массива подряд идущими числами.
	* `#array.prnt#` - вывод содержимого всех элементов массива в виде текста
	* `#array.prnt.few#` - вывод содержимого нескольких массивов.
	* `#array.sort#` - многофункциональная сортировка содержимого массива.
	* `#array.rstd#` - перетасовка элементов массива в соответствии с таблицей перестановки.
	* `#array.dsrt#` - операция обратная сортировке.
	* `#array.simp#` - сравнение содержимого двух массивов.
	* `#array.clr#` - удаление всех элементов массива, соответствующих указанному значению.
	* `#array.srch#` - поиск максимального или минимального значения числового массива по указанной области и в заданных пределах.
	* `#array.ins#` - вставка элемента в массив со сдвигом ячеек вправо.
	* `em.arr.chType` - изменение типа массива.
7. Вспомогательные функции
	* `get.word.inPos` - из строки вида `aaa|bbb|ccc|...|yyy|zzz` вычленяется подстрока, стоящая в указанной позиции.
	* `em.tag.getNum` - получает значение одиночного тега.
	* `em.tag.getCont` - получает значение сдвоенного тега.
	* `kill.var.olegus` - процедура, нагло национализированная у Olegus'а. Удаляет элемент массива по его текстовому индексу.
	* `em.maxVar` - поиск названия переменной среди перечисленных, которая содержит наибольшее значение.
	* `em.minVar` - поиск названия переменной среди перечисленных, которая содержит наименьшее значение.
	* `em.var.getType` - получение типа переменной.
	* `em.deRGB` - получает составляющие цвета на основе числового кода цвета QSP.
8. Работа с координатной сеткой
	* `#coords.get#` - определяет координаты ячейки по текущему номеру ячейки.
### Перспективы
Библиотека будет пополняться новыми функциями по мере необходимости, и если существование функции хоть как-то оправдано. Некоторые функции на сегодняшний день сделать невозможно - они будут либо слишком сложны, либо заметно снизят быстродействие игры. Вероятно, некоторые математические операции очень скоро будут встроены непосредственно в движок плеера, и необходимость в них отпадёт. Такие функции будут исключаться из последующих версий библиотеки. По возможности, алгоритмы будут упрощены и разгружены, а так же будут достраиваться необходимые для работы с функциями параметры.