from appium.webdriver import webdriver
from time import sleep
from pages.page import Page
from datetime import datetime


class AccountDetailsPageAndroid(Page):
    # def __init__(self, driver):
    #     super().__init__(driver)

    driver: webdriver = None

    PAGE_TITLE_XPATH = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView"

    FIRST_NAME_XPATH = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[1]"

    LAST_NAME_XPATH = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[2]"

    PHONE_XPATH = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[3]"

    EMAIL_XPATH = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[4]"

    USERNAME_XPATH = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[5]"

    PASSWORD_XPATH = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[6]"

    CONTINUE_BUTTON_XPATH = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[7]/android.widget.Button"


    # def check_page_title(self):
    #     assert self.find_xpath(self.PAGE_TITLE_XPATH).is_displayed()
    #     assert self.find_xpath(self.PAGE_TITLE_XPATH).text == "Account details"

    # def input_first_name(self, first_name):
    #     self.find_xpath(self.FIRST_NAME_XPATH).send_keys(first_name)
    #
    # def input_last_name(self, last_name):
    #     self.find_xpath(self.LAST_NAME_XPATH).send_keys(last_name)
    #
    # def input_phone(self, phone):
    #     #self.find_xpath(self.PHONE_XPATH).click()
    #     #sleep(1)
    #     self.find_xpath(self.PHONE_XPATH).send_keys(phone)
    #
    # def un_email_gen(self):
    #     un = 'testnikola' + datetime.now().strftime("%d%m%Y%H%M%S")
    #     email = un + "@gmail.com"
    #     return un,email
    #
    # def input_email(self, email):
    #     self.find_xpath(self.EMAIL_XPATH).send_keys(email)
    #
    # def input_username(self, username):
    #     self.find_xpath(self.USERNAME_XPATH).send_keys(username)
    #
    # def input_password(self, password):
    #     self.find_xpath(self.PASSWORD_XPATH).send_keys(password)

    # def click_continue(self):
    #     self.find_xpath(self.CONTINUE_BUTTON_XPATH).click()



class AccountDetailsPageiOS(Page):
    # def __init__(self, driver):
    #     super().__init__(driver)

    driver: webdriver = None

    PAGE_TITLE_XPATH = "//*[@text='Account details']"

    FIRST_NAME_XPATH = "//*[@class='UIATextField' and ./parent::*[./parent::*[./parent::*[./parent::*[./parent::*[@text='First name']]]]]]"

    LAST_NAME_XPATH = "//*[@class='UIATextField' and ./parent::*[./parent::*[./parent::*[./parent::*[./parent::*[@text='Last name']]]]]]"

    PHONE_XPATH = "(//*[@text='First name Last name Phone number US phone number only Email address Username Password Min. 8 characters and 1 number Continue By creating an account you agree to the  terms']/*/*/*/*/*[@class='UIATextField'])[1]"

    EMAIL_XPATH = "(//*[@text='First name Last name Phone number US phone number only Email address Username Password Min. 8 characters and 1 number Continue By creating an account you agree to the  terms']/*/*/*/*/*[@class='UIATextField'])[2]"

    USERNAME_XPATH = "(//*[@text='First name Last name Phone number US phone number only Email address Username Password Min. 8 characters and 1 number Continue By creating an account you agree to the  terms']/*/*/*/*/*[@class='UIATextField'])[3]"

    PASSWORD_XPATH = "//*[@class='UIAView' and ./parent::*[@class='UIAView' and ./parent::*[@class='UIAView' and ./parent::*[@class='UIAView' and ./parent::*[@class='UIAView' and ./parent::*[@text='First name Last name Phone number US phone number only Email address Username Password Min. 8 characters and 1 number Continue By creating an account you agree to the  terms']]] and (./preceding-sibling::* | ./following-sibling::*)[@class='UIAView']]]]"

    CONTINUE_BUTTON_XPATH = "//*[@class='UIAButton']"
