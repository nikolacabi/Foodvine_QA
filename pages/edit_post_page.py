from appium.webdriver import webdriver
from time import sleep
from pages.page import Page
from datetime import datetime


class EditPostPageAndroid(Page):
    # def __init__(self, driver):
    #     super().__init__(driver)

    driver: webdriver = None

    PAGE_TITLE_XPATH = "//*[@text='New Post']"

    POST_TITLE_XPATH = "//*[@text='Required' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[@text='Post title']]]"

    POST_CAPTION_XPATH = "//*[@text='Required' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[@text='Post caption']]]"

    ADD_TAGS_XPATH = "//*[@text='Add tags (optional)']"

    PREVIEW_BUTTON_XPATH = "//*[@text='Preview']"


class FeedPageiOS(Page):
    # def __init__(self, driver):
    #     super().__init__(driver)

    driver: webdriver = None

