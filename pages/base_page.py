from src.urls import Urls


def title(driver):
    return Urls.title(driver)


def open_page(driver, url):
    Urls.open(driver, url)
