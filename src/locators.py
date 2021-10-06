from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Locators:
    @staticmethod
    def find_element(driver, locator):
        el = WebDriverWait(driver, 10).until(ec.visibility_of_element_located(locator))
        return el

    @staticmethod
    def click_element(el):
        el.click()

    @staticmethod
    def fill_field(el, value):
        el.send_keys(value)

    @staticmethod
    def move_to_element(driver, el):
        action = ActionChains(driver)
        action.move_to_element(el).click().perform()
