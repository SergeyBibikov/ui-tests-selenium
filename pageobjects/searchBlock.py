from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


class SearchBlock():

    offer_type_loc = '[data-mark="FilterOfferType"]'
    dropdown_loc = '[class*="dropdown"]'

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.root: WebElement = driver.find_element(
            By.CSS_SELECTOR, 'div[data-name="Hero"]')
        self.offer_type: WebElement = self.root.find_element(
            By.CSS_SELECTOR, self.offer_type_loc)
        self.room_count: WebElement = self.root.find_element(
            By.CSS_SELECTOR, '[data-mark="FilterRoomsCount"]')
        self.price: WebElement = self.root.find_element(
            By.CSS_SELECTOR, '[data-mark="FilterPrice"]')

    def choose_kind(self, kind_name):
        self.root.find_element(By.LINK_TEXT, kind_name).click()

    def get_filter_dropdown_text(self):
        return self.offer_type.find_element(By.CSS_SELECTOR, self.dropdown_loc).get_attribute('textContent')
