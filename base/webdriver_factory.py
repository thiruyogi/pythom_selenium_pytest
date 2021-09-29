"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class WebDriverFactory():

    def __init__(self, browser, baseUrl):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser.lower()
        self.baseUrl = baseUrl

    """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie(IEDriverManager().install())
        elif self.browser == "firefox":
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif self.browser == "chrome":
            # Set chrome driver
            driver = webdriver.Chrome(ChromeDriverManager().install())
        else:
            driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(10)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(self.baseUrl)
        return driver
