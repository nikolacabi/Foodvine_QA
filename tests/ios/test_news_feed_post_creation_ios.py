import pytest
from appium import webdriver
from time import sleep
import random
from pages.landing_page import LandingPageiOS
from pages.account_details_page import AccountDetailsPageAndroid
from pages.phone_number_verification_page import PhoneNumberVerificationPageAndroid
from pages.food_preferences_page import FoodPreferencesPageiOS
from pages.location_page import LocationPageiOS
from pages.enter_postcode_page import EnterPostcodePageiOS
from pages.whats_available_page import WhatsAvailablePageiOS
from pages.feed_page import FeedPageiOS
from functions.users import genuser
from functions.users import getuser
from functions.set_up import setup_with_app_local
from functions.get_sms_code import getsmscode
from functions.gen_city import gencity
from pages.login_page import LoginPageiOS
from functions.set_up import setup_no_app_local
from functions.start_foodvine_from_homescreen import startfoodvinefromhomescreen
from pages.forgot_password_page import ForgotPasswordPageAndroid
from pages.choose_new_password_page import ChooseNewPasswordPageAndroid
from functions.users import changepw
from functions.users import saveuser
from pages.new_post_page import NewPostPageiOS
from pages.edit_post_page import EditPostPageiOS
from pages.input_page import InputPageiOS
from pages.preview_post_page import PreviewPostPageiOS
from functions.set_up import setup_with_app_cloud_android
from functions.set_up import setup_with_app_cloud_ios
from pages.add_tags_page import AddTagsPageiOS



def test_media_post_creation_ios():

    driver = setup_with_app_cloud_ios("IPhone 11 Pro IO-UK 10")
    # driver = setup_with_app_cloud_ios("IPhone 11 Pro IO-UK 06")
    sleep(10)

    #### [Automated test] Login to Foodie Account ####
    #### Landing page ####
    landingpage = LandingPageiOS(driver)

    landingpage.click_button(landingpage.ALLREADY_HAVE_AN_ACCOUNT_BUTTON_XPATH)
    sleep(2)

    #### Login page ####
    loginpage = LoginPageiOS(driver)

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
    foodpreferencespage = FoodPreferencesPageiOS(driver)
    foodpreferencespage.click_button(foodpreferencespage.SKIP_BUTTON_XPATH)
    sleep(1)

    locationpage = LocationPageiOS(driver)
    locationpage.click_button(locationpage.SKIP_BUTTON_XPATH)
    sleep(1)

    whatsavailablepage = WhatsAvailablePageiOS(driver)
    whatsavailablepage.click_button(whatsavailablepage.FINISH_BUTTON_XPATH, 300)
    sleep(5)
    #### TEMP ####



    #### [Automated Test] News Feed Post Creation ####
    #### Feed page ####
    feedpage = FeedPageiOS(driver)
    assert feedpage.get_text(feedpage.FEED_XPATH) == "Feed"
    # feedpage.click_button(feedpage.PLUS_BUTTON_XPATH)
    driver.tap([(849, 174)])
    sleep(2)

    ### Allow pop-up ###
    feedpage.click_button(feedpage.ALLOW_XPATH)
    sleep(2)




    #### New Post page ####
    newpostpage = NewPostPageiOS(driver)
    sleep(1)
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
    editpostpage = EditPostPageiOS(driver)
    editpostpage.click_button(editpostpage.POST_TITLE_XPATH)
    sleep(2)

    ### Post title page ###
    titlepage = InputPageiOS(driver)
    titlepage.input_text(titlepage.INPUT_FIELD_XPATH, "testTitle")
    sleep(1)
    titlepage.click_button(titlepage.SAVE_BUTTON_XPATH)
    sleep(1)

    #### Edit Post page ####
    editpostpage.click_button(editpostpage.POST_CAPTION_XPATH)
    sleep(2)

    #### Post caption page ####
    descriptionpage = InputPageiOS(driver)
    descriptionpage.input_text(descriptionpage.INPUT_FIELD_XPATH, "testCaption")
    sleep(1)
    descriptionpage.click_button(descriptionpage.SAVE_BUTTON_XPATH)
    sleep(1)

    #### Edit Post page ####
    editpostpage.click_button(editpostpage.ADD_TAGS_XPATH)
    sleep(2)

    #### Add tags page ####
    addtagspage = AddTagsPageiOS(driver)
    addtagspage.input_text(addtagspage.INPUT_XPATH, "ch")
    sleep(1)
    # addtagspage.click_button(addtagspage.TAG_2_XPATH)
    driver.tap([(291, 708)])
    sleep(1)
    addtagspage.click_button(addtagspage.SAVE_BUTTON_XPATH)
    sleep(2)

    #### Edit Post page ####
    editpostpage.click_button(editpostpage.PREVIEW_BUTTON_XPATH)
    sleep(2)

    #### Preview Post page ####
    previewpostpage = PreviewPostPageiOS(driver)
    assert previewpostpage.get_text(previewpostpage.post_title("testTitle")) == "testTitle"
    assert previewpostpage.get_text(previewpostpage.post_caption("a few seconds ago testCaption")) == "a few seconds ago testCaption"
    previewpostpage.click_button(previewpostpage.POST_BUTTON_XPATH)
    sleep(2)


    #### Feed page ####
    sleep(5)
    assert feedpage.get_text(feedpage.FEED_XPATH) == "Feed"
    # assert feedpage.get_text(feedpage.POST_CREATOR_XPATH) == un
    # assert feedpage.get_text(feedpage.POST_TITLE_XPATH) == "testTitle"
    # assert feedpage.get_text(feedpage.POST_CAPTION_XPATH) == "a few seconds ago testCaption"


    sleep(5)
    # driver.close_app()

