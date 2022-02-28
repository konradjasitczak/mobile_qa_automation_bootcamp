import pytest
import logging
from appium import webdriver

class WebCommon:
    def __init__(self, apk_name):
        self.apk_name = apk_name
        self.driver = None

    def init_driver(self):
        desired_caps = {
            "platformName": "",
            "appPackage": "",
            "appActivity": "",
        }

        self.driver = webdriver.Remote('localhost', desired_caps)

    def get_driver(self):
        return self.driver

    def close_driver(self):
        self.driver.quit()