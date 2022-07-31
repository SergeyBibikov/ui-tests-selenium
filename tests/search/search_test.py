import time

import allure
import pytest_check as check

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

from pageobjects.searchblock import SearchBlock

import helpers.waits as w
import helpers.elements as eh

from constants import CommonElements

DEAL_TYPE_FILTER = '#mainFilter_dealType'
RENT_SELECT_OPTION = '//div[@data-name="SelectPopupOption" and text()="Снять"]'
SAVE_SEARCH_BUTTON = '//span[text()="Сохранить поиск"]'
SAVE_SEARCH_MODAL = '//div[@aria-modal="true" and contains(., "Сохранение поиска")]'

def test_buy_default_filters(driver: WebDriver):

    sb = SearchBlock(driver)
    
    check.is_in("Квартиру в новостройке и вторичке", sb.offer_type.text)
    check.is_in("1, 2 комн.", sb.room_count.text)

def test_non_existing_city_search(driver: WebDriver):
    sb = SearchBlock(driver)

    sb.enter_location('dfsdfasdfa')

    w.wait_for_text(driver, 20, By.CSS_SELECTOR, sb.suggestion_popup_loc, "Ничего не найдено")

def test_flat_search_results_additional_filters_list(driver_buy_flat_results: WebDriver):
    d = driver_buy_flat_results

    d.find_element(By.CSS_SELECTOR, CommonElements.ADVANCED_FILTERS).click()

    text = d.find_element(By.XPATH, CommonElements.ADVANCED_FILTERS_CARD).get_attribute('textContent')

    check.is_in('Тип сделки',text)
    check.is_in('До метро',text)
    check.is_in('Площадь, м2',text)
    check.is_in('Планировка',text)
    check.is_in('Высота потолков',text)
    check.is_in('Санузел',text)
    check.is_in('Балкон/Лоджия',text)
    check.is_in('Кухонная плита',text)
    check.is_in('Ремонт',text)
    check.is_in('Этаж',text)
    check.is_in('Этажей в доме',text)
    check.is_in('Вид из окна',text)
    check.is_in('Год постройки',text)
    check.is_in('Тип дома',text)
    check.is_in('Дома под снос',text)
    check.is_in('Лифт',text)
    check.is_in('Парковка',text)
    check.is_in('Тип продажи',text)
    check.is_in('Апартаменты',text)
    check.is_in('Дата публикации',text)
    check.is_in('Содержит слова в объявлении',text)
    check.is_in('Исключить слова в объявлении',text)
    check.is_in('Номер телефона',text)
    check.is_in('Номер объявления',text)

def test_save_search_popup(driver_buy_flat_results: WebDriver):
    d = driver_buy_flat_results

    d.find_element(By.XPATH, SAVE_SEARCH_BUTTON).click()
    modal = d.find_element(By.XPATH, SAVE_SEARCH_MODAL)

    text = modal.get_attribute('textContent')

    check.is_in('Назовите поиск', text)
    check.is_in('Частота уведомлений', text)
    check.is_in('Укажите почту', text)
    check.is_in('Хочу получать новости Cian.ru', text)
    check.is_in('Включить push-уведомления', text)

    eh.check_element_is_present(modal, SAVE_SEARCH_BUTTON, By.XPATH)

def test_popup_on_operation_kind_change(driver_buy_flat_results: WebDriver):
    d = driver_buy_flat_results

    d.find_element(By.CSS_SELECTOR, DEAL_TYPE_FILTER).click()
    d.find_element(By.XPATH, RENT_SELECT_OPTION).click()

    text = d.find_element(By.XPATH, CommonElements.POPPER).get_attribute('textContent')
    check.is_in('Найдено', text)
    check.is_in('объявлен', text)
    check.is_in('Применить', text)