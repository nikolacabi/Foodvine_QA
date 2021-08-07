from appium.webdriver import webdriver
from time import sleep
from pages.page import Page
from datetime import datetime


class AddIngredientsPageAndroid(Page):
    # def __init__(self, driver):
    #     super().__init__(driver)

    driver: webdriver = None

    PAGE_TITLE_XPATH = "//*[@class='android.widget.TextView' and ./parent::*[@class='android.view.ViewGroup'] and (./preceding-sibling::* | ./following-sibling::*)[./*[@class='android.widget.Button']] and (./preceding-sibling::* | ./following-sibling::*)[./*[@text]]]"

    SAVE_BUTTON_XPATH = "//*[@text='Save']"

    INGREDIENT_1_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*/*/*[@class='android.view.ViewGroup' and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[1]"
    INGREDIENT_2_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*/*/*[@class='android.view.ViewGroup' and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[2]"
    INGREDIENT_3_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*/*/*[@class='android.view.ViewGroup' and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[3]"
    INGREDIENT_4_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*/*/*[@class='android.view.ViewGroup' and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[4]"
    INGREDIENT_5_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*/*/*[@class='android.view.ViewGroup' and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[5]"
    INGREDIENT_6_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*/*/*[@class='android.view.ViewGroup' and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[6]"
    INGREDIENT_7_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*/*/*[@class='android.view.ViewGroup' and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[7]"


    ### Ingredient pop-up ###

    SAVE_INGREDIENT_BUTTON_XPATH = "//*[@class='android.widget.Button' and ./*[@text] and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.EditText']]]"

    INGREDIENT_INPUT_XPATH = "//*[@class='android.widget.EditText' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.view.ViewGroup']]"

    POUND_XPATH =       "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.HorizontalScrollView']]/*/*[@class='android.view.ViewGroup' and ./*[./*[@class='android.view.ViewGroup' and ./*[@text]]]])[1]"
    GALLON_XPATH =      "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.HorizontalScrollView']]/*/*[@class='android.view.ViewGroup' and ./*[./*[@class='android.view.ViewGroup' and ./*[@text]]]])[2]"
    QUART_XPATH =       "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.HorizontalScrollView']]/*/*[@class='android.view.ViewGroup' and ./*[./*[@class='android.view.ViewGroup' and ./*[@text]]]])[3]"
    TEASPOON_XPATH =    "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.HorizontalScrollView']]/*/*[@class='android.view.ViewGroup' and ./*[./*[@class='android.view.ViewGroup' and ./*[@text]]]])[4]"
    TABLESPOON_XPATH =  "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.HorizontalScrollView']]/*/*[@class='android.view.ViewGroup' and ./*[./*[@class='android.view.ViewGroup' and ./*[@text]]]])[5]"


class AddIngredientsPageiOS(Page):
    # def __init__(self, driver):
    #     super().__init__(driver)

    driver: webdriver = None

