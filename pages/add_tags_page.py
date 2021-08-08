from appium.webdriver import webdriver
from time import sleep
from pages.page import Page
from datetime import datetime


class AddTagsPageAndroid(Page):
    # def __init__(self, driver):
    #     super().__init__(driver)

    driver: webdriver = None

    PAGE_TITLE_XPATH = "//*[@text='Add tags']"

    INPUT_XPATH =   "//*[@class='android.widget.EditText']"

    TAG_1_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]]/*[./*[@class='android.view.ViewGroup' and ./*[@class='android.widget.TextView']]])[1]"
    TAG_2_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]]/*[./*[@class='android.view.ViewGroup' and ./*[@class='android.widget.TextView']]])[2]"
    TAG_3_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]]/*[./*[@class='android.view.ViewGroup' and ./*[@class='android.widget.TextView']]])[3]"


    SAVE_BUTTON_XPATH = "//*[@text='Save']"


class AddTagsPageiOS(Page):
    # def __init__(self, driver):
    #     super().__init__(driver)

    driver: webdriver = None

    PAGE_TITLE_XPATH = "//*[@text='Add tags']"

    INPUT_XPATH =   "//*[@text='Search tags to add']"

    # TAG_1_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]]/*[./*[@class='android.view.ViewGroup' and ./*[@class='android.widget.TextView']]])[1]"
    # TAG_2_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]]/*[./*[@class='android.view.ViewGroup' and ./*[@class='android.widget.TextView']]])[2]"
    # TAG_3_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]]/*[./*[@class='android.view.ViewGroup' and ./*[@class='android.widget.TextView']]])[3]"

    SAVE_BUTTON_XPATH = "//*[@text='Save']"