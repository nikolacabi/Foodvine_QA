import pytest
from appium import webdriver
from time import sleep
import random
from pages.landing_page import LandingPage
from pages.account_details_page import AccountDetailsPage
from pages.phone_number_verification_page import PhoneNumberVerificationPage
from pages.food_preferences_page import FoodPreferencesPage
from pages.location_page import LocationPage
from pages.enter_postcode_page import EnterPostcodePage
from pages.whats_available_page import WhatsAvailablePage
from pages.feed_page import FeedPage
from functions.users import genuser
from functions.users import getuser
from functions.set_up import setup
from functions.get_sms_code import getsmscode
from functions.gen_city import gencity
from pages.login_page import LoginPage
from functions.set_up import setup_no_app
from functions.start_foodvine_from_homescreen import startfoodvinefromhomescreen
from pages.forgot_password_page import ForgotPasswordPage
from pages.choose_new_password_page import ChooseNewPasswordPage
from functions.users import changepw
from functions.users import saveuser



def test_login_username():

    driver = setup()

    #### [Automated test] Login to Foodie Account ####
    #### Landing page ####
    landingpage = LandingPage(driver)

    landingpage.click_button(landingpage.ALLREADY_HAVE_AN_ACCOUNT_BUTTON_XPATH)
    sleep(2)

    #### Login page ####
    loginpage = LoginPage(driver)

    assert loginpage.get_text(loginpage.PAGE_TITLE_XPATH) == "Login"


    un = getuser()[0]
    email = getuser()[1]
    pw = getuser()[2]

    # un = 'testnikola1'
    # email = 'testnikola1@gmail.com'
    # pw = '1234Tests'

    print("Username, email and password are:", un, ',', email, ',', pw)
    loginpage.input_text(loginpage.USERNAME_OR_EMAIL_XPATH, un)
    sleep(1)
    loginpage.input_text(loginpage.PASSWORD_XPATH, pw)
    sleep(1)

    loginpage.click_button(loginpage.LOGIN_BUTTON_XPATH)

    #### Feed page ####
    sleep(5)
    feedpage = FeedPage(driver)
    try:
        print("Page title is ", feedpage.get_text(feedpage.PAGE_TITLE_XPATH))
        assert feedpage.get_text(feedpage.PAGE_TITLE_XPATH) == 'Most recent'
    except:
        print("Couldnt parse Feed page")

    sleep(1)
    driver.close_app()

    sleep(1)
    driver = setup_no_app()

    sleep(1)
    startfoodvinefromhomescreen(driver)

    #### Feed page ####
    sleep(5)
    feedpage = FeedPage(driver)
    try:
        print("Page title is ", feedpage.get_text(feedpage.PAGE_TITLE_XPATH))
        assert feedpage.get_text(feedpage.PAGE_TITLE_XPATH) == 'Most recent'
    except:
        print("Couldnt parse Feed page")



    driver.close_app()




def test_login_email():

    driver = setup()

    #### [Automated test] Login to Foodie Account ####
    #### Landing page ####
    landingpage = LandingPage(driver)

    landingpage.click_button(landingpage.ALLREADY_HAVE_AN_ACCOUNT_BUTTON_XPATH)
    sleep(2)

    #### Login page ####
    loginpage = LoginPage(driver)

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

    #### Feed page ####
    sleep(5)
    feedpage = FeedPage(driver)
    try:
        print("Page title is ", feedpage.get_text(feedpage.PAGE_TITLE_XPATH))
        assert feedpage.get_text(feedpage.PAGE_TITLE_XPATH) == 'Most recent'
    except:
        print("Couldnt parse Feed page")

    sleep(1)
    driver.close_app()

    sleep(1)
    driver = setup_no_app()

    sleep(1)
    startfoodvinefromhomescreen(driver)

    #### Feed page ####
    sleep(5)
    feedpage = FeedPage(driver)
    try:
        print("Page title is ", feedpage.get_text(feedpage.PAGE_TITLE_XPATH))
        assert feedpage.get_text(feedpage.PAGE_TITLE_XPATH) == 'Most recent'
    except:
        print("Couldnt parse Feed page")



    driver.close_app()