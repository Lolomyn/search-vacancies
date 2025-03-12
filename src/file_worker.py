import json
from abc import ABC, abstractmethod
from typing import Any

from src.vacancies import Vacancy


class AbstractSaver(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Добавить вакансию в файл"""
        pass

    @abstractmethod
    def get_vacancies(self, criteria: str) -> None:
        """Получить вакансии из файла по критерию"""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """Удалить вакансию из файла"""
        pass


class JSONSaver(AbstractSaver):
    """Класс для работы с JSON-файлами"""

    def __init__(self, filename: str = "data/vacancies.json") -> None:
        """Конструктор для работы с JSON-файлами"""
        self.__filename = filename

    def save_to_json(self, vacancies: list) -> None:
        """Сохранение переданных вакансий в JSON"""
        data = self._load_data()

        for vacancy in vacancies:
            data.append(vacancy)

        self._save_data(data)

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Добавить вакансию в JSON-файл"""
        data: list = self._load_data()
        existing_urls = {item["url"] for item in data}

        if vacancy.url not in existing_urls:
            data.append(
                {
                    "name": vacancy.name,
                    "url": vacancy.url,
                    "salary": {
                        "salary_from": vacancy.salary_from,
                        "salary_to": vacancy.salary_to,
                    },
                    "snippet": {"requirement": vacancy.requirement, "responsibility": vacancy.responsibility},
                }
            )
            self._save_data(data)

    def get_vacancies(self, criteria: str) -> list[Any]:
        """Получить вакансии из JSON-файла"""
        data: list = self._load_data()
        result = []

        for item in data:
            if any(str(criteria).lower() in str(value).lower() for value in item.values()):
                result.append(item)

        return result

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """Удалить вакансию из JSON-файла"""
        data: list = self._load_data()
        data = [item for item in data if not (item["name"] == vacancy.name and item["alternate_url"] == vacancy.url)]
        self._save_data(data)

    def _load_data(self) -> Any:
        """Метод загрузки данных из JSON"""
        try:
            with open(self.__filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def _save_data(self, data: list) -> None:
        """Метод сохранения данных в JSON"""
        with open(self.__filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


class CSVSaver(AbstractSaver):
    """Класс для работы с CSV-файлами"""

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Добавить вакансию в CSV-файл"""
        pass

    def get_vacancies(self, criteria: str) -> None:
        """Получить вакансии из CSV-файла"""
        pass

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """Удалить вакансию из CSV-файла"""
        pass


class EXCELSaver(AbstractSaver):
    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Добавить вакансию в EXCEL-файл"""
        pass

    def get_vacancies(self, criteria: str) -> None:
        """Получить вакансии из EXCEL-файла"""
        pass

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """Удалить вакансию из EXCEL-файла"""
        pass


class TXTSaver(AbstractSaver):
    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Добавить вакансию в TXT-файл"""
        pass

    def get_vacancies(self, criteria: str) -> None:
        """Получить вакансии из TXT-файла"""
        pass

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """Удалить вакансию из TXT-файла"""
        pass
