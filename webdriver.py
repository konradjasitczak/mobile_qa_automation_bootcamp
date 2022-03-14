from appium import webdriver


class WebCommon:
    def __init__(self, apk_name):
        self.driver = None
        self.init_driver(apk_name)

    def init_driver(self, apk_name):
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "7"
        desired_caps["deviceName"] = "Android_Emulator"
        if apk_name == "filemanager":
            desired_caps["app"] = "C:\\Users\\Konrad\\PycharmProjects\\mobile_qa_automation_bootcamp\\app" \
                                  "\\filemanager.apk "
        else:
            desired_caps["app"] = 'C:\\Users\\Konrad\\PycharmProjects\\mobile_qa_automation_bootcamp\\app\\theapp.apk'
        desired_caps["autoGrantPermissions"] = "true"
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def get_driver(self):
        return self.driver

    def close_driver(self):
        self.driver.quit()
