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

    POST_TITLE_XPATH =  "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.ImageView']]/*[@text])[2]"
    # POST_TITLE_XPATH =  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[1]"

    POST_CAPTION_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.ImageView']]/*[@text])[3]"
    # POST_CAPTION_XPATH =    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[2]"



class FeedPageiOS(Page):
    # def __init__(self, driver):
    #     super().__init__(driver)

    driver: webdriver = None

