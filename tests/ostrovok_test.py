from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

import helpers.elements as eh
import helpers.waits as w
import helpers.actions as a
from helpers.checks import check_text, check_length, check_not_equal

import time

from pageobjects.avito import Locators as l, confirm_location


DESTINATION_DROPDOWN = '//div[contains(@class, "Popup-module") and div[text()="Regions"]]'
SEARCH_BUTTON = '//div[text()="Search"]'


def test_destination_dropdown_on_empty_search_attempt(ostrovok: WebDriver):
    d = ostrovok

    eh.check_element_is_not_present(d, DESTINATION_DROPDOWN, By.XPATH)

    d.find_element(By.XPATH, SEARCH_BUTTON).click()

    eh.check_element_is_present(d, DESTINATION_DROPDOWN, By.XPATH)
