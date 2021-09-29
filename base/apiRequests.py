import requests
from pytest_testconfig import config
import json

from requests.models import Response


class Request:
    @staticmethod
    def post(endpoint: str, data: dict = None, headers: dict = None, cookies: dict = None):
        response = Request._send(endpoint, data, headers, cookies, 'POST')
        return response.json()

    @staticmethod
    def get(endpoint: str, data: dict = None, headers: dict = None, cookies: dict = None):
        response = Request._send(endpoint, data, headers, cookies, 'GET')
        return response.json()

    @staticmethod
    def put(endpoint: str, data: dict = None, headers: dict = None, cookies: dict = None):
        response = Request._send(endpoint, data, headers, cookies, 'PUT')
        return response.json()

    @staticmethod
    def delete(endpoint: str, data: dict = None, headers: dict = None, cookies: dict = None):
        response = Request._send(endpoint, data, headers, cookies, 'DELETE')
        return response.json()

    @staticmethod
    def _send(endpoint: str, data: dict, headers: dict, cookies: dict, method: str):
        baseUrl = config["APP_SETTINGS"]["DASHBOARD_API_URL"]+endpoint

        if headers is None:
            headers = {}

        if cookies is None:
            cookies = {}


        if method == 'GET':
            response = requests.get(baseUrl, params=data, headers=headers, cookies=cookies)
        elif method == 'POST':
            response = requests.post(baseUrl, data=json.dumps(data), headers=headers, cookies=cookies)
        elif method == 'PUT':
            response = requests.put(baseUrl, data=json.dumps(data), headers=headers, cookies=cookies)
        elif method == 'DELETE':
            response = requests.get(baseUrl, params=data, headers=headers, cookies=cookies)
        else:
            raise Exception(f'Bad HTTP method "{method}" was received')

        return response
