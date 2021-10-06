from selenium.webdriver.common.by import By


class BasePage:
    url = "https://kadrtour.com/"
    browser = "chrome"
    headless_mode = False


class Language:
    arm_lang = (By.XPATH, "//a[3]/img")
