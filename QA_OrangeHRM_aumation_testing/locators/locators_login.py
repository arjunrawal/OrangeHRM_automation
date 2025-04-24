from selenium.webdriver.common.by import By

class LoginPageLocators:
    username_field = (By.NAME, "username")  # correct
    password_field = (By.XPATH, "//input[@name='password']")  # correct
    login_button = (By.XPATH, "//button[@type='submit']")  # correct
