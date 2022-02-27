from appium import webdriver


class WebCommon:
    def __init__(self, apk_name):
        self.apk_name = apk_name
        self.driver = None

    def init_driver(self):
        self.driver = self.get_driver()

    def get_driver(self):
        desired_caps = {
            "platformName": "",
            "appPackage": "",
            "appActivity": "",
        }

        return webdriver.Remote('localhost', desired_caps)

    def close_driver(self):
        self.driver.quit()
