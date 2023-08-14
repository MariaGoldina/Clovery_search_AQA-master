import pytest
from Skill_search import *


def test_skill_search_base_nesessary_fields():
    # Базовый позитивный с обязательными параметрами
    # S-API-Ss-01
    status, response, res_headers = skill_s.ssn(some_url=None, some_headers=None,
                                                some_data=None)
    # print(f"\nCode: {status}")
    # print(f"Response: {response}")
    # print(f'Response headers: {res_headers}')
    assert status == 200
    #Проверка ожидаемой выгрузки сотрудников
    list_e = [n['person_name'] for n in response[0]['items']]
    # print(list_e)
    assert list_e == ['Светлана Хохлова', 'Игорь Борисов', 'Семен Котов', 'Евгения Орлова']
    #Проверка на наличие нужных полей в ответе
    for n in response[0]['items']:
        assert "person_id" in n and "person_name" in n and "skills" in n
    # Проверка значения page
    assert response[0]['page'] == 0
    # Проверка значения limit
    assert response[0]['limit'] == 50
    # Проверка значения total
    assert response[0]['total'] == 4
    #Проверка выгрузки навыков сотрудников и сверка их со списком навыков в запросе (list_skills_q)
    list_skills_q = ['2c901b0c-f1cb-41e9-b566-a53f1b89714f', '6796cfb9-a61c-48fd-ac9c-a395a001fad1', 'a3c1ef15-6d4f-4290-abee-62247c5465ff']
    list_skills_1 = [n['id'] for n in response[0]['items'][0]['skills']]
    list_skills_2 = [n['id'] for n in response[0]['items'][1]['skills']]
    list_skills_3 = [n['id'] for n in response[0]['items'][2]['skills']]
    list_skills_4 = [n['id'] for n in response[0]['items'][3]['skills']]
    assert list_skills_1 == list_skills_q and list_skills_2 == list_skills_q and list_skills_3 == list_skills_q and list_skills_4 == list_skills_q
    # print(f'перечень навыков первого сотрудника: {list_skills_1}')
    # print(f'перечень навыков второго сотрудника:{list_skills_2}')
    # print(f'перечень навыков третьего сотрудника: {list_skills_3}')
    # print(f'перечень навыков четвертого сотрудника: {list_skills_4}')
    #Проверка заголовков в ответе
    assert "'Content-Type': 'application/json'" in str(res_headers)


@pytest.mark.smoke
def test_skill_search_with_optional_fields():
    # Базовый позитивный со всеми опциональными параметрами в body и query params
    # S-API-Ss-02b
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data=None, some_params=None)
    # print(f"\nCode: {status}")
    # print(f"Response: {response}")
    # print(f'Response headers: {res_headers}')
    assert status == 200
    # Проверка ожидаемой выгрузки сотрудника
    list_e = [n['person_name'] for n in response[0]['items']]
    # print(list_e)
    assert list_e == ['Игорь Борисов']
    #Проверка наличия полей ответа
    for n in response[0]['items']:
        assert "person_id" in n and "person_name" in n and "skills" in n \
               and 'professions' in n and 'teams' in n and 'assessment' in str(n['skills'])
    # Проверка значения page
    assert response[0]['page'] == 0
    # Проверка значения limit
    assert response[0]['limit'] == 50
    # Проверка значения total
    assert response[0]['total'] == 1
    #Проверка выгрузки навыков сотрудников и сверка их со списком навыков в запросе (list_skills_q)
    list_skills_q = ['2c901b0c-f1cb-41e9-b566-a53f1b89714f', '6796cfb9-a61c-48fd-ac9c-a395a001fad1', 'a3c1ef15-6d4f-4290-abee-62247c5465ff']
    list_skills_1 = [n['id'] for n in response[0]['items'][0]['skills']]
    assert list_skills_1 == list_skills_q
    # print(f'перечень навыков первого сотрудника: {list_skills_1}')
    #Проверка заголовков в ответе
    assert "'Content-Type': 'application/json'" in str(res_headers)


