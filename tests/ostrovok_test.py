from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

import helpers.elements as eh
import helpers.waits as w
import helpers.actions as a
from helpers.checks import check_text

BUSINESS_TRIPS_TAB = '//a[text()="For business trips"]'
DESTINATION_DROPDOWN = '//div[contains(@class, "Popup-module") and div[text()="Regions"]]'
HERO = 'section[class*=Hero]'
SEARCH_BUTTON = '//div[text()="Search"]'


def test_destination_dropdown_on_empty_search_attempt(ostrovok: WebDriver):
    d = ostrovok

    eh.check_element_is_not_present(d, DESTINATION_DROPDOWN, By.XPATH)

    d.find_element(By.XPATH, SEARCH_BUTTON).click()

    eh.check_element_is_present(d, DESTINATION_DROPDOWN, By.XPATH)


def test_business_trips_successful_lead(ostrovok: WebDriver):
    d = ostrovok

    d.find_element(By.XPATH, BUSINESS_TRIPS_TAB).click()
    a.switchToNthTab(d, 2)

    check_text('corp.ostrovok.ru', d.current_url)
    w.wait_for_text(d, 30, By.CSS_SELECTOR, HERO,
                    'Easy organization of business trips')
