from appium.webdriver import webdriver
from time import sleep
from pages.page import Page
from datetime import datetime


class PreviewPostPageAndroid(Page):
    # def __init__(self, driver):
    #     super().__init__(driver)

    driver: webdriver = None

    PAGE_TITLE_XPATH = "//*[@text='Preview post']"

    POST_BUTTON_XPATH = "//*[@class='android.widget.Button' and ./*[@text='Post']]"



class FeedPageiOS(Page):
    # def __init__(self, driver):
    #     super().__init__(driver)

    driver: webdriver = None

