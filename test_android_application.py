import pytest
import logging
import time

from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from webdriver import WebCommon
from appium.webdriver.webdriver import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

log = logging.getLogger()
log.setLevel(logging.INFO)


class Test01Android:
    @classmethod
    def setup_class(cls):
        log.info("setup_class")

    def setup_method(self, method):
        log.info("setup_method")
        log.info(method.__name__)
        # if
        apk_name = "theapp"
        # else:
        #     apk_name = "filemanager"
        self.webcommon = WebCommon(apk_name)
        self.driver = self.webcommon.get_driver()

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
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'List Demo').click()
        #self.driver.find_elements_by_xpath(f"//*[@text='List Demo']")
        self.driver.implicitly_wait(1)
        try:
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Cirrus')
        except NoSuchElementException:
            return False
        return True
        #self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Cirrus').size != 0

    def test_06_send_keys(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Echo Box').click()
        self.driver.implicitly_wait(1)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'messageInput').send_keys("Hello World")
        self.driver.implicitly_wait(1)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'messageSaveBtn').click()
        self.driver.implicitly_wait(1)
        log.info("Check 'Hello World' is printed")
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Hello World')

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

    def test_08_scroll(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'List Demo').click()
        self.driver.implicitly_wait(1)
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(570, 1344)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(579, 512)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        log.info("Check last item is available")
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Stratus')
