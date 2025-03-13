def filter_vacancies(vacancies: list, keywords: list) -> list:
    """Функция фильтрации вакансий по ключевым словам"""
    filtered = []

    if keywords:

        for vacancy in vacancies:
            for keyword in keywords:
                if any(str(keyword).lower() in str(value).lower() for value in vacancy.values()):
                    filtered.append(vacancy)
                    break

        return filtered
    return vacancies


def sort_vacancies(vacancies: list) -> list:
    """Сортировка вакансий по убыванию минимальной зарплаты"""
    return sorted(vacancies, key=lambda x: x["salary"]["from"], reverse=True)


def get_vacancies_by_salary(vacancies: list, salary_range: str) -> list:
    """Получение вакансий, соответствующих указанному зарплатному диапазону"""
    min_salary, max_salary = map(int, salary_range.split(" - "))
    result = []

    for vacancy in vacancies:
        if vacancy.get("salary") is not None:
            if isinstance(vacancy["salary"]["from"], int):
                if min_salary <= vacancy["salary"]["from"] <= max_salary:
                    result.append(vacancy)

    return result


def get_top_vacancies(vacancies: list, top_n: int) -> list:
    """Вернуть список из N вакансий"""
    return vacancies[:top_n]


def print_vacancies(vacancies: list) -> None:
    """Вывод на экран вакансий"""
    for i, vacancy in enumerate(vacancies, 1):
        print(f"{i}. {vacancy['name']} " f"({vacancy['salary']['from']} - {vacancy['salary']['to']})")
        print(f"   {vacancy['url']}\n")
        print(f"   {vacancy['snippet']['requirement']}")
        print(f"   {vacancy['snippet']['responsibility']}\n")
