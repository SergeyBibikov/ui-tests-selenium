import time

import pytest_check as check

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pageobjects.searchblock import SearchBlock
import helpers.elements as eh


""" TESTS OF VARIOUS DROPDOWNS IN THE SEARCH FILTERS BLOCK """


def test_buy_possible_estate_choices(driver: WebDriver):

    search = SearchBlock(driver)

    eh.check_element_is_not_present(
        driver, f"{search.offer_type_loc} {search.dropdown_loc}")

    search.offer_type.click()

    text = search.get_kind_filter_dropdown_text()

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

    text = search.get_kind_filter_dropdown_text()

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

    text = search.get_kind_filter_dropdown_text()

    check.is_in('Квартира', text)
    check.is_in('Комната', text)
    check.is_in('Койко-место', text)
    check.is_in('Дом, дача', text)


def test_estimate_estate_kinds(driver: WebDriver):
    filterButton = '[data-testId="estimation_target_control"]'
    filterDropdown = '[data-testId="estimation_target_dropdown"]'

    search = SearchBlock(driver)
    search.choose_kind('Оценить')

    eh.check_element_is_not_present(driver, filterDropdown)
    driver.find_element(By.CSS_SELECTOR, filterButton).click()

    text = driver.find_element(
        By.CSS_SELECTOR, filterDropdown).get_attribute('textContent')
    check.is_in('Квартира', text)
    check.is_in('ЖК', text)


def test_MORTGAGE_MAIN_estate_kinds(driver: WebDriver):

    search = SearchBlock(driver)

    search.choose_kind('Ипотека')
    eh.check_element_is_not_present(driver, SearchBlock.dropdown_loc)
    driver.find_element(
        By.XPATH, SearchBlock.MORTGAGE_MAIN_filters["estate_kind"]).click()

    text = driver.find_element(
        By.CSS_SELECTOR, SearchBlock.dropdown_loc).get_attribute("textContent")

    check.is_in('Квартира в новостройке', text)
    check.is_in('Квартира во вторичке', text)
    check.is_in('Дом или таунхаус', text)
    check.is_in('Комната или доля', text)


def test_estate_agent_search(driver: WebDriver):

    search = SearchBlock(driver)

    search.choose_kind('Подбор риелтора')
    eh.check_element_is_not_present(
        driver, SearchBlock.agent_operation_filter_dropdown)
    driver.find_element(
        By.CSS_SELECTOR, SearchBlock.agent_operation_filter).click()
    text = driver.find_element(
        By.CSS_SELECTOR, SearchBlock.agent_operation_filter_dropdown).get_attribute('textContent')

    check.is_in('Купить', text)
    check.is_in('Продать', text)
    check.is_in('Продать, чтобы купить', text)
    check.is_in('Снять', text)
    check.is_in('Сдать', text)


def test_room_count_filter(driver: WebDriver):

    search = SearchBlock(driver)

    eh.check_element_is_not_present(driver, search.dropdown_loc)

    search.room_count.click()

    eh.check_element_is_present(driver, search.dropdown_loc)

    text = driver.find_element(
        By.CSS_SELECTOR, search.dropdown_loc).get_attribute('textContent')
    check.is_in('1', text)
    check.is_in('2', text)
    check.is_in('3', text)
    check.is_in('4', text)
    check.is_in('5', text)
    check.is_in('6+', text)
    check.is_in('Студия', text)
    check.is_in('Свободная планировка', text)


def test_price_input_fields_presence(driver: WebDriver):

    search = SearchBlock(driver)

    eh.check_element_is_not_present(driver, search.dropdown_loc)

    search.price.click()

    dropdown = driver.find_element(By.CSS_SELECTOR, search.dropdown_loc)

    eh.check_element_is_present(dropdown, 'input[placeholder="от"]')
    eh.check_element_is_present(dropdown, 'input[placeholder="до"]')


def test_location_suggestion_popup_should_include_different_location_types(driver: WebDriver):

    search = SearchBlock(driver)
    search.enter_location('Москва')
    text = driver.find_element(
        By.CSS_SELECTOR, search.suggestion_popup_loc).get_attribute('textContent')
    check.is_in('Адреса', text)
    check.is_in('Метро', text)
    check.is_in('Жилые комплексы', text)
    check.is_in('Коттеджные поселки', text)
    check.is_in('Город', text)
    check.is_in('Ж/Д станции', text)
    check.is_in('Шоссе', text)
