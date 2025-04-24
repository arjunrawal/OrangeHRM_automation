from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators_login import LoginPageLocators

class Loginpage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Initialize locators
        self.username_field = LoginPageLocators.username_field
        self.password_field = LoginPageLocators.password_field
        self.login_button = LoginPageLocators.login_button

    def open(self):
        """Open the login page URL."""
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    def login(self, username, password):
        """Login using the provided credentials."""
        username_input = self.wait.until(EC.visibility_of_element_located(self.username_field))
        password_input = self.wait.until(EC.visibility_of_element_located(self.password_field))
        login_btn = self.wait.until(EC.element_to_be_clickable(self.login_button))

        username_input.clear()
        username_input.send_keys(username)
        password_input.clear()
        password_input.send_keys(password)
        login_btn.click()
