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

ADD_VILLAGE_BUTTON = '//button[span[text()="Добавить посёлок"]]'
LAND_SELL_LINK = '//a[text()="Продажа участков"]'
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