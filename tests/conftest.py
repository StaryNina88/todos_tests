import pytest
from client.api import APIClient
from client.create_id import CreateId
from client.delete_id import DeleteId

@pytest.fixture
def api_client() -> APIClient:
    """ Фикстура для получения клиента API """
    return APIClient()
#выполняет действие До теста и После
#
@pytest.fixture
def task_id():
    create_new_id = CreateId()
    body = {
    "id": 1,
    "title": "первая",
    "description": "задача",
    "completed": True
    }
    create_new_id.create_new_id(body)
    yield create_new_id.response_json['data']['id']

    delete_task = DeleteId()
    delete_task.delete_by_id(create_new_id.response_json['data']['id'])

    #добавить 2 фикстуры - 1) только создаст - для делита 2) только удаляет - для создания