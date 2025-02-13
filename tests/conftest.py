import pytest
from client.api import APIClient


@pytest.fixture
def api_client() -> APIClient:
    """ Фикстура для получения клиента API """
    return APIClient()
