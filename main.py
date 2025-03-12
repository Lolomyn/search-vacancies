from src.file_worker import JSONSaver
from src.head_hunter_api import HeadHunterAPI
from src.utils import filter_vacancies, get_top_vacancies, get_vacancies_by_salary, print_vacancies, sort_vacancies

head_hunter_api = HeadHunterAPI()


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
    salary_range = input("Введите диапазон зарплат: ")
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    # сортировка по убыванию зарплаты
    sorted_vacancies = sort_vacancies(ranged_vacancies)

    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)

    print(f"Получено вакансий: {len(sorted_vacancies)}")
    save_query = input("Сохранить полученные вакансии в файл? [да/нет]: ")
    if save_query == "да":
        json_saver = JSONSaver()
        json_saver.save_to_json(sorted_vacancies)


def employer_interaction() -> None:
    pass


if __name__ == "__main__":
    user_name = input("Доброго времени суток! Как вас зовут?\n")
    print(f"Приятно познакомиться, {user_name}!")
    user_role = input("Вы хотите искать работу (1) или добавить вакансию (2)? [1 / 2]: ")

    if user_role == "1":
        user_interaction()
    else:
        employer_interaction()
