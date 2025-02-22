from typing import Any

from requests import Response
from requests import Session
from http import HTTPStatus

from config import BASE_PATH


class APIClient:
    """ Класс по работе с API запросами """

    def __init__(self):
        self.base_url = BASE_PATH
        self.session = Session()

    def __request(
            self, method: str, url: str, status_code: int = HTTPStatus.OK, params: dict[str, Any] = None,
            data: dict[str, Any] = None, headers: dict[str, Any] = None, json: dict[str, Any] = None, timeout: int = 5
    ) -> Response:
        """ Универсальный метод отправки запросов с проверкой статус кода

        Args:
            method: тип запроса (GET, POST, ...)
            url: ссылка
            status_code: ожидаемый статус код
            params: именованные параметры (дополнительно подставляются в url)
            data:
            headers: заголовки
            json:
            timeout: предельное время ожидания запроса
        """
        headers = headers or {"Content-Type": "application/json"}
        response = self.session.request(method=method, url=url, params=params, data=data, headers=headers,
                                        json=json, timeout=timeout)
        assert response.status_code == status_code, f'Получен не верный статус код запроса!' \
                                                    f'\nОР: {status_code}\nФР: {response.status_code}'
        return response

    def get(self, endpoint: str, params: dict[str, Any] = None, status_code: int = HTTPStatus.OK):
        url = f"{self.base_url}{endpoint}"
        return self.__request(method='GET', url=url, params=params, status_code=status_code)

    def post(self, endpoint: str, params=None, data=None, json=None, status_code: int = HTTPStatus.CREATED):
        url = f"{self.base_url}{endpoint}"
        return self.__request(method='POST', url=url, params=params, data=data, json=json, status_code=status_code)

    def put(self, endpoint: str, status_code: int = HTTPStatus.OK, json=None):
        url = f"{self.base_url}{endpoint}"
        return self.__request(method='PUT', url=url, status_code=status_code, json=json)

    def delete(self, endpoint: str, status_code: int = HTTPStatus.OK):
        url = f"{self.base_url}{endpoint}"
        return self.__request(method='DELETE', url=url, status_code=status_code)
