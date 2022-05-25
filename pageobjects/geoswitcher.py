from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


class GeoSwitcher:

    main_page_button = '[data-name="GeoSwitcher"] button'
    header = '[data-name="GeoSwitcherHeader"]'
    body = '[data-name="GeoSwitcherBody"]'
    city_input = header + ' input'
    choose_button = header + ' button'
    geo_suggest = header + ' [data-name="GeoSuggest"]'

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def change_location(self, new_location):
        root = self.driver.find_element(By.CSS_SELECTOR, self.main_page_button)
        root.click()

        header = self.driver.find_element(By.CSS_SELECTOR, self.header)
        city_input = self.driver.find_element(By.CSS_SELECTOR, self.city_input)
        choose_button = self.driver.find_element(
            By.CSS_SELECTOR, self.choose_button)
        city_input.click()
        city_input.send_keys(Keys.CONTROL + "a")
        city_input.send_keys(Keys.DELETE)
        city_input.send_keys(new_location)
        header.click()
        city_input.click()
        # suggestion sync
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, self.geo_suggest).click()
        choose_button.click()
