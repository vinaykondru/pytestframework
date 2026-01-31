from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def dynamic_wait_click(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).click()

    def dynamic_wait_type(self,locator,data):
        return self.wait.until(EC.visibility_of_element_located(locator)).send_keys(data)

