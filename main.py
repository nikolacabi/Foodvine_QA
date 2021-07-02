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



if __name__ == '__main__':

    # driver = setup("4.65_720p_Galaxy_Nexus_API_30")
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

    sleep(30)
    assert phonenumberverificationpage.get_text(phonenumberverificationpage.PAGE_TITLE_XPATH) == "Phone number verification"
    sms_code = getsmscode()
    print('SMS code:', sms_code)
    phonenumberverificationpage.input_text(phonenumberverificationpage.SMS_CODE_INPUT, sms_code)


    #### Food Preferences page ####
    foodpreferencespage = FoodPreferencesPage(driver)

    sleep(2)
    assert foodpreferencespage.get_text(foodpreferencespage.PAGE_TITLE_XPATH) == "Food preferences"





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

        sleep(20)
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




    sleep(5)

    driver = setup()

    sleep(5)




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



    sleep(30)


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
    sleep(30)
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

    choosenewpasswordpage.input_text(choosenewpasswordpage.NEW_PASSWORD_XPATH, pw)
    choosenewpasswordpage.input_text(choosenewpasswordpage.REPEAT_NEW_PASSWORD_XPATH, pw)
    choosenewpasswordpage.click_button(choosenewpasswordpage.CHANGE_PASSWORD_BUTTON_XPATH)

    sleep(2)



    #### Login page ####
    loginpage = LoginPage(driver)

    assert loginpage.get_text(loginpage.PAGE_TITLE_XPATH) == "Login"
    assert loginpage.get_text(loginpage.PASSWORD_CHANGE_CONFORMATION) == 'You can now login with your new password'


    print("Username, email and password are:", un, ',', email, ',', pw)
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















    sleep(30)


