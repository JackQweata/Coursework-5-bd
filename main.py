from src.parser import run_parser
from src.printing_information import print_vacancies


def main():
    count_api_vacancy = run_parser()
    print_vacancies(count_api_vacancy)


if __name__ == '__main__':
    main()
