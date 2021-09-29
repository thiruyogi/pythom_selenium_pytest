from selenium.webdriver.common.by import By

class WebAppAdminSettings():
    #Elements in the Admin settings screen
    add_member_button = (By.XPATH, "//span[contains(text(),'Add Member')]")
    filters_button = (By.XPATH,"//span[contains(text(),'Filters')]")
    status_filter_dropdown = (By.XPATH, "//span[contains(text(),'Status')]")
    role_filter_dropdown = (By.XPATH,"//span[contains(text(),'Role')]")
    organization_name_header = (By.XPATH,"//span[contains(text(),'Organization Name')]")
    organization_name = (By.XPATH,"//span[contains(text(),'Organization Name')]/following-sibling::p")
    level_text = (By.XPATH,"//span[contains(text(),'Level')]/following-sibling::div//span")
    organization_type =(By.XPATH,"//span[contains(text(),'Organization type')]/following-sibling::div//span")
    headquarters_location = (By.XPATH,"//span[contains(text(),'Headquarter Location')]/following-sibling::p")
    license_usage = (By.XPATH,"//span[contains(text(),'License Usage')]/following-sibling::p")
    status_toggle = (By.XPATH,"//span[contains(text(),'Status')]/following-sibling::div/span")
    member_full_name = (By.XPATH,"//input[contains(@aria-placeholder,'Full Name')]")
    member_title = (By.XPATH,"//input[@aria-placeholder='Title']")
    member_email = (By.XPATH,"//input[contains(@aria-placeholder,'Email')]")
    phone_code_dropdown = (By.XPATH,"//span[contains(text(),'Code')]")
    phone_code_search = (By.XPATH,"//input[starts-with(@placeholder,'Search ...')]")
    phone_number = (By.XPATH,"//input[@placeholder='Phone Number']")
    assign_roles_dropdown = (By.XPATH,"//p[contains(text(),'Assign Role(s)')]/following-sibling::div")
    send_welcome_email = (By.XPATH,"//span[contains(text(),'Send Welcome Email')]")
    next_button = (By.XPATH,"//span[contains(text(),'Next')]")

    @classmethod
    def adminSettingsSecondaryNav(self, tabName):
        return (By.XPATH,"//div[contains(text(),'{0}')]".format(tabName))

    #Elements in Add Member screen
    @classmethod
    def addMemberTabs(self, tabName):
        return (By.XPATH,"//div[contains(text(),'{0}')]".format(tabName))

    @classmethod
    def member_alert_delivery_options(self, option):
        return (By.XPATH,"//span[contains(text(),'{0}')]/parent::span/preceding-sibling::span".format(option))