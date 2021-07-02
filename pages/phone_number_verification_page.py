from lxml import html
import requests
from appium.webdriver import webdriver
from time import sleep
from pages.page import Page
from datetime import datetime


class PhoneNumberVerificationPage(Page):
    # def __init__(self, driver):
    #     super().__init__(driver)

    driver: webdriver = None

    PAGE_TITLE_XPATH =              "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView"
    PAGE_TITLE_PW_CHANGE_XPATH =    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView"


    SMS_CODE_INPUT =            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText"
    SMS_CODE_PW_CHANGE_INPUT =  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText"

    # def check_page_title(self):
    #     assert self.find_xpath(self.PAGE_TITLE_XPATH).is_displayed()
    #     assert self.find_xpath(self.PAGE_TITLE_XPATH).text == "Phone number verification"


    # def input_sms_code(self, sms_code):
    #     self.find_xpath(self.SMS_CODE_INPUT).send_keys(sms_code)


    # def get_sms_code(self):
    #
    #     page = requests.get('https://www.receivesms.org/us-number/3456/')
    #     tree = html.fromstring(page.content)
    #
    #     self.sms_code = ['0000']
    #
    #     for i in range(1, 10):
    #
    #         try:
    #
    #             self.sms_text = tree.xpath('/html/body/section/div/div/div/div[4]/div[' + str(i * 3) + ']/text()')
    #             time_received = tree.xpath('/html/body/section/div/div/div/div[4]/div[' + str(i * 3 - 1) + ']/div/text()')
    #
    #             if self.sms_text == ['Sent from your Twilio trial account - Welcome to Phone Verify! Please use security code ', ' to proceed.'] and time_received[0].endswith('sec ago'):
    #                 self.sms_code = tree.xpath('/html/body/section/div/div/div/div[4]/div[' + str(i * 3) + ']/span/b/text()')
    #                 break
    #
    #         except:
    #             continue
    #
    #     return self.sms_code