import pytest
from appium import webdriver
from time import sleep
import random

from pages.landing_page import LandingPageAndroid
from pages.account_details_page import AccountDetailsPageAndroid
from pages.phone_number_verification_page import PhoneNumberVerificationPageiOS
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
# from tests import test_login
from pages.new_post_page import NewPostPageAndroid
from pages.edit_post_page import EditPostPageAndroid
from pages.input_page import InputPageAndroid
from pages.preview_post_page import PreviewPostPageAndroid
from functions.set_up import setup_with_app_cloud_android
from pages.new_post_page import NewPostRecipePageAndroid
from pages.add_tags_page import AddTagsAndroid
from pages.add_ingredients_page import AddIngredientsPageAndroid


def test_recipe_post_creation_android():

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



    #### [Automated Test] News Feed Post Creation ####
    #### Feed page ####
    feedpage = FeedPageAndroid(driver)
    feedpage.click_button(feedpage.PLUS_BUTTON_XPATH)
    sleep(2)

    ### Allow pop-up ###
    feedpage.click_button(feedpage.ALLOW_XPATH)
    sleep(2)


    ### TEMP ###
    newpostpage = NewPostRecipePageAndroid(driver)
    newpostpage.click_button(newpostpage.X_BUTTON_XPATH)
    sleep(3)
    feedpage.click_button(feedpage.PLUS_BUTTON_XPATH)
    sleep(2)
    ### TEMP ###



    #### New Post page ####
    newpostpage = NewPostRecipePageAndroid(driver)
    assert newpostpage.get_text(newpostpage.PAGE_TITLE_XPATH) == "New Post"
    newpostpage.click_button(newpostpage.RECIPE_XPATH)
    sleep(1)
    newpostpage.click_button(newpostpage.ADD_PHOTO_OR_VIDEO_XPATH)
    sleep(1)
    if random.randint(0, 1) == 0:
        newpostpage.click_button(newpostpage.MEDIA_1_XPATH)
    else:
        newpostpage.click_button(newpostpage.SELECT_MULTIPLE_XPATH)
        newpostpage.click_button(newpostpage.MEDIA_1_XPATH)
        newpostpage.click_button(newpostpage.MEDIA_2_XPATH)
    sleep(1)
    newpostpage.click_button(newpostpage.X_BUTTON_MEDIA_XPATH)
    sleep(1)
    newpostpage.click_button(newpostpage.TITLE_XPATH)
    sleep(1)

    ### Title page ###
    titlepage = InputPageAndroid(driver)
    titlepage.input_text(titlepage.INPUT_FIELD_XPATH, "testTitle")
    sleep(1)
    titlepage.click_button(titlepage.SAVE_BUTTON_XPATH)
    sleep(1)

    #### New Post page ####
    newpostpage.click_button(newpostpage.DESCRIPTION_XPATH)
    sleep(1)

    ### Description page ###
    descriptionpage = InputPageAndroid(driver)
    descriptionpage.input_text(descriptionpage.INPUT_FIELD_XPATH, "testDescription")
    sleep(1)
    descriptionpage.click_button(descriptionpage.SAVE_BUTTON_XPATH)
    sleep(1)

    #### New Post page ####
    newpostpage.click_button(newpostpage.ADD_TAGS_XPATH)

    #### Add tags page ####
    addtagspage = AddTagsAndroid(driver)
    addtagspage.input_text(addtagspage.INPUT_XPATH, "ch")
    sleep(1)
    addtagspage.click_button(addtagspage.TAG_2_XPATH)
    sleep(1)
    addtagspage.click_button(addtagspage.SAVE_BUTTON_XPATH)
    sleep(1)

    #### New Post page ####
    newpostpage.click_button(newpostpage.DIFFICULTY_XPATH)
    sleep(1)

    #### Difficulty pop-up ####
    newpostpage.click_button(newpostpage.ADVANCE_XPATH)
    sleep(1)
    newpostpage.click_button(newpostpage.SAVE_BUTTON_XPATH)
    sleep(1)

    #### New Post page ####
    newpostpage.click_button(newpostpage.SERVINGS_XPATH)
    sleep(1)

    #### Servings pop-up ####
    newpostpage.click_button(newpostpage.SERVING_NUMBER_XPATH)
    sleep(1)
    serving_number = str(random.randint(1, 12))
    servings_select_xpath = newpostpage.set_list(serving_number)
    newpostpage.click_button(servings_select_xpath)
    sleep(1)
    newpostpage.click_button(newpostpage.SAVE_BUTTON_XPATH)
    sleep(1)

    #### New Post page ####
    newpostpage.swipe_down()
    sleep(1)
    newpostpage.click_button(newpostpage.PREP_TIME_XPATH)
    sleep(1)

    #### Prep pop-up ####
    assert newpostpage.get_text(newpostpage.TIMING_TITLE_XPATH) == "Prep time"
    newpostpage.click_button(newpostpage.HOUR_XPATH)
    sleep(1)
    hour = str(random.randint(0, 10))
    hour_select_xpath = newpostpage.set_list(hour)
    newpostpage.click_button(hour_select_xpath)
    sleep(1)

    newpostpage.click_button(newpostpage.MIN_XPATH)
    sleep(1)
    minute = str(random.randint(1, 12))
    minute_select_xpath = newpostpage.set_list(minute)
    newpostpage.click_button(minute_select_xpath)
    sleep(1)

    newpostpage.click_button(newpostpage.SAVE_BUTTON_XPATH)
    sleep(1)

    #### New Post page ####
    newpostpage.click_button(newpostpage.COOK_TIME_XPATH)
    sleep(1)

    #### Cook pop-up ####
    assert newpostpage.get_text(newpostpage.TIMING_TITLE_XPATH) == "Cook time"
    newpostpage.click_button(newpostpage.HOUR_XPATH)
    sleep(1)
    hour = str(random.randint(0, 10))
    hour_select_xpath = newpostpage.set_list(hour)
    newpostpage.click_button(hour_select_xpath)
    sleep(1)

    newpostpage.click_button(newpostpage.MIN_XPATH)
    sleep(1)
    minute = str(random.randint(1, 12))
    minute_select_xpath = newpostpage.set_list(minute)
    newpostpage.click_button(minute_select_xpath)
    sleep(1)

    newpostpage.click_button(newpostpage.SAVE_BUTTON_XPATH)
    sleep(1)

    #### New Post page ####
    newpostpage.click_button(newpostpage.ALLERGENS_XPATH)
    sleep(1)

    #### Allregnes pop-up ####
    if random.randint(0, 3) == 0:
        newpostpage.click_button(newpostpage.ALLERGEN_1_XPATH)
    if random.randint(0, 3) == 0:
        newpostpage.click_button(newpostpage.ALLERGEN_2_XPATH)
    if random.randint(0, 3) == 0:
        newpostpage.click_button(newpostpage.ALLERGEN_3_XPATH)
    if random.randint(0, 3) == 0:
        newpostpage.click_button(newpostpage.ALLERGEN_4_XPATH)
    if random.randint(0, 3) == 0:
        newpostpage.click_button(newpostpage.ALLERGEN_5_XPATH)
    if random.randint(0, 3) == 0:
        newpostpage.click_button(newpostpage.ALLERGEN_6_XPATH)
    if random.randint(0, 3) == 0:
        newpostpage.click_button(newpostpage.ALLERGEN_7_XPATH)
    if random.randint(0, 3) == 0:
        newpostpage.click_button(newpostpage.ALLERGEN_8_XPATH)
    if random.randint(0, 3) == 0:
        newpostpage.click_button(newpostpage.ALLERGEN_9_XPATH)

    newpostpage.click_button(newpostpage.SAVE_BUTTON_XPATH)
    sleep(1)

    #### New Post page ####
    newpostpage.click_button(newpostpage.DIETARY_INFO_XPATH)
    sleep(1)

    #### Dietary pop-up ####
    if random.randint(0, 3) == 0:
        newpostpage.click_button(newpostpage.DIETARY_1_XPATH)
    if random.randint(0, 3) == 0:
        newpostpage.click_button(newpostpage.DIETARY_2_XPATH)
    if random.randint(0, 3) == 0:
        newpostpage.click_button(newpostpage.DIETARY_3_XPATH)
    if random.randint(0, 3) == 0:
        newpostpage.click_button(newpostpage.DIETARY_4_XPATH)
    if random.randint(0, 3) == 0:
        newpostpage.click_button(newpostpage.DIETARY_5_XPATH)
    if random.randint(0, 3) == 0:
        newpostpage.click_button(newpostpage.DIETARY_6_XPATH)


    newpostpage.click_button(newpostpage.SAVE_BUTTON_XPATH)
    sleep(1)

    #### New Post page ####
    newpostpage.click_button(newpostpage.INGREDIENTS_XPATH)
    sleep(1)

    #### Ingredients page ####
    ingredientspage = AddIngredientsPageAndroid(driver)
    driver.hide_keyboard()
    sleep(1)
    ingredientspage.click_button(ingredientspage.INGREDIENT_1_XPATH)
    sleep(1)
    ingredientspage.input_text(ingredientspage.INGREDIENT_INPUT_XPATH, str(random.randint(1, 99)))
    ingred_type = random.randint(0, 4)
    if ingred_type == 0:
        ingredientspage.click_button(ingredientspage.POUND_XPATH)
    elif ingred_type == 1:
        ingredientspage.click_button(ingredientspage.GALLON_XPATH)
    elif ingred_type == 2:
        ingredientspage.click_button(ingredientspage.QUART_XPATH)
    elif ingred_type == 3:
        ingredientspage.click_button(ingredientspage.TEASPOON_XPATH)
    elif ingred_type == 4:
        ingredientspage.click_button(ingredientspage.TABLESPOON_XPATH)
    sleep(2)
    ingredientspage.click_button(ingredientspage.SAVE_INGREDIENT_BUTTON_XPATH)
    if random.randint(0, 3) == 0:
        ingredientspage.click_button(ingredientspage.INGREDIENT_2_XPATH)
        sleep(1)
        ingredientspage.input_text(ingredientspage.INGREDIENT_INPUT_XPATH, str(random.randint(1, 99)))
        ingred_type = random.randint(0, 4)
        if ingred_type == 0:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 1:
            ingredientspage.click_button(ingredientspage.GALLON_XPATH)
        elif ingred_type == 2:
            ingredientspage.click_button(ingredientspage.QUART_XPATH)
        elif ingred_type == 3:
            ingredientspage.click_button(ingredientspage.TEASPOON_XPATH)
        elif ingred_type == 4:
            ingredientspage.click_button(ingredientspage.TABLESPOON_XPATH)
        sleep(2)
        ingredientspage.click_button(ingredientspage.SAVE_INGREDIENT_BUTTON_XPATH)
    if random.randint(0, 3) == 0:
        ingredientspage.click_button(ingredientspage.INGREDIENT_3_XPATH)
        sleep(1)
        ingredientspage.input_text(ingredientspage.INGREDIENT_INPUT_XPATH, str(random.randint(1, 99)))
        ingred_type = random.randint(0, 4)
        if ingred_type == 0:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 1:
            ingredientspage.click_button(ingredientspage.GALLON_XPATH)
        elif ingred_type == 2:
            ingredientspage.click_button(ingredientspage.QUART_XPATH)
        elif ingred_type == 3:
            ingredientspage.click_button(ingredientspage.TEASPOON_XPATH)
        elif ingred_type == 4:
            ingredientspage.click_button(ingredientspage.TABLESPOON_XPATH)
        sleep(2)
        ingredientspage.click_button(ingredientspage.SAVE_INGREDIENT_BUTTON_XPATH)
    if random.randint(0, 3) == 0:
        ingredientspage.click_button(ingredientspage.INGREDIENT_4_XPATH)
        sleep(1)
        ingredientspage.input_text(ingredientspage.INGREDIENT_INPUT_XPATH, str(random.randint(1, 99)))
        ingred_type = random.randint(0, 4)
        if ingred_type == 0:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 1:
            ingredientspage.click_button(ingredientspage.GALLON_XPATH)
        elif ingred_type == 2:
            ingredientspage.click_button(ingredientspage.QUART_XPATH)
        elif ingred_type == 3:
            ingredientspage.click_button(ingredientspage.TEASPOON_XPATH)
        elif ingred_type == 4:
            ingredientspage.click_button(ingredientspage.TABLESPOON_XPATH)
        sleep(1)
        ingredientspage.click_button(ingredientspage.SAVE_INGREDIENT_BUTTON_XPATH)
    if random.randint(0, 3) == 0:
        ingredientspage.click_button(ingredientspage.INGREDIENT_5_XPATH)
        sleep(1)
        ingredientspage.input_text(ingredientspage.INGREDIENT_INPUT_XPATH, str(random.randint(1, 99)))
        ingred_type = random.randint(0, 4)
        if ingred_type == 0:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 1:
            ingredientspage.click_button(ingredientspage.GALLON_XPATH)
        elif ingred_type == 2:
            ingredientspage.click_button(ingredientspage.QUART_XPATH)
        elif ingred_type == 3:
            ingredientspage.click_button(ingredientspage.TEASPOON_XPATH)
        elif ingred_type == 4:
            ingredientspage.click_button(ingredientspage.TABLESPOON_XPATH)
        sleep(1)
        ingredientspage.click_button(ingredientspage.SAVE_INGREDIENT_BUTTON_XPATH)
    if random.randint(0, 3) == 0:
        ingredientspage.click_button(ingredientspage.INGREDIENT_6_XPATH)
        sleep(1)
        ingredientspage.input_text(ingredientspage.INGREDIENT_INPUT_XPATH, str(random.randint(1, 99)))
        ingred_type = random.randint(0, 4)
        if ingred_type == 0:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 1:
            ingredientspage.click_button(ingredientspage.GALLON_XPATH)
        elif ingred_type == 2:
            ingredientspage.click_button(ingredientspage.QUART_XPATH)
        elif ingred_type == 3:
            ingredientspage.click_button(ingredientspage.TEASPOON_XPATH)
        elif ingred_type == 4:
            ingredientspage.click_button(ingredientspage.TABLESPOON_XPATH)
        sleep(1)
        ingredientspage.click_button(ingredientspage.SAVE_INGREDIENT_BUTTON_XPATH)
    if random.randint(0, 3) == 0:
        ingredientspage.click_button(ingredientspage.INGREDIENT_7_XPATH)
        sleep(1)
        ingredientspage.input_text(ingredientspage.INGREDIENT_INPUT_XPATH, str(random.randint(1, 99)))
        ingred_type = random.randint(0, 4)
        if ingred_type == 0:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 1:
            ingredientspage.click_button(ingredientspage.GALLON_XPATH)
        elif ingred_type == 2:
            ingredientspage.click_button(ingredientspage.QUART_XPATH)
        elif ingred_type == 3:
            ingredientspage.click_button(ingredientspage.TEASPOON_XPATH)
        elif ingred_type == 4:
            ingredientspage.click_button(ingredientspage.TABLESPOON_XPATH)
        sleep(1)
        ingredientspage.click_button(ingredientspage.SAVE_INGREDIENT_BUTTON_XPATH)
    sleep(1)
    newpostpage.click_button(newpostpage.SAVE_BUTTON_XPATH)
    sleep(1)
    newpostpage.swipe_down()
    sleep(1)

    #### New Post page ####
    newpostpage.swipe_down()
    sleep(1)
    newpostpage.click_button(newpostpage.STEP_TITLE_XPATH)
    sleep(1)

    ### Step title page ###
    steptitlepage = InputPageAndroid(driver)
    steptitlepage.input_text(steptitlepage.INPUT_FIELD_XPATH, "testStep1Title")
    sleep(1)
    steptitlepage.click_button(steptitlepage.SAVE_BUTTON_XPATH)
    sleep(1)

    #### New Post page ####
    newpostpage.click_button(newpostpage.STEP_DESCRIPTION_XPATH)
    sleep(1)

    ### Step title page ###
    stepdescriptionpage = InputPageAndroid(driver)
    stepdescriptionpage.input_text(stepdescriptionpage.INPUT_FIELD_XPATH, "testStep1Description")
    sleep(1)
    stepdescriptionpage.click_button(stepdescriptionpage.SAVE_BUTTON_XPATH)
    sleep(1)

    ### Choose media pop-up ###
    newpostpage.click_button(newpostpage.ADD_PHOTO_TO_STEP)
    sleep(1)
    newpostpage.click_button(newpostpage.MEDIA_1_XPATH)
    sleep(1)
    newpostpage.click_button(newpostpage.X_BUTTON_MEDIA_XPATH)
    sleep(1)

    #### New Post page ####
    newpostpage.swipe_down()
    sleep(1)
    newpostpage.click_button(newpostpage.ADD_ANOTHER_STEP)
    sleep(1)
    newpostpage.click_button(newpostpage.STEP_TITLE_XPATH)
    sleep(1)

    ### Step title page ###
    steptitlepage = InputPageAndroid(driver)
    steptitlepage.input_text(steptitlepage.INPUT_FIELD_XPATH, "testStep2Title")
    sleep(1)
    steptitlepage.click_button(steptitlepage.SAVE_BUTTON_XPATH)
    sleep(1)

    #### New Post page ####
    newpostpage.click_button(newpostpage.STEP_DESCRIPTION_XPATH)
    sleep(1)

    ### Step title page ###
    stepdescriptionpage = InputPageAndroid(driver)
    stepdescriptionpage.input_text(stepdescriptionpage.INPUT_FIELD_XPATH, "testStep2Description")
    sleep(1)
    stepdescriptionpage.click_button(stepdescriptionpage.SAVE_BUTTON_XPATH)
    sleep(1)

    ### Choose media pop-up  ###
    newpostpage.click_button(newpostpage.ADD_PHOTO_TO_STEP)
    sleep(1)
    newpostpage.click_button(newpostpage.SELECT_MULTIPLE_XPATH)
    newpostpage.click_button(newpostpage.MEDIA_1_XPATH)
    newpostpage.click_button(newpostpage.MEDIA_2_XPATH)
    newpostpage.click_button(newpostpage.X_BUTTON_MEDIA_XPATH)
    sleep(1)

    #### New Post page ####
    sleep(2)
    newpostpage.click_button(newpostpage.PREVIEW_BUTTON_XPATH)
    sleep(5)


    #### Preview Post page ####
    previewpostpage = PreviewPostPageAndroid(driver)
    assert previewpostpage.get_text(previewpostpage.POST_TITLE_XPATH) == "testTitle"
    assert previewpostpage.get_text(previewpostpage.POST_CAPTION_XPATH) == "a few seconds ago testDescription"
    previewpostpage.click_button(previewpostpage.POST_BUTTON_XPATH)
    sleep(2)


    #### Feed page ####
    sleep(5)
    assert feedpage.get_text(feedpage.POST_CREATOR_XPATH, 30) == un
    assert feedpage.get_text(feedpage.POST_TITLE_XPATH, 30) == "testTitle"
    assert feedpage.get_text(feedpage.POST_CAPTION_XPATH, 30) == "a few seconds ago testDescription"


    sleep(5)
    driver.close_app()