from locators.locators_pim import PimLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PimPage:
    def __init__(self, driver):
        self.driver = driver

    def get_pim_header(self):
        return self.driver.find_element(*PimLocators.PIM_HEADER).text

    def click_add_employee(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(PimLocators.ADD_EMPLOYEE_BUTTON)
        ).click()

    def fill_employee_form(self, first_name, last_name):
        self.driver.find_element(*PimLocators.FIRST_NAME_FIELD).send_keys(first_name)
        self.driver.find_element(*PimLocators.LAST_NAME_FIELD).send_keys(last_name)
        self.driver.find_element(*PimLocators.SAVE_BUTTON).click()

        # Wait for the save action to complete (optional, if save button disappears after submission)
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(PimLocators.SAVE_BUTTON)
        )

    def logout(self):
        # First click on the user icon dropdown
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(PimLocators.USER_DROPDOWN_ICON)
        ).click()
    
        # Then click on the Logout button
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(PimLocators.LOGOUT_BUTTON)
        ).click()
    