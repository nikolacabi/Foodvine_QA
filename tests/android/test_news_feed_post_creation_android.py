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
from pages.new_post_page import NewPostPageAndroid
from pages.edit_post_page import EditPostPageAndroid
from pages.input_page import InputPageAndroid
from pages.preview_post_page import PreviewPostPageAndroid
from functions.set_up import setup_with_app_cloud_android
from functions.set_up import setup_with_app_cloud_ios
from pages.add_tags_page import AddTagsPageAndroid



def test_media_post_creation_android():

    driver = setup_with_app_local("Pixel_3a_API_30_x86")
    sleep(10)

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



    #### TEMP ####
    foodpreferencespage = FoodPreferencesPageAndroid(driver)
    foodpreferencespage.click_button(foodpreferencespage.SKIP_BUTTON_XPATH)
    sleep(1)

    locationpage = LocationPageAndroid(driver)
    locationpage.click_button(locationpage.SKIP_BUTTON_XPATH)
    sleep(1)

    whatsavailablepage = WhatsAvailablePageAndroid(driver)
    whatsavailablepage.click_button(whatsavailablepage.FINISH_BUTTON_XPATH_3, 300)
    sleep(5)
    #### TEMP ####



    #### [Automated Test] News Feed Post Creation ####
    #### Feed page ####
    feedpage = FeedPageAndroid(driver)
    feedpage.click_button(feedpage.PLUS_BUTTON_XPATH)
    sleep(2)

    ### Allow pop-up ###
    feedpage.click_button(feedpage.ALLOW_XPATH)
    sleep(2)


    #### TEMP ####
    newpostpage = NewPostPageAndroid(driver)
    newpostpage.click_button(newpostpage.X_BUTTON_XPATH)
    sleep(3)
    feedpage.click_button(feedpage.PLUS_BUTTON_XPATH)
    sleep(5)
    #### TEMP ####


    #### New Post page ####
    #newpostpage = NewPostPageAndroid(driver)
    if random.randint(0, 1) == 0:
        newpostpage.click_button(newpostpage.MEDIA_1_XPATH)
    else:
        newpostpage.click_button(newpostpage.SELECT_MULTIPLE_XPATH)
        newpostpage.click_button(newpostpage.MEDIA_1_XPATH)
        newpostpage.click_button(newpostpage.MEDIA_2_XPATH)
    sleep(1)
    newpostpage.click_button(newpostpage.NEXT_BUTTON_XPATH)
    sleep(2)

    #### Edit Post page ####
    editpostpage = EditPostPageAndroid(driver)
    editpostpage.click_button(editpostpage.POST_TITLE_XPATH)
    sleep(2)

    ### Post title page ###
    titlepage = InputPageAndroid(driver)
    titlepage.input_text(titlepage.INPUT_FIELD_XPATH, "testTitle")
    sleep(1)
    titlepage.click_button(titlepage.SAVE_BUTTON_XPATH)
    sleep(1)

    #### Edit Post page ####
    editpostpage.click_button(editpostpage.POST_CAPTION_XPATH)
    sleep(2)

    #### Post caption page ####
    descriptionpage = InputPageAndroid(driver)
    descriptionpage.input_text(descriptionpage.INPUT_FIELD_XPATH, "testCaption")
    sleep(1)
    descriptionpage.click_button(descriptionpage.SAVE_BUTTON_XPATH)
    sleep(1)

    #### Edit Post page ####
    editpostpage.click_button(editpostpage.ADD_TAGS_XPATH)
    sleep(1)

    #### Add tags page ####
    addtagspage = AddTagsPageAndroid(driver)
    addtagspage.input_text(addtagspage.INPUT_XPATH, "ch")
    sleep(1)
    addtagspage.click_button(addtagspage.TAG_2_XPATH)
    sleep(1)
    addtagspage.click_button(addtagspage.SAVE_BUTTON_XPATH)
    sleep(1)

    #### Edit Post page ####
    editpostpage.click_button(editpostpage.PREVIEW_BUTTON_XPATH)
    sleep(2)

    #### Preview Post page ####
    previewpostpage = PreviewPostPageAndroid(driver)
    assert previewpostpage.get_text(previewpostpage.POST_TITLE_XPATH) == "testTitle"
    assert previewpostpage.get_text(previewpostpage.POST_CAPTION_XPATH) == "a few seconds ago testCaption"
    previewpostpage.click_button(previewpostpage.POST_BUTTON_XPATH)
    sleep(2)


    #### Feed page ####
    sleep(5)
    assert feedpage.get_text(feedpage.POST_CREATOR_XPATH) == un
    assert feedpage.get_text(feedpage.POST_TITLE_XPATH) == "testTitle"
    assert feedpage.get_text(feedpage.POST_CAPTION_XPATH) == "a few seconds ago testCaption"


    sleep(5)
    driver.close_app()

