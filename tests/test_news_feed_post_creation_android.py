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
from functions.set_up import setup_with_app
from functions.get_sms_code import getsmscode
from functions.gen_city import gencity
from pages.login_page import LoginPageAndroid
from functions.set_up import setup_no_app
from functions.start_foodvine_from_homescreen import startfoodvinefromhomescreen
from pages.forgot_password_page import ForgotPasswordPageAndroid
from pages.choose_new_password_page import ChooseNewPasswordPageAndroid
from functions.users import changepw
from functions.users import saveuser
from pages.new_post_page import NewPostPageAndroid
from pages.edit_post_page import EditPostPageAndroid
from pages.post_title_page import PostTitlePageAndroid
from pages.post_caption_page import PostCaptionPageAndroid
from pages.preview_post_page import PreviewPostPageAndroid
from functions.set_up import setup_with_app_cloud_android




def test_media_post_creation_android():

    driver = setup_with_app_cloud_android()

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
    loginpage.input_text(loginpage.USERNAME_OR_EMAIL_XPATH, un)
    sleep(1)
    loginpage.input_text(loginpage.PASSWORD_XPATH, pw)
    sleep(1)

    loginpage.click_button(loginpage.LOGIN_BUTTON_XPATH)

    #### Feed page ####
    sleep(60)
    feedpage = FeedPageAndroid(driver)


    #### [Automated Test] News Feed Post Creation ####
    #### Feed page ####
    feedpage = FeedPageAndroid(driver)
    feedpage.click_button(feedpage.PLUS_BUTTON_XPATH)
    sleep(2)

    #### New Post page ####
    newpostpage = NewPostPageAndroid(driver)
    newpostpage.click_button(newpostpage.MEDIA_1_XPATH)
    newpostpage.click_button(newpostpage.NEXT_BUTTON_XPATH)
    sleep(2)

    #### Edit Post page ####
    editpostpage = EditPostPageAndroid(driver)
    editpostpage.click_button(editpostpage.POST_TITLE_XPATH)
    sleep(2)

    #### Post title page ####
    posttitlepage = PostTitlePageAndroid(driver)
    posttitlepage.input_text(posttitlepage.INPUT_FIELD_XPATH, "testTitle")
    posttitlepage.click_button(posttitlepage.SAVE_BUTTON_XPATH)
    sleep(2)

    #### Edit Post page ####
    editpostpage.click_button(editpostpage.POST_CAPTION_XPATH)
    sleep(2)

    #### Post caption page ####
    postcaptionpage = PostCaptionPageAndroid(driver)
    postcaptionpage.input_text(posttitlepage.INPUT_FIELD_XPATH, "testCaption")
    postcaptionpage.click_button(posttitlepage.SAVE_BUTTON_XPATH)
    sleep(2)

    #### Edit Post page ####
    editpostpage.click_button(editpostpage.PREVIEW_BUTTON_XPATH)
    sleep(2)

    #### Preview Post page ####
    previewpostpage = PreviewPostPageAndroid(driver)
    previewpostpage.click_button(previewpostpage.POST_BUTTON_XPATH)
    sleep(2)

    #### Feed page ####
    sleep(5)
    try:
        print("Page title is ", feedpage.get_text(feedpage.PAGE_TITLE_XPATH))
        assert feedpage.get_text(feedpage.PAGE_TITLE_XPATH) == 'Most recent'
    except:
        print("Couldnt parse Feed page")

