from appium import webdriver
from time import sleep

def setup():

    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '11'
    desired_caps['deviceName'] = 'Pixel_3a_API_30_x86'
    desired_caps['app'] = 'C:/Users/Nikola/Desktop/Foodvine/APKs/bitrise/app-release-bitrise-signed.apk'
    desired_caps['noResetValue'] = 'false'

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    sleep(7)

    return driver


def setup_no_app():

    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '11'
    desired_caps['deviceName'] = 'Pixel_3a_API_30_x86'
    desired_caps['noResetValue'] = 'false'

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    sleep(7)

    return driver