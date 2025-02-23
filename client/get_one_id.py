import requests
from client.base_endpoint import Endpoint


class GetId(Endpoint):
    # специфический метод
    def get_by_id(self, todo_task_id):
        self.response = requests.get(f'https://deshtuka.pythonanywhere.com/todos/{todo_task_id}')
        self.response_json = self.response.json()

    # проверка статус кода ответа
    def check_response_is_200(self):
        assert self.response.status_code == 200

    # проверка идентификатора объекта
    def check_response_id(self, todo_task_id):
        assert self.response_json['data']['id'] == todo_task_id

    # проверка статус кода ответа
    def check_response_is_404(self):
        assert self.response.status_code == 404 , 'Не верный статус код'
