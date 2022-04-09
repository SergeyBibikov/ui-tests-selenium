from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

class Header():

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.root = driver.find_element(By.CSS_SELECTOR, 'div[data-name="Header"]')
    