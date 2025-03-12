from abc import ABC, abstractmethod

import requests


class Parser(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def _load_vacancies(self, keyword: str) -> None:
        """Загрузка вакансий"""
        pass

    @abstractmethod
    def get_vacancies(self, query: str) -> None:
        """Получение вакансий"""
        pass


class HeadHunterAPI(Parser):
    """Класс для работы с API HeadHunter"""

    def __init__(self) -> None:
        """Конструктор параметров для работы с API HeadHunter"""
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies: list = []

    def _load_vacancies(self, keyword: str) -> None:
        """Загрузка вакансий из API"""
        self.__params["text"] = keyword
        while self.__params.get("page") != 20:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            if response.status_code == 200:
                vacancies = response.json()["items"]
                self.__vacancies.extend(vacancies)
                self.__params["page"] += 1
            else:
                raise Exception(f"Failed to fetch data: {response.status_code}")

    def get_vacancies(self, query: str) -> list:
        """Вернуть пользователю полученные вакансии"""
        self._load_vacancies(query)
        return self.__vacancies
