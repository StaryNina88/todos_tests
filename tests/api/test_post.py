from __future__ import annotations
from typing import Any

import pytest
from http import HTTPStatus

from client.api import APIClient


@pytest.mark.api    #марки относятся к конкретному тесту, маркировка теста что он апи, описание маркера в pytest.ini
@pytest.mark.parametrize(
    "idx, title, description, completed",
    [
        (1, "Помыть полы", "С мистером пропером",   True),
        (2, "Помыть полы", "С мылом",               False),
        (3, "Помыть полы", None,                    False),
        (1.1, "Помыть полы", "С мистером пропером", True), # создание с типом float успешное, статус 201, убрала из негативных
    ]
)
def test_create_todo(api_client: APIClient, idx: int, title: str, description: str | None, completed: bool):
    """ Позитивная проверка создания записи """
    # Формирование тела запроса
    body = {
        "id": idx,
        "title": title,
        "description": description,
        "completed": completed
    }
    # Отправка запроса
    response = api_client.post("/todos", json=body).json()


    # Проверка тела ответа
    assert response["data"] is not None #дата не null
    assert response["error"] is None
    assert response["success"] is True


@pytest.mark.api
#@pytest.mark.skip("не надо прогонять тесты") #маркер чтоб не запускать тесты
@pytest.mark.parametrize(
    "idx, title, description, completed",
    [
        # idx
        (-1,        "Помыть полы", "С мистером пропером", True),
        (0,         "Помыть полы", "С мистером пропером", True),
        ('null',    "Помыть полы", "С мистером пропером", True),
        (None,      "Помыть полы", "С мистером пропером", True),
    ]
)
def test_create_todo_negative(api_client: APIClient, idx: Any, title: Any, description: Any, completed: Any):
    """ Негативная проверка создания записи """
    body = {
        "id": idx,
        "title": title,
        "description": description,
        "completed": completed
    }
    response = api_client.post("/todos", json=body, status_code=HTTPStatus.OK).json()

    # Проверка тела ответа
    assert response["success"] is True, f'Статус не верный'
    assert response["data"] is None

    # В зависимости от типа переменной разный ответ
    if isinstance(idx, int) and idx < 1:
        error = 'id: ensure this value is greater than or equal to 1'
    elif isinstance(idx, str):
        error = 'id: value is not a valid integer'
    else:
        error = 'id: none is not an allowed value'
    assert response["error"] == error
