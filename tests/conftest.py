import pytest
from base.webdriver_factory import WebDriverFactory
from pytest_testconfig import config
import configparser
import os
import time
import sys

webapp_driver = None


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")
    parser.addoption("--base_url", action="store", default="https://verify.cywarestg.com/webappv3/auth/login")

@pytest.fixture(scope="class")
def one_time_setup(request):
    global webapp_driver
    browser = request.config.getoption("browser_name")
    webappUrl = config["APP_SETTINGS"]["WEBAPP_URL"]
    dashboardUrl = config["APP_SETTINGS"]["DASHBOARD_URL"]
    wd = WebDriverFactory(browser, webappUrl)
    webapp_driver = wd.getWebDriverInstance()
    request.cls.webapp_driver = webapp_driver
    request.cls.browser = browser
    request.cls.webappUrl = webappUrl
    request.cls.dashboardUrl= dashboardUrl
    yield
    webapp_driver.quit()


@pytest.fixture(scope="class")
def demo_setup():
    print("This is from conftest fixture")


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    webapp_driver.get_screenshot_as_file(name)
