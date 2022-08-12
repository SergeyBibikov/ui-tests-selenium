import time
from constants import Urls

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

import pytest_check as check

from pageobjects.header import Header
from pageobjects.base import Base
from pageobjects.searchresults import SearchResults, CardIcons
import helpers.elements as eh
import helpers.waits as w
import helpers.actions as actions

buttons = {
    "ADD_TO_FOLDER": "[data-name='AddToFolderButtonContainer']",
    "NOTE": "[data-name='NoteButton']",
    "REMOVE": "[data-name='RemoveFavorite']",
    "REPORT": "button[title='Пожаловаться']"
}

SORT_OPTIONS = '[data-testid="sort_buttons"]'
DELETE_ALL = '//span[text()="Удалить все"]'


def test_DELETE_popup_on_all_favs_deletion(driver_rent: WebDriver):
    d = driver_rent

    SearchResults.toggle_first_result_icon(d, CardIcons.FAVOURITES)
    header = Header(d)
    header.favourites.click()
    actions.switchToNthTab(d, 2)
    d.find_element(By.XPATH, DELETE_ALL).click()
    eh.check_element_is_present(d,
                                '//div[text()="Вы действительно хотите удалить все избранные объекты?"]',
                                By.XPATH)


def test_sort_order_criteria(driver_no_link: WebDriver):
    d = driver_no_link
    d.get(Urls.FAVOURITES)
    d.find_element(
        By.XPATH, '//span[text()="По дате добавления в избранное"]').click()

    w.wait_for_text(d, 20, By.CSS_SELECTOR, SORT_OPTIONS,
                    "По дате добавления в избранное")
    w.wait_for_text(d, 20, By.CSS_SELECTOR, SORT_OPTIONS, "По цене")


def test_DELETE_action_buttons_on_the_ad_in_favs(driver_rent: WebDriver):
    d = driver_rent

    SearchResults.toggle_first_result_icon(d, CardIcons.FAVOURITES)
    header = Header(d)
    header.favourites.click()
    actions.switchToNthTab(d, 2)

    eh.check_element_is_present(d, buttons["ADD_TO_FOLDER"])
    eh.check_element_is_present(d, buttons["NOTE"])
    eh.check_element_is_present(d, buttons["REMOVE"])
    eh.check_element_is_present(d, buttons["REPORT"])