def test_ss_all_fields_and_full_match_false():
    #S-API-Ss-08. Позитивный сценарий. Отправка запроса со всеми обязательными параметрами,
    # опциональными параметрами profession_ids, team_ids, assessment_from > 0, assessment_to < 1,
    # и опциональным параметром "full_match_of_skills": False
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "profession_ids": ["3a4651a7-8bf0-4855-875b-5ff04e3fdf85",
                                                                              "9c08af9c-22d8-4bc6-a598-cb3ad035ceef"],
                                                           "team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883",
                                                                        "23a4363f-28d0-43e2-b66e-f2aedd4175ae"],
                                                           "skills": [{"skill_id": "ab12549c-a157-4790-9ff0-83edbfd22a10",
                                                                       "assessment_from": 0, "assessment_to": 0.99},
                                                                      {"skill_id": "a2a2a3ff-64cf-49b4-a44b-7e957dd5a41c",
                                                                       "assessment_from": 0, "assessment_to": 0.99},
                                                                      {"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1",
                                                                       "assessment_from": 0, "assessment_to": 0.99}],
                                                           "full_match_of_skills": False})
    # print(f"\nCode: {status}")
    # print(f"Response: {response}")
    # print(f'Response headers: {res_headers}')
    assert status == 200
    list_e = [n['person_name'] for n in response[0]['items']]
    # print(list_e)
    assert list_e == ["Алексей Лыжин", "Иван Афонин", "Мария Недочетова", "Игорь Борисов", "Евгения Лязникова", "Евгения Орлова", "Валерия Садчикова"]
    #Проверка на наличие нужных полей в ответе
    for n in response[0]['items']:
        assert "person_id" in n and "person_name" in n and "skills" in n \
               and 'professions' in n and 'teams' in n and 'assessment' in str(n['skills'])
    # Проверка значения page
    assert response[0]['page'] == 0
    # Проверка значения limit
    assert response[0]['limit'] == 50
    # Проверка значения total
    assert response[0]['total'] == 7
    #Проверка выгрузки навыков сотрудников и сверка их со списком навыков в запросе (list_skills_q)
    list_skills_q = ["a2a2a3ff-64cf-49b4-a44b-7e957dd5a41c", "ab12549c-a157-4790-9ff0-83edbfd22a10", "6796cfb9-a61c-48fd-ac9c-a395a001fad1"]
    list_skills_1 = [n['id'] for n in response[0]['items'][0]['skills']]
    list_skills_2 = [n['id'] for n in response[0]['items'][1]['skills']]
    list_skills_3 = [n['id'] for n in response[0]['items'][2]['skills']]
    list_skills_4 = [n['id'] for n in response[0]['items'][3]['skills']]
    list_skills_5 = [n['id'] for n in response[0]['items'][4]['skills']]
    list_skills_6 = [n['id'] for n in response[0]['items'][5]['skills']]
    list_skills_7 = [n['id'] for n in response[0]['items'][6]['skills']]
    for i in list_skills_1:
        assert i in list_skills_q
    for i in list_skills_2:
        assert i in list_skills_q
    for i in list_skills_3:
        assert i in list_skills_q
    for i in list_skills_4:
        assert i in list_skills_q
    for i in list_skills_5:
        assert i in list_skills_q
    for i in list_skills_6:
        assert i in list_skills_q
    for i in list_skills_7:
        assert i in list_skills_q
    # print(f'перечень навыков первого сотрудника: {list_skills_1}')
    # print(f'перечень навыков второго сотрудника:{list_skills_2}')
    # print(f'перечень навыков третьего сотрудника: {list_skills_3}')
    # print(f'перечень навыков четвертого сотрудника: {list_skills_4}')
    # print(f'перечень навыков пятого сотрудника: {list_skills_5}')
    # print(f'перечень навыков шестого сотрудника: {list_skills_6}')
    # print(f'перечень навыков седьмого сотрудника: {list_skills_7}')
    #Проверка заголовков в ответе
    assert "'Content-Type': 'application/json'" in str(res_headers)


def test_1_skill_assessment_from_0_98():
    #S-API-Ss-12. Проверка граничных значений. Отправка запроса с обязательными параметрами:
    # 1 навыком в поле skills и assessment_from = assessment тестового сотрудника
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "2c901b0c-f1cb-41e9-b566-a53f1b89714f",
                                                                       "assessment_from": 0.98}]})
    # print(f"\nCode: {status}")
    # print(f"Response: {response}")
    # print(f'Response headers: {res_headers}')
    assert status == 200
    list_e = [n['person_name'] for n in response[0]['items']]
    # print(list_e)
    expected_list = ['Светлана Хохлова']
    assert list_e == expected_list


def test_1_skill_assessment_to_0_36():
    #S-API-Ss-13. Проверка граничных значений. Отправка запроса с обязательными параметрами:
    # 1 навыком в поле skills и assessment_to = assessment тестового сотрудника
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "skills": [{"skill_id": "2c901b0c-f1cb-41e9-b566-a53f1b89714f",
                                                                       "assessment_to": 0.36}]})
    # print(f"\nCode: {status}")
    # print(f"Response: {response}")
    # print(f'Response headers: {res_headers}')
    assert status == 200
    list_e = [n['person_name'] for n in response[0]['items']]
    # print(list_e)
    expected_list = ['Игорь Борисов', 'Семен Котов', 'Евгения Орлова']
    assert list_e == expected_list


def test_obl_fields_page_4_limit_1():
    #S-API-Ss-17. Отправка запроса с обязательными параметрами в установленных пределах
    # и параметрами в Query params: page = 4, limit = 1
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None, some_params={"page": 4, "limit": 1},
                                                some_data=({"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skills": [{"skill_id": "c91c3df2-2cc3-4cfa-97d7-dbb1fc927121"}]}))
    # print(f"\nCode: {status}")
    # print(f"Response: {response}")
    # print(f'Response headers: {res_headers}')
    assert status == 200
    list_e = [n['person_name'] for n in response[0]['items']]
    # print(list_e)
    expected_list = ['Евгения Лязникова']
    assert list_e == expected_list


def test_profession_ids_non_matching():
    #S-API-Ss-98. Отправка запроса, в котором обязательные параметры соответствуют тестовым сотрудникам,
    # а profession_id в списке в поле не соответствуют тестовым сотрудникам
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None,
                                                some_data={"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                           "profession_ids": ["3a4651a7-8bf0-4855-875b-5ff04e3fdf85"],
                                                           "skills": [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"}]},
                                                some_params= None)

    # print(f"\nCode: {status}")
    # print(f"Response: {response}")
    # print(f'Response headers: {res_headers}')
    assert status == 404
    assert response[0] == {'detail': 'Nothing found for specified search parameters', 'type': 'not_found'}


def test_page_more_than_total():
    #S-API-Ss-38. Отправка запроса со значением в поле page, превышающем поле total (ожидаемого ответа)
    status, response, res_headers = skill_s.sso(some_url=None, some_headers=None, some_params={"page": 100, "limit": 5},
                                                some_data=({"company_id": "4b871f91-45aa-4a72-8cb5-417ef561307f",
                                                            "skills": [{"skill_id": "c91c3df2-2cc3-4cfa-97d7-dbb1fc927121"}]}))
    # print(f"\nCode: {status}")
    # print(f"Response: {response}")
    # print(f'Response headers: {res_headers}')
    assert status == 404
    assert response[0] == {'detail': 'Nothing found on this page', 'type': 'not_found'}
