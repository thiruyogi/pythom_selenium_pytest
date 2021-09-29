from selenium.webdriver.common.by import By


class WebappSettings():
    # Elements in the settings page:
    no_channels_message = (By.XPATH, "//div[contains(text(),'No custom channels have been marked active.')]")
    edit_button = (By.XPATH, "//button[contains(text(),'Edit')]")
    update_button = (By.XPATH, "//button[contains(text(),'Update')]")
    discard_changes_button = (By.XPATH, "//button[contains(text(),'Discard Changes')]")

    # Elements in channels page
    create_new_channel_button = (By.XPATH, "//button[contains(text(),'Create New Channel')]")
    save_channel_button = (By.XPATH, "//button[contains(text(),'Save')]")
    cancel_button = (By.XPATH, "//button[contains(text(),'Cancel')]")
    status_toggle_button = (By.XPATH, "//div[contains(text(),'Status')]/following-sibling::div/span")
    tags_dropdown = (By.XPATH, "//span[contains(text(),'Search & Select Tag(s)')]/parent::div/following-sibling::div["
                               "contains(@class,'cy-select__menu--icon')]")
    search_shares = (By.XPATH, "//div[contains(@class,'cy-select-search multiple')]/input")
    search_tags = (By.XPATH, "//div[contains(@class,'cy-select-search multiple')]/input")
    sharing_dropdown = (By.XPATH, "//span[contains(text(),'Select Sharing')]/parent::div/following-sibling::div[ "
                                  "contains(@class,'cy-select__menu--icon')]")
    channel_title = (By.XPATH, "//input[@aria-placeholder='Title']")
    search_tag = (By.XPATH, "//input[@placeholder='Search ...']")

    # Elements in Alert Categories Screen:
    edit_categories_selection_button = (By.XPATH, "//button[contains(text(),'Edit')]")
    update_categories_selection_button = (By.XPATH, "//button[contains(text(),'Update')]")
    discard_changes_button = (By.XPATH, "//button[contains(text(),'Discard Changes')]")

    # Elements in Crisis Profile Screen:
    start_time = (By.XPATH,"//div[@cy-test-id='business-start-hour']")
    end_time = (By.XPATH,"//div[@cy-test-id='business-end-hour']")
    clear_time_selection = (By.XPATH, "//i[contains(@class,'el-icon-circle-close')]")
    time_zone = (By.XPATH,"//div[@cy-test-id='business-time-zone']")
    voice_preference = (By.XPATH,"//div[@cy-test-id='crisis-voice-preference']")
    add_contact_info_button = (By.XPATH,"//button[@cy-test-id='crisis-add-number']")
    start_time_text_field = (By.XPATH,"//div[@cy-test-id='business-start-hour']//input")
    end_time_text_field = (By.XPATH,"//div[@cy-test-id='business-end-hour']//input")
    add_contact_number_header = (By.XPATH,"//div[contains(text(),'Add Contact Numbers')]")
    delete_contact_info_button =(By.XPATH,"//button[@cy-test-id='crisis-delete-number']")

    @classmethod
    def generalSettingsTab(self, tabName):
        return (By.XPATH, "//div[contains(text(),'{0}')]".format(tabName))

    @classmethod
    def settingsSecondaryNavTabs(self, tabName):
        return (By.XPATH, "//a[contains(text(),'{0}')]".format(tabName))

    # Elements in channels page
    @classmethod
    def channelsTab(self, channelDivision="My Channel"):
        return (By.XPATH, "//div[contains(text(),'{0}')]".format(channelDivision))

    @classmethod
    def channelsNotificationToggle(self, toggleName):
        return (By.XPATH, "//div[contains(text(),'{0}')]/following-sibling::span".format(toggleName))

    @classmethod
    def recommendedTags(self, tagName):
        return (By.XPATH, "//span[contains(text(),'{0}')]".format(tagName))

    @classmethod
    def tagSearchResult(self, tagName):
        return (By.XPATH, "//div[contains(text(),'{0}')]".format(tagName))

    @classmethod
    def searchReultTagCheckbox(self, tagName):
        return (By.XPATH, "//div[contains(text(),'{0}')]".format(tagName))

    @classmethod
    def searchResultOrgChecbox(self, orgName):
        return (By.XPATH, "//div[contains(text(),'{0}')]".format(orgName))

    @classmethod
    def createNewTag(self, tagName):
        return (By.XPATH, "//div[contains(text(),'Create new tag: {0}')]".format(tagName))

    @classmethod
    def channelInList(self, channelName):
        return (By.XPATH, "//div[contains(text(),'{0}')]".format(channelName))

    @classmethod
    def selectedSharingInChannel(self, channelName):
        return (By.XPATH, "//div[contains(text(),'{0}')]/ancestor::td/following-sibling::td[5]//div[contains("
                          "@class,'csp-text-md')]/span".format(channelName))

    @classmethod
    def addToMyChannels(self, channelName):
        return (By.XPATH, "//div[contains(text(),'{0}')]/ancestor::td/following-sibling::td[3]//button[contains(text("
                          "),'Add to My Channels')]".format(channelName))

    # Elements in Categories selection screen
    @classmethod
    def categoryToggle(self, categoryName):
        return (By.XPATH, "//div[contains(text(),'{0}')]/parent::div/"
                "following-sibling::div//input[@type='checkbox']".format(categoryName))
    
    @classmethod
    def categoryToggleCheck(self, categoryName):
        return (By.XPATH,"//div[contains(text(),'{0}')]/parent::div/"
                "following-sibling::div/div[@role='switch']".format(categoryName))

    #Elements in Crisis Profile Screen
    @classmethod
    def phone_number(self, index):
        return (By.XPATH,"//div[contains(text(),'Add Contact Numbers')]/following-sibling::div[2]/div[{0}]//input[@placeholder='Phone Number' or @placeholder='Enter Numbers Only']".format(index))
    
    @classmethod
    def phone_code(self,index):
        return (By.XPATH,"//div[contains(text(),'Add Contact Numbers')]/following-sibling::div[2]/div[{0}]//div[contains(@class,'phone-input__code')]".format(index))

    @classmethod
    def send_sms(self, index):
        return (By.XPATH,"//div[contains(text(),'Add Contact Numbers')]/following-sibling::div[2]/div[{0}]//div[contains(text(),'Send SMS')]".format(index))

    @classmethod
    def call_priority_dropdown(self, row, column):
        return (By.XPATH,"//div[@cy-test-id='crisis-call-priority-{0}-{1}']".format(row,column))

    @classmethod
    def call_priority_dropdown_selected_value(self, row, column):
        return (By.XPATH,"//div[@cy-test-id='crisis-call-priority-{0}-{1}']//div[contains(@class,'cy-select__menu--label__value')]".format(row,column))