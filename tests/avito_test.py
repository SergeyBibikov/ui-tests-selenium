from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

import helpers.elements as eh
import helpers.waits as w
import helpers.actions as a
from helpers.checks import check_text, check_length, check_not_equal

import time

from pageobjects.avito import Locators as l, confirm_location


def test_city_confirmation_popup_buttons(avito: WebDriver):
    popup = avito.find_element(By.XPATH, l.YOUR_CITY_CONFIRMATION_POPUP)

    eh.check_element_is_present(popup, l.YES_BUTTON, By.XPATH)
    eh.check_element_is_present(popup, l.CHANGE_BUTTON, By.XPATH)


def test_services_list_includes_three_points(avito: WebDriver):
    text = avito.find_element(
        By.XPATH, l.SERVICES_LIST).get_attribute('textContent')

    check_text('Доставка', text)
    check_text('Автотека', text)
    check_text('Онлайн-бронирование жилья', text)


def test_search_kinds_options(avito: WebDriver):
    d = avito

    confirm_location(d)

    text = d.find_element(
        By.CSS_SELECTOR, l.SEARCH_KINDS_LIST).get_attribute('textContent')
    check_text('Авто', text)
    check_text('Недвижимость', text)
    check_text('Работа', text)
    check_text('Услуги', text)
    check_text('ещё', text)


def test_categories_of_the_more_option(avito: WebDriver):
    d = avito

    d.find_element(
        By.CSS_SELECTOR, l.SEARCH_KINDS_LIST
    ).find_element(
        By.XPATH, l.MORE_OPTION).click()
    text = d.find_element(
        By.CSS_SELECTOR, l.MORE_POPUP).get_attribute('textContent')
    check_text('Транспорт', text)
    check_text('Для дома и дачи', text)
    check_text('Готовый бизнес и оборудование', text)
    check_text('Недвижимость', text)
    check_text('Электроника', text)
    check_text('Работа', text)
    check_text('Услуги', text)
    check_text('Хобби и отдых', text)
    check_text('Личные вещи', text)
    check_text('Животные', text)


def test_ad_search_parameters_checkboxes(avito: WebDriver):
    d = avito
    params = d.find_element(By.CSS_SELECTOR, l.SEARCH_PARAMETERS)

    checkboxes = params.find_elements(
        By.CSS_SELECTOR, 'input[type="checkbox"]')
    check_length(checkboxes, 3)

    text = params.get_attribute('textContent')
    check_text('только в названиях', text)
    check_text('только с фото', text)
    check_text('сначала из Москвы', text)


def test_search_suggestions_dropdown(avito: WebDriver):
    d = avito

    d.find_element(By.CSS_SELECTOR, l.SEARCH_BAR).click()

    text = d.find_element(
        By.CSS_SELECTOR, l.SUGGESTION_LIST).get_attribute('textContent')

    check_text('Вакансии', text)
    check_text('Автомобили', text)
    check_text('Снять квартиру (посуточно)', text)
    check_text('Снять квартиру (длительно)', text)
    check_text('Мобильные телефоны', text)
    check_text('Купить квартиру', text)
    check_text('Автомобили с пробегом', text)
    check_text('Купить дом', text)


def test_search_radius_determines_ads_number(avito: WebDriver):
    d = avito
    d.find_element(By.CSS_SELECTOR, l.SEARCH_RADIUS).click()
    radius_items = d.find_elements(By.CSS_SELECTOR, l.RADIUS_LIST_ITEMS)

    radius_items[0].click()
    button_text1 = d.find_element(
        By.CSS_SELECTOR, l.SHOW_ADS_BUTTON
    ).get_attribute('textContent')

    radius_items[1].click()
    button_text2 = d.find_element(
        By.CSS_SELECTOR, l.SHOW_ADS_BUTTON
    ).get_attribute('textContent')

    check_not_equal(button_text1, button_text2)


def test_search_works_in_general(avito: WebDriver):
    d = avito

    search_item = 'iphone'

    d.find_element(By.CSS_SELECTOR, l.SEARCH_BAR).send_keys(search_item)
    d.find_element(By.CSS_SELECTOR, l.SEARCH_BUTTON).click()

    text = d.find_element(
        By.CSS_SELECTOR, l.PAGE_TITLE).get_attribute('textContent')
    check_text('Объявления по', text)
    check_text('запросу', text)
    check_text(f'«{search_item}» в', text)
