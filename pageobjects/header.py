from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class Header():

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.root: WebElement = driver.find_element(
            By.CSS_SELECTOR, 'div[data-name="Header"]')
        self.compare_objects: WebElement = self.root.find_element(
            By.CSS_SELECTOR, '[data-name="UtilityCompareContainer"]')
        self.favourites: WebElement = self.root.find_element(
            By.CSS_SELECTOR, '[data-name="UtilityFavoritesContainer"]')
        self.notifications: WebElement = self.root.find_element(
            By.CSS_SELECTOR, '[data-name="UtilityNotificationsContainer"]')
