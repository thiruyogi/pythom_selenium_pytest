import pdb

from base.selenium_driver import SeleniumDriver
import logging
import utilities.Custom_Logger as cl
from locators.webapp.wa_home import WebappHomeLocators
from utilities.utils import Util


class WebAppHomePage(SeleniumDriver):
    log = cl.customLogger()

    #functions
    def enterEmail(self, email):
        self.clearSendKeys(email, WebappHomeLocators.userName_field)

    def enterPassword(self, password):
        self.clearSendKeys(password, WebappHomeLocators.passWord_field)

    def clickLogin(self):
        self.elementClick(WebappHomeLocators.login_button)

    def login(self, email="", password=""):
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLogin()

    def openMenu(self):
        self.elementClick(WebappHomeLocators.menu_icon)

    # def sideBarPrimaryNavigation(self, tabName):
    #     self.mouseOverElement(self.orgLogo_img, "Xpath")
    #     self.elementClick(self.navSidePaneTab(tabName))

    def menuSecondaryNavigation(self, tabName):
        self.openMenu()
        self.elementClick(WebappHomeLocators.menuSecondaryNavTabs(tabName))

    def pinMenuTabToSideBar(self, tabName):
        self.sideBarPrimaryNavigation("Menu")
        self.mouseOverElemenet(WebappHomeLocators.menuSecondaryNavTabs(tabName))
        self.elementClick(WebappHomeLocators.pinTabsToSideBar(tabName))

    def openSettings(self, tabName="General Settings"):
        self.elementClick(WebappHomeLocators.settings_icon)
        self.elementClick(WebappHomeLocators.settingsSecondaryNav(tabName))

