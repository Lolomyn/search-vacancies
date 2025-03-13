from typing import Any, Union


class Vacancy:
    """Класс для работы с вакансиями"""

    __slots__ = ("name", "url", "salary_from", "salary_to", "requirement", "responsibility")

    def __init__(
        self, name: str, url: str, salary_from: int, salary_to: int, requirement: str, responsibility: str
    ) -> None:
        """Конструктор вакансии"""
        self.name = name  # Наименование вакансии
        self.url = url  # Ссылка на вакансию на hh.ru

        # Диапазон з/п, проверка, что указаны числовые значения больше нуля
        self.salary_from = self.__check_salary(salary_from)
        self.salary_to = self.__check_salary(salary_to)

        self.requirement = requirement  # Требования
        self.responsibility = responsibility  # Обязанности

    def to_dict(self) -> dict:
        """Перевести экземпляр класса в словарный вид"""
        return {
            "name": self.name,
            "url": self.url,
            "salary": {
                "from": self.salary_from,
                "to": self.salary_to,
            },
            "snippet": {
                "requirement": self.requirement,
                "responsibility": self.responsibility,
            },
        }

    @classmethod
    def create_vacancy(
        cls, name: str, url: str, salary_from: int, salary_to: int, requirement: str, responsibility: str
    ):
        """Создание вакансии при помощи метода"""
        return cls(name, url, salary_from, salary_to, requirement, responsibility)

    @staticmethod
    def __check_salary(salary: int) -> Union[str, int]:
        """Проверка указана ли зарплата"""
        return salary if isinstance(salary, int) and salary > 0 else "Не указана"

    def __lt__(self, other: Any) -> bool:
        """Реализация функциональности оператора сравнения «меньше» (<)"""
        if isinstance(other, Vacancy):
            if self.salary_to == "Не указана":
                return True
            if other.salary_to == "Не указана":
                return False
            return self.salary_to < other.salary_to
        return NotImplemented

    def __le__(self, other: Any) -> bool:
        """Реализация функциональности оператора сравнения «меньше или равно» (<=)"""
        if isinstance(other, Vacancy):
            if self.salary_to == "Не указана" or other.salary_to == "Не указана":
                return True
            return self.salary_to <= other.salary_to
        return NotImplemented

    def __gt__(self, other: Any) -> bool:
        """Реализация функциональности оператора сравнения «больше» (>)"""
        if isinstance(other, Vacancy):
            if self.salary_to == "Не указана":
                return False
            if other.salary_to == "Не указана":
                return True
            return self.salary_to > other.salary_to
        return NotImplemented

    def __ge__(self, other: Any) -> bool:
        """Реализация функциональности оператора сравнения «больше или равно» (>=)"""
        if isinstance(other, Vacancy):
            if self.salary_to == "Не указана" or other.salary_to == "Не указана":
                return True
            return self.salary_to >= other.salary_to
        return NotImplemented
