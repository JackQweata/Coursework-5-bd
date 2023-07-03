import requests
from fake_headers import Headers
from module.manager import DBManager


class HeadHunterAPI:
    def __init__(self):
        self.__headers = Headers(headers=True)
        self.__employers_id = DBManager().get_employer_id()
        self._count_vacancies: int = 0

    def get_vacancies(self) -> None:
        """ Получение вакансий HeadHunter через API, записывает в бд"""

        try:
            for key, value in self.__employers_id.items():
                vacancies_api = requests.get(f'https://api.hh.ru/vacancies/?employer_id={value}',
                                             headers=self.__headers.generate())

                vacancies_api = vacancies_api.json().get('items')

                for vacancy in vacancies_api:
                    vacancies_type = (
                        int(vacancy['id']),
                        vacancy['name'],
                        vacancy['salary']['to'] if vacancy.get('salary') and vacancy['salary']['to'] else 0,
                        vacancy['alternate_url'],
                        key
                    )
                    self._count_vacancies += DBManager().set_vacancy(vacancies_type)

        except Exception as __err:
            print(f'Что-то пошло не так: {__err}')

    @property
    def count_vacancies(self):
        return self._count_vacancies
