from selenium.webdriver.common.by import By

class PimLocators:
    # Header
    PIM_HEADER = (By.XPATH, "//h6[text()='PIM']")

    # Buttons
    ADD_EMPLOYEE_BUTTON = (By.XPATH, "//button[normalize-space()='Add']")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")
    LOGOUT_BUTTON = (By.XPATH, "//a[normalize-space()='Logout']")

    # Input Fields
    FIRST_NAME_FIELD = (By.NAME, "firstName")
    LAST_NAME_FIELD = (By.NAME, "lastName")

    USER_DROPDOWN_ICON = (By.CLASS_NAME, "oxd-userdropdown-tab")
    LOGOUT_BUTTON = (By.LINK_TEXT, "Logout")

