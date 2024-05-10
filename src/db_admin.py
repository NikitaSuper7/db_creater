import psycopg2
from bd_connector import connector


class DbAdmin:
    """Класс для управление Базой данных."""

    def __init__(self, host=connector['host'], database=connector['database'], user=connector['user'],
                 password=connector['password']):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def _delete_db(self, name: str):
        """Удаляет базу данных."""
        connect = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        cursor = connect.cursor()
        request_del = f"""DROP DATABASE IF EXISTS {name}"""
        cursor.execute(request_del)
        connect.commit()
        cursor.close()
        connect.close()

    def _create_db(self, name: str):
        """Создает базу данных."""
        connect = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        cursor = connect.cursor()
        request_create = f"""CREATE DATABASE {name}"""
        cursor.execute(request_create)
        # connect.commit()

        cursor.close()
        connect.close()
    def _create_table(self, table_name: str, **kwargs):
        """Создает таблицу.
        name - название таблицы.
        kwargs - столбец=type"""
        columns = []
        for key, val in kwargs.items():
            list_1 = [key, val]
            data = ' '.join(list_1)
            columns.append(data)
        col_type = ', '.join(columns)

        connect = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        cursor = connect.cursor()
        request_create = f"""CREATE TABLE {table_name}
                        (
                            {col_type}
                        )"""
        cursor.execute(request_create)
        connect.commit()
        cursor.close()
        connect.close()
    def _delete_table(self, table_name: str):
        """Удаляет таблицу"""
        connect = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        cursor = connect.cursor()
        request = f"""DROP TABLE IF EXISTS {table_name}"""
        cursor.execute(request)
        connect.commit()
        cursor.close()
        connect.close()

    def _truncate_table(self, table_name: str):
        """отчищает таблицу."""
        connect = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        cursor = connect.cursor()
        request = f"""TRUNCATE TABLE IF EXISTS {table_name}"""
        cursor.execute(request)
        connect.commit()
        cursor.close()
        connect.close()

    def _insert_into_table(self, table_name:str, *args: tuple):
        """Добавляет данные в таблицу.
        table_name -имя таблицы.
        args - данные в кортеже, которые хотим добавить.
        Например:
        (1, test), (2, test_2) - добавит 2 строки в таблицу.
        кол-во элементов в кортеже должно быть равно кол-ву столбцов выбранной таблице.
        если в столбец не заносятся данные, то ставим - NULL"""
        connect = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        cursor = connect.cursor()
        cursor.execute(f"""select * from {table_name} limit 0""")
        val = '%s, '*len(cursor.description)
        request_into = f"""insert into {table_name} values ({val[:-2]})"""
        data_into = args
        cursor.executemany(request_into, data_into)
        connect.commit()
        cursor.close()
        connect.close()

    # def change_column_type(self, table_name:str):



if __name__ == '__main__':
    test_1 = DbAdmin()
    # test_1._create_db('test_3')
    # test_1._delete_table('test_test')
    # test_1._create_table('test_test', test_id='serial', name='varchar(50)')
    # test_1._insert_into_table('test_test', (1, 'Nikita'), (2, 'Alina'))
