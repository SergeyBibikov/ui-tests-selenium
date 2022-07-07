import time

import pytest_check as check

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from pageobjects.searchblock import SearchBlock
import helpers.elements as eh
import constants

""" TESTS OF SEARCH FILTERS IN VARIOUS SEARCH TABS"""

def test_estimate_should_have_4_filters(driver: WebDriver):

    

    search = SearchBlock(driver)

    search.choose_kind('Оценить')

    _filters = search.filters_MORTGAGE_MAIN_and_agent + search.single_filter_loc
    filters = driver.find_elements(By.XPATH, _filters)

    check.equal(len(filters), 4)

def test_MORTGAGE_MAIN_should_have_5_filters(driver: WebDriver):

    

    search = SearchBlock(driver)

    search.choose_kind('Ипотека')
    f = search.MORTGAGE_MAIN_filters

    eh.check_element_is_present(driver, f["estate_kind"], By.XPATH)
    eh.check_element_is_present(driver, f["estate_price"], By.XPATH)
    eh.check_element_is_present(driver, f["first_payment_sum"], By.XPATH)
    eh.check_element_is_present(driver, f["period"], By.XPATH)
    eh.check_element_is_present(driver, f["region"], By.XPATH)

def test_estate_agent_selection_should_have_3_filters(driver: WebDriver):

    

    search = SearchBlock(driver)

    search.choose_kind('Подбор риелтора')

    _filters = search.filters_MORTGAGE_MAIN_and_agent + search.single_filter_loc
    filters = driver.find_elements(By.XPATH, _filters)
    check.equal(len(filters), 3)

def test_buy_should_have_4_filters(driver: WebDriver):
    

    search = SearchBlock(driver)

    search.choose_kind('Купить')

    eh.check_element_is_present(driver, search.offer_type_loc)
    eh.check_element_is_present(driver, search.room_count_loc)
    eh.check_element_is_present(driver, search.price_filter_loc)
    eh.check_element_is_present(driver, search.location_filter_loc)

def test_rent_should_have_4_filters(driver: WebDriver):
    

    search = SearchBlock(driver)

    search.choose_kind('Снять')

    eh.check_element_is_present(driver, search.offer_type_loc)
    eh.check_element_is_present(driver, search.room_count_loc)
    eh.check_element_is_present(driver, search.price_filter_loc)
    eh.check_element_is_present(driver, search.location_filter_loc)

def test_24_hour_rent_should_have_4_filters(driver: WebDriver):
    

    search = SearchBlock(driver)

    search.choose_kind('Посуточно')

    eh.check_element_is_present(driver, search.offer_type_loc)
    eh.check_element_is_present(driver, search.room_count_loc)
    eh.check_element_is_present(driver, search.price_filter_loc)
    eh.check_element_is_present(driver, search.location_filter_loc)

def test_new_houses_search_shoulld_have_4_filters(driver: WebDriver):
    driver.get(constants.urls["NEW_HOUSES"])

    filters = driver.find_elements(By.XPATH, '//div[@data-name="SearchFilters"]//div[contains(@data-name, "Filter")]')
    
    assert len(filters) == 4

def test_country_property_search_shoulld_have_3_filters(driver: WebDriver):
    driver.get(constants.urls["COUNTRY_PROPERTY"])

    filters = driver.find_elements(By.XPATH, '//div[@data-name="Filters"]//div[starts-with(@data-mark, "Filter")]')
    
    assert len(filters) == 3