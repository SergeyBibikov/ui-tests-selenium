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

    _filters = search.filters_mortgage_and_agent + search.single_filter_loc
    filters = driver.find_elements(By.XPATH, _filters)

    check.equal(len(filters), 4)

def test_mortgage_should_have_5_filters(driver: WebDriver):

    driver.implicitly_wait(10)

    search = SearchBlock(driver)

    search.choose_kind('Ипотека')
    f = search.mortgage_filters

    eh.check_element_is_present(driver, f["estate_kind"], By.XPATH)
    eh.check_element_is_present(driver, f["estate_price"], By.XPATH)
    eh.check_element_is_present(driver, f["first_payment_sum"], By.XPATH)
    eh.check_element_is_present(driver, f["period"], By.XPATH)
    eh.check_element_is_present(driver, f["region"], By.XPATH)

def test_estate_agent_selection_should_have_3_filters(driver: WebDriver):

    driver.implicitly_wait(10)

    search = SearchBlock(driver)

    search.choose_kind('Подбор риелтора')

    _filters = search.filters_mortgage_and_agent + search.single_filter_loc
    filters = driver.find_elements(By.XPATH, _filters)
    check.equal(len(filters), 3)