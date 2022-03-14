import pytest
import logging
import time
import re

from webdriver import WebCommon
from appium.webdriver.webdriver import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException

log = logging.getLogger()
log.setLevel(logging.INFO)


class Test01Android:
    @classmethod
    def setup_class(cls):
        log.info("setup_class")

    def setup_method(self, method):
        log.info("setup_method")
        log.info(method.__name__)
        test_number = int(re.match(f'test_(\d+)', method.__name__).group(1))
        if test_number > 8:
            apk_name = "filemanager"
        else:
            apk_name = "theapp"
        self.webcommon = WebCommon(apk_name)
        self.driver = self.webcommon.get_driver()

    def get_element_by_text(self, text):
        return self.driver.find_element_by_xpath(f"//*[@text=\"{text}\"]")

    def create_folder(self, name):
        self.get_element_by_text('SD card').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(AppiumBy.ID, "android:id/button1").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options').click()
        self.get_element_by_text('New').click()
        self.get_element_by_text('Folder').click()
        self.driver.find_element(AppiumBy.ID, 'com.alphainventor.filemanager:id/file_name').send_keys(name)
        self.driver.find_element(AppiumBy.ID, "android:id/button1").click()
        self.driver.implicitly_wait(1)

    def delete_folder(self):
        actions = TouchAction(self.driver)
        actions.long_press(self.get_element_by_text('test_folder'))
        actions.perform()
        self.driver.implicitly_wait(1)
        self.driver.find_element(AppiumBy.ID, 'com.alphainventor.filemanager:id/bottom_menu_delete').click()
        self.driver.find_element(AppiumBy.ID, 'android:id/button1').click()
        self.driver.implicitly_wait(1)

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

    def test_09_create_folder(self):
        self.create_folder("test_folder")
        log.info("Check if test_folder was created")
        assert self.get_element_by_text('test_folder')

    def test_10_delete_folder(self):
        log.info("Create test_folder")
        self.create_folder("test_folder")
        log.info("Delete test_folder")
        self.delete_folder()
        try:
            self.get_element_by_text('test_folder')
        except NoSuchElementException:
            log.info("Test_folder was deleted")

    def test_11_rename(self):
        log.info("Create test_folder")
        self.create_folder("test_folder")
        log.info("Rename test_folder to secure_folder")
        actions = TouchAction(self.driver)
        actions.long_press(self.get_element_by_text('test_folder'))
        actions.perform()
        self.driver.implicitly_wait(1)
        self.driver.find_element(AppiumBy.ID, 'com.alphainventor.filemanager:id/bottom_menu_rename').click()
        self.driver.find_element(AppiumBy.ID, 'com.alphainventor.filemanager:id/file_name').send_keys("secure_folder")
        self.driver.find_element(AppiumBy.ID, "android:id/button1").click()
        self.driver.implicitly_wait(1)
        log.info("Check if folder was renamed")
        assert self.get_element_by_text('secure_folder')

    def test_12_exception(self):
        log.info("Create test_folder")
        self.create_folder("test_folder")
        log.info("Delete test_folder")
        self.delete_folder()
        log.info("Click on deleted folder")
        try:
            self.get_element_by_text('test_folder')
        except NoSuchElementException:
            log.info("Exception catched")

    def test_13_while(self):
        log.info("Create test_folder")
        self.create_folder("test_folder")
        log.info("Wait 10 seconds")
        timeout = 10
        timeout_start = time.time()
        while time.time() < timeout_start + timeout:
            test = 0
            if test == 10:
                break
            test -= 1
        log.info("Check if test_folder is present")
        assert self.get_element_by_text('test_folder')
