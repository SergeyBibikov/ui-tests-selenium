import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

import pytest_check as check

from pageobjects.header import Header
from pageobjects.base import Base
from pageobjects.searchresults import SearchResults
import helpers.elements as eh
import helpers.waits as w
import helpers.actions as actions

buttons = {
    "ADD_TO_FOLDER":"[data-name='AddToFolderButtonContainer']",
    "NOTE":"[data-name='NoteButton']",
    "REMOVE":"[data-name='RemoveFavorite']",
    "REPORT":"button[title='Пожаловаться']"
}

def test_popup_when_ad_is_added_to_favs(driver_rent: WebDriver):
    d = driver_rent

    SearchResults.toggle_first_result_favs(d)

    eh.check_element_is_present(
        d, '//div[text()="Сохранено в избранное"]', By.XPATH)


def test_popup_when_ad_is_unfaved(driver_rent: WebDriver):

    d = driver_rent

    SearchResults.toggle_first_result_favs(d)
    SearchResults.toggle_first_result_favs(d)

    eh.check_element_is_present(d,'//span[text()="Удалено из избранного"]',By.XPATH)
    eh.check_element_is_present(d,'//p[text()="Объявление удалено из избранного и всех подборок"]',By.XPATH)
    eh.check_element_is_present(d,'//button[span[text()="Понятно"]]',By.XPATH)


def test_popup_on_deletion_from_favs(driver_no_link: WebDriver):
    pass


def test_sort_order_criteria(driver_no_link: WebDriver):
    """  
    Should have two criferia 
    """
    pass


def test_action_buttons_on_the_ad_in_favs(driver_rent: WebDriver):
    d = driver_rent

    SearchResults.toggle_first_result_favs(d)
    header = Header(d)
    header.favourites.click()
    actions.switchToNthTab(d, 2)

    eh.check_element_is_present(d, buttons["ADD_TO_FOLDER"])
    eh.check_element_is_present(d, buttons["NOTE"])
    eh.check_element_is_present(d, buttons["REMOVE"])
    eh.check_element_is_present(d, buttons["REPORT"])