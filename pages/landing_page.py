from appium.webdriver import webdriver
from time import sleep
from pages.page import Page


class LandingPageAndroid(Page):
    # def __init__(self, driver):
    #     super().__init__(driver)

    driver: webdriver = None

    CAROUSEL_TEXT_XPATH = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[1]"

    JOIN_FOR_FREE_BUTTON_XPATH = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[2]/android.widget.Button"

    START_EXPLORING_NEW_FLAVOURS_POPUP_XPATH = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup"

    SIGN_UP_WITH_EMAIL_BUTTON_XPATH = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.Button"

    ALLREADY_HAVE_AN_ACCOUNT_BUTTON_XPATH = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[3]/android.widget.Button"


    # def click_signup_emial(self):
    #     self.find_xpath(self.SIGN_UP_WITH_EMAIL_BUTTON_XPATH).click()

    # def click_join_for_free(self):
    #     self.find_xpath(self.JOIN_FOR_FREE_BUTTON_XPATH).click()
    #     sleep(2)
    #     assert self.find_xpath(self.START_EXPLORING_NEW_FLAVOURS_POPUP_XPATH).is_displayed()

    def swipe_right_to_left(self):
        self.driver.swipe(start_x=1000, start_y=1000, end_x=50, end_y=1000, duration=200)



class LandingPageiOS(Page):

    driver: webdriver = None

    CAROUSEL_TEXT_XPATH = "//*[@text='Authentic food from local farmers and home chefs']"

    JOIN_FOR_FREE_BUTTON_XPATH = "//*[@text='Join for free' and @class='UIAButton']"

    # START_EXPLORING_NEW_FLAVOURS_POPUP_XPATH =

    SIGN_UP_WITH_EMAIL_BUTTON_XPATH = "//*[@text='Sign up with email' and @class='UIAButton']"

    ALLREADY_HAVE_AN_ACCOUNT_BUTTON_XPATH = "//*[@text='Already have an account?' and @class='UIAButton']"

    def swipe_right_to_left(self):
        self.driver.swipe(start_x=1000, start_y=1000, end_x=50, end_y=1000, duration=200)