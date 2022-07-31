import time

import allure
import pytest_check as check

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

from pageobjects.searchblock import SearchBlock
from pageobjects.header import Header
import helpers.waits as w
import helpers.actions as a
import helpers.elements as eh

from constants import Urls
from constants import CommonElements

ADD_VILLAGE_BUTTON = '//button[span[text()="Добавить посёлок"]]'
LAND_SELL_LINK = '//a[text()="Продажа участков"]'
RENT_HOUSE_LINK = '//a[text()="Аренда домов"]'
VILLAGE_LIST_LINK = '//a[text()="в посёлках "]'

def test_housing_community_add_village_button(driver_no_link: WebDriver):
    d = driver_no_link

    d.get(Urls.HOUSING_COMMUNITY)

    eh.check_element_is_present(d, ADD_VILLAGE_BUTTON, By.XPATH)

def test_link_to_villages_list(driver: WebDriver):
    d = driver
    
    header_link = driver.find_element(By.XPATH, Header.houses_and_land)

    a.hover(d, header_link)

    driver.find_element(By.XPATH, LAND_SELL_LINK).click()

    eh.check_element_is_present(driver, VILLAGE_LIST_LINK, By.XPATH)

def test_house_rent_additional_filters(driver: WebDriver):
    d = driver
    
    header_link = driver.find_element(By.XPATH, Header.houses_and_land)

    a.hover(d, header_link)

    driver.find_element(By.XPATH, RENT_HOUSE_LINK).click()

    d.find_element(By.CSS_SELECTOR, CommonElements.ADVANCED_FILTERS).click()

    text = d.find_element(By.XPATH, CommonElements.ADVANCED_FILTERS_CARD).get_attribute('textContent')

    check.is_in('Срок аренды',text)
    check.is_in('От МКАД',text)
    check.is_in('До метро',text)
    check.is_in('Площадь',text)
    check.is_in('Удобства',text)
    check.is_in('Дополнительно',text)
    check.is_in('Ванна/Душ',text)
    check.is_in('Санузел',text)
    check.is_in('Ремонт',text)
    check.is_in('Этажей в доме',text)
    check.is_in('Материал дома',text)
    check.is_in('Тип отопления',text)
    check.is_in('Год постройки',text)
    check.is_in('Условия сделки',text)
    check.is_in('Условия проживания',text)
    check.is_in('Дата публикации',text)
    check.is_in('Продавец',text)
    check.is_in('Содержит слова в объявлении',text)
    check.is_in('Исключить слова в объявлении',text)
    check.is_in('Номер телефона',text)
    check.is_in('Номер объявления',text)