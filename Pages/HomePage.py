from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class HomePage(BasePage):
    HEADER = (By.CSS_SELECTOR, "h1.dashboard-selector__title")
    ACCOUNT_NAME = (By.CSS_SELECTOR, "account-name ")
    SETTINGS_ICON = (By.ID, "navSetting")

    def  __int__(self, driver):
        super().__init__(driver)
