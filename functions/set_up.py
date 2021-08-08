from appium import webdriver
from time import sleep


ACCESS_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJ4cC51IjoxMjM1OTk4NCwieHAucCI6MTIzNTk5ODMsInhwLm0iOjE2Mjc5MjQzNDM5MjAsImV4cCI6MTk0MzI4NDQ3MCwiaXNzIjoiY29tLmV4cGVyaXRlc3QifQ.-sEUFN3Tovaj_qRCyShLa8ZD0cPYTsajz04SQbPqsE0"


def setup_with_app_local(phone):

    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '11'
    desired_caps['deviceName'] = phone
    desired_caps['app'] = 'C:/Users/Nikola/Desktop/Foodvine/APKs/bitrise/app-release-bitrise-signed.apk'
    desired_caps['noResetValue'] = 'false'
    desired_caps['newCommandTimeout'] = 300

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    sleep(7)

    return driver


def setup_no_app_local(phone):

    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '11'
    desired_caps['deviceName'] = phone
    desired_caps['noResetValue'] = 'false'
    desired_caps['newCommandTimeout'] = 150

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    sleep(7)

    return driver



def setup_with_app_cloud_ios(phone, access_key = ACCESS_KEY):

    dc={}
    dc['reportDirectory'] = 'reports'
    dc['reportFormat'] = 'xml'
    dc['testName'] = 'Quick Start iOS NATIVE Demo'
    dc['accessKey'] = access_key
    dc['app'] = 'cloud:com.foodvine'
    dc['platformName'] = 'ios'
    dc['deviceName'] = phone
    driver = webdriver.Remote("https://cloud.seetest.io/wd/hub", dc)

    return driver


def setup_with_no_app_cloud_ios(phone, access_key = ACCESS_KEY):

    dc={}
    dc['reportDirectory'] = 'reports'
    dc['reportFormat'] = 'xml'
    dc['testName'] = 'Quick Start iOS NATIVE Demo'
    dc['accessKey'] = access_key
    dc['platformName'] = 'ios'
    dc['deviceName'] = phone
    driver = webdriver.Remote("https://cloud.seetest.io/wd/hub", dc)

    return driver


def setup_with_app_cloud_android(phone, access_key = ACCESS_KEY):

    dc={}
    dc['reportDirectory'] = 'reports'
    dc['reportFormat'] = 'xml'
    dc['testName'] = 'Quick Start Android NATIVE Demo'
    dc['accessKey'] = access_key
    dc['app'] = 'cloud:com.foodvine/.MainActivity'
    dc['platformName'] = 'Android'
    dc['deviceName'] = phone
    dc['newCommandTimeout'] = 300
    driver = webdriver.Remote("https://cloud.seetest.io/wd/hub", dc)

    return driver