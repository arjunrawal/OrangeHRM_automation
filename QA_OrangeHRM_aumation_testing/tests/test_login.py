import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import Loginpage
import time

class TestLogin(unittest.TestCase):
    def setUp(self):
        """Set up the WebDriver for the test."""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.login_page = Loginpage(self.driver)

    def test_login_valid_credentials(self):
        """Test login with valid credentials."""
        self.login_page.open()
        self.login_page.login("Admin", "admin123")

        # Add a delay to see the actions
        time.sleep(3)

        # Wait for the URL to contain '/dashboard/index' after login
        WebDriverWait(self.driver, 10).until(EC.url_contains("/dashboard/index"))

        # Assert that the current URL contains '/dashboard/index' (indicating successful login)
        self.assertIn("/dashboard/index", self.driver.current_url)

    def test_invalid_login_incorrect_password(self):
        """Test login with incorrect password."""
        self.login_page.open()
        self.login_page.login("Admin", "wrongpass")
        
        # Add a delay to see the actions
        time.sleep(3)

        error = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//p[@class="oxd-text oxd-text--p oxd-alert-content-text"]')))
        self.assertEqual(error.text, "Invalid credentials")

    def test_invalid_login_incorrect_username(self):
        """Test login with incorrect username."""
        self.login_page.open()
        self.login_page.login("wronguser", "admin123")
        
        # Add a delay to see the actions
        time.sleep(3)

        error = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//p[@class="oxd-text oxd-text--p oxd-alert-content-text"]')))
        self.assertEqual(error.text, "Invalid credentials")

    def test_empty_username(self):
        """Test login with empty username."""
        self.login_page.open()
        self.login_page.login("", "admin123")
        
        # Add a delay to see the actions
        time.sleep(3)

        error = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message"]')))
        self.assertEqual(error.text, "Required")

    def test_empty_password(self):
        """Test login with empty password."""
        self.login_page.open()
        self.login_page.login("Admin", "")
        
        # Add a delay to see the actions
        time.sleep(3)

        error = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/span')))
        self.assertEqual(error.text, "Required")

    def test_empty_fields(self):
        """Test login with both fields empty."""
        self.login_page.open()
        self.login_page.login("", "")
        
        # Add a delay to see the actions
        time.sleep(3)

        username_error = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/span')))
        self.assertEqual(username_error.text, "Required")

        password_error = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/span')))
        self.assertEqual(password_error.text, "Required")

    def tearDown(self):
        """Quit the WebDriver after each test."""
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
