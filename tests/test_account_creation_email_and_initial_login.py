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



#@pytest.mark.dependency()
@pytest.mark.timeout(600)
def test_account_creation_with_email_and_randomized_initial_login():

    driver = setup()

    #### [Automated Test] Foodie account creation with email ####
    #### Landing page ####
    landingpage = LandingPage(driver)

    assert landingpage.get_text(landingpage.CAROUSEL_TEXT_XPATH) == "Authentic food from local farmers and home chefs"
    landingpage.swipe_right_to_left()
    sleep(1)
    assert landingpage.get_text(landingpage.CAROUSEL_TEXT_XPATH) == "Explore behind the scenes content, recipes and more"
    landingpage.swipe_right_to_left()
    sleep(1)
    assert landingpage.get_text(landingpage.CAROUSEL_TEXT_XPATH) == "Follow your favorites, and build a following with your own content"
    landingpage.swipe_right_to_left()
    sleep(1)
    assert landingpage.get_text(landingpage.CAROUSEL_TEXT_XPATH) == "Join a community of small producers, home chefs and foodies like you"

    landingpage.click_button(landingpage.JOIN_FOR_FREE_BUTTON_XPATH)
    sleep(2)
    landingpage.click_button(landingpage.SIGN_UP_WITH_EMAIL_BUTTON_XPATH)
    sleep(2)


    #### Account Details page ####
    accountdetailspage = AccountDetailsPage(driver)

    sleep(1)
    assert accountdetailspage.get_text(accountdetailspage.PAGE_TITLE_XPATH) == "Account details"
    accountdetailspage.input_text(accountdetailspage.FIRST_NAME_XPATH, "Nikola")
    sleep(1)
    accountdetailspage.input_text(accountdetailspage.LAST_NAME_XPATH, "Pavicevic")
    sleep(1)
    accountdetailspage.input_text(accountdetailspage.PHONE_XPATH, "6054094539")
    sleep(1)
    un = genuser()[0]
    email = genuser()[1]
    pw = genuser()[2]
    print("Username, email and password are:", un, ',', email, ',', pw)
    accountdetailspage.input_text(accountdetailspage.EMAIL_XPATH, email)
    sleep(1)
    accountdetailspage.input_text(accountdetailspage.USERNAME_XPATH, un)
    sleep(1)
    accountdetailspage.input_text(accountdetailspage.PASSWORD_XPATH, pw)
    sleep(1)
    accountdetailspage.click_button(accountdetailspage.CONTINUE_BUTTON_XPATH)


    #### Phone Number Verification page ####
    phonenumberverificationpage = PhoneNumberVerificationPage(driver)

    sleep(2)

    assert phonenumberverificationpage.get_text(phonenumberverificationpage.PAGE_TITLE_XPATH) == "Phone number verification"
    sms_code = getsmscode()
    print('SMS code:', sms_code)
    phonenumberverificationpage.input_text(phonenumberverificationpage.SMS_CODE_INPUT, sms_code)


    #### Food Preferences page ####
    foodpreferencespage = FoodPreferencesPage(driver)

    sleep(2)
    assert foodpreferencespage.get_text(foodpreferencespage.PAGE_TITLE_XPATH) == "Food preferences"
    # saveuser(un, email, pw)


    sleep(2)


    #### [Automated Test] Initial Login to Foodie Account ####
    #### Food Preferences page ####
    preferences_selected = []
    if random.randint(0, 4) == 0:
        foodpreferencespage.click_button(foodpreferencespage.SKIP_BUTTON_XPATH)
    else:
        if random.randint(0, 3) == 0:
            foodpreferencespage.click_button(foodpreferencespage.AFRICAN_XPATH)
            preferences_selected.append("African")
        if random.randint(0, 3) == 0:
            foodpreferencespage.click_button(foodpreferencespage.ASIAN_XPATH)
            preferences_selected.append("Asian")
        if random.randint(0, 3) == 0:
            foodpreferencespage.click_button(foodpreferencespage.CARIBBEAN_XPATH)
            preferences_selected.append("Caribbean")
        if random.randint(0, 3) == 0:
            foodpreferencespage.click_button(foodpreferencespage.MEXICAN_XPATH)
            preferences_selected.append("Mexican")
        if random.randint(0, 3) == 0:
            foodpreferencespage.click_button(foodpreferencespage.THAI_XPATH)
            preferences_selected.append("Thai")
        if random.randint(0, 3) == 0:
            foodpreferencespage.click_button(foodpreferencespage.ITALIAN_XPATH)
            preferences_selected.append("Italian")
        if random.randint(0, 3) == 0:
            foodpreferencespage.click_button(foodpreferencespage.GREEK_XPATH)
            preferences_selected.append("Greek")
        if random.randint(0, 3) == 0:
            foodpreferencespage.click_button(foodpreferencespage.SEAFOOD_XPATH)
            preferences_selected.append("Seafood")
        if random.randint(0, 3) == 0:
            foodpreferencespage.click_button(foodpreferencespage.ORGANIC_XPATH)
            preferences_selected.append("Organic")

        print("Preferences selected:", preferences_selected)

        sleep(2)
        foodpreferencespage.click_button(foodpreferencespage.CONTINUE_BUTTON_XPATH)


    #### Location page ####
    locationpage = LocationPage(driver)

    city = gencity()
    print("Location is set to:", city)

    sleep(1)
    assert locationpage.get_text(locationpage.PAGE_TITLE_XPATH) == "Location"

    # loc_method:
    # 0 - Skip
    # 1 - Enable Location Services
    # 2 - Input postcode
    loc_method = random.randint(0, 2)
    if loc_method == 0:
        print('will skip')
        sleep(1)
        locationpage.click_button(locationpage.SKIP_BUTTON_XPATH)
        sleep(1)

    elif loc_method == 1:

        print('will use location', city[3], city[4])

        driver.set_location(city[3], city[4])

        sleep(2)

        locationpage.click_button(locationpage.ENABLE_LOCATION_SERVICES_BUTTON_XPATH)
        sleep(2)
        # print(locationpage.get_text(locationpage.ALLOW_LOCATION_POPUP_XPATH))
        # assert locationpage.get_text(locationpage.ALLOW_LOCATION_POPUP_XPATH) == "Allow Foodvine to access this device’s location?"


        # allow_loc
        # 0 - while using the app
        # 1 - only this time
        allow_loc = random.randint(0, 1)
        if allow_loc == 0:
            print('while using the app')
            locationpage.click_button(locationpage.WHILE_USING_THE_APP_XPATH)
            sleep(1)
        elif allow_loc == 1:
            print('only this time')
            locationpage.click_button(locationpage.ONLY_THIS_TIME_XPATH)
            sleep(1)

    if loc_method == 2:
        print('will use postcode', city[2])
        sleep(1)
        locationpage.click_button(locationpage.ENTER_POSTCODE_BUTTON_XPATH)
        sleep(1)

        enterpostcodepage = EnterPostcodePage(driver)
        assert enterpostcodepage.get_text(enterpostcodepage.PAGE_TITLE_XPATH) == 'Enter postcode'
        enterpostcodepage.input_text(enterpostcodepage.ZIP_XPATH, city[2])
        sleep(1)
        enterpostcodepage.click_button(enterpostcodepage.CONTINUE_BUTTON_XPATH)


    #### Whats available page ####
    whatsavailablepage = WhatsAvailablePage(driver)

    sleep(2)

    if loc_method==0:
        try:
            # print("Will try with 3")
            assert whatsavailablepage.get_text(whatsavailablepage.PAGE_TITLE_XPATH_3, 300) == "What's available in"
            # assert whatsavailablepage.get_text(whatsavailablepage.FARMER_MARKET_XPATH_AVAILABILITY_XPATH_3) == 'Available'
            # assert whatsavailablepage.get_text(whatsavailablepage.RECIPES_AVAILABILITY_XPATH_3) == 'Available'
            # assert whatsavailablepage.get_text(whatsavailablepage.LIVE_CLASSES_AVAILABILITY_XPATH_3) == 'Available'
            # assert whatsavailablepage.get_text(whatsavailablepage.ORDER_FROM_HOME_CHEFS_AVAILABILITY_XPATH_3) == 'Soon'
            whatsavailablepage.click_button(whatsavailablepage.FINISH_BUTTON_XPATH_3, 300)
        except:
            print("Couldnt parse What's available in page with 3")

    if loc_method==1:
        try:
            # print("Will try with 3")
            assert whatsavailablepage.get_text(whatsavailablepage.PAGE_TITLE_XPATH_3, 300) == "What's available in"
            assert whatsavailablepage.get_text(whatsavailablepage.CITY_XPATH_3, 300) == city[1]
            assert whatsavailablepage.get_text(whatsavailablepage.FARMER_MARKET_XPATH_AVAILABILITY_XPATH_3, 300) == city[5]
            assert whatsavailablepage.get_text(whatsavailablepage.RECIPES_AVAILABILITY_XPATH_3, 300) == city[6]
            assert whatsavailablepage.get_text(whatsavailablepage.LIVE_CLASSES_AVAILABILITY_XPATH_3, 300) == city[7]
            assert whatsavailablepage.get_text(whatsavailablepage.ORDER_FROM_HOME_CHEFS_AVAILABILITY_XPATH_3, 300) == city[8]
            whatsavailablepage.click_button(whatsavailablepage.FINISH_BUTTON_XPATH_3, 300)
        except:
            print("Couldnt parse What's available in page with 3")

    if loc_method==2:
        try:
            # print("Will try with 4")
            assert whatsavailablepage.get_text(whatsavailablepage.PAGE_TITLE_XPATH_4, 300) == "What's available in"
            assert whatsavailablepage.get_text(whatsavailablepage.CITY_XPATH_4, 300) == city[1]
            assert whatsavailablepage.get_text(whatsavailablepage.FARMER_MARKET_XPATH_AVAILABILITY_XPATH_4, 300) == city[5]
            assert whatsavailablepage.get_text(whatsavailablepage.RECIPES_AVAILABILITY_XPATH_4, 300) == city[6]
            assert whatsavailablepage.get_text(whatsavailablepage.LIVE_CLASSES_AVAILABILITY_XPATH_4, 300) == city[7]
            assert whatsavailablepage.get_text(whatsavailablepage.ORDER_FROM_HOME_CHEFS_AVAILABILITY_XPATH_4, 300) == city[8]
            whatsavailablepage.click_button(whatsavailablepage.FINISH_BUTTON_XPATH_4, 300)
        except:
            print("Couldnt parse What's available in page")


    #### Feed page ####
    sleep(5)
    feedpage = FeedPage(driver)
    try:
        print("Page title is ", feedpage.get_text(feedpage.PAGE_TITLE_XPATH))
        assert feedpage.get_text(feedpage.PAGE_TITLE_XPATH) == 'Most recent'
    except:
        print("Couldnt parse Feed page")


    driver.close_app()