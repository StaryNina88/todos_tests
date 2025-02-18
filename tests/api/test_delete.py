import pytest
from http import HTTPStatus

from client.api import APIClient

@pytest.mark.api

def test_delete_todos_id(api_client: APIClient):
    """ Позитивная проверка удаления записи с id = 1 """
    # Нет тела запроса

    # Отправка запроса
    response = api_client.delete("/todos/1").json()
    status_code = api_client.delete("/todos/1").status_code

    # Проверка тела ответа
    assert response["data"] is not None #дата не null
    assert response["data"]["completed"] == True
    assert response["error"] is None
    assert response["success"] is True
    # Проверка статус кода ответа
    assert status_code == 200

def test_delete_todos_negative(api_client: APIClient):
    """ Негативная проверка получения записи """
    # Нет тела запроса

    # Отправка запроса
    response = api_client.delete("/todos/111").json()
    status_code = api_client.delete("/todos/111").status_code

    # Проверка тела ответа
    assert response["data"] is None
    assert response["error"] == 'Задача с id=111 не найдена'
    assert response["success"] is False
    # Проверка статус кода ответа
    assert status_code == 404
