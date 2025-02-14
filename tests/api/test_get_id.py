import pytest
from http import HTTPStatus

from client.api import APIClient

@pytest.mark.api

def test_get_todos_id(api_client: APIClient):
    """ Позитивная проверка получения записей """
    # Нет тела запроса

    # Отправка запроса
    response = api_client.get("/todos").json()
    status_code = api_client.get("/todos").status_code

    # Проверка тела ответа
    assert response["data"] is not None #дата не null
    assert response["error"] is None
    assert response["success"] is True
    # Проверка статус кода ответа
    assert status_code == 200

def test_get_todos_negative(api_client: APIClient):
    """ Негативная проверка получения записи """
    # Нет тела запроса

    # Отправка запроса
    response = api_client.get("/todos").json()
    status_code = api_client.get("/todos").status_code

    # Проверка тела ответа
    assert response["data"] is None
    assert response["error"] is None
    assert response["success"] is True
    # Проверка статус кода ответа
    assert status_code == 200
