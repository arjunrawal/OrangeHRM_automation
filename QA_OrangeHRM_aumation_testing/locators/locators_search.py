from selenium.webdriver.common.by import By

class SearchLocators:
    SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Search']")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
    RESULT_DASHBOARD = (By.XPATH, "//span[text()='Dashboard']")
    NO_RESULTS_MESSAGE = (By.XPATH, "//div[@class='no-results']")
