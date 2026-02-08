from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    products_text = (By.XPATH,"//span[text()='Products']")

