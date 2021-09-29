from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import logging
import utilities.Custom_Logger as cl


class LoginPage(SeleniumDriver):

    log = cl.customLogger()

    def __init__(self, driver):
        self.driver = driver

    # Elements in the page:
    userName_field = (By.XPATH, "//*[@placeholder='Enter your email address']")
    passWord_field = (By.XPATH, "//*[@placeholder='Enter your password']")
    login_button = (By.XPATH, "//span[contains(text(),'Login')]")
    alerts_tab = (By.XPATH, "//div[contains(text(),'Alerts')]")
    invalid_creds_error = (By.XPATH, "//p[contains(text(),'Invalid Username or Password')]")

    def enterEmail(self, email):
        self.clearSendKeys(email, self.userName_field)

    def enterPassword(self, password):
        self.clearSendKeys(password, self.passWord_field)

    def clickLogin(self):
        self.elementClick(self.login_button)

    def login(self, email="", password=""):
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLogin()

    def verifyLoginSuccessful(self):
        return self.isElementPresent(self.alerts_tab)

    def isInvalidCredentials(self):
        return self.isElementPresent(self.invalid_creds_error)

