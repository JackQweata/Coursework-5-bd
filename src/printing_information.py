from module.manager import DBManager


def print_vacancies(count_vacancy) -> None:
    """ UI Пользователя """

    print(f"В бд добавлено: {count_vacancy}")

    while True:
        bd_manage = DBManager()

        print("------\n\n"
              "1) получает список всех компаний и количество вакансий у каждой компании.\n"
              "2) получает список всех вакансий с названия компании\n"
              "3) получает среднюю зарплату по вакансиям\n"
              "4) получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.\n"
              "5) получает список всех вакансий, по ключевым слову\n"
              "Чтоб выйти, напишите \"выход\""
              "\n\n------"
              )

        user_input = input()

        if user_input.lower() == 'выход':
            break

        elif user_input == '1':
            vacancies = bd_manage.get_companies_and_vacancies_count()
            for vacancy in vacancies:
                table: str = print_table(vacancy)
                print(f"{table} вакансий")

        elif user_input == '2':
            vacancies = bd_manage.get_all_vacancies()
            for vacancy in vacancies:
                table: str = print_table(vacancy)
                print(f"{table} рублей")

        elif user_input == '3':
            vacancies = bd_manage.get_avg_salary()
            for vacancy in vacancies:
                table: str = print_table(vacancy)
                print(f"Средняя зарплата: {table} руб")

        elif user_input == '4':
            vacancies = bd_manage.get_vacancies_with_higher_salary()
            for vacancy in vacancies:
                table: str = print_table(vacancy)
                print(f"{table} рублей")

        elif user_input == '5':
            user_input = input("Введите ключевое слово: ")
            vacancies = bd_manage.get_vacancies_with_keyword(user_input)
            for vacancy in vacancies:
                table: str = print_table(vacancy)
                print(f"{table} рублей")


def print_table(vacancy) -> str:
    return ': '.join(map(str, (vacancy)))
