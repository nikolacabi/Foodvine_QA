from appium.webdriver import webdriver
from time import sleep
from pages.page import Page
from datetime import datetime


class InputPageAndroid(Page):
    # def __init__(self, driver):
    #     super().__init__(driver)

    driver: webdriver = None

    PAGE_TITLE_XPATH =  "//*[@text and @class='android.widget.TextView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.view.ViewGroup' and ./*[@class='android.widget.TextView']] and ./parent::*[@class='android.view.ViewGroup']]"

    INPUT_FIELD_XPATH = "//*[@class='android.widget.EditText']"

    SAVE_BUTTON_XPATH = "//*[@text='Save']"


class FeedPageiOS(Page):
    # def __init__(self, driver):
    #     super().__init__(driver)

    driver: webdriver = None

