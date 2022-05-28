import time

import allure
import pytest_check as check

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pageobjects.searchblock import SearchBlock
import helpers.elements as eh


@allure.step
def checkText(textToFind, actualText, msg=""):
    check.is_in(textToFind, actualText, msg)


def test_buy_default_filters(driver: WebDriver):
    """ Estate type and room filters must have default values """
    sb = SearchBlock(driver)
    checkText("Квартиру в новостройке и вторичке", sb.offer_type.text)
    checkText("1, 2 комн.", sb.room_count.text)


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
