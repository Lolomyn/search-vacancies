from typing import Any


class Vacancy:
    """Класс для работы с вакансиями"""

    __slots__ = ("name", "url", "salary_from", "salary_to", "requirement", "responsibility")

    def __init__(self, name: str, url: str, salary_from: int, salary_to: int, requirement: str, responsibility: str):
        """Конструктор вакансии"""
        self.name = name  # Наименование вакансии
        self.url = url  # Ссылка на вакансию на hh.ru

        # Диапазон з/п, проверка, что указаны числовые значения больше нуля
        self.salary_from = self.__check_salary(salary_from)
        self.salary_to = self.__check_salary(salary_to)

        self.requirement = requirement  # Требования
        self.responsibility = responsibility  # Обязанности

    @staticmethod
    def __check_salary(salary: int) -> [str, int]:
        """Проверка указана ли зарплата"""
        return salary if isinstance(salary, int) and salary > 0 else "Не указана"

    def __lt__(self, other: Any) -> [bool]:
        """Реализация функциональности оператора сравнения «меньше» (<)"""
        if isinstance(other, Vacancy):
            if self.salary_to == "Не указана":
                return True
            if other.salary_to == "Не указана":
                return False
            return self.salary_to < other.salary_to
        return NotImplemented

    def __le__(self, other: Any) -> [bool]:
        """Реализация функциональности оператора сравнения «меньше или равно» (<=)"""
        if isinstance(other, Vacancy):
            if self.salary_to == "Не указана" or other.salary_to == "Не указана":
                return True
            return self.salary_to <= other.salary_to
        return NotImplemented

    def __gt__(self, other: Any) -> [bool]:
        """Реализация функциональности оператора сравнения «больше» (>)"""
        if isinstance(other, Vacancy):
            if self.salary_to == "Не указана":
                return False
            if other.salary_to == "Не указана":
                return True
            return self.salary_to > other.salary_to
        return NotImplemented

    def __ge__(self, other: Any) -> [bool]:
        """Реализация функциональности оператора сравнения «больше или равно» (>=)"""
        if isinstance(other, Vacancy):
            if self.salary_to == "Не указана" or other.salary_to == "Не указана":
                return True
            return self.salary_to >= other.salary_to
        return NotImplemented
