class Urls:
    @staticmethod
    def open(driver, url):
        driver.get(url)

    @staticmethod
    def title(driver):
        return driver.title
