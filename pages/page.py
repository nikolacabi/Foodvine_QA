from appium.webdriver import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class Page:

    driver: webdriver = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # Positioning according to xpath
    def find_xpath(self, locator, wait=10):
        try:
            # The location of a single element gets the location of a single element
            self.driver.implicitly_wait(wait)
            return self.driver.find_element_by_xpath(locator)
        except:
            # To locate multiple same xpath elements, you can get a list. You can use the list query for the location of a specific element (xpath is the only location, generally it is not necessary to use this method)
            self.driver.implicitly_wait(wait)
            return self.driver.find_elements(locator)

    def get_text(self, TXT_XPATH, wait=10):
        assert self.find_xpath(TXT_XPATH, wait).is_displayed()
        return self.find_xpath(TXT_XPATH, wait).text

    def click_button(self, BTN_XPATH, wait=10):
        self.find_xpath(BTN_XPATH, wait).click()

    def input_text(self, TXT_FIELD_XPATH, text):
        self.find_xpath(TXT_FIELD_XPATH).send_keys(text)
