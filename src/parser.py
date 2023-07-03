from src.hh_api_request import HeadHunterAPI


def run_parser() -> int:
    """ Парсит вакансии, возвращает кол вакансий """

    print('Парсим вакансии...')

    hh_api = HeadHunterAPI()
    hh_api.get_vacancies()

    return hh_api.count_vacancies

