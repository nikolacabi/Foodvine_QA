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
# from tests import test_login
from pages.new_post_page import NewPostPageAndroid
from pages.edit_post_page import EditPostPageAndroid
from pages.input_page import InputPageAndroid
from pages.preview_post_page import PreviewPostPageAndroid
from functions.set_up import setup_with_app_cloud_android
from pages.new_post_page import NewPostRecipePageAndroid
from pages.add_tags_page import AddTagsAndroid
from pages.add_ingredients_page import AddIngredientsPageAndroid


if __name__ == '__main__':


    driver = setup_with_app()
    #
    #
    #
    # #### [Automated Test] Foodie account creation with email ####
    # #### Landing page ####
    # landingpage = LandingPage(driver)
    #
    # assert landingpage.get_text(landingpage.CAROUSEL_TEXT_XPATH) == "Authentic food from local farmers and home chefs"
    # landingpage.swipe_right_to_left()
    # sleep(1)
    # assert landingpage.get_text(landingpage.CAROUSEL_TEXT_XPATH) == "Explore behind the scenes content, recipes and more"
    # landingpage.swipe_right_to_left()
    # sleep(1)
    # assert landingpage.get_text(landingpage.CAROUSEL_TEXT_XPATH) == "Follow your favorites, and build a following with your own content"
    # landingpage.swipe_right_to_left()
    # sleep(1)
    # assert landingpage.get_text(landingpage.CAROUSEL_TEXT_XPATH) == "Join a community of small producers, home chefs and foodies like you"
    #
    # landingpage.click_button(landingpage.JOIN_FOR_FREE_BUTTON_XPATH)
    # sleep(2)
    # landingpage.click_button(landingpage.SIGN_UP_WITH_EMAIL_BUTTON_XPATH)
    # sleep(2)
    #
    #
    # #### Account Details page ####
    # accountdetailspage = AccountDetailsPage(driver)
    #
    # sleep(1)
    # assert accountdetailspage.get_text(accountdetailspage.PAGE_TITLE_XPATH) == "Account details"
    # accountdetailspage.input_text(accountdetailspage.FIRST_NAME_XPATH, "Nikola")
    # sleep(1)
    # accountdetailspage.input_text(accountdetailspage.LAST_NAME_XPATH, "Pavicevic")
    # sleep(1)
    # accountdetailspage.input_text(accountdetailspage.PHONE_XPATH, "6054094539")
    # sleep(1)
    # un = genuser()[0]
    # email = genuser()[1]
    # pw = genuser()[2]
    # print("Username, email and password are:", un, ',', email, ',', pw)
    # accountdetailspage.input_text(accountdetailspage.EMAIL_XPATH, email)
    # sleep(1)
    # accountdetailspage.input_text(accountdetailspage.USERNAME_XPATH, un)
    # sleep(1)
    # accountdetailspage.input_text(accountdetailspage.PASSWORD_XPATH, pw)
    # sleep(1)
    # accountdetailspage.click_button(accountdetailspage.CONTINUE_BUTTON_XPATH)
    #
    #
    # #### Phone Number Verification page ####
    # phonenumberverificationpage = PhoneNumberVerificationPage(driver)
    #
    # sleep(5)
    # assert phonenumberverificationpage.get_text(phonenumberverificationpage.PAGE_TITLE_XPATH) == "Phone number verification"
    # sms_code = getsmscode()
    # print('SMS code:', sms_code)
    # phonenumberverificationpage.input_text(phonenumberverificationpage.SMS_CODE_INPUT, sms_code)
    #
    #
    # #### Food Preferences page ####
    # foodpreferencespage = FoodPreferencesPage(driver)
    #
    # sleep(2)
    # assert foodpreferencespage.get_text(foodpreferencespage.PAGE_TITLE_XPATH) == "Food preferences"
    # # saveuser(un, email, pw)
    #
    #
    #
    #
    # #### [Automated Test] Initial Login to Foodie Account ####
    # #### Food Preferences page ####
    # preferences_selected = []
    # if random.randint(0, 4) == 0:
    #     foodpreferencespage.click_button(foodpreferencespage.SKIP_BUTTON_XPATH)
    # else:
    #     if random.randint(0, 3) == 0:
    #         foodpreferencespage.click_button(foodpreferencespage.AFRICAN_XPATH)
    #         preferences_selected.append("African")
    #     if random.randint(0, 3) == 0:
    #         foodpreferencespage.click_button(foodpreferencespage.ASIAN_XPATH)
    #         preferences_selected.append("Asian")
    #     if random.randint(0, 3) == 0:
    #         foodpreferencespage.click_button(foodpreferencespage.CARIBBEAN_XPATH)
    #         preferences_selected.append("Caribbean")
    #     if random.randint(0, 3) == 0:
    #         foodpreferencespage.click_button(foodpreferencespage.MEXICAN_XPATH)
    #         preferences_selected.append("Mexican")
    #     if random.randint(0, 3) == 0:
    #         foodpreferencespage.click_button(foodpreferencespage.THAI_XPATH)
    #         preferences_selected.append("Thai")
    #     if random.randint(0, 3) == 0:
    #         foodpreferencespage.click_button(foodpreferencespage.ITALIAN_XPATH)
    #         preferences_selected.append("Italian")
    #     if random.randint(0, 3) == 0:
    #         foodpreferencespage.click_button(foodpreferencespage.GREEK_XPATH)
    #         preferences_selected.append("Greek")
    #     if random.randint(0, 3) == 0:
    #         foodpreferencespage.click_button(foodpreferencespage.SEAFOOD_XPATH)
    #         preferences_selected.append("Seafood")
    #     if random.randint(0, 3) == 0:
    #         foodpreferencespage.click_button(foodpreferencespage.ORGANIC_XPATH)
    #         preferences_selected.append("Organic")
    #
    #     print("Preferences selected:", preferences_selected)
    #
    #     sleep(20)
    #     foodpreferencespage.click_button(foodpreferencespage.CONTINUE_BUTTON_XPATH)
    #
    #
    # #### Location page ####
    # locationpage = LocationPage(driver)
    #
    # city = gencity()
    # print("Location is set to:", city)
    #
    # sleep(1)
    # assert locationpage.get_text(locationpage.PAGE_TITLE_XPATH) == "Location"
    #
    # # loc_method:
    # # 0 - Skip
    # # 1 - Enable Location Services
    # # 2 - Input postcode
    # loc_method = random.randint(0, 2)
    # if loc_method == 0:
    #     print('will skip')
    #     sleep(1)
    #     locationpage.click_button(locationpage.SKIP_BUTTON_XPATH)
    #     sleep(1)
    #
    # elif loc_method == 1:
    #
    #     print('will use location', city[3], city[4])
    #
    #     driver.set_location(city[3], city[4])
    #
    #     sleep(2)
    #
    #     locationpage.click_button(locationpage.ENABLE_LOCATION_SERVICES_BUTTON_XPATH)
    #     sleep(2)
    #     # print(locationpage.get_text(locationpage.ALLOW_LOCATION_POPUP_XPATH))
    #     # assert locationpage.get_text(locationpage.ALLOW_LOCATION_POPUP_XPATH) == "Allow Foodvine to access this device’s location?"
    #
    #
    #     # allow_loc
    #     # 0 - while using the app
    #     # 1 - only this time
    #     allow_loc = random.randint(0, 1)
    #     if allow_loc == 0:
    #         print('while using the app')
    #         locationpage.click_button(locationpage.WHILE_USING_THE_APP_XPATH)
    #         sleep(1)
    #     elif allow_loc == 1:
    #         print('only this time')
    #         locationpage.click_button(locationpage.ONLY_THIS_TIME_XPATH)
    #         sleep(1)
    #
    # if loc_method == 2:
    #     print('will use postcode', city[2])
    #     sleep(1)
    #     locationpage.click_button(locationpage.ENTER_POSTCODE_BUTTON_XPATH)
    #     sleep(1)
    #
    #     enterpostcodepage = EnterPostcodePage(driver)
    #     assert enterpostcodepage.get_text(enterpostcodepage.PAGE_TITLE_XPATH) == 'Enter postcode'
    #     enterpostcodepage.input_text(enterpostcodepage.ZIP_XPATH, city[2])
    #     sleep(1)
    #     enterpostcodepage.click_button(enterpostcodepage.CONTINUE_BUTTON_XPATH)
    #
    #
    # #### Whats available page ####
    # whatsavailablepage = WhatsAvailablePage(driver)
    #
    # sleep(2)
    #
    # if loc_method==0:
    #     try:
    #         # print("Will try with 3")
    #         assert whatsavailablepage.get_text(whatsavailablepage.PAGE_TITLE_XPATH_3, 300) == "What's available in"
    #         # assert whatsavailablepage.get_text(whatsavailablepage.FARMER_MARKET_XPATH_AVAILABILITY_XPATH_3) == 'Available'
    #         # assert whatsavailablepage.get_text(whatsavailablepage.RECIPES_AVAILABILITY_XPATH_3) == 'Available'
    #         # assert whatsavailablepage.get_text(whatsavailablepage.LIVE_CLASSES_AVAILABILITY_XPATH_3) == 'Available'
    #         # assert whatsavailablepage.get_text(whatsavailablepage.ORDER_FROM_HOME_CHEFS_AVAILABILITY_XPATH_3) == 'Soon'
    #         whatsavailablepage.click_button(whatsavailablepage.FINISH_BUTTON_XPATH_3, 300)
    #     except:
    #         print("Couldnt parse What's available in page with 3")
    #
    # if loc_method==1:
    #     try:
    #         # print("Will try with 3")
    #         assert whatsavailablepage.get_text(whatsavailablepage.PAGE_TITLE_XPATH_3, 300) == "What's available in"
    #         assert whatsavailablepage.get_text(whatsavailablepage.CITY_XPATH_3, 300) == city[1]
    #         assert whatsavailablepage.get_text(whatsavailablepage.FARMER_MARKET_XPATH_AVAILABILITY_XPATH_3, 300) == city[5]
    #         assert whatsavailablepage.get_text(whatsavailablepage.RECIPES_AVAILABILITY_XPATH_3, 300) == city[6]
    #         assert whatsavailablepage.get_text(whatsavailablepage.LIVE_CLASSES_AVAILABILITY_XPATH_3, 300) == city[7]
    #         assert whatsavailablepage.get_text(whatsavailablepage.ORDER_FROM_HOME_CHEFS_AVAILABILITY_XPATH_3, 300) == city[8]
    #         whatsavailablepage.click_button(whatsavailablepage.FINISH_BUTTON_XPATH_3, 300)
    #     except:
    #         print("Couldnt parse What's available in page with 3")
    #
    # if loc_method==2:
    #     try:
    #         # print("Will try with 4")
    #         assert whatsavailablepage.get_text(whatsavailablepage.PAGE_TITLE_XPATH_4, 300) == "What's available in"
    #         assert whatsavailablepage.get_text(whatsavailablepage.CITY_XPATH_4, 300) == city[1]
    #         assert whatsavailablepage.get_text(whatsavailablepage.FARMER_MARKET_XPATH_AVAILABILITY_XPATH_4, 300) == city[5]
    #         assert whatsavailablepage.get_text(whatsavailablepage.RECIPES_AVAILABILITY_XPATH_4, 300) == city[6]
    #         assert whatsavailablepage.get_text(whatsavailablepage.LIVE_CLASSES_AVAILABILITY_XPATH_4, 300) == city[7]
    #         assert whatsavailablepage.get_text(whatsavailablepage.ORDER_FROM_HOME_CHEFS_AVAILABILITY_XPATH_4, 300) == city[8]
    #         whatsavailablepage.click_button(whatsavailablepage.FINISH_BUTTON_XPATH_4, 300)
    #     except:
    #         print("Couldnt parse What's available in page")
    #
    #
    # #### Feed page ####
    # sleep(5)
    # feedpage = FeedPage(driver)
    # try:
    #     print("Page title is ", feedpage.get_text(feedpage.PAGE_TITLE_XPATH))
    #     assert feedpage.get_text(feedpage.PAGE_TITLE_XPATH) == 'Most recent'
    # except:
    #     print("Couldnt parse Feed page")
    #
    #
    #
    #
    # sleep(5)
    #
    # driver = setup()
    #
    # sleep(5)
    #
    #




    #### [Automated test] Login to Foodie Account ####
    #### Landing page ####
    landingpage = LandingPageAndroid(driver)

    landingpage.click_button(landingpage.ALLREADY_HAVE_AN_ACCOUNT_BUTTON_XPATH)
    sleep(2)

    #### Login page ####
    loginpage = LoginPageAndroid(driver)

    # assert loginpage.get_text(loginpage.PAGE_TITLE_XPATH) == "Login"

    un = getuser()[0]
    email = getuser()[1]
    pw = getuser()[2]
    print("Username, email and password are:", un, ',', email, ',', pw)
    loginpage.input_text(loginpage.USERNAME_OR_EMAIL_XPATH, un)
    sleep(1)
    loginpage.input_text(loginpage.PASSWORD_XPATH, pw)
    sleep(1)

    loginpage.click_button(loginpage.LOGIN_BUTTON_XPATH)
    sleep(2)

    # #### Feed page ####
    # sleep(5)
    # feedpage = FeedPageAndroid(driver)
    # try:
    #     print("Page title is ", feedpage.get_text(feedpage.PAGE_TITLE_XPATH))
    #     assert feedpage.get_text(feedpage.PAGE_TITLE_XPATH) == 'Most recent'
    # except:
    #     print("Couldnt parse Feed page")
    #
    # sleep(1)
    # driver.close_app()
    #
    # sleep(1)
    # driver = setup_no_app()
    #
    # sleep(1)
    # startfoodvinefromhomescreen(driver)
    #
    # #### Feed page ####
    # sleep(5)
    # feedpage = FeedPageAndroid(driver)
    # try:
    #     print("Page title is ", feedpage.get_text(feedpage.PAGE_TITLE_XPATH))
    #     assert feedpage.get_text(feedpage.PAGE_TITLE_XPATH) == 'Most recent'
    # except:
    #     print("Couldnt parse Feed page")





    #
    # #### [Automated test] Forgot password ####
    # #### Landing page ####
    # landingpage = LandingPage(driver)
    #
    # landingpage.click_button(landingpage.ALLREADY_HAVE_AN_ACCOUNT_BUTTON_XPATH)
    # sleep(2)
    #
    # #### Login page ####
    # loginpage = LoginPage(driver)
    #
    # assert loginpage.get_text(loginpage.PAGE_TITLE_XPATH) == "Login"
    #
    # loginpage.click_button(loginpage.FORGOT_PASSWORD_BUTTON_XPATH)
    # sleep(1)
    #
    #
    # #### Forgot password page ####
    # sleep(1)
    # forgotpasswordpage = ForgotPasswordPage(driver)
    #
    # assert forgotpasswordpage.get_text(forgotpasswordpage.PAGE_TITLE_XPATH) == "Forgot password"
    #
    # un = getuser()[0]
    # email = getuser()[1]
    # pw = getuser()[2]
    # print("Username, email and password are:", un, ',', email, ',', pw)
    # forgotpasswordpage.input_text(forgotpasswordpage.USERNAME_OR_EMAIL_XPATH, un)
    # forgotpasswordpage.click_button(forgotpasswordpage.SEND_BUTTON_XPATH)
    #
    # sleep(2)
    #
    #
    # #### Phone Number Verification page ####
    # phonenumberverificationpage = PhoneNumberVerificationPage(driver)
    # assert phonenumberverificationpage.get_text(phonenumberverificationpage.PAGE_TITLE_PW_CHANGE_XPATH) == "Phone number verification"
    # sleep(30)
    # sms_code = getsmscode()
    # print('SMS code:', sms_code)
    # phonenumberverificationpage.input_text(phonenumberverificationpage.SMS_CODE_PW_CHANGE_INPUT, sms_code)
    #
    # sleep(2)
    #
    # #### Choose new password page ####
    # choosenewpasswordpage = ChooseNewPasswordPage(driver)
    # assert choosenewpasswordpage.get_text(choosenewpasswordpage.PAGE_TITLE_XPATH) == 'Choose new password'
    #
    # if pw == "1234Test":
    #     pw = "1234Tests"
    # else:
    #     pw = "1234Test"
    # changepw(un, email, pw)
    #
    # print("Username, email and password are now:", un, ',', email, ',', pw)
    #
    # choosenewpasswordpage.input_text(choosenewpasswordpage.NEW_PASSWORD_XPATH, pw)
    # choosenewpasswordpage.input_text(choosenewpasswordpage.REPEAT_NEW_PASSWORD_XPATH, pw)
    # choosenewpasswordpage.click_button(choosenewpasswordpage.CHANGE_PASSWORD_BUTTON_XPATH)
    #
    # sleep(2)
    #
    #
    #
    # #### Login page ####
    # loginpage = LoginPage(driver)
    #
    # assert loginpage.get_text(loginpage.PAGE_TITLE_XPATH) == "Login"
    # assert loginpage.get_text(loginpage.PASSWORD_CHANGE_CONFORMATION) == 'You can now login with your new password'
    #
    #
    # loginpage.input_text(loginpage.USERNAME_OR_EMAIL_XPATH, un)
    # sleep(1)
    # loginpage.input_text(loginpage.PASSWORD_XPATH, pw)
    # sleep(1)
    #
    # loginpage.click_button(loginpage.LOGIN_BUTTON_PW_CHANGE_XPATH)
    #
    # #### Feed page ####
    # sleep(5)
    # feedpage = FeedPage(driver)
    # try:
    #     print("Page title is ", feedpage.get_text(feedpage.PAGE_TITLE_XPATH))
    #     assert feedpage.get_text(feedpage.PAGE_TITLE_XPATH) == 'Most recent'
    # except:
    #     print("Couldnt parse Feed page")
    #
    #
    # sleep(30)


    foodpreferencespage = FoodPreferencesPageAndroid(driver)
    foodpreferencespage.click_button(foodpreferencespage.SKIP_BUTTON_XPATH)
    sleep(1)

    locationpage = LocationPageAndroid(driver)
    locationpage.click_button(locationpage.SKIP_BUTTON_XPATH)
    sleep(1)

    whatsavailablepage = WhatsAvailablePageAndroid(driver)
    whatsavailablepage.click_button(whatsavailablepage.FINISH_BUTTON_XPATH_3, 300)
    sleep(2)




    #### [Automated Test] News Feed Post Creation ####
    #### Feed page ####
    feedpage = FeedPageAndroid(driver)
    feedpage.click_button(feedpage.PLUS_BUTTON_XPATH)
    sleep(2)

    ### Allow pop-up ###
    feedpage.click_button(feedpage.ALLOW_XPATH)
    sleep(2)

    newpostpage = NewPostRecipePageAndroid(driver)
    newpostpage.click_button(newpostpage.X_BUTTON_XPATH)
    sleep(3)
    feedpage.click_button(feedpage.PLUS_BUTTON_XPATH)
    sleep(2)


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
    sleep(1)

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
    serving_number = str(random.randint(0, 12))
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
    minute = str(random.randint(0, 12))
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
    minute = str(random.randint(0, 12))
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
    if random.randint(0, 3) == 0:
        newpostpage.click_button(newpostpage.DIETARY_7_XPATH)

    newpostpage.click_button(newpostpage.SAVE_BUTTON_XPATH)
    sleep(1)

    #### New Post page ####
    newpostpage.click_button(newpostpage.INGREDIENTS_XPATH)
    sleep(1)

    #### Ingredients page ####
    ingredientspage = AddIngredientsPageAndroid(driver)
    if random.randint(0, 3) == 0:
        ingredientspage.click_button(ingredientspage.INGREDIENT_1_XPATH)
        sleep(1)
        ingredientspage.input_text(ingredientspage.INGREDIENT_INPUT_XPATH, str(random.randint(1, 99)))
        ingred_type = random.randint(0, 5)
        if ingred_type == 0:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 1:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 2:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 3:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 4:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 5:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        sleep(2)
        ingredientspage.click_button(ingredientspage.SAVE_INGREDIENT_BUTTON_XPATH)
    if random.randint(0, 3) == 0:
        ingredientspage.click_button(ingredientspage.INGREDIENT_2_XPATH)
        sleep(1)
        ingredientspage.input_text(ingredientspage.INGREDIENT_INPUT_XPATH, str(random.randint(1, 99)))
        ingred_type = random.randint(0, 5)
        if ingred_type == 0:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 1:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 2:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 3:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 4:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 5:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        sleep(2)
        ingredientspage.click_button(ingredientspage.SAVE_INGREDIENT_BUTTON_XPATH)
    if random.randint(0, 3) == 0:
        ingredientspage.click_button(ingredientspage.INGREDIENT_3_XPATH)
        sleep(1)
        ingredientspage.input_text(ingredientspage.INGREDIENT_INPUT_XPATH, str(random.randint(1, 99)))
        ingred_type = random.randint(0, 5)
        if ingred_type == 0:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 1:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 2:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 3:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 4:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 5:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        sleep(2)
        ingredientspage.click_button(ingredientspage.SAVE_INGREDIENT_BUTTON_XPATH)
    if random.randint(0, 3) == 0:
        ingredientspage.click_button(ingredientspage.INGREDIENT_4_XPATH)
        sleep(1)
        ingredientspage.input_text(ingredientspage.INGREDIENT_INPUT_XPATH, str(random.randint(1, 99)))
        ingred_type = random.randint(0, 5)
        if ingred_type == 0:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 1:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 2:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 3:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 4:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 5:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        sleep(1)
        ingredientspage.click_button(ingredientspage.SAVE_INGREDIENT_BUTTON_XPATH)
    if random.randint(0, 3) == 0:
        ingredientspage.click_button(ingredientspage.INGREDIENT_5_XPATH)
        sleep(1)
        ingredientspage.input_text(ingredientspage.INGREDIENT_INPUT_XPATH, str(random.randint(1, 99)))
        ingred_type = random.randint(0, 5)
        if ingred_type == 0:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 1:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 2:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 3:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 4:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 5:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        sleep(1)
        ingredientspage.click_button(ingredientspage.SAVE_INGREDIENT_BUTTON_XPATH)
    if random.randint(0, 3) == 0:
        ingredientspage.click_button(ingredientspage.INGREDIENT_6_XPATH)
        sleep(1)
        ingredientspage.input_text(ingredientspage.INGREDIENT_INPUT_XPATH, str(random.randint(1, 99)))
        ingred_type = random.randint(0, 5)
        if ingred_type == 0:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 1:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 2:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 3:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 4:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 5:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        sleep(1)
        ingredientspage.click_button(ingredientspage.SAVE_INGREDIENT_BUTTON_XPATH)
    if random.randint(0, 3) == 0:
        ingredientspage.click_button(ingredientspage.INGREDIENT_7_XPATH)
        sleep(1)
        ingredientspage.input_text(ingredientspage.INGREDIENT_INPUT_XPATH, str(random.randint(1, 99)))
        ingred_type = random.randint(0, 5)
        if ingred_type == 0:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 1:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 2:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 3:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 4:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        elif ingred_type == 5:
            ingredientspage.click_button(ingredientspage.POUND_XPATH)
        sleep(1)
        ingredientspage.click_button(ingredientspage.SAVE_INGREDIENT_BUTTON_XPATH)

    sleep(1)
    newpostpage.click_button(newpostpage.SAVE_BUTTON_XPATH)

    sleep(1)

    #### New Post page ####
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
    newpostpage.swipe_up()
    sleep(1)
    newpostpage.click_button(newpostpage.PREVIEW_BUTTON_XPATH)
    sleep(1)

    #### Preview Post page ####
    previewpostpage = PreviewPostPageAndroid(driver)
    previewpostpage.click_button(previewpostpage.POST_BUTTON_XPATH)
    sleep(2)

