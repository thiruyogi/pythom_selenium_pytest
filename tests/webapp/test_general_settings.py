import pytest
from base.basePage import BaseClass
import utilities.Custom_Logger as cl
from base.webdriver_factory import WebDriverFactory
from pytest_testconfig import config
from utilities.utils import Util
from pages.webapp.wa_settings_page import SettingsPage
from expects import expect, be_true, be_false, equal
import pdb
import allure
from api.private_api.dashboard.db_api_login import DashboardApi
from api.private_api.dashboard.db_api_categories import DashboardCategories


@allure.feature("Webapp General Settings screen")
class TestGeneralSettings(BaseClass):

    log = cl.customLogger()

    
    @pytest.fixture(scope="class", autouse=True)
    def classSetup(self, one_time_setup):
        self.__class__.webapp_settings = SettingsPage(self.webapp_driver)
        self.webapp_settings.login(config["APP_SETTINGS"]["ADMIN_EMAIL"], config["APP_SETTINGS"]["ADMIN_PASSWORD"])
        wd1 = WebDriverFactory(self.browser, self.webappUrl)
        self.__class__.webapp_driver1 = wd1.getWebDriverInstance()
        self.__class__.webapp_settings1 = SettingsPage(self.webapp_driver1)
        self.webapp_settings1.login(config["APP_SETTINGS"]["SECONDUSER_EMAIL"], config["APP_SETTINGS"]["ADMIN_PASSWORD"])
        self.db_api_login = DashboardApi()
        self.__class__.token = self.db_api_login.apiLogin()
        self.__class__.categories_api = DashboardCategories(self.token)
        yield
        self.webapp_driver1.quit()

    @allure.title("Validate that user is able to create a new channel by enabling Email Notification and Mobile app "
            "notifications.")    
    def test_new_channel_create_with_Email_mobile_app_notification(self):
        channel_name = "CSAP_AUTO_New_" + Util.getUniqueName()
        self.webapp_settings.generalSettingsSecondaryNav("Channels")
        channel_details = {
            "title": channel_name,
            "tags": ["pir:vln-attn", "Test New tag"],
            "status": False,
            "email notification": False,
            "mobile notification": False,
            "sharing": ["Global", "Organization"]
        }
        self.webapp_settings.createNewChannel(channel_details)
        expect(self.webapp_settings.verifyChannelPresent(channel_name)).to(be_true)
        actualList = self.webapp_settings.getSelectedSharing(channel_name)
        expectedList = ['Organization,', 'Global']
        expect(self.webapp_settings.verifySelectedSharing(expectedList, actualList)).to(be_true)

    @allure.title("Validate that user is able to see the shared channels by other users in the shared channels tab")
    def test_view_shared_channels_under_shared_channels_tab(self):
        channel1_name = "CSAP_AUTO_Shared_" + Util.getUniqueName()
        self.webapp_settings.generalSettingsSecondaryNav("Channels")
        channel_details = {
            "title": channel1_name,
            "tags": "pir:vln-attn",
            "sharing": ["Global", "Organization"]
        }
        self.webapp_settings.createNewChannel(channel_details)
        self.webapp_settings1.generalSettingsSecondaryNav("Channels")
        self.webapp_settings1.navigateToSharedChannel()
        expect(self.webapp_settings1.verifyChannelPresent(channel1_name)).to(be_true)

    @allure.title("Validate that user is able to add the shared channels to user's my channel by clicking on Add to my "
            "channel button")
    def test_add_shared_channel_to_my_channel(self):
        channel2_name = "CSAP_AUTO_Shared_"+Util.getUniqueName()
        self.webapp_settings.generalSettingsSecondaryNav("Channels")
        self.webapp_settings.navigateToMyChannel()
        channel_details = {
            "title": channel2_name,
            "tags": "pir:vln-attn",
            "sharing": ["Global", "Organization"]
        }
        self.webapp_settings.createNewChannel(channel_details)
        self.webapp_driver1.refresh()
        self.webapp_settings1.navigateToSharedChannel()
        self.webapp_settings1.addToMyChannel(channel2_name)
        self.webapp_settings1.navigateToMyChannel()
        expect(self.webapp_settings1.verifyChannelPresent(channel2_name)).to(be_true)

    @allure.title("Validate that category selection is enabled only when 'Allow Category Selection' flag is ON in Dashboard")
    def test_category_selection_flag_member_portal(self):
        category_name = "CSAP_AUTO_Category_"+Util.getUniqueName()
        category_details = {
            "is_editable": True,
            "is_active": True,
            "use_default_image": True,
            "is_image_uploaded": None,
            "is_disabled": True,
            "category_name": category_name,
            "show_in_intel_submission": True
        }
        self.categories_api.create_new_category(category_details)
        category1_name = "CSAP_AUTO_Category1_"+Util.getUniqueName()
        category1_details = {
            "is_editable": True,
            "is_active": True,
            "use_default_image": True,
            "is_image_uploaded": None,
            "is_disabled": False,
            "category_name": category1_name,
            "show_in_intel_submission": True
        }
        self.categories_api.create_new_category(category1_details)
        self.webapp_settings.generalSettingsSecondaryNav("Alert Categories")
        expect(self.webapp_settings.verfiyCategoryEditable(category_name)).to(be_false)
        expect(self.webapp_settings.verfiyCategoryEditable(category1_name)).to(be_true)

    @allure.title("Validate that user is able to set the preferences for available categories.")
    def test_set_preferences_for_categories(self):
        category1_name = "CSAP_AUTO_Category1_"+Util.getUniqueName()
        category1_details = {
            "is_editable": True,
            "is_active": True,
            "use_default_image": True,
            "is_image_uploaded": None,
            "is_disabled": False,
            "category_name": category1_name,
            "show_in_intel_submission": True
        }
        self.categories_api.create_new_category(category1_details)
        self.webapp_settings.generalSettingsSecondaryNav("Alert Categories")
        self.webapp_driver.refresh()
        self.webapp_settings.enableCategory(category1_name)
        expect(self.webapp_settings.verifyCategoryStatus(category1_name)).to(be_true)
        pdb.set_trace()
        self.webapp_settings.disableCategory(category1_name)
        expect(self.webapp_settings.verifyCategoryStatus(category1_name)).to(be_false)

    @pytest.mark.debug
    @allure.title("Validate that user is able to edit crisis profile and add his contact number in the webapp.")
    def test_crisis_profile_update(self):
        crisis_profile_data = {
                    'start_time':'08:00',
                    'end_time':'17:00',
                    'time_zone':'Chennai, Kolkata, Mumbai',
                    'voice_preference':'John',
                    'contact_info':[{
                        'code':'+91',
                        'number':'123445666',
                        'send_sms':True
                    },
                    {
                        'code':'+91',
                        'number':'1212313113',
                        'send_sms':True
                    },
                    {
                        'code':'+91',
                        'number':'123456789',
                        'send_sms':False
                    }]
                    }
        self.webapp_settings.edit_crisis_profile(crisis_profile_data)
        expect(self.webapp_settings.verify_add_contact_button_present()).to(be_false)
        expect(self.webapp_settings.verify_call_priority_dropdwon(3,4)).to(be_true)
        call_priority_info = [{
            "business_hours":"123445666",
            "after_business_hours":"1212313113",
            "weekend":"123456789"
        },
        {
            "business_hours":"1212313113",
            "after_business_hours":"123456789",
            "weekend":"123445666"
        },
        {
            "business_hours":"123456789",
            "after_business_hours":"123445666",
            "weekend":"1212313113"
        }]
        self.webapp_settings.fill_call_priority_dropdown(call_priority_info)
        expect(self.webapp_settings.selected_call_priority_value(0,1)).to(equal("123445666"))
        expect(self.webapp_settings.selected_call_priority_value(0,2)).to(equal("1212313113"))
        expect(self.webapp_settings.selected_call_priority_value(0,3)).to(equal("123456789"))
        expect(self.webapp_settings.selected_call_priority_value(1,1)).to(equal("1212313113"))
        expect(self.webapp_settings.selected_call_priority_value(1,2)).to(equal("123456789"))
        expect(self.webapp_settings.selected_call_priority_value(1,3)).to(equal("123445666"))
        expect(self.webapp_settings.selected_call_priority_value(2,1)).to(equal("123456789"))
        expect(self.webapp_settings.selected_call_priority_value(2,2)).to(equal("123445666"))
        expect(self.webapp_settings.selected_call_priority_value(2,3)).to(equal("1212313113"))
        self.webapp_settings.clear_all_contact_info()