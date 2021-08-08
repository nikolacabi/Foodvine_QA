from appium.webdriver import webdriver
from time import sleep
from pages.page import Page
from datetime import datetime


class NewPostPageAndroid(Page):
    # def __init__(self, driver):
    #     super().__init__(driver)

    driver: webdriver = None

    PAGE_TITLE_XPATH = "//*[@text='New Post']"

    X_BUTTON_XPATH = "//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and ./*[@class='android.view.ViewGroup'] and (./preceding-sibling::* | ./following-sibling::*)[@text='New Post']]"

    SELECT_MULTIPLE_XPATH = "//*[@text='Select multiple']"

    RECIPE_XPATH = "//*[@text='Recipe']"

    MEDIA_1_XPATH = "((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[1]/*/*/*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']])[1]"

    MEDIA_2_XPATH = "((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[1]/*/*/*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']])[2]"

    MEDIA_3_XPATH = "((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[1]/*/*/*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']])[3]"

    NEXT_BUTTON_XPATH = "//*[@class='android.widget.Button']"

    ADD_TAGS_XPATH = "//*[@text='Add tags (optional)']"


class NewPostRecipePageAndroid(Page):

    PAGE_TITLE_XPATH = "//*[@text and ./parent::*[@class='android.view.ViewGroup'] and (./preceding-sibling::* | ./following-sibling::*)[./*[@class='android.widget.Button']] and (./preceding-sibling::* | ./following-sibling::*)[./*[@class='android.view.ViewGroup']]]"

    X_BUTTON_XPATH = "//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and ./*[@class='android.view.ViewGroup'] and (./preceding-sibling::* | ./following-sibling::*)[@text='New Post']]"

    PREVIEW_BUTTON_XPATH = "//*[@class='android.widget.Button']"

    RECIPE_XPATH = "//*[@text='Recipe']"

    ADD_PHOTO_OR_VIDEO_XPATH = "//*[@text='Add photos or videos']"

    TITLE_XPATH =       "//*[@class='android.view.ViewGroup' and ./*[@text='Required'] and (./preceding-sibling::* | ./following-sibling::*)[@text='Title']]"

    DESCRIPTION_XPATH = "//*[@class='android.view.ViewGroup' and ./*[@text='Required'] and (./preceding-sibling::* | ./following-sibling::*)[@text='Description']]"

    ADD_TAGS_XPATH = "//*[@text='Add tags (optional)']"

    DIFFICULTY_XPATH = "//*[@text='Add Difficulty']"

    SERVINGS_XPATH = "//*[@text='Add Servings']"

    PREP_TIME_XPATH = "//*[@text='Add prep time']"

    def swipe_down(self):
        self.driver.swipe(start_x=1000, start_y=1800, end_x=1000, end_y=400, duration=200)

    def swipe_up(self):
        self.driver.swipe(start_x=1000, start_y=400, end_x=1000, end_y=1800, duration=200)

    COOK_TIME_XPATH = "//*[@text='Add cook time']"

    ALLERGENS_XPATH = "//*[@text='Add allergens (optional)']"

    DIETARY_INFO_XPATH = "//*[@text='Add dietary info (optional)']"

    INGREDIENTS_XPATH = "//*[@text='Add ingredients']"

    STEP_TITLE_XPATH = "//*[@text='Add step title']"

    STEP_DESCRIPTION_XPATH = "//*[@text='Add what should be done in this step']"

    ADD_PHOTO_TO_STEP = "//*[@text='Add photos (optional)']"

    ADD_ANOTHER_STEP = "//*[@text='+ Add another step']"

    STEP_2_TITLE_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*/*/*/*/*[@text and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']] and (./preceding-sibling::* | ./following-sibling::*)[./*[@text]]]]])[2]"

    STEP_2_DESCRIPTION_XPATH = "((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[6]/*/*/*[@text and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']]])[2]"

    ADD_PHOTO_TO_STEP_2 = "(((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[6]/*[@class='android.view.ViewGroup'])[3]/*/*/*[@text and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']]])[1]"


    ### Choose media pop-up ###

    X_BUTTON_MEDIA_XPATH = "//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.Button']]"

    SELECT_MULTIPLE_XPATH = "//*[@text='Select multiple']"

    MEDIA_1_XPATH = "((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]]/*[@class='android.view.ViewGroup'])[1]/*/*/*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']])[1]"

    MEDIA_2_XPATH = "((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]]/*[@class='android.view.ViewGroup'])[1]/*/*/*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']])[2]"

    MEDIA_3_XPATH = "((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]]/*[@class='android.view.ViewGroup'])[1]/*/*/*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']])[3]"


    ### Difficulty pop-up ###

    INTERMEDIATE_XPATH =    "//*[@class='android.view.ViewGroup' and ./*[@class='android.view.ViewGroup' and ./*[@text='Intermediate'] and ./*[@class='android.view.ViewGroup']]]"

    ADVANCE_XPATH =         "//*[@class='android.view.ViewGroup' and ./*[@class='android.view.ViewGroup' and ./*[@class='android.view.ViewGroup'] and ./*[@text='Advanced']]]"

    BEGINNER_XPATH =        "//*[@class='android.view.ViewGroup' and ./*[@class='android.view.ViewGroup' and ./*[@text='Beginner'] and ./*[@class='android.view.ViewGroup']]]"

    # Shared between pop-ups
    SAVE_BUTTON_XPATH = "//*[@class='android.widget.Button' and ./*[@text='Save']]"


    ### Servings pop-up ###

    SERVING_NUMBER_XPATH = "//*[@class='android.widget.Spinner']"

    # Shared between pop-ups
    def set_list(self, num_to_set):
        return "//*[@text='" + num_to_set + "']"


    ### Prep time / Cook time pop-up ###

    TIMING_TITLE_XPATH = "//*[@text and ./parent::*[@class='android.view.ViewGroup'] and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]"
    TIMING_TITLE_XPATH = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView"

    # HOUR_XPATH =    "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and (./preceding-sibling::* | ./following-sibling::*)[@contentDescription='Close modal']]]/*[@class='android.widget.Spinner'])[1]"
    HOUR_XPATH =    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]"

    # MIN_XPATH =     "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and (./preceding-sibling::* | ./following-sibling::*)[@contentDescription='Close modal']]]/*[@class='android.widget.Spinner'])[2]"
    MIN_XPATH =     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]"

    ### Allergens pop-up ###

    ALLERGEN_1_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]]/*/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[1]"
    ALLERGEN_2_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]]/*/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[2]"
    ALLERGEN_3_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]]/*/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[3]"
    ALLERGEN_4_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]]/*/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[4]"
    ALLERGEN_5_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]]/*/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[5]"
    ALLERGEN_6_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]]/*/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[6]"
    ALLERGEN_7_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]]/*/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[7]"
    ALLERGEN_8_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]]/*/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[8]"
    ALLERGEN_9_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]]/*/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[9]"


    ### Dietary info ###

    DIETARY_1_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]]/*/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[1]"
    DIETARY_2_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]]/*/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[2]"
    DIETARY_3_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]]/*/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[3]"
    DIETARY_4_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]]/*/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[4]"
    DIETARY_5_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]]/*/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[5]"
    DIETARY_6_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]]/*/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[6]"




