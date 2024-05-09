import requests
import time

hh_headers = {'User-Agent': 'HH-User-Agent'}
hh_params = {'text': '', 'page': 0, 'per_page': 100, 'only_with_vacancies': True}


class HhParser:
    """Забирает вакансии с сайта HH.ru"""

    def __init__(self, url='https://api.hh.ru/employers', headers=hh_headers, params=hh_params):
        self.params = params
        self.headers = headers
        self.url = url
        self.employers_name = ['Тинькофф', 'МТС', 'ржд', 'днс', 'Альфабанк', 'Мегафон', 'газпром', 'роснефть']
        self.employers_data = []
    def employer_info(self):
        for employer in self.employers_name:
            self.params['text'] = employer
            respond = requests.get(url=self.url, headers=self.headers, params=self.params)
            employer_info = respond.json()['items']
            self.employers_data.extend(employer_info)



