import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.search_page import SearchPage
from pages.login_page import Loginpage
from selenium.webdriver.common.keys import Keys


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.search_page = SearchPage(self.driver)
        self.search_page.open()

        login_page = Loginpage(self.driver)
        login_page.login("Admin", "admin123")
        time.sleep(5)

    def test_search_dashboard(self):
        self.search_page.search("Dashboard")
        time.sleep(5)
        result = self.driver.find_element(By.XPATH, "//span[text()='Dashboard']")
        self.assertTrue(result.is_displayed())

    def test_search_invalid_term(self):
        """Test that invalid search filters out all sidebar items"""
        self.search_page.search("XYZ123")

        # Press Enter manually since there's no button
        search_field = self.driver.find_element(By.XPATH, "//input[@placeholder='Search']")
        search_field.send_keys(Keys.RETURN)

        time.sleep(2)

        # Sidebar items (like Dashboard, Admin, etc.) should be filtered out
        sidebar_items = self.driver.find_elements(By.XPATH, "//span[contains(@class, 'oxd-main-menu-item--name')]")

        # Assert that no sidebar items are shown
        self.assertEqual(len(sidebar_items), 0, "Sidebar items should not be shown for invalid input")


    def test_search_and_verify_element(self):
        self.search_page.search("Leave")
        time.sleep(5)
        result = self.driver.find_element(By.XPATH, "//span[text()='Leave']")
        self.assertTrue(result.is_displayed())

    def test_empty_search_field(self):
        """Test that all sidebar items appear when the search field is empty"""
        self.search_page.search("")

        search_field = self.driver.find_element(By.XPATH, "//input[@placeholder='Search']")
        search_field.send_keys(Keys.RETURN)

        time.sleep(2)

        # Sidebar items should reappear
        sidebar_items = self.driver.find_elements(By.XPATH, "//span[contains(@class, 'oxd-main-menu-item--name')]")

        # Expecting some items like Dashboard, Admin, etc. to be visible
        self.assertGreater(len(sidebar_items), 0, "Sidebar items should be visible when the search is empty")


    def test_partial_search_term(self):
        self.search_page.search("Dash")
        time.sleep(5)
        result = self.driver.find_element(By.XPATH, "//span[text()='Dashboard']")
        self.assertTrue(result.is_displayed())

    def test_search_with_special_characters(self):
        self.search_page.search("$pecial")
        time.sleep(5)
        result = self.driver.find_elements(By.XPATH, "//span[contains(text(), '$pecial')]")
        self.assertEqual(len(result), 0)

    def test_search_with_numbers(self):
        self.search_page.search("123")
        time.sleep(5)
        result = self.driver.find_elements(By.XPATH, "//span[contains(text(), '123')]")
        self.assertEqual(len(result), 0)

    def test_case_sensitivity(self):
        self.search_page.search("dashboard")
        time.sleep(5)
        result = self.driver.find_element(By.XPATH, "//span[text()='Dashboard']")
        self.assertTrue(result.is_displayed())

    def test_search_while_on_different_page(self):
        directory_link = self.driver.find_element(By.XPATH, "//span[text()='Directory']")
        directory_link.click()
        time.sleep(5)
        self.search_page.search("Dashboard")
        time.sleep(5)
        result = self.driver.find_element(By.XPATH, "//span[text()='Dashboard']")
        self.assertTrue(result.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
