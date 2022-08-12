from constants import Urls

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

import pytest_check as check

import helpers.elements as eh
import helpers.waits as w
import helpers.actions as a

import time

from pageobjects.avito import Locators as l, confirm_location


def test_city_confirmation_popup_buttons(avito: WebDriver):
    popup = avito.find_element(By.XPATH, l.YOUR_CITY_CONFIRMATION_POPUP)

    eh.check_element_is_present(popup, l.YES_BUTTON, By.XPATH)
    eh.check_element_is_present(popup, l.CHANGE_BUTTON, By.XPATH)


def test_services_list_includes_three_points(avito: WebDriver):
    text = avito.find_element(
        By.XPATH, l.SERVICES_LIST).get_attribute('textContent')

    check.is_in('Доставка', text)
    check.is_in('Автотека', text)
    check.is_in('Онлайн-бронирование жилья', text)


def test_search_kinds_options(avito: WebDriver):
    d = avito

    confirm_location(d)

    text = d.find_element(
        By.CSS_SELECTOR, l.SEARCH_KINDS_LIST).get_attribute('textContent')
    check.is_in('Авто', text)
    check.is_in('Недвижимость', text)
    check.is_in('Работа', text)
    check.is_in('Услуги', text)
    check.is_in('ещё', text)
