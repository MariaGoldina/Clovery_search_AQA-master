from Node_employees_search import *


def test_nes_base_positive():
    #S - API - NE - 1 - БАЗОВЫЙ ПОЗИТИВНЫЙ ТЕСТ
    data = {}
    if server == "test":
        data = {"node_id": 2919, "project_id": '3e3028cd-3849-461b-a32b-90c0d6411daa', "item_type": 'orgstructureM',
                "item": 'pytest', "page": 1, "limit": 50, "is_only_node": False}
    elif server == "prod":
        data = {"node_id": 150, "project_id": "4b871f91-45aa-4a72-8cb5-417ef561307f", "item_type": "orgstructureM",
                "item": "postman", "page": 1, "limit": 50, "is_only_node": False}
    status, response, res_headers = nes.search(wrong_url=None, wrong_headers=None,
                                               some_data=data)
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


def test_nes_without_optional_fields():
    #S - API - NE - 02 - Без опциональных полей
    data = {}
    if server == "test":
        data = {"node_id": 2919, "project_id": '3e3028cd-3849-461b-a32b-90c0d6411daa', "item_type": 'orgstructureM',
                "item": 'pytest'}
    elif server == "prod":
        data = {"node_id": 150, "project_id": "4b871f91-45aa-4a72-8cb5-417ef561307f", "item_type": "orgstructureM",
                "item": "postman"}
    status, response, res_headers = nes.search(wrong_url=None, wrong_headers=None,
                                               some_data=data)
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


def test_nes_is_only_node_true():
    #S - API - NE - 3 - is_only_node = True
    data = {}
    if server == "test":
        data = {"node_id": 2919, "project_id": '3e3028cd-3849-461b-a32b-90c0d6411daa', "item_type": 'orgstructureM',
                "item": 'pytest', "page": 1, "limit": 50, "is_only_node": True}
    elif server == "prod":
        data = {"node_id": 150, "project_id": "4b871f91-45aa-4a72-8cb5-417ef561307f", "item_type": "orgstructureM",
                "item": "postman", "page": 1, "limit": 50, "is_only_node": True}
    status, response, res_headers = nes.search(wrong_url=None, wrong_headers=None,
                                               some_data=data)
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
    assert response[0]['total'] == 5
    # Проверка ожидаемой выгрузки сотрудников
    list_e = [n['last_name'] for n in response[0]['response']]
    # print(list_e)
    expected_list = ['Лыжин', 'Афонин', 'Недочетова', 'Лязникова', 'Садчикова']
    assert list_e == sorted(expected_list)


def test_nes_page2_limit5():
    #S-API-NE-67 Отправка запроса с обязательными параметрами с валидными данными и параметрами: page = 2, limit = 5
    data = {}
    if server == "test":
        data = {"node_id": 2919, "project_id": '3e3028cd-3849-461b-a32b-90c0d6411daa', "item_type": 'orgstructureM',
                "item": 'pytest', "page": 2, "limit": 5, "is_only_node": False}
    elif server == "prod":
        data = {"node_id": 150, "project_id": "4b871f91-45aa-4a72-8cb5-417ef561307f", "item_type": "orgstructureM",
                "item": "postman", "page": 2, "limit": 5, "is_only_node": False}
    status, response, res_headers = nes.search(wrong_url=None, wrong_headers=None,
                                               some_data=data)
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


def test_nes_empty_team():
    #S-API-NE-24 -Запрос с указанием node_id узла без потомков, к которому не привязаны сотрудники (привязана пустая команда)
    data = {}
    if server == "test":
        data = {"node_id": 2982, "project_id": '3e3028cd-3849-461b-a32b-90c0d6411daa', "item_type": 'orgstructureM',
                "item": 'pytest', "page": 1, "limit": 50, "is_only_node": False}
    elif server == "prod":
        data = {"node_id": 153, "project_id": "4b871f91-45aa-4a72-8cb5-417ef561307f", "item_type": "orgstructureM",
                "item": "postman", "page": 1, "limit": 50, "is_only_node": False}
    status, response, res_headers = nes.search(wrong_url=None, wrong_headers=None,
                                               some_data=data)
    # print(f"\nCode: {status}")
    # print(f"Response: {response}")
    # print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Service Employees_search returned: Nothing found for specified search parameters'},)


def test_page_more_than_total():
    #S-API-NE-56 Отправка запроса со значением в поле page, превышающем поле total (ожидаемого ответа)
    data = {}
    if server == "test":
        data = {"node_id": 2919, "project_id": '3e3028cd-3849-461b-a32b-90c0d6411daa', "item_type": 'orgstructureM',
                "item": 'pytest', "page": 100, "limit": 50, "is_only_node": False}
    elif server == "prod":
        data = {"node_id": 150, "project_id": "4b871f91-45aa-4a72-8cb5-417ef561307f", "item_type": "orgstructureM",
                "item": "postman", "page": 100, "limit": 50, "is_only_node": False}
    status, response, res_headers = nes.search(wrong_url=None, wrong_headers=None,
                                               some_data=data)
    # print(f"\nCode: {status}")
    # print(f"Response: {response}")
    # print(f'Response headers: {res_headers}')
    assert status == 404
    assert response == ({'detail': 'Service Employees_search returned: Nothing found on this page'},)
