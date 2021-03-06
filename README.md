![alt tag](https://github.com/KseniiaKolesnichenko/GPN/blob/main/111.jpeg)
![alt tag](https://github.com/KseniiaKolesnichenko/GPN/blob/main/logo.jpg)


# Задача
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

Ноутбук по данному методу хранится в папке [model1](https://github.com/KseniiaKolesnichenko/GPN/tree/main/model1)

## Модель на основе методов машинного обучения
Методы машинного обучения делятся на 2 основные группы: «обучение с учителем» и «обучение без учителя». «Обучение с учителем» предполагает возможность анализировать данные на основании имеющегося набора признаков-факторов и признаков-результатов, а также прогнозировать (обучать) по новым единицам наблюдения, чьи признаки-факторы известны. 
«Обучение без учителя» («кластеризация») в рамках данной задачи позволило бы разбить статьи на группы с определёнными признаками, но это не сможет принести практической пользы для бизнес-заказчика. 
Было принято решение решить задачу как задачу как задачу «обучения с учителем», где «учителем» выступают экспертные оценки, предоставленные в файле «Geophisics-T». Создан отдельный столбец данных, в который взяты только те единицы наблюдения (строки из файлов БД SCOPUS), для которых в файле  «Geophisics-T» существуют экспертные оценки. Эти оценки добавлены и называются score. Данные переменные являются целевыми. 
Группа решила использовать различные методы машинного обучения в целях предсказания целевой переменной.

В качестве критерия оценки было принято решение использовать MAE (mean absolute error)

![alt tag](https://github.com/KseniiaKolesnichenko/GPN/blob/main/mae.jpg) ,

где y_i – фактические значения целевой переменной score,
y ̂ – прогнозные значения целевой переменной score,
n- число единиц наблюдения. 

Существует другая распространённая метрика MSE (mean squared error) 

![alt tag](https://github.com/KseniiaKolesnichenko/GPN/blob/main/mse.jpg),

но предпочтение было отдано MAE , так как значения переменной score лежат в интервале [0,1) и ошибка между фактическими и прогнозными значениями меньше 0. В результате при расчёте MSE при возведении в квадрат MSE будет занижаться (например, при ошибке 0,5 MSE станет равным 0,25, в то время как MAE останется 0,5). 

Группа провела предварительную очистку данных: были удалены столбцы (Title, Authors, Scopus Author Ids, Scopus Source title, Reference, Abstract, DOI, EID, Scopus Affiliation IDs, Scopus Affiliation names, Country/Region, All Science Journal Classification (ASJC) code, All Science Journal Classification (ASJC) field name, Topic Cluster name, Topic Cluster number, Topic name, Topic number, University, Institutions), а столбцы year и Publication type были преобразованы в категориальные переменные (создаётся набор дополнительных переменных, признаков факторов, где придаётся значение 1 существующему типу данных (например, article) и 0 всем остальным возможным значениям. 
Построена корреляционная матрица. 
 
 ![alt tag](https://github.com/KseniiaKolesnichenko/GPN/blob/main/matrix.jpg)
 
Корреляционная матрица – это набор попарных корреляций между признаками-факторами и признаками-результатами.  Благодаря этим значениям возможно убрать из модели признаки-факторы, которые имеют тесную корреляцию между собой, определить, какие признаки тесно коррелируют друг  с другом. Было принято решение убрать показатель Outputs in Top Citation Percentiles, per percentile, так как он связан с переменными Citations и Field-Weighted Outputs in Top Citation Percentiles, per percentile. 
Одновременно с этим показано, что целевая переменная слабо (менее 0,3) связана с признаками-факторами. 
Далее признаки-факторы были масштабированы посредством инструмента MinMax Scaler, а существующий набор данных был разделён на тренинговую и тестовую выборки в соотношении 80% данных передаются в тренинговую выборку (на которой будет строиться модель) и 20% на тестовую выборку, на которой будет проверяться качество модели как по значению MAE, так и на предмет переобучения.
Были построены следующие модели:
	Множественная линейная регрессия.
	Полином 4 степени
	Полином 3 степени
	Полином 2 степени
	Случайный лес
	Дерево решений
	Бэггинг
 
Во всех случаях средняя абсолютная ошибка либо: 
	на тренинговой выборке ниже, чем на тестовой, что говорит о переобучении модели. Иными словами, модель будет работать только на тестовой выборке, а на иных данных она не будет показывать достоверного результата
	либо слишком большая, что говорит о невозможности её практического применения. 

В связи с этим мы пришли к выводу о том, что на основании предоставленных данных методы машинного обучения не могут построить статистически значимую модель. Для построения прогнозного значения необходимо использовать другие методы.  

Ноутбук по данному методу хранится в папке [model2](https://github.com/KseniiaKolesnichenko/GPN/tree/main/model2)

## Обработка данных

Для удобства работы с данными была произведенная предварительная обработка, ноутбуки можно найти в папке [preprocessing](https://github.com/KseniiaKolesnichenko/GPN/tree/main/preprocessing).

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

