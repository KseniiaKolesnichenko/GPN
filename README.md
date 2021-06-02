![alt tag](https://github.com/KseniiaKolesnichenko/GPN/blob/main/11.jpeg)
![alt tag](https://github.com/KseniiaKolesnichenko/GPN/blob/main/logo4.jpg)

# Газпромнефть

## Задача
Разработать системы аналитики вузов на основе различных источников данных.

## Описание задачи
Компания находится в процессе постоянного поиска и отбора компетентных подрядчиков как для выполнения типовых работ инжинирингового сервиса, так и для выстраивания более сложных партнерских отношений для возможной реализации НИРов и НИОКРов. ВУЗы занимают в этом процессе особую роль, как потенциальные партнеры по значимым для компании направлениям. Одной из приоритетных задач является выделение ключевых метрик и проведение ранжирования ВУЗов на основе проведенной аналитики.

## Решение
Были выбраны 2 направления по созданию модели расчета и ранжирования ВУЗов:
1.	Модель на основе методов программирования, сокращающая размерность датасета.
2.	Модель на основе методов машинного обучения.

## Модель на основе методов сокращения размерности датасета

Выбор данного метода был обусловлен наличием уже известных классификаторов, которые имеют широкое распространение и представляют собой классификацию на нескольких уровнях. 

Был реализован метод, который на первой итерации будет осуществлять поиск соответствий по показателю «All Science Journal Classification (ASJC) field name», на второй - по показателю «Topic Cluster name» и на третей - по показателю «Topic name». Таким образом, с каждым шагом происходит уменьшение размерности исходных данных по ключевым показателям.

Итоговый результат представляет собой отсортированный список ВУЗов по показателю наибольшего цитирования «Citations».

Ноутбук по данному методу хранится в папке model1 (https://github.com/KseniiaKolesnichenko/GPN/tree/main/model1)

## Модель на основе методов машинного обучения.

Ноутбук по данному методу хранится в папке model2 (https://github.com/KseniiaKolesnichenko/GPN/tree/main/model2)

## Обработка данных

Для удобства работы с данными была произведенная предварительная обработка, ноутбуки можно найти в папке preprocessing (https://github.com/KseniiaKolesnichenko/GPN/tree/main/preprocessing).

## Описание полей

| Название                     | Описание           |
| -------------                |:------------------|
|  *Title*                     | название публикации    |
| *Authors*                    | авторы публикаций |
| *Number of Authors*          | количество авторов         |
| *Scopus Author Ids*          | система однозначной идентификации авторов, созданная компанией Elsevier для использования вместе с базой научной литературы Scopus         |
| *Year*                       | год       |
| *Scopus Source title*        | заглавие источника (журнала, трудов конференции и т.д.)         |
| *Field-Weighted View Impact* | Показатель цитируемости, взвешенный по предметной области. FWCI: отношение числа цитирований, полученных анализируемыми публикациями, к среднему числу цитирований, полученных публикациями того же типа, в той же области и за тот же промежуток времени         |
| *Views*  | просмотры         |
| *Citations*  | цитаты        |
| *Field-Weighted Citation*    | индекс цитирования в системе SciVal, взвешенный по дисциплине, рассчитывается как отношение числа цитирований публикаций объекта к среднему числу цитирований, полученных всеми остальными схожими публикациями в мире         |
| *Field-Weighted Citation Impact* | отношение суммарного количества цитирований, фактически полученных работами всех представителей категории, и общего количества цитирований, ожидаемого исходя из среднего показателя для соответствующей отрасли знания      |
| *Outputs in Top Citation Percentiles, per percentile* | указывает степень присутствия выходных данных сущности в наиболее цитируемых пороговых значениях источника данных за год публикации. 10% рекомендуется в качестве порогового значения по умолчанию. Другими порогами является количество публикаций в 1%, 5% и 25% наиболее цитируемых публикаций. Субъектом может быть учреждение, исследовательская группа или индивидуальный исследователь  |
| *DOI* | Digital Object Identifier - идентификатор цифрового объекта (также используется словосочетание цифровой идентификатор объекта, ЦИО) — стандарт обозначения представленной в сети информации  |
| *Publication type* | тип публикации      |
| *Country/Region* | страна,регион     |
| *All Science Journal Classification (ASJC) code* | классификация всех научных журналов Scopus. Коды, присваиваемые изданиям согласно ASJC (ASJC код), отражают соответствие журнала той или иной отрасли знания.   |
| *All Science Journal Classification (ASJC) field name* | классификация всех научных журналов Scopus    |
| *Topic Cluster Prominence Percentile*| указывает на динамику и популярность темы или тематического кластера, не является показателем качества   |
| *Topic Cluster name* | распределение публикаций по темам и кластерам     |
| *University* | университет    |


## Ссылки на классификаторы

https://www.timeshighereducation.com/world-university-rankings/2015/world-ranking?utm_campaign=THE2014&utm_source=ElsevierConnect&utm_medium=Blog%20Post&utm_term=67#!/page/0/length/25/sort_by/scores_citations/sort_order/asc/cols/undefined

https://www.usnews.com/education/best-global-universities/europe

https://www.topuniversities.com/subject-rankings/2021

