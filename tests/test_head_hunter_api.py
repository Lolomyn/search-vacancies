from unittest.mock import MagicMock, patch

import pytest

from src.head_hunter_api import HeadHunterAPI, Parser


def test_parser():
    with pytest.raises(TypeError):
        Parser()


def test_load_vacancies():
    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"items": [{"id": "1", "name": "Test Vacancy"}]}
        mock_get.return_value = mock_response

        hh_api = HeadHunterAPI()
        hh_api._load_vacancies("Python Developer")

    assert hh_api._HeadHunterAPI__vacancies[0]["name"] == "Test Vacancy"


def test_load_vacancies_with_error():
    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        hh_api = HeadHunterAPI()
        with pytest.raises(Exception) as exc_info:
            hh_api._load_vacancies("Invalid Query")

    assert str(exc_info.value) == "Failed to fetch data: 404"


def test_get_vacancies():
    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"items": [{"id": "1", "name": "Python Developer"}]}
        mock_get.return_value = mock_response

        hh_api = HeadHunterAPI()
        vacancies = hh_api.get_vacancies("Python Developer")

    assert vacancies[0]["name"] == "Python Developer"
