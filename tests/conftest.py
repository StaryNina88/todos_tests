import pytest

from client.api import APIClient
from tests.api.todos.helper.client_api_todos import APITodos


@pytest.fixture(scope="session")
def api_client() -> APIClient:
    """ Фикстура для получения клиента API """
    return APIClient()


@pytest.fixture(scope="session")
def api_todos() -> APITodos:
    """ Фикстура для работы только с api todos """
    return APITodos()


@pytest.fixture
def fixture_clear_data(api_todos: APITodos):
    """ Фикстура по очистке всех записей после теста """
    yield

    list_idx = []
    try:
        response = api_todos.get_all().json()
        for item in response.get('data', []):   # Пробегаем по всем записям и сохраняем "id"
            list_idx.append(item.get('id'))
    except Exception as ex:
        print(f'Ошибка: {ex}')
    else:
        for idx in list_idx:                    # Пробегаем по всем сохраненным "id" и удаляем
            api_todos.delete_todos_by_id(idx=idx)
