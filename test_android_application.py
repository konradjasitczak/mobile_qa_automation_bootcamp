import pytest
import logging
from webdriver import WebCommon


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
