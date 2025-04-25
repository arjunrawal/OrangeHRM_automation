from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators_dashboard import DashboardLocators

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_dashboard_widgets(self):
        assert self.driver.find_element(*DashboardLocators.TIME_AT_WORK).is_displayed()
        assert self.driver.find_element(*DashboardLocators.MY_ACTIONS).is_displayed()
        assert self.driver.find_element(*DashboardLocators.QUICK_LAUNCH).is_displayed()

    def is_dashboard_loaded(self):
        return DashboardLocators.DASHBOARD_URL_KEYWORD in self.driver.current_url

    def search_admin_and_navigate(self):
        self.driver.find_element(*DashboardLocators.SEARCH_BAR).send_keys("Admin")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(DashboardLocators.ADMIN_SEARCH_OPTION)
        ).click()
