from time import sleep


def startfoodvinefromhomescreen(driver):

    # swipe to show all apps
    driver.swipe(start_x=500, start_y=2000, end_x=500, end_y=400, duration=200)
    sleep(4)


    # start Foodvine
    accessibility_id = "Foodvine"
    element = driver.find_element_by_accessibility_id(accessibility_id)
    element.click()
    sleep(7)