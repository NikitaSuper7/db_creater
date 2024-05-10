
from employer_getter import HhParser

class Employe:
    """Класс работодателей"""
    all_employers: list
    all_employers = []

    def __init__(self, employer_id, name, link, vacancies):
        self.employer_id = int(employer_id)
        self.name = name
        self.link = link
        self.vacancies = vacancies

    @classmethod
    def employ_maker(cls):
        """Создает экземпляры класса Employe"""
        employers_hh = HhParser()
        employers_hh.employer_info()
        for employer in employers_hh.employers_data:
            cls.all_employers.append(cls(employer_id=employer['id'], name=employer['name'],
                                         link=employer['alternate_url'], vacancies=employer['vacancies_url']))
# if __name__ == '__main__':
#     Employe.employ_maker()
#     for employ in Employe.all_employers[:4]:
#         print(employ.employer_id, employ.name, employ.link, employ.vacancies, sep=' - ')
