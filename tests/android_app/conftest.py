import pytest
from appium.options.android import UiAutomator2Options
from selene import browser
import os

from config import settings
from utils import attach


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        "app": "bs://sample.app",

        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            "userName": settings.USER_NAME,
            "accessKey": settings.ACCESS_KEY
        }
    })

    browser.config.driver_remote_url = settings.BROWSERSTACK_URL
    browser.config.driver_options = options

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield
    attach.add_screenshot(browser)

    attach.add_xml(browser)

    session_id = browser.driver.session_id

    attach.add_video(session_id, settings.USER_NAME, settings.ACCESS_KEY)

    browser.quit()