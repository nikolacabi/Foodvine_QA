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



#@pytest.mark.timeout(300)
def test_reset_password():

    driver = setup()

    #### [Automated test] Forgot password ####
    #### Landing page ####
    landingpage = LandingPage(driver)

    landingpage.click_button(landingpage.ALLREADY_HAVE_AN_ACCOUNT_BUTTON_XPATH)
    sleep(2)

    #### Login page ####
    loginpage = LoginPage(driver)

    assert loginpage.get_text(loginpage.PAGE_TITLE_XPATH) == "Login"

    loginpage.click_button(loginpage.FORGOT_PASSWORD_BUTTON_XPATH)
    sleep(1)


    #### Forgot password page ####
    sleep(1)
    forgotpasswordpage = ForgotPasswordPage(driver)

    assert forgotpasswordpage.get_text(forgotpasswordpage.PAGE_TITLE_XPATH) == "Forgot password"

    un = getuser()[0]
    email = getuser()[1]
    pw = getuser()[2]
    print("Username, email and password are:", un, ',', email, ',', pw)
    forgotpasswordpage.input_text(forgotpasswordpage.USERNAME_OR_EMAIL_XPATH, un)
    forgotpasswordpage.click_button(forgotpasswordpage.SEND_BUTTON_XPATH)

    sleep(2)


    #### Phone Number Verification page ####
    phonenumberverificationpage = PhoneNumberVerificationPage(driver)
    assert phonenumberverificationpage.get_text(phonenumberverificationpage.PAGE_TITLE_PW_CHANGE_XPATH) == "Phone number verification"
    sleep(1)
    sms_code = getsmscode()
    print('SMS code:', sms_code)
    phonenumberverificationpage.input_text(phonenumberverificationpage.SMS_CODE_PW_CHANGE_INPUT, sms_code)

    sleep(2)

    #### Choose new password page ####
    choosenewpasswordpage = ChooseNewPasswordPage(driver)
    assert choosenewpasswordpage.get_text(choosenewpasswordpage.PAGE_TITLE_XPATH) == 'Choose new password'

    if pw == "1234Test":
        pw = "1234Tests"
    else:
        pw = "1234Test"
    changepw(un, email, pw)

    print("Username, email and password are now:", un, ',', email, ',', pw)

    choosenewpasswordpage.input_text(choosenewpasswordpage.NEW_PASSWORD_XPATH, pw)
    choosenewpasswordpage.input_text(choosenewpasswordpage.REPEAT_NEW_PASSWORD_XPATH, pw)
    choosenewpasswordpage.click_button(choosenewpasswordpage.CHANGE_PASSWORD_BUTTON_XPATH)

    sleep(2)



    #### Login page ####
    loginpage = LoginPage(driver)

    assert loginpage.get_text(loginpage.PAGE_TITLE_XPATH) == "Login"
    assert loginpage.get_text(loginpage.PASSWORD_CHANGE_CONFORMATION) == 'You can now login with your new password'


    loginpage.input_text(loginpage.USERNAME_OR_EMAIL_XPATH, un)
    sleep(1)
    loginpage.input_text(loginpage.PASSWORD_XPATH, pw)
    sleep(1)

    loginpage.click_button(loginpage.LOGIN_BUTTON_PW_CHANGE_XPATH)

    #### Feed page ####
    sleep(5)
    feedpage = FeedPage(driver)
    try:
        print("Page title is ", feedpage.get_text(feedpage.PAGE_TITLE_XPATH))
        assert feedpage.get_text(feedpage.PAGE_TITLE_XPATH) == 'Most recent'
    except:
        print("Couldnt parse Feed page")

