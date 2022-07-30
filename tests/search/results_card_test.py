import time

import pytest_check as check

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from pageobjects.searchblock import SearchBlock
from pageobjects.searchresults import SearchResults
import helpers.elements as eh
import helpers.waits as w
from constants import CommonElements

COMPARISON_NOTIFICATION = '[data-name="ComparisonNotification"]'

def test_popup_when_ad_is_added_to_favs(driver_rent: WebDriver):
    d = driver_rent

    SearchResults.toggle_first_result_favs(d)

    eh.check_element_is_present(
        d, '//div[text()="Сохранено в избранное"]', By.XPATH)


def test_popup_when_ad_is_unfaved(driver_rent: WebDriver):

    d = driver_rent

    SearchResults.toggle_first_result_favs(d)
    SearchResults.toggle_first_result_favs(d)

    eh.check_element_is_present(
        d, '//span[text()="Удалено из избранного"]', By.XPATH)
    eh.check_element_is_present(
        d, '//p[text()="Объявление удалено из избранного и всех подборок"]', By.XPATH)
    eh.check_element_is_present(
        d, '//button[span[text()="Понятно"]]', By.XPATH)

def test_popup_when_ad_is_added_to_comparison(driver_buy_flat_results: WebDriver):
    d = driver_buy_flat_results

    SearchResults.toggle_first_result_comparison(d)

    eh.check_element_is_present(d, COMPARISON_NOTIFICATION)

    text = d.find_element(By.CSS_SELECTOR, COMPARISON_NOTIFICATION).get_attribute('textContent')

    check.is_in('Вы сравниваете 1 квартиру', text)
    check.is_in('Можно добавить ещё 19', text)

def test_popup_when_ad_is_removed_from_comparison(driver_buy_flat_results: WebDriver):
    d = driver_buy_flat_results

    SearchResults.toggle_first_result_comparison(d)
    SearchResults.toggle_first_result_comparison(d)

    eh.check_element_is_present(d, COMPARISON_NOTIFICATION)

    w.wait_for_text(d, 20, By.CSS_SELECTOR, COMPARISON_NOTIFICATION, 'Вы очистили список сравнения')
    w.wait_for_text(d, 20, By.CSS_SELECTOR, COMPARISON_NOTIFICATION, 'добавьте что-нибудь')

def test_hide_ad_triggers_sign_in_window(driver_buy_flat_results: WebDriver):
    d = driver_buy_flat_results

    SearchResults.hide_ad(d)

    eh.check_element_is_present(d, CommonElements.AUTH_MODAL)