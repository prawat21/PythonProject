import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("init_driver")
class BaseTest():
    pass


class TestHubSpot(BaseTest):

    @pytest.mark.parametrize(
        "username, password",
        [
            ("admin@gmail.com", "admin123"),
            ("puneetrawat@gmail.com", "puneet123"),
        ]

    )
    def test_login(self, username, password):
        """
        This method is used to login to hub spot applicable
        :param username:
        :param password:
        :return:
        """
        self.driver.get("https://app.hubspot.com/login")
        self.driver.find_element(By.ID, 'username').send_keys(username)
        self.driver.find_element(By.ID, 'password').send_keys(password)
