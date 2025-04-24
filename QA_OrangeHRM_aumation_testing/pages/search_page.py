from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

    def search(self, text):
        # Locate the search input field using XPath
        search_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
        search_input.clear()
        search_input.send_keys(text)

    def click_search_button(self):
        # Locate and click the search button using XPath
        search_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
        search_button.click()

    def get_result_dashboard(self):
        # Locate the result dashboard using XPath
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Dashboard']")))


