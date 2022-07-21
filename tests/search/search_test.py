import time

import allure
import pytest_check as check

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

from pageobjects.searchblock import SearchBlock

import helpers.waits as w


@allure.step
def checkText(textToFind, actualText, msg=""):
    check.is_in(textToFind, actualText, msg)


def test_buy_default_filters(driver: WebDriver):

    sb = SearchBlock(driver)
    
    checkText("Квартиру в новостройке и вторичке", sb.offer_type.text)
    checkText("1, 2 комн.", sb.room_count.text)

def test_non_existing_city_search(driver: WebDriver):
    sb = SearchBlock(driver)

    sb.enter_location('dfsdfasdfa')

    w.wait_for_text(driver, 20, By.CSS_SELECTOR, sb.suggestion_popup_loc, "Ничего не найдено")