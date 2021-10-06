class Window:
    @staticmethod
    def get_window_size(driver):
        window_size = driver.get_window_size()
        return window_size

    @staticmethod
    def minimize_maximize_window(driver, change_type):
        if change_type == "maximize":
            driver.maximize_window()
        else:
            driver.minimize_window()

    @staticmethod
    def change_window_size(driver, width, height):
        driver.set_window_size(width, height)

    @staticmethod
    def quit_window(driver):
        driver.quit()

    @staticmethod
    def scroll_page(driver, vertical):
        driver.execute_script(f"window.scrollTo(0, {vertical});")
