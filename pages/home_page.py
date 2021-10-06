from pages.base_page import open_page, title
from data.locators import BasePage, Language
from src.locators import Locators


def home(driver):
    open_page(driver, BasePage.url)


def get_title(driver):
    title_ = title(driver)
    return title_


def click_lang_element(driver):
    el = Locators.find_element(driver, Language.arm_lang)
    Locators.click_element(el)
