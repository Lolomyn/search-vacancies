import json

import pytest

from src.file_worker import AbstractSaver, JSONSaver


def test_abstract_saver():
    with pytest.raises(TypeError):
        AbstractSaver()


def test_abstract_saver_invalid_sub():
    class InvalidSubClass(AbstractSaver):
        pass

    with pytest.raises(TypeError):
        InvalidSubClass()


def test_json_saver_init():
    assert JSONSaver()


def test_add_vacancy_unique_url(vacancy, test_filename):
    saver = JSONSaver(filename=test_filename)
    saver.add_vacancy(vacancy)

    with open(test_filename, "r", encoding="utf-8") as file:
        data = json.load(file)
        assert len(data) == 1
        assert data[0]["url"] == vacancy.url


def test_get_vacancies_existing_criteria(vacancy, another_vacancy, test_filename):
    saver = JSONSaver(filename=test_filename)
    saver.add_vacancy(vacancy)
    saver.add_vacancy(another_vacancy)

    # Поиск по критерию "Python"
    result = saver.get_vacancies(criteria="Python")
    assert len(result) == 1
    assert result[0]["name"] == "Python Dev Jun"


def test_get_vacancies_non_existing_criteria(vacancy, test_filename):
    saver = JSONSaver(filename=test_filename)
    saver.add_vacancy(vacancy)

    # Поиск по критерию "Java"
    result = saver.get_vacancies(criteria="Java")
    assert len(result) == 0


def test_save_to_json(vacancy, another_vacancy, test_filename):
    saver = JSONSaver(filename=test_filename)
    saver.save_to_json([vacancy.to_dict(), another_vacancy.to_dict()])

    with open(test_filename, "r", encoding="utf-8") as file:
        data = json.load(file)
        assert len(data) == 2
        assert data[0]["name"] == "Python Dev Jun"
        assert data[1]["name"] == "JS Dev Mid"


def test_delete_vacancy_existing(vacancy, another_vacancy, test_filename):
    saver = JSONSaver(filename=test_filename)

    saver.save_to_json([vacancy.to_dict(), another_vacancy.to_dict()])

    saver.delete_vacancy(vacancy)

    with open(test_filename, "r", encoding="utf-8") as file:
        data = json.load(file)
        assert len(data) == 1
        assert data[0]["name"] == "JS Dev Mid"


def test_delete_vacancy_non_existing(vacancy, another_vacancy, test_filename):
    saver = JSONSaver(filename=test_filename)
    saver.save_to_json([vacancy.to_dict()])

    # Попытка удалить несуществующую вакансию
    saver.delete_vacancy(another_vacancy)

    # Проверяем, что файл не изменился
    with open(test_filename, "r", encoding="utf-8") as file:
        data = json.load(file)
        assert len(data) == 1
        assert data[0]["name"] == "Python Dev Jun"
