import pytest
from Employees_search.Employees_search import *


def test_tm_base_positive():
    # S-API-TM-01 - БАЗОВЫЙ ПОЗИТИВНЫЙ ТЕСТ
    status, response, res_headers = es.es_search(some_url=None, some_headers=None,
                                                 some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883",
                                                                         "23a4363f-28d0-43e2-b66e-f2aedd4175ae"]})
    # print(f"\nCode: {status}")
    # print(f"Response: {response}")
    # print(f'Response headers: {res_headers}')
    assert status == 200
    # Проверка на наличие нужных полей в ответе
    for n in response[0]['response']:
        assert "first_name" in n and "last_name" in n \
               and "mobile_number" in n and "email" in n and "profession_list" in n \
               and "team_list" in n and "grade_list" in n
    # Проверка значения page
    assert response[0]['page'] == 1
    # Проверка значения limit
    assert response[0]['limit'] == 50
    # Проверка значения total
    assert response[0]['total'] == 8
    # Проверка ожидаемой выгрузки сотрудников
    list_e = [n['last_name'] for n in response[0]['response']]
    # print(list_e)
    expected_list = ['Орлова', 'Хохлова', 'Борисов', 'Лыжин', 'Афонин', 'Недочетова', 'Лязникова', 'Садчикова']
    assert list_e == sorted(expected_list)


def test_tm_teams_without_employees():
    # S-API-TM-02 - Отправка запроса с указанием списка команд, к которым не привязаны сотрудники.
    # Получение пустого списка в ответе
    status, response, res_headers = es.es_search(some_url=None, some_headers=None,
                                                 some_data={"team_ids": ["6d020bb3-05ae-4380-8a1c-8273bfe543b5"]})
    # print(f"\nCode: {status}")
    # print(f"Response: {response}")
    # print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Nothing found for specified search parameters', 'type': 'not_found'},)


def test_tm_page2_limit5():
    # S-API-TM-06 - Отправка запроса с обязательными параметрами
    # в установленных пределах и параметрами в теле: page = 2, limit = 49
    status, response, res_headers = es.es_search(some_url=None, some_headers=None,
                                                 some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883",
                                                                         "23a4363f-28d0-43e2-b66e-f2aedd4175ae"],
                                                            "page": 2, "limit": 5})
    # print(f"\nCode: {status}")
    # print(f"Response: {response}")
    # print(f'Response headers: {res_headers}')
    assert status == 200
    # Проверка на наличие нужных полей в ответе
    for n in response[0]['response']:
        assert "first_name" in n and "last_name" in n \
               and "mobile_number" in n and "email" in n and "profession_list" in n \
               and "team_list" in n and "grade_list" in n
    # Проверка значения page
    assert response[0]['page'] == 2
    # Проверка значения limit
    assert response[0]['limit'] == 5
    # Проверка значения total
    assert response[0]['total'] == 8
    # Проверка ожидаемой выгрузки сотрудников
    list_e = [n['last_name'] for n in response[0]['response']]
    # print(list_e)
    expected_list = ['Орлова', 'Хохлова', 'Садчикова']
    assert list_e == sorted(expected_list)


def test_tm_with_first_and_last_name_and_profession():
    #S - API - TM - 67, 68
    status, response, res_headers = es.es_search(some_url=None, some_headers=None,
                                                 some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883"],
                                                            "first_name": "Иван", "last_name": "Афонин",
                                                            "profession": "Product-менеджер"})
    # print(f"\nCode: {status}")
    # print(f"Response: {response}")
    # print(f'Response headers: {res_headers}')
    assert status == 200
    # Проверка на наличие нужных полей в ответе
    for n in response[0]['response']:
        assert "first_name" in n and "last_name" in n \
               and "mobile_number" in n and "email" in n and "profession_list" in n \
               and "team_list" in n and "grade_list" in n
    # Проверка значения page
    assert response[0]['page'] == 1
    # Проверка значения limit
    assert response[0]['limit'] == 50
    # Проверка значения total
    assert response[0]['total'] == 1
    # Проверка ожидаемой выгрузки сотрудников
    assert response[0]['first_name'] == 'Иван' and response[0]['last_name'] == 'Афонин'


def test_tm_with_profession():
    #S - API - TM - 69
    status, response, res_headers = es.es_search(some_url=None, some_headers=None,
                                                 some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883"],
                                                            "profession": "Project-менеджер"})
    # print(f"\nCode: {status}")
    # print(f"Response: {response}")
    # print(f'Response headers: {res_headers}')
    assert status == 200
    # Проверка на наличие нужных полей в ответе
    for n in response[0]['response']:
        assert "first_name" in n and "last_name" in n \
               and "mobile_number" in n and "email" in n and "profession_list" in n \
               and "team_list" in n and "grade_list" in n
    # Проверка значения page
    assert response[0]['page'] == 1
    # Проверка значения limit
    assert response[0]['limit'] == 50
    # Проверка значения total
    assert response[0]['total'] == 1
    # Проверка ожидаемой выгрузки сотрудников
    assert response[0]['first_name'] == 'Евгения' and response[0]['last_name'] == 'Лязникова'


def test_tm_with_half_first_and_last_name():
    #S - API - TM - 71
    status, response, res_headers = es.es_search(some_url=None, some_headers=None,
                                                 some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883"],
                                                            "first_name": "Вал", "last_name": "Сад"})
    # print(f"\nCode: {status}")
    # print(f"Response: {response}")
    # print(f'Response headers: {res_headers}')
    assert status == 200
    # Проверка на наличие нужных полей в ответе
    for n in response[0]['response']:
        assert "first_name" in n and "last_name" in n \
               and "mobile_number" in n and "email" in n and "profession_list" in n \
               and "team_list" in n and "grade_list" in n
    # Проверка значения page
    assert response[0]['page'] == 1
    # Проверка значения limit
    assert response[0]['limit'] == 50
    # Проверка значения total
    assert response[0]['total'] == 1
    # Проверка ожидаемой выгрузки сотрудников
    assert response[0]['first_name'] == 'Валерия' and response[0]['last_name'] == 'Садчикова'


def test_page_10_limit_5():
    #S - API - TM - 45 Отправка запроса со значением в поле page, превышающем поле total (ожидаемого ответа)
    status, response, res_headers = es.es_search(some_url=None, some_headers=None,
                                                 some_data={"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883"],
                                                            "page": 10, "limit": 5})
    # print(f"\nCode: {status}")
    # print(f"Response: {response}")
    # print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Nothing found on this page', 'type': 'not_found'},)
