from selenium.webdriver.common.by import By


class WebappHomeLocators:
    orgLogo_img = (By.XPATH, "//div[contains(@class,'WaSidebar_logo')]")
    userName_field = (By.XPATH, "//div[@cy-test-id='user-email']/input")
    passWord_field = (By.XPATH, "//div[@cy-test-id='user-password']/input")
    login_button = (By.XPATH, "//button[@cy-test-id='submit-btn']")
    settings_icon = (By.XPATH, "//span[contains(@class,'cp-icon-settings')]")
    menu_icon = (By.XPATH, "//span[contains(@class,'cp-icon-hamburger')]")
    alerts_icon = (By.XPATH, "//span[contains(@class,'cp-icon-alert')]")

    @classmethod
    def navSidePaneTab(self, tabName):
        return (By.XPATH, "//span[contains(@class,'WaSidebar_menu-item') and contains(text(),'{0}')]".format(tabName))

    @classmethod
    def settingsSecondaryNav(self, tabName):
        return (By.XPATH, "//p[contains(text(),'{0}')]".format(tabName))

    # Locators for secondary navigation tabs under Menu
    @classmethod
    def menuSecondaryNavTabs(self, tabName):
        return (By.XPATH, "//span[contains(text(),'{0}')]".format(tabName))

    @classmethod
    def pinTabsToSideBar(self, tabName):
        return (By.XPATH, "//span[contains(text(),'{0}')]/ancestor::a/following-sibling::" \
                          "div[contains(@class,'WaMenubar_pin-icon')]".format(tabName))
