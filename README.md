## db_creater
В данном проекте забираются данные из hh.ru с  помощью API.
Затем создается БД и таблицы.
Данные по работодателям кладутся в таблицу employers.
Данные по вакансиям в таблицу vacancies.

Класс "Employe" получает необходимые данные о работодателях и формирует экземпляры.
Класс "Vacansy" получает инфоримацию о вакансиях каждого работодателя.
Hh_parser забирает данные с hh.ru
hh_data_into_tables - в данном файле происходит создание таблиц в БД и заливка данных.

connector - Здесь содержаться данные для подключения к серверу.
У вас они должны быть свои.

### main.py - функционал для работы с пользователем.