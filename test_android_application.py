import pytest
import logging
import time

from webdriver import WebCommon
from appium.webdriver.webdriver import AppiumBy

log = logging.getLogger()
log.setLevel(logging.INFO)


class Test01Android:
    @classmethod
    def setup_class(cls):
        log.info("setup_class")

    def setup_method(self, method):
        log.info("setup_method")
        log.info(method.__name__)
        apk_name = "theapp"
        self.webcommon = WebCommon(apk_name)
        self.driver = self.webcommon.get_driver()
        apk_filemanager = "filemanager"
        self.webcommon2 = WebCommon(apk_filemanager)
        self.filemanager = self.webcommon2.get_driver()

    def get_element_by_text(self, text):
        return self.driver.find_element_by_xpath(f"//*[@text=\"{text}\"]")

    def teardown_method(self):
        log.info("teardown_method")
        self.webcommon.close_driver()

    @classmethod
    def teardown_class(cls):
        log.info("teardown_class")

    @pytest.mark.parametrize('os', ['android'])
    def test_01_parametrization(self, os):
        log.info(f"mark value is {os}")

    @pytest.mark.xfail(reason="Unable to execute test")
    def test_02_xfail(self):
        print("Execute test case 2")

    @pytest.mark.skip(reason="Unable to execute test")
    def test_03_skip(self):
        print("Execute test case 3")

    def test_04_list_length(self):
        list_elements = self.driver.find_elements_by_xpath(
            "//android.widget.FrameLayout[@resource-id='android:id/content']"
            "//android.widget.FrameLayout/android.view.ViewGroup/*[@class='android.view.ViewGroup']")

        log.info(f'List size: {len(list_elements)}, expected: 7')
        assert len(list_elements) == 7, "list length is not 7"

    def test_05_text(self):
        self.get_element_by_text("List Demo").click()
        self.driver.implicitly_wait(1)
        log.info("Check if Cirrus element exists")
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Cirrus')

    def test_06_send_keys(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Echo Box').click()
        self.driver.implicitly_wait(1)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'messageInput').send_keys("Hello World")
        self.driver.implicitly_wait(1)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'messageSaveBtn').click()
        self.driver.implicitly_wait(1)
        log.info("Check 'Hello World' is printed")
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Hello World')

    def test_07_wait(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'List Demo').click()
        log.info("Wait 10 seconds")
        timeout = 10
        timeout_start = time.time()
        while time.time() < timeout_start + timeout:
            test = 0
            if test == 10:
                break
            test -= 1
        log.info("Check Cirrus element is present")
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Cirrus')

    def test_08_scroll(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'List Demo').click()
        self.driver.implicitly_wait(1)
        self.driver.swipe(0, 1344, 0, 512)
        log.info("Check last item is available")
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Stratus')
