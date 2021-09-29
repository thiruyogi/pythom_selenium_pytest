import pytest
from expects import *
from base.basePage import BaseClass
from pages.dashboard.login_Page import LoginPage
import pdb


class TestLogin(BaseClass):

    @pytest.fixture(autouse=True)
    def classSetup(self, one_time_setup):
        self.LoginPage = LoginPage(self.driver)
        print("This is from class setup")

    def test_invalid_login(self):
        self.LoginPage.login("thiru@cyware.com", "Test1234")
        expect(self.LoginPage.isInvalidCredentials()).to(be_true)

    def test_valid_login(self):
        self.LoginPage.login("thiru.gnanam@cyware.com", "Cyware@321")
        expect(self.LoginPage.verifyLoginSuccessful()).to(be_true)
