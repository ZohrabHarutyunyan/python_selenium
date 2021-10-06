from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from os import devnull


class DriverFactory:
    @staticmethod
    def get_driver(browser, headless_mode=False):
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--disable-logging")
            if headless_mode is True:
                options.add_argument("--headless")
            driver = webdriver.Chrome(ChromeDriverManager().install(),
                                      chrome_options=options)
            return driver
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            if headless_mode is True:
                options.headless = True
            driver = webdriver.Firefox(
                executable_path=GeckoDriverManager().install(),
                options=options, service_log_path=devnull)
            return driver
        raise Exception("The browser name is invalid")
