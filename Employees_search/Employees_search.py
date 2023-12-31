import requests
import json
from settings import *


class Teem_members_search():
    def __init__(self):
        pass

    def es_search(self, some_url=None, some_headers=None, some_data=None):
        '''Метод поиска сотрудников узла и потомков'''
        if some_headers is None:
            headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        else:
            headers = some_headers

        if some_url is None:
            url = url_employees_search
        else:
            url = some_url

        if some_data is None:
            data = {"team_ids": ["4ae7df2a-a5dd-4267-aaa8-093b84031883", "23a4363f-28d0-43e2-b66e-f2aedd4175ae"]}

        else:
            data = some_data

        res = requests.post(url, headers=headers, json=data)
        status = res.status_code
        res_headers = res.headers
        response = ""
        try:
            response = res.json(),
        except json.decoder.JSONDecodeError:
            response = res.text
        return status, response, res_headers

es = Teem_members_search()