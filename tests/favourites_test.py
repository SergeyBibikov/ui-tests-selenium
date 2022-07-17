import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pageobjects.header import Header
from pageobjects.base import Base
from pageobjects.searchresults import SearchResults
import helpers.elements as eh
import helpers.waits as w


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


def test_popup_on_deletion_from_favs(driver: WebDriver):
    pass


def test_sort_order_criteria(driver: WebDriver):
    """  
    Should have two criferia 
    """
    pass


def test_action_buttons_on_the_ad_in_favs(driver: WebDriver):
    """ 
    Checks that there are buttons allowing
    various actions on an item in favs
    """
    pass
