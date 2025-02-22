from enum import StrEnum

BASE_PATH = 'https://deshtuka.pythonanywhere.com'


class UrlApi(StrEnum):
    """ Класс с константами эндпоинтов """
    POST            = '/todos'
    GET             = '/todos'
    GET_BY_ID       = '/todos/{}'
    DELETE_BY_ID    = '/todos/{}'
