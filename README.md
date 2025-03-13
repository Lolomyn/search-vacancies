# HeadHunter API console app
by lolomyn

## Description:

Консольное приложение для поиска и добавления вакансий на HeadHunter

## Install:

**Ubuntu**

`sudo apt update` - update all packages

- python

`sudo apt install python3` - install python

`python3 -V` - check python version

- git

`sudo apt install git` - install git

`git --version` - check git version

- poetry

`sudo apt install python3-poetry` - install poetry

`poetry --version` - check poetry version

- clone repo

`git clone git@github.com:Lolomyn/search-vacancies.git`

- install dependencies

`poetry add requests`

- start

`python3 main.py`

**Windows**

`sudo apt update` - update all packages

- python

Download it  [here](https://www.python.org/) and follow instructions

`python --version` - check python version

- git

Download in [here](https://git-scm.com/) and follow instructions

`git --version` - check git version

- poetry

`curl -sSL https://install.python-poetry.org | python -` - install poetry

`poetry --version` - check poetry version

- clone repo

`git clone git@github.com:Lolomyn/search-vacancies.git`

- install dependencies

`poetry add requests`

- start

`python main.py`

## Functional
### Class Vacancy
Класс для работы с вакансиями: создание, сравнение зарплат, перевод в словарный вид

    name, url, salary_from, salary_to, requirement, responsibility

### Class HeadHunterAPI
Класс для работы с API от HeadHunter: get-запрос к API, загрузка в список словарей, передача списка
    
    url, headers, params, vacancies

### Class JSONSaver
Класс для работы с JSON-файлами: выгрузка/загрузка вакансий, добавление/удаление вакансий
    
    filename

### utils.py
- **filter_vacancies** - фильтрация вакансий по ключевым словам
- **sort_vacancies** - сортировка вакансий по зарплате (по убыванию)
- **get_vacancies_by_salary** - сортировка вакансий по минимальной зарплате
- **get_top_vacancies** - вывод топ N вакансий для просмотра
- **print_vacancies** - печать в консоль