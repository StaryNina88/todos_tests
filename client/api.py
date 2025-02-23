from requests import Response
from requests import Session
#не нагружать систему, импортировать только то что хотим получить
from http import HTTPStatus

from config import BASE_PATH


class APIClient:
    """ Класс по работе с API запросами """

    def __init__(self):
        self.base_url = BASE_PATH
        self.session = Session()
#общий метод отправки запроса, request из библиотеки, делаем для себя уменьшенный с атрибутами, None значит что переменная не обязат

    def request(self, method: str, url: str, status_code: int = HTTPStatus.OK, params=None, data=None, headers=None,
                json=None, timeout: int = 5) -> Response:
        response = self.session.request(method=method, url=url, params=params, data=data, headers=headers,
                                        json=json, timeout=timeout)

        assert response.status_code == status_code, f'Получен не верный статус код запроса!' \
                                                    f'\nОР: {status_code}\nФР: {response.status_code}'
        return response

    def get(self, endpoint: str, params=None):
        url = f"{self.base_url}{endpoint}"
        return self.request(method='GET', url=url, params=params)

    def post(self, endpoint: str, status_code: int = HTTPStatus.CREATED, json=None):
        url = f"{self.base_url}{endpoint}"
        return self.request(method='POST', url=url, status_code=status_code, json=json)

    def put(self, endpoint: str, status_code: int = HTTPStatus.OK, json=None):
        url = f"{self.base_url}{endpoint}"
        return self.request(method='PUT', url=url, status_code=status_code, json=json)

    def delete(self, endpoint: str, status_code: int = HTTPStatus.OK):
        url = f"{self.base_url}{endpoint}"
        return self.request(method='DELETE', url=url, status_code=status_code)
