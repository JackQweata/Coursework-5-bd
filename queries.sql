-- Database: queries

-- DROP DATABASE IF EXISTS queries;

CREATE DATABASE queries
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Russian_Russia.1251'
    LC_CTYPE = 'Russian_Russia.1251'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

CREATE TABLE company(
  id serial PRIMARY KEY,
  name varchar(50) NOT NULL,
  employer_id int
);

CREATE TABLE vacancies(
  id serial PRIMARY KEY,
  title varchar(100) NOT NULL,
  price int,
  link varchar(255),
  company_id int,

  CONSTRAINT fk_vacancies_company_id
    FOREIGN KEY (company_id)
    REFERENCES company (id)
);

INSERT INTO company (name, employer_id)
VALUES ('Яндекс Крауд', 9498112),
		('ООО МедСофт', 1893006),
		('ООО Инфинити Групп', 3080564),
		('AXELSOFT', 1737461),
		('ООО ГСКС Профи', 1493980),
		('НУ-ОО ШКОЛА ДИАЛОГ', 5865573),
		('ООО Петэксперт', 9070435),
		('Цемрос', 2222),
		('ООО Эй Си Эс', 5560887),
		('EasyCode', 8977564);