from bd_connector import connector
from db_admin import DbAdmin
from employers import Employe
from vacansies import Vacansy
import psycopg2

if __name__ == '__main__':
    # для заливки свежих данных в БД
    db = DbAdmin(host=connector['host'], database='hh_data', user=connector['user'],
                 password=connector['password'])
    db._delete_table('employers')
    db._create_table('employers', employer_id='int', name='varchar(200)', link='text')
    Employe.employ_maker()
    for employer in Employe.all_employers:
        db._insert_into_table('employers', ['employer_id', 'name', 'link'],
                              (employer.employer_id, employer.name, employer.link))
    db._delete_table('vacancies')
    db._create_table('vacancies', vacancies_id='int', employer_id='int', name='varchar(100)', salary='float',
                     location='varchar(100)', link='text')
    Vacansy._make_objects()
    for vacansy in Vacansy.all_vacancies:
        db._insert_into_table('vacancies', ['vacancies_id', 'employer_id', 'name', 'salary',
                                            'location', 'link'],
                              (vacansy.vac_id, vacansy.employer_id, vacansy.name, vacansy.salary, vacansy.location,
                               vacansy.link))

