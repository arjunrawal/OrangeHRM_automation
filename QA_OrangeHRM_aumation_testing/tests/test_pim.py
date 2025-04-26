import unittest
import time  # ✅ Added for sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import Loginpage
from pages.pim_page import PimPage

class TestPIMModule(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def test_pim_form(self):
        driver = self.driver

        # Login
        login = Loginpage(driver)
        login.login("Admin", "admin123")

        # Wait for Dashboard to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
        )
        time.sleep(1)  # ⏳ Slight pause after login

        # Navigate to PIM
        dashboard_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']"))
        )
        dashboard_button.click()

        # Wait for PIM header to be visible
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h6[text()='PIM']"))
        )
        time.sleep(2)  # ⏳ Let the page load fully

        # Fill PIM form
        pim = PimPage(driver)
        self.assertIn("PIM", pim.get_pim_header())
        pim.click_add_employee()

        # Wait for the form to be displayed and fill it
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "firstName"))
        )
        time.sleep(3)  # ⏳ Small wait before form entry
        pim.fill_employee_form("John", "Doe")

        # Wait for the save button to disappear (optional, depends on the site behavior)
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, "//button[@type='submit']"))
        )
        time.sleep(3)  # ⏳ Let the page update after saving

        # Logout
        pim.logout()
        time.sleep(3)  # ⏳ Ensure logout is processed

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
