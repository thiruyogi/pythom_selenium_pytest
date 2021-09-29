import pdb

from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.Custom_Logger as cl
from selenium.webdriver import ActionChains
import time


class SeleniumDriver():
    log = cl.customLogger()
    def __init__(self, driver):
        self.driver = driver

    def getElement(self, locator):
        element = None
        try:
            element = self.driver.find_element(*locator)
            self.log.info("Element Found with locator: " + locator[1])
        except:
            self.log.info("Element not found with locator: " + locator[1])
        return element

    def getElementList(self, locator):
        """
        Get list of elements
        """
        elements = self.driver.find_elements(*locator)
        if len(elements) > 0:
            self.log.info("Element list FOUND with locator: " + locator[1])
        else:
            self.log.info("Element list NOT FOUND with locator: " + locator[1])
        return elements

    def elementClick(self, locator):
        try:
            element = self.getElement(locator)
            element.click()
            self.log.info("Clicked on element with locator: " + locator[1])
        except:
            self.log.info("Cannot click on the element with locator: " + locator[1])
            print_stack()

    def sendKeys(self, data, locator):
        try:
            element = self.getElement(locator)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator[1])
        except:
            self.log.info("Cannot send data on the element with locator: " + locator[1])
            print_stack()

    def clearField(self, locator):
        element = self.getElement(locator)
        while len(element.get_attribute("value")) > 0:
            element.send_keys(Keys.BACK_SPACE)
        time.sleep(1)

    def getText(self, locator):
        """
        NEW METHOD
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            element = self.getElement(locator)
            text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + locator[1])
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + locator[1])
            print_stack()
            text = None
        return text

    def clearSendKeys(self, data, locator):
        try:
            self.clearField(locator)
            self.sendKeys(data, locator)
            self.log.info("Sent data on element with locator: " + locator[1])
        except:
            self.log.info("Cannot send data on the element with locator: " + locator[1])
            print_stack()

    def isElementPresent(self, locator):
        try:
            elements = self.getElementList(locator)
            if len(elements) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def isElementDisplayed(self, locator):
        """
        Check if element is displayed
        provide locator tuple as parameter
        """
        isDisplayed = False
        try:
            element = self.getElement(locator)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed")
            else:
                self.log.info("Element not displayed")
            return isDisplayed
        except:
            print("Element not found")
            return False

    def waitForElement(self, locator,
                       timeout=10, pollFrequency=0.5):
        element = None
        try:
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable(*locator))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def getCurrentUrl(self):
        return self.driver.current_url

    def mouseOverElemenet(self, locator):
        try:
            element = self.getElement(locator)
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            self.log.info("Hovered Over element with locator: " + locator[1])
        except:
            self.log.info("Not able to hover on the element")
            print_stack()

    def scrollToElement(self, locator):
        """
        :param locator:
        :return:
        """
        try:
            element = self.getElement(locator)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            self.log.info(" Scroll to element " + locator[1])
        except:
            print(" Cannot scroll to element " + locator[1])
            print_stack()

    def webScroll(self, direction="up"):
        """
        NEW METHOD
        """
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -800);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 800);")

    def getTexts(self, locator):
        texts = []
        elements = self.getElementList(locator)
        for element in elements:
            text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
                texts.append(text)
            if len(text) != 0:
                self.log.info("Getting text on element :: " + locator[1])
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
                texts.append(text)
        return texts

    def getElementAttributeValue(self, locator, attribute, element=None):
        """
        Get value of the attribute of element
        Parameters:
            1. Required:
                1. attribute - attribute whose value to find
            2. Optional:
                1. element   - Element whose attribute need to find
                2. locator   - Locator of the element
                3. locatorType - Locator Type to find the element
        Returns:
            Value of the attribute
        Exception:
            None
        """
        if locator:
            element = self.getElement(locator)
        value = element.get_attribute(attribute)
        return value

    def isEnabled(self, locator, info=""):
        """
        Check if element is enabled

        Parameters:
            1. Required:
                1. locator - Locator of the element to check
            2. Optional:
                1. locatorType - Type of the locator(id(default), xpath, css, className, linkText)
                2. info - Information about the element, label/name of the element
        Returns:
            boolean
        Exception:
            None
        """
        element = self.getElement(locator)
        enabled = False
        try:
            attributeValue = self.getElementAttributeValue(locator=locator,attribute="disabled")
            if attributeValue is not None:
                enabled = element.is_enabled()
            else:
                value = self.getElementAttributeValue(locator=locator, attribute="class")
                self.log.info("Attribute value From Application Web UI --> :: " + value)
                enabled = not ("disabled" in value)
            if enabled:
                self.log.info("Element :: '" + info + "' is enabled")
            else:
                self.log.info("Element :: '" + info + "' is not enabled")
        except:
            self.log.error("Element :: '" + info + "' state could not be found")
        return enabled

    # All the methods below are specific to CSAP

    def enableToggle(self, locator):
        if (self.getElementAttributeValue(locator=locator,attribute='class'))=='el-switch':
            self.elementClick(locator)
    
    def disableToggle(self, locator):
        if (self.getElementAttributeValue(locator=locator,attribute='class'))=='el-switch is-checked':
            self.elementClick(locator)

    def getToggleStatus(self, locator):
        value = self.getElementAttributeValue(locator=locator,attribute='class')
        if value == 'el-switch is-checked':
            return True
        else:
            return False

    def selectDropdown(self,locator,value):
        search_input_tag = (By.XPATH,"//input[@placeholder='Search ...']")
        value_to_select = (By.XPATH,"//div[contains(@class,'cy-select-menu-option-label')][contains(text(),'{0}')]".format(value))
        self.elementClick(locator)
        if self.isElementPresent(search_input_tag):
            self.clearSendKeys(value,search_input_tag)
        self.elementClick(value_to_select)


