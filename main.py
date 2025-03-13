from src.file_worker import JSONSaver
from src.head_hunter_api import HeadHunterAPI
from src.utils import filter_vacancies, get_top_vacancies, get_vacancies_by_salary, print_vacancies, sort_vacancies
from src.vacancies import Vacancy

head_hunter_api = HeadHunterAPI()
json_saver = JSONSaver()


def user_interaction() -> None:
    """Интерфейс для взаимодействия с вакансиями"""
    # platforms = ["HeadHunter"]

    # получение вакансий по поисковому запросу
    search_query = input("Введите поисковый запрос: ")
    vacancies_list = head_hunter_api.get_vacancies(search_query)

    # формирование вывода вакансий в консоль
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))

    # фильтрация отобранных вакансий
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    # фильтрация полученных вакансий по зарплате
    salary_range = input("Введите диапазон зарплат (n - m): ")
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    # сортировка по убыванию зарплаты
    sorted_vacancies = sort_vacancies(ranged_vacancies)

    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)

    print(f"Получено вакансий: {len(sorted_vacancies)}")
    save_query = input("Сохранить полученные вакансии в файл? [да/нет]: ")
    if save_query == "да":
        json_saver.save_to_json(sorted_vacancies)

    print("Завершение работы программы...")


def employer_interaction() -> None:
    new_vacancies = []
    while True:
        vacancy_name = input("Введите название вакансии: ")
        vacancy_url = input("Вставьте ссылку на вакансию: ")

        vacancy_salary_from, vacancy_salary_to = input("Укажите диапазон з/п (пример: 50000 - 150000): ").split(" - ")
        vacancy_salary_from = int(vacancy_salary_from)
        vacancy_salary_to = int(vacancy_salary_to)

        vacancy_requirement = input("Укажите требования к работникам: ")
        vacancy_responsibility = input("Укажите обязанности работников: ")

        new_vacancy = Vacancy.create_vacancy(
            vacancy_name,
            vacancy_url,
            vacancy_salary_from,
            vacancy_salary_to,
            vacancy_requirement,
            vacancy_responsibility,
        )

        print(f"Вакансия {new_vacancy.name} успешно добавлена!")
        new_vacancies.append(new_vacancy.to_dict())

        is_exit = input("Хотите продолжить добавлять вакансии? [да / нет]: ")
        if is_exit == "нет":

            is_save = input("Хотите сохранить вакансии в файл? [да / нет]: ")
            if is_save == "да":
                json_saver.save_to_json(new_vacancies)

            break

    print("Завершение работы программы...")


if __name__ == "__main__":
    user_name = input("Доброго времени суток! Как вас зовут?\n")
    print(f"Приятно познакомиться, {user_name}!")

    user_role = input("Вы хотите искать работу (1) или добавить вакансию (2)? [1 / 2]: ")

    if user_role == "1":
        user_interaction()
    else:
        employer_interaction()
