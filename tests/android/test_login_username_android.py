import pytest
from appium import webdriver
from time import sleep
import random
from pages.landing_page import LandingPageAndroid
from pages.account_details_page import AccountDetailsPageAndroid
from pages.phone_number_verification_page import PhoneNumberVerificationPageAndroid
from pages.food_preferences_page import FoodPreferencesPageAndroid
from pages.location_page import LocationPageAndroid
from pages.enter_postcode_page import EnterPostcodePageAndroid
from pages.whats_available_page import WhatsAvailablePageAndroid
from pages.feed_page import FeedPageAndroid
from functions.users import genuser
from functions.users import getuser
from functions.set_up import setup_with_app_local
from functions.get_sms_code import getsmscode
from functions.gen_city import gencity
from pages.login_page import LoginPageAndroid
from functions.set_up import setup_no_app_local
from functions.start_foodvine_from_homescreen import startfoodvinefromhomescreen
from pages.forgot_password_page import ForgotPasswordPageAndroid
from pages.choose_new_password_page import ChooseNewPasswordPageAndroid
from functions.users import changepw
from functions.users import saveuser




def test_login_email():

    driver = setup_with_app_local("Pixel_3a_API_30_x86")

    #### [Automated test] Login to Foodie Account ####
    #### Landing page ####
    landingpage = LandingPageAndroid(driver)

    landingpage.click_button(landingpage.ALLREADY_HAVE_AN_ACCOUNT_BUTTON_XPATH)
    sleep(2)

    #### Login page ####
    loginpage = LoginPageAndroid(driver)

    assert loginpage.get_text(loginpage.PAGE_TITLE_XPATH) == "Login"


    un = getuser()[0]
    email = getuser()[1]
    pw = getuser()[2]

    # un = 'testnikola1'
    # email = 'testnikola1@gmail.com'
    # pw = '1234Tests'

    print("Username, email and password are:", un, ',', email, ',', pw)
    loginpage.input_text(loginpage.USERNAME_OR_EMAIL_XPATH, email)
    sleep(1)
    loginpage.input_text(loginpage.PASSWORD_XPATH, pw)
    sleep(1)

    loginpage.click_button(loginpage.LOGIN_BUTTON_XPATH)




    ### TEMP ###
    foodpreferencespage = FoodPreferencesPageAndroid(driver)
    foodpreferencespage.click_button(foodpreferencespage.SKIP_BUTTON_XPATH)
    sleep(1)

    locationpage = LocationPageAndroid(driver)
    locationpage.click_button(locationpage.SKIP_BUTTON_XPATH)
    sleep(1)

    whatsavailablepage = WhatsAvailablePageAndroid(driver)
    whatsavailablepage.click_button(whatsavailablepage.FINISH_BUTTON_XPATH_3, 300)
    sleep(2)
    ### TEMP ###




    #### Feed page ####
    sleep(5)
    feedpage = FeedPageAndroid(driver)
    assert feedpage.get_text(feedpage.FEED_XPATH) == 'Feed'
    assert feedpage.get_text(feedpage.DISCOVER_XPATH) == 'Discover'
    assert feedpage.get_text(feedpage.ORDERS_XPATH) == 'Orders'
    assert feedpage.get_text(feedpage.PROFILE_XPATH) == 'Profile'
    assert feedpage.get_text(feedpage.MY_STORE_XPATH) == 'My Store'


    sleep(1)
    driver.close_app()

    sleep(1)
    driver = setup_no_app_local("Pixel_3a_API_30_x86")

    sleep(1)
    startfoodvinefromhomescreen(driver)

    #### Feed page ####
    sleep(5)
    feedpage = FeedPageAndroid(driver)
    assert feedpage.get_text(feedpage.FEED_XPATH) == 'Feed'
    assert feedpage.get_text(feedpage.DISCOVER_XPATH) == 'Discover'
    assert feedpage.get_text(feedpage.ORDERS_XPATH) == 'Orders'
    assert feedpage.get_text(feedpage.PROFILE_XPATH) == 'Profile'
    assert feedpage.get_text(feedpage.MY_STORE_XPATH) == 'My Store'

    sleep(5)
    driver.close_app()