class NewPostPageiOS(Page):
    # def __init__(self, driver):
    #     super().__init__(driver)

    driver: webdriver = None

    PAGE_TITLE_XPATH = "//*[@text='New Post']"

    X_BUTTON_XPATH = "(//*[@text='New Post Next' and ./parent::*[@text='New Post Next' and ./parent::*[@text='New Post Next']]]/*/*[@class='UIAView' and ./parent::*[@class='UIAView']])[1]"

    SELECT_MULTIPLE_XPATH = "//*[@text='Select multiple']"

    RECIPE_XPATH = "//*[@text='Recipe']"

    MEDIA_1_XPATH = "(((//*[@class='UIAScrollView' and ./parent::*[@text='Horizontal scroll bar, 1 page']]/*[@class='UIAView'])[1]/*/*[@class='UIAView' and ./parent::*[@class='UIAView']])[1]/*[@class='UIAView' and ./*[@class='UIAView']])[1]"

    MEDIA_2_XPATH = "(((//*[@class='UIAScrollView' and ./parent::*[@text='Horizontal scroll bar, 1 page']]/*[@class='UIAView'])[1]/*/*[@class='UIAView' and ./parent::*[@class='UIAView']])[1]/*[@class='UIAView' and ./*[@class='UIAView']])[2]"

    MEDIA_3_XPATH = "(((//*[@class='UIAScrollView' and ./parent::*[@text='Horizontal scroll bar, 1 page']]/*[@class='UIAView'])[1]/*/*[@class='UIAView' and ./parent::*[@class='UIAView']])[1]/*[@class='UIAView' and ./*[@class='UIAView']])[3]"

    NEXT_BUTTON_XPATH = "//*[@class='UIAButton']"




