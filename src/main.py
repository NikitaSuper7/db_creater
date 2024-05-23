from db_admin import DbAdmin
from hh_data_into_tabels import hh_data_into_t


def main():
    """Воспроизводит функционал для пользователя."""
    print("Hello dear user")
    sql_data = DbAdmin()
    while True:
        print("""        1 - вывести на экран список всех компаний и количество вакансий у каждой компании
        2 - вывести на экран список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию
        3 - вывести на экран среднюю зарплату по вакансиям.
        4 - вывести на экран список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        5 - вывести на экран список всех вакансий, в названии которых содержится ключевое слово.
        6 - Перезалить данные в таблицы
        0 - завершение программы""")
        answer = int(input('Your answer is: '))
        if answer == 0:
            print("Работа завершена, соединение закрыто.")
            sql_data.connect.close()
            break
        elif answer == 1:
            sql_data.get_companies_and_vacancies_count()

        elif answer == 2:
            sql_data.get_all_vacancies()

        elif answer == 3:
            sql_data.get_avg_salary()
        elif answer == 4:
            sql_data.get_vacancies_with_higher_salary()
        elif answer == 5:
            keywords_1 = input("Введите пожалуйста ключевые слов, разделяя их ',': ")
            keywords_2 = keywords_1.replace(' ', '').split(',')
            sql_data.get_vacancies_with_keyword(keywords_2)
            # data = sql_data.get_vacancies_with_keyword(keywords_2)
            # print(data.columns)
        elif answer == 6:
            hh_data_into_t()
            print("Данные перезалиты")
        else:
            print("Команда не распознана, пожалуйста выберите снова: ")

if __name__ == '__main__':
    main()