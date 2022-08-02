from pageobjects.header import Header
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains

import helpers.elements as eh
import helpers.waits as w
import helpers.actions as a

import pytest_check as check
import time
from constants import Urls

SEARCH_FLATS = '//span[text()="Искать квартиры"]'

def test_flat_search_button_leads_to_search_page(driver_no_link: WebDriver):
    d = driver_no_link

    d.get(Urls.COMPARISON)

    d.find_element(By.XPATH, SEARCH_FLATS).click()

    check.is_in('kupit-kvartiru', d.current_url)