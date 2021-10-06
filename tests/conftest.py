from src.driver_factory import DriverFactory
from data.locators import BasePage
import pytest


@pytest.fixture
def driver():
    driver = DriverFactory.get_driver(BasePage.browser, BasePage.headless_mode)
    return driver
