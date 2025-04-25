from selenium.webdriver.common.by import By

class DashboardLocators:
    TIME_AT_WORK = (By.XPATH, "//p[text()='Time at Work']")
    MY_ACTIONS = (By.XPATH, "//p[text()='My Actions']")
    QUICK_LAUNCH = (By.XPATH, "//p[text()='Quick Launch']")
    SEARCH_BAR = (By.XPATH, "//input[@placeholder='Search']")
    ADMIN_SEARCH_OPTION = (By.XPATH, "//span[text()='Admin']")
    DASHBOARD_URL_KEYWORD = "dashboard"
