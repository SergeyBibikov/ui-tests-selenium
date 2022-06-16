import time

import pytest_check as check

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from pageobjects.searchblock import SearchBlock
import helpers.elements as eh


def test_estimate_should_have_4_filters(driver: WebDriver):

    driver.implicitly_wait(10)

    search = SearchBlock(driver)

    search.choose_kind('Оценить')

    filters = driver.find_elements(By.XPATH, search.filters_mortgage_and_agent+search.single_filter_loc)
    check.equal(len(filters), 4)

