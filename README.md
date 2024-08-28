# Easy.Math

Версия 3.x.x

Библиотека математических функций "easy.math" для Quest Soft Player.

Разрабатывалась для плееров версий 5.9.0 — это: классический плеер [версии 5.9.0](https://qsp.org/attachments/qsp580b7.zip), [qSpider](https://aleksversus.github.io/howdo_faq/docs/articles/qspider_0120/). Не гарантируется правильная работа на плеерах иных версий. Некоторые функции имеют ограничения на значение числовых аргументов, это связано с используемыми плеером библиотеками. Для разных версий плеера могут быть разные ограничения, поэтому внимательно читайте документацию к плееру, под который разрабатываете игру.

Для плееров версии 5.7.0. существует ветка версий [2.x.x](https://github.com/AleksVersus/easy.math).

По всем вопросам и предложениям обращаться:

* aleksversus@mail.ru
* Вконтакте: [id40090736](https://vk.com/id40090736)
* Бусти: [boosty.to/aleksversus](https://boosty.to/aleksversus)

## Подключение и использование

Предполагается, что Вы читали справку по QSP, пробовали писать игры и уже знаете, что такое локации, подпрограммы (процедуры) и функции, чем отличаются текстовые и числовые переменные, что такое аргументы и для чего они нужны.

Чтобы использовать функции библиотеки при написании своей игры, сделайте следующее:

1. скачайте архив с библиотекой [отсюда](https://github.com/AleksVersus/easy.math.3/releases), и распакуйте в папку, где лежит ваша игра. В папке с вашей игрой должна появиться папка "lib".
2. В своей игре на самой первой локации, в поле "выполнить при посещении" введите
	```qsp
	inclib 'lib\easy.math.qsp'
	```
3. Теперь Вы можете пользоваться функциями библиотеки.

Все функции вызываются с помощью ключевого слова `FUNC( )` - для получения числовых значений, и `$FUNC( )` - для получения текстовых значений.

Исключением являются функции, результат которых записывается в массив. Такие функции вызываются оператором `GOSUB`, или `GS`.

```qsp
$FUNC('em.foo',$args[0],$args[1],$args[2],$args[3],$args[4],$args[5],$args[6],$args[7],$args[8])
```

Можно использовать неявный вызов функции, если вам удобно:

```qsp
@em.foo($args[0],$args[1],$args[2],$args[3],$args[4],$args[5],$args[6],$args[7],$args[8])
```

Аргументы могут быть текстовыми, числовыми или кортежами в зависимости от требований и назначения функции.

Все переменные, использующиеся функциями, являются локальными, т.е. уничтожаются после использования, кроме переменных/массивов, в который может быть возвращён результат.

Если результат работы функции помещается в массив, одним из параметров функции указывается имя массива, в который должен быть помещён результат. Имена массивов, передаваемые в аргументах функций, должны записываться по общим правилам записи имён переменных для плеера:
- кортежи - символом `%` в начале имени;
- текстовые массивы - с символом `$` перед именем,
- числовые - без символов `$` и `%` перед именем.

Функции могут принимать или возвращать кортежи значений.

## Работа с исходниками

Вы можете [скачать исходный код библиотеки с гитхаба](https://github.com/AleksVersus/easy.math.3/tree/main/%5Bsource%5D) и собрать собственный модуль лишь из тех функций, которые вам нужны.

Сборку рекомендуется осуществлять через билдер в Sublime Text из [пакета QSP для SublimeText](https://github.com/AleksVersus/JAD_for_QSP).

При включенном препроцессоре необходимо подключить файл `00_sets/_variables.qsps_` к сборке, чтобы все функции добавились в модуль, либо написать собственный файл с метками нужных функций и так же подключить его к сборке. Для примера, можно взять `project.json` из исходников.

## Мануалы

Офлайн версия руководства по использованию библиотеки доступна в формате HTML вместе с [релизной](https://github.com/AleksVersus/easy.math.3/releases) версией библиотеки.

Онлайн руководство доступно по ссылкам:
- [easy.math.3 на народе](https://aleksversus.narod.ru/index/easy_math_3/0-73)
- [easy.math.3 на GitHub](https://aleksversus.github.io/easy.math.3)

## Перспективы

Библиотека будет пополняться новыми функциями по мере необходимости, и если существование функции хоть как-то оправдано. Некоторые функции на сегодняшний день сделать невозможно - они будут либо слишком сложны, либо заметно снизят быстродействие игры. Вероятно, некоторые математические операции очень скоро будут встроены непосредственно в движок плеера, и необходимость в них отпадёт. Такие функции будут исключаться из последующих версий библиотеки. По возможности, алгоритмы будут упрощены и разгружены, а так же будут достраиваться необходимые для работы с функциями параметры.