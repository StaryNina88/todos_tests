import requests
import pytest

from client.create_id import CreateId
from client.delete_id import DeleteId
from client.get_one_id import GetId


def test_create_id():
    new_id = CreateId()
    body = {
    "id": 1,
    "title": "первая",
    "description": "задача",
    "completed": True
    }
    new_id.create_new_id(body=body)
    new_id.check_response_is_201()
    new_id.check_task_id(body['id'])

def test_get_id(task_id):
    get_id = GetId()
    get_id.get_by_id(task_id)
    get_id.check_response_is_200()
    get_id.check_response_id(task_id)


def test_delete_id(task_id):
    delete_task_id = DeleteId()
    delete_task_id.delete_by_id(task_id)
    delete_task_id.check_response_is_200()
    get_id = GetId()
    get_id.get_by_id(task_id)
    get_id.check_response_is_404()
