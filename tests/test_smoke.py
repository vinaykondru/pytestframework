from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage
from selenium.webdriver.support import expected_conditions as EC
from config.data_reader import read_csv

@pytest.mark.usefixtures("browser_setup")
class TestSmoke:
    data = read_csv("uat_data.csv")
    @pytest.mark.parametrize("user", data)
    def test_login(self,user,config):
        print(config["username"])
        login_page = LoginPage(self.driver)
        login_page.enter_username(LoginPage.username,config["username"])
        login_page.enter_password(LoginPage.password,config["password"])
        login_page.click_login(LoginPage.login_button)
        base_page = BasePage(self.driver)
        productText = base_page.get_text(InventoryPage.products_text)
        assert productText == "Products"
        assert self.driver.find_element(By.CLASS_NAME,"app_logo").is_displayed()
        # self.driver.quit()