from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    username = (By.ID,"user-name")
    password = (By.ID,"password")
    login_button = (By.ID,"login-button")


    def enter_username(self,locator,username):
        self.driver.find_element(*locator).send_keys(username)

    def enter_password(self, locator, password):
        self.driver.find_element(*locator).send_keys(password)

    def click_login(self,locator):
        self.driver.find_element(*locator).click()