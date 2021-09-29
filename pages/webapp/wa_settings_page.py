from locators.webapp.wa_settings_member_settings import webAppAdminSettings
import pdb
import utilities.Custom_Logger as cl
from pages.webapp.wa_webapp_home_page import WebAppHomePage
from locators.webapp.wa_settings import WebappSettings
from utilities.utils import Util
from selenium.webdriver.common.by import By
import time


class SettingsPage(WebAppHomePage):
    log = cl.customLogger()

    def __init__(self, driver):
        self.driver = driver

    # Functions
    def navigateToGeneralSettingsPage(self):
        if "user/settings/general" not in self.getCurrentUrl():
            self.openSettings()

    def generalSettingsSecondaryNav(self, tabName):
        self.navigateToGeneralSettingsPage()
        self.elementClick(WebappSettings.generalSettingsTab(tabName))

    #Functions related to channels
    def verifyNoChannelsPresent(self):
        return self.isElementPresent(WebappSettings.no_channels_message)

    def fillChannelTitle(self, channelTitle):
        self.clearSendKeys(channelTitle, WebappSettings.channel_title)

    def searchTags(self, tagName):
        self.elementClick(WebappSettings.tags_dropdown)
        self.elementClick(WebappSettings.search_tags)
        self.clearSendKeys(tagName, WebappSettings.search_tags)

    def selectSearchResultTag(self, tagName):
        self.elementClick(WebappSettings.searchReultTagCheckbox(tagName))

    def createNewTag(self, tagName):
        self.elementClick(WebappSettings.createNewTag(tagName))

    def fillChannelTags(self, tags):
        if isinstance(tags, list):
            for tag in tags:
                if self.isElementPresent(WebappSettings.recommendedTags(tag)):
                    self.elementClick(WebappSettings.recommendedTags(tag))
                else:
                    self.searchTags(tag)
                    if self.isElementPresent(WebappSettings.searchReultTagCheckbox(tag)):
                        self.selectSearchResultTag(tag)
                    else:
                        self.createNewTag(tag)
        else:
            if self.isElementPresent(WebappSettings.recommendedTags(tags)):
                self.elementClick(WebappSettings.recommendedTags(tags))
            else:
                self.searchTags(tags)
                if self.isElementPresent(WebappSettings.searchReultTagCheckbox(tags)):
                    self.selectSearchResultTag()
                else:
                    self.createNewTag(tags)

    def selectSharing(self, sharing):
        self.elementClick(WebappSettings.sharing_dropdown)
        if isinstance(sharing, list):
            for share in sharing:
                self.elementClick(WebappSettings.searchResultOrgChecbox(share))
        else:
            self.elementClick(WebappSettings.searchResultOrgChecbox(sharing))

    def toggleStatus(self):
        self.elementClick(WebappSettings.status_toggle_button)

    def toggleNotification(self, notificationType):
        self.elementClick(WebappSettings.channelsNotificationToggle(notificationType))

    def fillChannelFields(self, channelDetails):
        for key, value in channelDetails.items():
            if key == "title":
                self.fillChannelTitle(value)
            elif key == "tags":
                self.fillChannelTags(value)
            elif key == "status":
                if not value:
                    self.toggleStatus()
            elif key == "email notification":
                if not value:
                    self.toggleNotification("Email Notification")
            elif key == "mobile notification":
                if not value:
                    self.toggleNotification("Mobile Notification")
            elif key == "sharing":
                self.selectSharing(value)

    def createNewChannel(self, channelDetails):
        self.elementClick(WebappSettings.create_new_channel_button)
        self.fillChannelFields(channelDetails)
        self.elementClick(WebappSettings.save_channel_button)
        time.sleep(2)

    def verifyChannelPresent(self, channelName):
        return self.isElementPresent(WebappSettings.channelInList(channelName))

    def getSelectedSharing(self, channelName):
        return self.getTexts(WebappSettings.selectedSharingInChannel(channelName))

    def verifySelectedSharing(self, expectedList, actualList):
        return Util.verifyListMatch(expectedList, actualList)

    def navigateToSharedChannel(self):
        self.elementClick(WebappSettings.channelsTab("Shared Channel"))

    def navigateToDefaultChannel(self):
        self.elementClick(WebappSettings.channelsTab("Default Channel"))

    def navigateToMyChannel(self):
        self.elementClick(WebappSettings.channelsTab())

    def addToMyChannel(self, sharedChannelName):
        self.elementClick(WebappSettings.addToMyChannels(sharedChannelName))
        self.elementClick(WebappSettings.save_channel_button)

    #functions related to categories
    def verfiyCategoryEditable(self, categoryName):
        self.elementClick(WebappSettings.edit_categories_selection_button)
        status = self.isEnabled(WebappSettings.categoryToggle(categoryName))
        self.elementClick(WebappSettings.update_categories_selection_button)
        return status

    def enableCategory(self, categoryName):
        self.elementClick(WebappSettings.edit_categories_selection_button)
        self.enableToggle(WebappSettings.categoryToggleCheck(categoryName))
        self.elementClick(WebappSettings.update_categories_selection_button)

    def disableCategory(self, categoryName):
        self.elementClick(WebappSettings.edit_categories_selection_button)
        self.disableToggle(WebappSettings.categoryToggleCheck(categoryName))
        self.elementClick(WebappSettings.update_categories_selection_button)

    def verifyCategoryStatus(self, categoryName):
        return self.getToggleStatus(WebappSettings.categoryToggleCheck(categoryName))

    #functions related to crisis profile
    def set_start_time(self, start_time):
        self.elementClick(WebappSettings.start_time)
        self.clearSendKeys(start_time,WebappSettings.start_time_text_field)
        self.elementClick(WebappSettings.add_contact_number_header)
    
    def set_end_time(self, end_time):
        self.elementClick(WebappSettings.end_time)
        self.clearSendKeys(end_time,WebappSettings.end_time_text_field)
        self.elementClick(WebappSettings.add_contact_number_header)
    
    def set_time_zone(self, time_zone):
        self.selectDropdown(WebappSettings.time_zone,time_zone)

    def set_voice_preference(self, voice_preference):
        self.selectDropdown(WebappSettings.voice_preference, voice_preference)
    
    def set_contact_info(self,contact_info):
        if isinstance(contact_info,list):
            no_of_contacts = len(contact_info)
            for i in range(1, no_of_contacts):
                if self.isElementPresent(WebappSettings.add_contact_info_button):
                    self.elementClick(WebappSettings.add_contact_info_button)    
            index = 1
            for contact in contact_info:
                for key, value in contact.items():
                    if key == 'code':
                        self.selectDropdown(WebappSettings.phone_code(index),value)
                    elif key == 'number':
                        self.clearSendKeys(value, WebappSettings.phone_number(index))
                    elif key == 'send_sms':
                        if value:
                            self.elementClick(WebappSettings.send_sms(index))
                index = index+1
        else:
            for key, value in contact_info.items():
                    if key == 'code':
                        self.selectDropdown(WebappSettings.phone_code(1),value)
                    elif key == 'number':
                        self.clearSendKeys(value, WebappSettings.phone_number(1))
                    elif key == 'send_sms':
                        if value:
                            self.elementClick(WebappSettings.send_sms(1))

    def edit_crisis_profile(self, crisis_profile_data):
        self.generalSettingsSecondaryNav('Crisis Profile')
        self.elementClick(WebappSettings.edit_button)
        for key,value in crisis_profile_data.items():
            if key == 'start_time':
                self.set_start_time(value)
            elif key == 'end_time':
                self.set_end_time(value)
            elif key == 'time_zone':
                self.set_time_zone(value)
            elif key == 'voice_preference':
                self.set_voice_preference(value)
            elif key == 'contact_info':
                self.set_contact_info(value)
        self.elementClick(WebappSettings.update_button)

    def verify_add_contact_button_present(self):
        self.elementClick(WebappSettings.edit_button)
        element_present= self.isElementPresent(WebappSettings.add_contact_info_button)
        self.elementClick(WebappSettings.update_button)
        return element_present
    
    def verify_call_priority_dropdwon(self,row_max,column_max):
        dropdown_presence =[]
        self.elementClick(WebappSettings.edit_button)
        for row in range(0,row_max):
            for column in range(1,column_max):
                element_present = self.isElementPresent(WebappSettings.call_priority_dropdown(row,column))
                dropdown_presence.append(element_present)
        self.elementClick(WebappSettings.update_button)
        if False in dropdown_presence:
            return False
        else:
            return True

    def fill_call_priority_dropdown(self, call_priority_info):
        self.elementClick(WebappSettings.edit_button)
        if isinstance(call_priority_info,list):
            no_of_rows = len(call_priority_info)
            for i in range(0,no_of_rows):
                for key, number in call_priority_info[i].items():
                    if key == 'business_hours':
                        self.selectDropdown(WebappSettings.call_priority_dropdown(i,1),number)
                    elif key == 'after_business_hours':
                        self.selectDropdown(WebappSettings.call_priority_dropdown(i,2),number)
                    elif key == 'weekend':
                        self.selectDropdown(WebappSettings.call_priority_dropdown(i,3),number)
        else:
            for key, number in call_priority_info.items():
                if key == 'business_hours':
                    self.selectDropdown(WebappSettings.call_priority_dropdown(0,1),number)
                elif key == 'after_business_hours':
                    self.selectDropdown(WebappSettings.call_priority_dropdown(0,2),number)
                elif key == 'weekend':
                    self.selectDropdown(WebappSettings.call_priority_dropdown(0,3),number)
        self.elementClick(WebappSettings.update_button)

    def selected_call_priority_value(self, row, column):
        self.elementClick(WebappSettings.edit_button)
        value = self.getText(WebappSettings.call_priority_dropdown_selected_value(row, column))
        self.elementClick(WebappSettings.update_button)
        return value

    def clear_all_contact_info(self):
        self.elementClick(WebappSettings.edit_button)
        no_of_contacts = len(self.getElementList(WebappSettings.delete_contact_info_button))
        if not no_of_contacts==None:
            for i in range(1,no_of_contacts):
                self.elementClick(WebappSettings.delete_contact_info_button)
        self.selectDropdown(WebappSettings.phone_code(1),"+1")
        self.elementClick(WebappSettings.update_button)



