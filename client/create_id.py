#from requests import Response
#from requests import Session
#from http import HTTPStatus

#from config import BASE_PATH
import requests
from client.base_endpoint import Endpoint


class CreateId(Endpoint):

    def create_new_id(self, body):
        self.response = requests.post('https://deshtuka.pythonanywhere.com/todos', json=body)
        self.response_json = self.response.json()

    # проверка идентификатора
    def check_task_id(self, task_idd):
        assert self.response_json['data']['id']== task_idd

    # проверка статус кода ответа
    def check_response_is_201(self):
        assert self.response.status_code == 201
