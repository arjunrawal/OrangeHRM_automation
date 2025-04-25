import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import Loginpage
from pages.dashboard_page import DashboardPage

class DashboardTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()

        login = Loginpage(self.driver)
        login.login("Admin", "admin123")

        # Wait for dashboard to be ready
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="oxd-topbar-header-title"]'))
        )
        time.sleep(2)
        self.dashboard = DashboardPage(self.driver)

    def test_assign_leave_form(self):
        wait = WebDriverWait(self.driver, 15)

        # 1. Navigate to Assign Leave
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Assign Leave']"))).click()
        wait.until(EC.url_contains("/leave/assign"))
        time.sleep(3)
        
        # 2. Enter Employee Name
        emp_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type for hints...']")))

        # Enter the employee name
        emp_input.send_keys("Joseph")

        # Wait for autocomplete suggestions to appear (adjust time as needed)
        time.sleep(3)  # You can replace this with an explicit wait if necessary

        # Use arrow keys to select the first suggestion and hit Enter
        emp_input.send_keys(Keys.ARROW_DOWN)  # Navigate through autocomplete suggestions
        time.sleep(2)  # Small delay before hitting Enter
        emp_input.send_keys(Keys.ENTER)

        # Optionally, check if the value is correctly populated
        entered_value = emp_input.get_attribute("value")
        print(f"Entered employee name: {entered_value}")

        # 3. Select Leave Type
        leave_dropdown = self.driver.find_element(By.XPATH, "//label[text()='Leave Type']/following::div[@class='oxd-select-wrapper'][1]")
        leave_dropdown.click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@role='listbox']//span[contains(text(),'CAN - Vacation')]").click()

        # 4. Enter From Date
        from_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='From Date']/following::input[1]")))
        from_input.send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)
        from_input.send_keys("2024-04-25")

        # 5. Enter To Date
        to_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='To Date']/following::input[1]")))
        to_input.send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)
        to_input.send_keys("2024-04-25")

        # 6. Comment
        comment_box = self.driver.find_element(By.XPATH, "//textarea")
        comment_box.send_keys("Leave requested for vacation.")

        time.sleep(1)

        # 7. Click Assign
        assign_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Assign']")
        assign_button.click()

        # 8. Confirm Yes in the popup
        confirm_yes = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-button-margin"]')))
        confirm_yes.click()

        # 9. Optional: Verify success toast (if you want)
        # success_msg = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Successfully Assigned')]")))
        # self.assertIn("Successfully", success_msg.text)

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
