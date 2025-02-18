import requests
from client.base_endpoint import Endpoint


class DeleteId(Endpoint):

    def delete_by_id(self, todo_task_id):
        self.response = requests.delete(f'https://deshtuka.pythonanywhere.com/todos/{todo_task_id}')
        self.response_json = self.response.json()

    # проверка статус кода ответа
    def check_response_is_200(self):
        assert self.response.status_code == 200
