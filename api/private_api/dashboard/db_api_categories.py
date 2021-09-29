from requests.models import Response
from api.private_api.dashboard.db_api_login import TOKEN
from pytest_testconfig import config
from base.apiRequests import Request


class DashboardCategories:

    def __init__(self, token):
        self.headers ={
            'content-type': 'application/json;charset=UTF-8',
            'authorization': f'Token {token}'
        }

    def create_new_category(self, category_details):
        response = Request.post(config["API_ENDPOINTS"]["CATEGORY_CREATE"],category_details,self.headers)
