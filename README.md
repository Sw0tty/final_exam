# REST API "Mountain passes" (EN)

## Description
> This API was developed in order to solve the long and inconvenient processing of adding mountain passes to the database of the website of the Sports Tourism Federation of Russia (FSTR), which is replenished by tourists who have visited a particular pass.
> During the development process, the database structure was redesigned, methods of interaction between the front and the back were developed. The user can easily go to the FSTR website and fill out a form to add the pass that he visited. While the record is being processed by site moderation, the user can edit it. The method of viewing all existing records and filtering these records by mail of the author of the record is also implemented.

## REST API Views
### SubmitData
> To add a record, the SubmitData view is used. The user fills out a form on the site, after which a request for data processing is sent. If all the data is entered according to the database logic, then the record is saved and submitted for moderation. Otherwise, an error with invalid data will be returned to the user.

### DetailMountainPass
> The DetailMountainPass view is used for editing. The user selects his entry on the site, and then enters the necessary edits in the transmitted data. If all the data is correct, then the data is overwritten, otherwise an error is returned. Also, the user cannot edit his personal data (full name, email and phone number), only view it. The field editing is supposed to be blocked on the front side. In a situation where edited data is transmitted, the back does not process user data in any way.

### ListMountainPasses
> To view and filter records, the ListMountainPasses view is used. It is assumed that there is a field on the front through which the data filtering request changes. Only a json request is sent to the back, which changes the search query and returns filtered data.\\\\



# REST API "Горные перевалы" (RU)

## Описание
> Данное API было разработано с целью решить долгую и не удобную обработку добавления горных перевалов в БД сайта Федерации Спортивного Туризма России (ФСТР), которую пополняют туристы, посетившие тот или иной перевал.
> В процессе разработки была переработана структура БД, разработаны методы взаимодействия фронта с бэком. Пользователь может без проблем зайти на сайт ФСТР и заполнить форму на добавление перевала, который он посетил. Пока запись обрабатывается модерацией сайта, пользователь может отредактировать ее. Также реализован метод просмотра всех существующих записей и фильтрации этих записей по почте автора записи.

## REST API Описание представлений
### SubmitData
> Чтобы добавить запись, используется представление SubmitData. Пользователь на сайте заполняет форму, после чего отправляется запрос на обработку данных. Если все данные введены по логике БД, то запись сохраняется и передается на модерацию. Иначе пользователю будет возвращена ошибка с указанием недопустимых данных.

### DetailMountainPass
> Для редактирования используется представление DetailMountainPass. Пользователь на сайте выбирает свою запись, после чего в переданных данных вводит необходимые правки. Если все данные корректны, то данные перезаписываются, иначе возвращается ошибка. Также пользователь не может редактировать свои личные данные (ФИО, электронная почта и телефон), только просматривать. Блокировка редактирования поля предполагается на стороне фронта. В ситуации, когда переданы отредактированные данные, бэк никак не обрабатывает данные о пользователе.

### ListMountainPasses
> Для просмотра, фильтрации записей используется представление ListMountainPasses. Предполагается, что на фронте есть поле, через которое меняется запрос фильтрации данных. На бэк передается только json запрос, который меняет поисковый запрос и возвращает отфильтрованные данные.