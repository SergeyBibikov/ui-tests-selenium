from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


class SearchBlock():
    root_loc = 'div[data-name="Hero"]'
    offer_type_loc = '[data-mark="FilterOfferType"]'
    dropdown_loc = '[class*="dropdown"]'
    mortgage_filter = '[data-mark="FilterSingleChoose"]'
    agent_operation_filter = '[data-testid="dealType_filter_control"]'
    agent_operation_filter_dropdown = '[data-testid="dealType_filter_dropdown"]'
    show_on_map_loc = '[data-mark="FiltersSearchOnMapButton"]'
    room_count_loc = '[data-mark="FilterRoomsCount"]'

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.root: WebElement = driver.find_element(
            By.CSS_SELECTOR, self.root_loc)
        self.offer_type: WebElement = self.root.find_element(
            By.CSS_SELECTOR, self.offer_type_loc)
        self.room_count: WebElement = self.root.find_element(
            By.CSS_SELECTOR, self.room_count_loc)
        self.price: WebElement = self.root.find_element(
            By.CSS_SELECTOR, '[data-mark="FilterPrice"]')

    def choose_kind(self, kind_name):
        self.root.find_element(By.LINK_TEXT, kind_name).click()

    def get_kind_filter_dropdown_text(self):
        return self.offer_type.find_element(By.CSS_SELECTOR, self.dropdown_loc).get_attribute('textContent')

    def show_on_map(self):
        self.driver.find_element(
            By.CSS_SELECTOR, self.show_on_map_loc).click()
