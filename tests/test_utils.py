from src.utils import filter_vacancies, get_top_vacancies, get_vacancies_by_salary, print_vacancies, sort_vacancies


def test_filter_vacancies(vacancies):
    result = filter_vacancies(vacancies, ["Python"])
    assert result == [
        {
            "name": "Python",
            "url": "hh.ru/best_vacancy",
            "salary": {
                "from": 100_000,
                "to": 150_000,
            },
            "snippet": {
                "requirement": "requirements",
                "responsibility": "responsibilities",
            },
        }
    ]


def test_filter_vacancies_no_keywords(vacancies):
    result = filter_vacancies(vacancies, [])
    assert result == [
        {
            "name": "Python",
            "url": "hh.ru/best_vacancy",
            "salary": {
                "from": 100_000,
                "to": 150_000,
            },
            "snippet": {
                "requirement": "requirements",
                "responsibility": "responsibilities",
            },
        },
        {
            "name": "JavaScript",
            "url": "hh.ru/good_vacancy",
            "salary": {
                "from": 170_000,
                "to": 100_000,
            },
            "snippet": {
                "requirement": "requirements",
                "responsibility": "responsibilities",
            },
        },
    ]


def test_sort_vacancies(vacancies):
    result = sort_vacancies(vacancies)
    assert result == [
        {
            "name": "JavaScript",
            "url": "hh.ru/good_vacancy",
            "salary": {
                "from": 170_000,
                "to": 100_000,
            },
            "snippet": {
                "requirement": "requirements",
                "responsibility": "responsibilities",
            },
        },
        {
            "name": "Python",
            "url": "hh.ru/best_vacancy",
            "salary": {
                "from": 100_000,
                "to": 150_000,
            },
            "snippet": {
                "requirement": "requirements",
                "responsibility": "responsibilities",
            },
        },
    ]


def test_get_vacancies_by_salary(vacancies):
    result = get_vacancies_by_salary(vacancies, "110000 - 200000")
    assert result == [
        {
            "name": "JavaScript",
            "url": "hh.ru/good_vacancy",
            "salary": {
                "from": 170_000,
                "to": 100_000,
            },
            "snippet": {
                "requirement": "requirements",
                "responsibility": "responsibilities",
            },
        },
    ]


def test_get_vacancies_by_salary_empty_result(vacancies):
    result = get_vacancies_by_salary(vacancies, "200000 - 300000")
    assert result == []


def test_get_top_vacancies(vacancies):
    result = get_top_vacancies(vacancies, 1)
    assert result == [
        {
            "name": "Python",
            "url": "hh.ru/best_vacancy",
            "salary": {
                "from": 100_000,
                "to": 150_000,
            },
            "snippet": {
                "requirement": "requirements",
                "responsibility": "responsibilities",
            },
        }
    ]


def test_print_vacancies(capsys, vacancies):
    print_vacancies(vacancies)
    print_result = capsys.readouterr()
    assert (
        print_result.out == "1. Python (100000 - 150000)\n"
        "   hh.ru/best_vacancy\n"
        "\n"
        "   requirements\n"
        "   responsibilities\n"
        "\n"
        "2. JavaScript (170000 - 100000)\n"
        "   hh.ru/good_vacancy\n"
        "\n"
        "   requirements\n"
        "   responsibilities\n"
        "\n"
    )
