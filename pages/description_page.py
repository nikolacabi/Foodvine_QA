from appium.webdriver import webdriver
from time import sleep
from pages.page import Page
from datetime import datetime


class PostDescriptionPageAndroid(Page):
    # def __init__(self, driver):
    #     super().__init__(driver)

    driver: webdriver = None

    PAGE_TITLE_XPATH = "//*[@text='Description']"

    INPUT_FIELD_XPATH = "//*[@class='android.widget.EditText']"

    SAVE_BUTTON_XPATH = "//*[@text='Save']"


class PostDescriptionPageiOS(Page):
    # def __init__(self, driver):
    #     super().__init__(driver)

    driver: webdriver = None

