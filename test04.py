from appium import webdriver
from selenium.webdriver.common.by import By
import logging

log = logging.getLogger()
log.setLevel(logging.INFO)

def setup():
    desired_caps = {}
    desired_caps["platformName"] = "Android"
    desired_caps["deviceName"] = "Amdroid_Emulator"
    desired_caps["appPackage"] = "io.cloudgrey.the_app"
    desired_caps["appActivity"] = "io.cloudgrey.the_app.MainActivity"

    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

def test_04():
    driver = setup()

    list_elements = driver.find_elements(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup')
    list_length = len(list_elements)

    driver.quit()

    assert list_length == 7
    log.info('List size: ' + str(list_length) + ', expected: 7')