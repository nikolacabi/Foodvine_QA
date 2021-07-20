from appium import webdriver
from time import sleep

def setup_with_app():

    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '11'
    desired_caps['deviceName'] = 'Pixel_3a_API_30_x86'
    desired_caps['app'] = 'C:/Users/Nikola/Desktop/Foodvine/APKs/bitrise/app-release-bitrise-signed.apk'
    desired_caps['noResetValue'] = 'false'
    desired_caps['newCommandTimeout'] = 300

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    sleep(7)

    return driver


def setup_no_app():

    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '11'
    desired_caps['deviceName'] = 'Pixel_3a_API_30_x86'
    desired_caps['noResetValue'] = 'false'
    desired_caps['newCommandTimeout'] = 150

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    sleep(7)

    return driver



def setup_with_app_cloud_ios():

    dc={}
    dc['reportDirectory'] = 'reports'
    dc['reportFormat'] = 'xml'
    dc['testName'] = 'Quick Start iOS NATIVE Demo'
    dc['accessKey'] = "eyJhbGciOiJIUzI1NiJ9.eyJ4cC51IjoxMjIyNzE3MiwieHAucCI6MTIyMjcxNzEsInhwLm0iOjE2MjY3MjY3MjU3NzgsImV4cCI6MTk0MjA4Njc1MSwiaXNzIjoiY29tLmV4cGVyaXRlc3QifQ.19J9dqE5S8dWBtFVH7RFHiWNPcGnrmzMbfxJz0sKlFc"
    dc['app'] = 'cloud:com.foodvine'
    dc['platformName'] = 'ios'
    # dc['deviceName'] = "IPhone 11 Pro IO-UK 06"
    # dc['deviceName'] = "IPhone SE IO-DE 39"
    dc['deviceName'] = "iPhone 11 pro IO-UK 10"
    driver = webdriver.Remote("https://cloud.seetest.io/wd/hub", dc)

    return driver
