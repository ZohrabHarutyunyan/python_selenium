from pages.home_page import *


class TestHomePage:
    def test_home_page(self, driver):
        home(driver)
        title = get_title(driver)
        assert "Kadr" in title, "The 'Kadr' is not in title"
        driver.quit()

    def test_change_site_language(self, driver):
        home(driver)
        click_lang_element(driver)
        title = get_title(driver)
        assert "Կադր" in title, "The 'Կադր' is not in title"
        driver.quit()
