from employer_getter import HhParser, hh_params, hh_headers
from employers import Employe
import requests
import time


class Vacansy:
    """Класс для работы с вакансиями"""
    all_vacancies: list

    def __init__(self, employer_id: str, vac_id: str, name: str, description: str, salary: float, location: str,
                 link: str,
                 vac_type: str):
        self.employer_id = employer_id
        self.vac_id = vac_id
        self.name = name
        self.description = description
        self.salary = salary
        self.location = location
        self.link = link
        self.vac_type = vac_type

    def __salary_validator(self):
        """валидатор зарплаты"""
        if self.salary is None:
            self.salary = 0

    def __lt__(self, other):
        """Сравнивает зарплаты объектов"""
        return self.salary < other.salary

    def __repr__(self):
        return (f"{self.__class__.__name__} "
                f"({self.employer_id}, {self.vac_id}, {self.name}, {self.description}, {self.salary}, {self.location}, {self.link}, {self.vac_type})")

    @classmethod
    def _sorter_salary(cls):
        """Сортирует зарплаты по убыванию."""
        cls.all_vacancies.sort(reverse=True)
        return cls.all_vacancies

    @classmethod
    def _salary_range(cls, lst: list):
        """Отбирает зарплаты входящие в диапазон."""
        salary_from = int(lst[0])
        salary_to = int(lst[1])
        new_list = []
        for vacansy in cls.all_vacancies:
            # print(salary_from <= vacansy.salary <= salary_to)
            if salary_from <= vacansy.salary <= salary_to:
                new_list.append(vacansy)
        cls.all_vacancies = new_list
        return cls.all_vacancies

    # def __del__(self):
    #     print('object_deleted')

    @classmethod
    def _make_objects(cls):
        """Создает объекты класса."""
        list_vacansy = []
        error_employer = []
        # employer_vacancies = []
        for employer in Employe.all_employers:
            employer_vacancies = []
            respond = requests.get(url=employer.vacancies)
            time.sleep(0.05)

            try:
                all_vacancies_employer = respond.json()['items']
                employer_vacancies.extend(all_vacancies_employer)
            except KeyError:
                error_employer.append(employer.vacancies)
                break
            else:
                for vacansy in employer_vacancies:
                    name = f"{vacansy['id']}"
                    list_vacansy.append(name)
                    if vacansy['salary']:
                        if vacansy['salary']['to']:
                            list_vacansy[-1] = cls(employer.employer_id, vacansy['id'], vacansy['name'],
                                                   vacansy['snippet']['requirement'],
                                                   vacansy['salary']['to'],
                                                   vacansy['area']['name'], vacansy['alternate_url'],
                                                   vacansy['type']['id'])
                        else:
                            list_vacansy[-1] = cls(employer.employer_id, vacansy['id'], vacansy['name'],
                                                   vacansy['snippet']['requirement'],
                                                   vacansy['salary']['from'],
                                                   vacansy['area']['name'], vacansy['alternate_url'],
                                                   vacansy['type']['id'])
                    else:
                        list_vacansy[-1] = cls(employer.employer_id, vacansy['id'], vacansy['name'],
                                               vacansy['snippet']['requirement'],
                                               vacansy['salary'],
                                               vacansy['area']['name'], vacansy['alternate_url'],
                                               vacansy['type']['id'])
                    list_vacansy[-1].__salary_validator()
                    cls.all_vacancies = list_vacansy
        return cls.all_vacancies


# if __name__=='__main__':
#     Employe.employ_maker()
#     print(Vacansy._make_objects())
    # print(Vacansy.all_vacancies[:4])
    # test_1 = []
    # respond = requests.get('https://api.hh.ru/vacancies?employer_id=1299873')
    # vac = respond.json()['items']
    # test_1.extend(vac)
    # print(test_1)
