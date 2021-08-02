from appium.webdriver import webdriver
from time import sleep
from pages.page import Page
from datetime import datetime


class NewPostPageAndroid(Page):
    # def __init__(self, driver):
    #     super().__init__(driver)

    driver: webdriver = None

    PAGE_TITLE_XPATH = "//*[@text='New Post']"

    SELECT_MULTIPLE_XPATH = "//*[@text='Select multiple']"

    MEDIA_1_XPATH = "((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[1]/*/*/*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']])[1]"

    MEDIA_2_XPATH = "((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[1]/*/*/*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']])[2]"

    MEDIA_3_XPATH = "((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[1]/*/*/*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']])[3]"

    NEXT_BUTTON_XPATH = "// *[ @ text = 'Next']"



class FeedPageiOS(Page):
    # def __init__(self, driver):
    #     super().__init__(driver)

    driver: webdriver = None

