import pytest

from src.vacancies import Vacancy


@pytest.fixture()
def vacancy():
    return Vacancy("Python Dev Jun", "hh.ru/best_vacancy", 100_000, 500_000, "requirements", "responsibilities")


@pytest.fixture()
def another_vacancy():
    return Vacancy("JS Dev Mid", "hh.ru/good_vacancy", 70_000, 300_000, "requirements", "responsibilities")


@pytest.fixture
def test_filename(tmp_path):
    filename = tmp_path / "test_vacancies.json"
    yield filename
    filename.unlink()


@pytest.fixture()
def vacancies():
    return [
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
