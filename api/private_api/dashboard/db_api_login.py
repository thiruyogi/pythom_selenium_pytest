from base.apiRequests import Request
from pytest_testconfig import config

TOKEN = None
class DashboardApi:

    def apiLogin(self):
        global token
        payload = {
            "email": "{0}".format(config["APP_SETTINGS"]["ADMIN_EMAIL"]),
            "password": "{0}".format(config["APP_SETTINGS"]["ADMIN_API_PASSWORD"]),
            'tenant_code': "{0}".format(config["APP_SETTINGS"]["TENANT"]),
            'hideNotifyErr': True
        }
        headers = {
            'content-type': 'application/json;charset=UTF-8'
        }

        response = Request.post(config["API_ENDPOINTS"]["DASHBOARD_LOGIN"], data=payload, headers=headers)
        token = response['key']
        return token
