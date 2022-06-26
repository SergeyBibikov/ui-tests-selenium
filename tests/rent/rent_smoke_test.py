from operator import gt
import time

import pytest_check as check

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from pageobjects.searchblock import SearchBlock
import helpers.elements as eh
import constants

QUICK_LINKS = '[data-name="QuickLinksList"]'
SORT_BUTTON = 'button[data-mark="SortDropdownButton"]'
SORT_FILTER_DROPDOWN = 'div[data-name="SummaryButtonWrapper"] div[class*="dropdown"]'

def test_recommend_block_categories(driver_rent: WebDriver):
    d = driver_rent
    text = d.find_element(By.CSS_SELECTOR, QUICK_LINKS).get_attribute('textContent')

    check.is_in('без посредников', text)
    check.is_in('холодильник', text)
    check.is_in('с мебелью', text)
    check.is_in('стиральная машина', text)
    check.is_in('изолированные комнаты', text)
    check.is_in('на длительный срок', text)
    check.is_in('не под реновацию', text)
    check.is_in('рядом с метро', text)

def test_sort_order_filter(driver_rent: WebDriver):
    d = driver_rent
    d.find_element(By.CSS_SELECTOR, SORT_BUTTON).click()

    eh.check_element_is_present(d, SORT_FILTER_DROPDOWN)

    text = d.find_element(By.CSS_SELECTOR, SORT_FILTER_DROPDOWN).get_attribute('textContent')

    check.is_in('По умолчанию', text)
    check.is_in('По цене (сначала дешевле)', text)
    check.is_in('По цене (сначала дороже)', text)
    check.is_in('По общей площади', text)
    check.is_in('По времени до метро', text)
    check.is_in('По улице', text)
    check.is_in('По дате добавления (сначала новые)', text)
    check.is_in('По дате добавления (сначала старые)', text)