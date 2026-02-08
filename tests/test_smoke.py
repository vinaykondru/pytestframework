from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage
from selenium.webdriver.support import expected_conditions as EC
from config.data_reader import read_csv
from utils.env_loader import get_secret


@pytest.mark.usefixtures("browser_setup")
class TestSmoke:
    data = read_csv("uat_data.csv")
    def test_login(self):
        username = get_secret("LOGIN_USERNAME")
        password = get_secret("LOGIN_PASSWORD")
        login_page = LoginPage(self.driver)
        login_page.enter_username(LoginPage.username,username)
        login_page.enter_password(LoginPage.password,password)
        login_page.click_login(LoginPage.login_button)
        base_page = BasePage(self.driver)
        inventory_page = InventoryPage(self.driver)
        productText = base_page.get_text(inventory_page.products_text)
        assert productText == "Products"
        assert self.driver.find_element(By.CLASS_NAME,"app_logo").is_displayed()
        # self.driver.quit()