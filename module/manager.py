import psycopg2


class DBManager:
    def __init__(self):
        self.__connection = psycopg2.connect(
            host="localhost",
            database="queries",
            user="postgres",
            password="123"
        )

    def get_employer_id(self) -> dict:
        """ получить id компаний """
        cursor = self.__connection.cursor()
        try:
            with self.__connection:
                with cursor:
                    cursor.execute("SELECT id, employer_id FROM company")
                    employers_id = {item[0]: item[1] for item in cursor.fetchall()}
                    return employers_id
        finally:
            self.__connection.close()

    def get_companies_and_vacancies_count(self) -> list:
        """ получает список всех компаний и количество вакансий у каждой компании. """

        cursor = self.__connection.cursor()
        try:
            with self.__connection:
                with cursor:
                    cursor.execute("SELECT c.id, c.name AS company, COUNT(v.*) FROM company c LEFT JOIN vacancies v ON "
                                   "c.id = v.company_id GROUP BY c.id, c.name ORDER BY c.id")
                    return cursor.fetchall()
        finally:
            self.__connection.close()

    def get_all_vacancies(self) -> list:
        """
        получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию.
        """

        cursor = self.__connection.cursor()
        try:
            with self.__connection:
                with cursor:
                    cursor.execute("SELECT c.name AS company, v.title, v.link, v.price "
                                   "FROM vacancies v LEFT JOIN company c ON c.id = v.company_id")
                    return cursor.fetchall()
        finally:
            self.__connection.close()

    def get_avg_salary(self) -> list:
        """ получает среднюю зарплату по вакансиям. """

        cursor = self.__connection.cursor()
        try:
            with self.__connection:
                with cursor:
                    cursor.execute("SELECT ROUND(AVG(price)) FROM vacancies")
                    return cursor.fetchall()
        finally:
            self.__connection.close()

    def get_vacancies_with_higher_salary(self) -> list:
        """ получает список всех вакансий, у которых зарплата выше средней по всем вакансиям. """

        cursor = self.__connection.cursor()
        try:
            with self.__connection:
                with cursor:
                    cursor.execute("SELECT title, link, price FROM vacancies "
                                   "WHERE price > (SELECT AVG(price) FROM vacancies)")
                    return cursor.fetchall()
        finally:
            self.__connection.close()

    def get_vacancies_with_keyword(self, word) -> list:
        """
         получает список всех вакансий,
        в названии которых содержатся переданные в метод слова
        """

        cursor = self.__connection.cursor()
        try:
            with self.__connection:
                with cursor:
                    cursor.execute(f"SELECT title, link, price FROM vacancies WHERE title LIKE '%{word}%'")
                    return cursor.fetchall()
        finally:
            self.__connection.close()

    def set_vacancy(self, vacancies: tuple) -> int:
        """ Запись в бд """

        cursor = self.__connection.cursor()
        try:
            with self.__connection:
                with cursor:
                    cursor.execute("INSERT INTO vacancies (id, title, price, link, company_id) VALUES "
                                   "(%s, %s, %s, %s, %s)", vacancies)
                    return 1

        except psycopg2.IntegrityError:
            return 0
        finally:
            self.__connection.close()
