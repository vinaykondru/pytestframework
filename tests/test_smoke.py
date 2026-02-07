from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from config.data_reader import read_csv

@pytest.mark.usefixtures("browser_setup")
class TestSmoke:
    data = read_csv("uat_data.csv")
    @pytest.mark.parametrize("user", data)
    def test_login(self,user,config):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID,"user-name").send_keys(config["username"])
        self.driver.find_element(By.ID,"password").send_keys(config["password"])
        self.driver.find_element(By.ID,"login-button").click()
        productText = self.driver.find_element(By.XPATH,"//span[text()='Products']").text
        assert productText == "Productss"
        assert self.driver.find_element(By.CLASS_NAME,"app_logo").is_displayed()
        # self.driver.quit()