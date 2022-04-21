from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


class SearchBlock():
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.root: WebElement = driver.find_element(
            By.CSS_SELECTOR, 'div[data-name="Hero"]')
        self.offerType: WebElement = self.root.find_element(
            By.CSS_SELECTOR, '[data-mark="FilterOfferType"]')
        self.roomCount: WebElement = self.root.find_element(
            By.CSS_SELECTOR, '[data-mark="FilterRoomsCount"]')
        self.price: WebElement = self.root.find_element(
            By.CSS_SELECTOR, '[data-mark="FilterPrice"]')