class NewPostRecipePageiOS(Page):

    PAGE_TITLE_XPATH = "//*[@text and ./parent::*[@class='android.view.ViewGroup'] and (./preceding-sibling::* | ./following-sibling::*)[./*[@class='android.widget.Button']] and (./preceding-sibling::* | ./following-sibling::*)[./*[@class='android.view.ViewGroup']]]"

    X_BUTTON_XPATH = "//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and ./*[@class='android.view.ViewGroup'] and (./preceding-sibling::* | ./following-sibling::*)[@text='New Post']]"

    PREVIEW_BUTTON_XPATH = "//*[@class='android.widget.Button']"

    RECIPE_XPATH = "//*[@text='Recipe']"

    ADD_PHOTO_OR_VIDEO_XPATH = "//*[@text='Add photos or videos']"

    TITLE_XPATH =       "//*[@class='android.view.ViewGroup' and ./*[@text='Required'] and (./preceding-sibling::* | ./following-sibling::*)[@text='Title']]"

    DESCRIPTION_XPATH = "//*[@class='android.view.ViewGroup' and ./*[@text='Required'] and (./preceding-sibling::* | ./following-sibling::*)[@text='Description']]"

    ADD_TAGS_XPATH = "//*[@text='Add tags (optional)']"

    DIFFICULTY_XPATH = "//*[@text='Add Difficulty']"

    SERVINGS_XPATH = "//*[@text='Add Servings']"

    PREP_TIME_XPATH = "//*[@text='Add prep time']"

    def swipe_down(self):
        self.driver.swipe(start_x=1000, start_y=1800, end_x=1000, end_y=400, duration=200)

    def swipe_up(self):
        self.driver.swipe(start_x=1000, start_y=400, end_x=1000, end_y=1800, duration=200)

    COOK_TIME_XPATH = "//*[@text='Add cook time']"

    ALLERGENS_XPATH = "//*[@text='Add allergens (optional)']"

    DIETARY_INFO_XPATH = "//*[@text='Add dietary info (optional)']"

    INGREDIENTS_XPATH = "//*[@text='Add ingredients']"

    STEP_TITLE_XPATH = "//*[@text='Add step title']"

    STEP_DESCRIPTION_XPATH = "//*[@text='Add what should be done in this step']"

    ADD_PHOTO_TO_STEP = "//*[@text='Add photos (optional)']"

    ADD_ANOTHER_STEP = "//*[@text='+ Add another step']"

    STEP_2_TITLE_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*/*/*/*/*[@text and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']] and (./preceding-sibling::* | ./following-sibling::*)[./*[@text]]]]])[2]"

    STEP_2_DESCRIPTION_XPATH = "((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[6]/*/*/*[@text and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']]])[2]"

    ADD_PHOTO_TO_STEP_2 = "(((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[6]/*[@class='android.view.ViewGroup'])[3]/*/*/*[@text and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']]])[1]"


    ### Choose media pop-up ###

    X_BUTTON_MEDIA_XPATH = "//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.Button']]"

    SELECT_MULTIPLE_XPATH = "//*[@text='Select multiple']"

    MEDIA_1_XPATH = "((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]]/*[@class='android.view.ViewGroup'])[1]/*/*/*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']])[1]"

    MEDIA_2_XPATH = "((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]]/*[@class='android.view.ViewGroup'])[1]/*/*/*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']])[2]"

    MEDIA_3_XPATH = "((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]]/*[@class='android.view.ViewGroup'])[1]/*/*/*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']])[3]"


    ### Difficulty pop-up ###

    INTERMEDIATE_XPATH =    "//*[@class='android.view.ViewGroup' and ./*[@class='android.view.ViewGroup' and ./*[@text='Intermediate'] and ./*[@class='android.view.ViewGroup']]]"

    ADVANCE_XPATH =         "//*[@class='android.view.ViewGroup' and ./*[@class='android.view.ViewGroup' and ./*[@class='android.view.ViewGroup'] and ./*[@text='Advanced']]]"

    BEGINNER_XPATH =        "//*[@class='android.view.ViewGroup' and ./*[@class='android.view.ViewGroup' and ./*[@text='Beginner'] and ./*[@class='android.view.ViewGroup']]]"

    # Shared between pop-ups
    SAVE_BUTTON_XPATH = "//*[@class='android.widget.Button' and ./*[@text='Save']]"


    ### Servings pop-up ###

    SERVING_NUMBER_XPATH = "//*[@class='android.widget.Spinner']"

    # Shared between pop-ups
    def set_list(self, num_to_set):
        return "//*[@text='" + num_to_set + "']"


    ### Prep time / Cook time pop-up ###

    TIMING_TITLE_XPATH = "//*[@text and ./parent::*[@class='android.view.ViewGroup'] and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]"
    TIMING_TITLE_XPATH = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView"

    # HOUR_XPATH =    "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and (./preceding-sibling::* | ./following-sibling::*)[@contentDescription='Close modal']]]/*[@class='android.widget.Spinner'])[1]"
    HOUR_XPATH =    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]"

    # MIN_XPATH =     "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and (./preceding-sibling::* | ./following-sibling::*)[@contentDescription='Close modal']]]/*[@class='android.widget.Spinner'])[2]"
    MIN_XPATH =     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]"

    ### Allergens pop-up ###

    ALLERGEN_1_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]]/*/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[1]"
    ALLERGEN_2_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]]/*/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[2]"
    ALLERGEN_3_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]]/*/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[3]"
    ALLERGEN_4_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]]/*/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[4]"
    ALLERGEN_5_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]]/*/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[5]"
    ALLERGEN_6_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]]/*/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[6]"
    ALLERGEN_7_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]]/*/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[7]"
    ALLERGEN_8_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]]/*/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[8]"
    ALLERGEN_9_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]]/*/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[9]"


    ### Dietary info ###

    DIETARY_1_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]]/*/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[1]"
    DIETARY_2_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]]/*/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[2]"
    DIETARY_3_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]]/*/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[3]"
    DIETARY_4_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]]/*/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[4]"
    DIETARY_5_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]]/*/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[5]"
    DIETARY_6_XPATH = "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.Button']]]/*/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and ./*[./*[@text] and ./*[@class='android.view.ViewGroup']]])[6]"

