from appium.webdriver import webdriver
from time import sleep
from pages.page import Page
from datetime import datetime


class FeedPageAndroid(Page):
    # def __init__(self, driver):
    #     super().__init__(driver)

    driver: webdriver = None

    # PAGE_TITLE_XPATH =  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView[1]"

    FEED_XPATH = "//*[@text='Feed']"

    DISCOVER_XPATH = "//*[@text='Discover']"

    ORDERS_XPATH = "//*[@text='Orders']"

    PROFILE_XPATH = "//*[@text='Profile']"

    MY_STORE_XPATH = "//*[@text='My Store']"

    PLUS_BUTTON_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and (./preceding-sibling::* | ./following-sibling::*)[@class='androidx.viewpager.widget.ViewPager']]/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']])[1]"

    ALLOW_ACCESS_XPATH = "//*[@text='Allow Foodvine to access photos, media, and files on your device?']"

    ALLOW_XPATH = "//*[@text='Allow']"

    DENY_XPATH = "//*[@id='permission_deny_button']"

    POST_TITLE_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.ImageView']]/*[@text])[1]"

    POST_CAPTION_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.ImageView']]/*[@text])[2]"

    POST_CREATOR_XPATH = "((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.ImageView']]/*[@class='android.view.ViewGroup'])[1]/*[@text])[1]"


class FeedPageiOS(Page):
    # def __init__(self, driver):
    #     super().__init__(driver)

    driver: webdriver = None

    PAGE_TITLE_XPATH = ""

    FEED_XPATH = "//*[@text='Feed']"

    DISCOVER_XPATH = "//*[@text='Discover']"

    ORDERS_XPATH = "//*[@text='Orders']"

    PROFILE_XPATH = "//*[@text='Profile']"

    MY_STORE_XPATH = "//*[@text='My Store']"

    PLUS_BUTTON_XPATH = '''((//*[@text="'" and ./parent::*[@text="'"]]/*[@class='UIAView'])[3]/*[@class='UIAView'])[1]'''

    ALLOW_ACCESS_XPATH = "//*[@text='Allow Foodvine to access photos, media, and files on your device?']"

    ALLOW_XPATH = "//*[@text='Allow Access to All Photos']"

    DENY_XPATH = "//*[@text='Don’t Allow']"

    POST_TITLE_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.ImageView']]/*[@text])[1]"

    POST_CAPTION_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.ImageView']]/*[@text])[2]"

    POST_CREATOR_XPATH = "((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.ImageView']]/*[@class='android.view.ViewGroup'])[1]/*[@text])[1]"



