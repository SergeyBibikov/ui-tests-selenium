import time
import constants as c

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

import pytest_check as check

from pageobjects.header import Header
from pageobjects.base import Base
from pageobjects.searchresults import SearchResults
import helpers.elements as eh
import helpers.waits as w
import helpers.actions as actions

AGENT_SELECTION_BANNER = '//*[@data-name="RealtorBannerCard"]'
CALL_BUTTON = '//button[span[text()="+7 800 511-79-..."]]'
CALL_US_BANNER = '//div[@data-name="CallUsBanner"]/following-sibling::div[1]'
FILTER_DROPDOWN = '//div[contains(@class, "dropdown") and contains(., "По умолчанию")]'
SORT_FILTER = '[data-name="SortFilter"]'
SELECT_AGENT_BUTTON = AGENT_SELECTION_BANNER + \
    '//a[span[text()="Подобрать риелтора"]]'


def test_agents_list_sorting_filters(driver_no_link: WebDriver):
    d = driver_no_link

    d.get(c.urls["AGENTS_LIST"])

    eh.check_element_is_not_present(d, FILTER_DROPDOWN, By.XPATH)

    d.find_element(By.CSS_SELECTOR, SORT_FILTER).click()

    text = d.find_element(
        By.XPATH, FILTER_DROPDOWN).get_attribute('textContent')

    check.is_in('По времени на Циан', text)
    check.is_in('По алфавиту', text)
    check.is_in('По количеству объявлений', text)


def test_call_us_banner_is_present(driver_no_link: WebDriver):
    d = driver_no_link

    d.get(c.urls["AGENTS_LIST"])

    text = d.find_element(
        By.XPATH, CALL_US_BANNER).get_attribute('textContent')

    check.is_in('Позвоните нам', text)
    check.is_in('Мы бесплатно подберём риелтора по вашим запросам', text)
    check.is_in('Для звонков по России', text)

    eh.check_element_is_present(d, CALL_US_BANNER + CALL_BUTTON, By.XPATH)


def test_agent_selection_help_banner_is_present(driver_no_link: WebDriver):

    d = driver_no_link

    d.get(c.urls["AGENTS_LIST"])

    w.wait_for_text(d, 20, By.XPATH,
                    AGENT_SELECTION_BANNER, 'Бесплатно подберем риелтора')
    w.wait_for_text(d, 20, By.XPATH, AGENT_SELECTION_BANNER,
                    'Ответьте на несколько вопросов и вам позвонят подходящие риелторы')
    eh.check_element_is_present(d, SELECT_AGENT_BUTTON, By.XPATH)