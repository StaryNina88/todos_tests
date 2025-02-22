from requests import Response
from http import HTTPStatus
from typing import Any

from client.api import APIClient
from config import UrlApi


class APITodos(APIClient):
    """ Класс по работе с апи todos """

    def get_all(self, status_code: HTTPStatus = HTTPStatus.OK) -> Response:
        """ Получить все записи """
        return self.get(
            endpoint=UrlApi.GET,
            status_code=status_code
        )

    def post_todos(self, data: dict[str, Any], status_code: HTTPStatus = HTTPStatus.CREATED) -> Response:
        """ Создание записи """
        return self.post(
            endpoint=UrlApi.POST,
            json=data,
            status_code=status_code
        )

    def delete_todos_by_id(self, idx: int, status_code: HTTPStatus = HTTPStatus.OK) -> Response:
        """ Удаление записи по "id" """
        return self.delete(
            endpoint=UrlApi.DELETE_BY_ID.format(idx),
            status_code=status_code
        )
