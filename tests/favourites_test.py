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


def test_sort_order_criteria(driver_no_link: WebDriver):
    d = driver_no_link
    d.get(Urls.FAVOURITES)
    d.find_element(
        By.XPATH, '//span[text()="По дате добавления в избранное"]').click()

    w.wait_for_text(d, 20, By.CSS_SELECTOR, SORT_OPTIONS,
                    "По дате добавления в избранное")
    w.wait_for_text(d, 20, By.CSS_SELECTOR, SORT_OPTIONS, "По цене")
