from src.vacancies import Vacancy


def test_vacancy_init(vacancy):
    assert vacancy.name == "Python Dev Jun"
    assert vacancy.url == "hh.ru/best_vacancy"
    assert vacancy.salary_from == 100_000
    assert vacancy.salary_to == 500_000
    assert vacancy.requirement == "requirements"
    assert vacancy.responsibility == "responsibilities"


def test_vacancy_create_vacancy():
    new_vacancy = Vacancy.create_vacancy(
        "JS Dev Mid", "hh.ru/good_vacancy", 70_000, 300_000, "requirements", "responsibilities"
    )
    assert new_vacancy.name == "JS Dev Mid"
    assert new_vacancy.url == "hh.ru/good_vacancy"
    assert new_vacancy.salary_from == 70_000
    assert new_vacancy.salary_to == 300_000
    assert new_vacancy.requirement == "requirements"
    assert new_vacancy.responsibility == "responsibilities"


def test_vacancies_comparison(vacancy, another_vacancy):
    assert vacancy > another_vacancy
    assert vacancy >= another_vacancy
    assert another_vacancy < vacancy
    assert another_vacancy <= vacancy

    vacancy.salary_to = "Не указана"
    assert vacancy < another_vacancy
    assert vacancy <= another_vacancy
    assert vacancy >= another_vacancy
    assert not vacancy > another_vacancy

    vacancy.salary_to = 100_000
    another_vacancy.salary_to = "Не указана"
    assert vacancy > another_vacancy
    assert not vacancy < another_vacancy

    assert vacancy.__lt__("a lot of money") is NotImplemented
    assert vacancy.__le__("a lot of money") is NotImplemented
    assert vacancy.__gt__("a lot of money") is NotImplemented
    assert vacancy.__ge__("a lot of money") is NotImplemented
