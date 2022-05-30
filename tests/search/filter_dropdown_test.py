import time

import pytest_check as check

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pageobjects.searchblock import SearchBlock
import helpers.elements as eh


def test_buy_possible_estate_choices(driver: WebDriver):

    search = SearchBlock(driver)

    eh.check_element_is_not_present(
        driver, f"{search.offer_type_loc} {search.dropdown_loc}")

    search.offer_type.click()

    text = search.get_filter_dropdown_text()

    check.is_in('Жилая', text)
    check.is_in('Коммерческая', text)
    check.is_in('Квартира в новостройке', text)
    check.is_in('Квартира во вторичке', text)
    check.is_in('Комната', text)
    check.is_in('Доля', text)
    check.is_in('Дом, дача', text)
    check.is_in('Часть дома', text)
    check.is_in('Таунхаус', text)
    check.is_in('Участок', text)
    check.is_in('Гараж', text)


def test_rent_possible_estate_choices(driver: WebDriver):
    search = SearchBlock(driver)
    search.choose_kind('Снять')
    search.offer_type.click()

    text = search.get_filter_dropdown_text()

    check.is_in('Жилая', text)
    check.is_in('Коммерческая', text)
    check.is_in('Квартира', text)
    check.is_in('Комната', text)
    check.is_in('Койко-место', text)
    check.is_in('Дом, дача', text)
    check.is_in('Часть дома', text)
    check.is_in('Таунхаус', text)
    check.is_in('Гараж', text)


def test_24_hour_rent(driver: WebDriver):
    search = SearchBlock(driver)
    search.choose_kind('Посуточно')
    search.offer_type.click()

    text = search.get_filter_dropdown_text()

    check.is_in('Квартира', text)
    check.is_in('Комната', text)
    check.is_in('Койко-место', text)
    check.is_in('Дом, дача', text)


def test_estimate_estate_kinds(driver: WebDriver):
    filterButton = '[data-testId="undefined_control"]'
    filterDropdown = '[data-testId="undefined_dropdown"]'

    search = SearchBlock(driver)
    search.choose_kind('Оценить')

    eh.check_element_is_not_present(driver, filterDropdown)
    driver.find_element(By.CSS_SELECTOR, filterButton).click()

    text = driver.find_element(
        By.CSS_SELECTOR, filterDropdown).get_attribute('textContent')
    check.is_in('Квартиру', text)
    check.is_in('ЖК', text)
    

def test_mortgage_estate_kinds(driver: WebDriver):

    search = SearchBlock(driver)

    search.choose_kind('Ипотека')
    eh.check_element_is_not_present(driver,SearchBlock.dropdown_loc)
    driver.find_element(By.CSS_SELECTOR, SearchBlock.mortgage_filter).click()

    text = driver.find_element(By.CSS_SELECTOR, SearchBlock.dropdown_loc).get_attribute("textContent")

    check.is_in('Квартира в новостройке', text)
    check.is_in('Квартира во вторичке', text)
    check.is_in('Дом или таунхаус', text)
    check.is_in('Комната или доля', text)