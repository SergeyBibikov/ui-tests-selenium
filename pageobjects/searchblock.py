import allure

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


class SearchBlock():
    root_loc = 'div[data-name="Hero"]'
    offer_type_loc = '[data-mark="FilterOfferType"]'
    dropdown_loc = '[class*="dropdown"]'
    agent_operation_filter = '[data-testid="dealType_filter_control"]'
    agent_operation_filter_dropdown = '[data-testid="dealType_filter_dropdown"]'
    show_on_map_loc = '[data-mark="FiltersSearchOnMapButton"]'
    room_count_loc = '[data-mark="FilterRoomsCount"]'
    price_filter_loc = '[data-mark="FilterPrice"]'
    location_filter_loc = '[data-mark="FilterGeo"]'

    suggestion_popup_loc = '[data-name="SuggestionPopup"]'

    filters_general = '[data-name="Filters"]'
    filters_MORTGAGE_MAIN_and_agent = '//div[contains(@class,"filters")]'
    single_filter_loc = '//div[contains(@class,"filter") and not(contains(@class, "container"))]'

    search_button = '[data-mark="FiltersSearchButton"]'

    MORTGAGE_MAIN_filters = {
        "estate_kind": '//div[@data-mark="FilterSingleChoose"][1]',
        "estate_price": '//div[@data-name="FilterAmountInput"][1]',
        "first_payment_sum": '//div[@data-name="FilterAmountInput"][2]',
        "period": '//div[@data-mark="FilterSingleChoose"][2]',
        "region": '//div[@data-mark="FilterRegion"]'
    }

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.root: WebElement = driver.find_element(
            By.CSS_SELECTOR, self.root_loc)
        self.offer_type: WebElement = self.root.find_element(
            By.CSS_SELECTOR, self.offer_type_loc)
        self.room_count: WebElement = self.root.find_element(
            By.CSS_SELECTOR, self.room_count_loc)
        self.price: WebElement = self.root.find_element(
            By.CSS_SELECTOR, self.price_filter_loc)
        self.location: WebElement = self.root.find_element(
            By.CSS_SELECTOR, self.location_filter_loc)
        self.search_button: WebElement = self.root.find_element(
            By.CSS_SELECTOR, self.search_button
        )

    @allure.step
    def search(self):
        self.search_button.click()

    def choose_kind(self, kind_name):
        self.root.find_element(By.LINK_TEXT, kind_name).click()

    def get_kind_filter_dropdown_text(self):
        return self.offer_type.find_element(By.CSS_SELECTOR, self.dropdown_loc).get_attribute('textContent')

    def show_on_map(self):
        self.driver.find_element(
            By.CSS_SELECTOR, self.show_on_map_loc).click()
            
    @allure.step
    def enter_location(self, location):
        self.location.find_element(By.CSS_SELECTOR, 'input').send_keys(location)