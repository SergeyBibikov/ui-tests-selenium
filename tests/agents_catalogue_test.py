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
import helpers.actions as a

AGENCIES_BUTTON = '//button[span[text()="Агентства"]]'
AGENT_SELECTION_BANNER = '//*[@data-name="RealtorBannerCard"]'
CALL_BUTTON = '//button[span[text()="+7 800 511-79-..."]]'
CALL_US_BANNER = '//div[@data-name="CallUsBanner"]/following-sibling::div[1]'
DEAL_TYPE_FILTER = '//div[@data-name="DealTypeContainer"]'
DEAL_FILTER_DROPDOWN = '//div[contains(@class, "dropdown") and contains(., "Любая сделка")]'
ESTATE_KIND_FILTER = '//div[@data-name="DropdownWrapper"]'
ESTATE_KIND_DROPDOWN = '//div[contains(@class, "dropdown") and not(contains(., "Любая недвижимость"))]'
INTRO_SECTION = '//section[contains(@class,"intro")]'
LISTING = '//div[@data-name="ListingLayout"]'
RATING_COMMERCIAL_ESTATE_LABEL = '//label[contains(., "Коммерческая недвижимость")]' 
RATING_LINK = '//a[span[text()="Ежемесячный рейтинг профессионалов ↗"]]'
RATING_HEADINGS = '//div[@class="rating__headings"]'
SEARCH_BAR = '//input[@placeholder="Имя, телефон или название агентства"]'
SORT_FILTER_DROPDOWN = '//div[contains(@class, "dropdown") and contains(., "По умолчанию")]'
SORT_FILTER = '[data-name="SortFilter"]'
SELECT_AGENT_BUTTON = AGENT_SELECTION_BANNER + '//a[span[text()="Подобрать риелтора"]]'

def test_monthly_ratings_lead(driver_agents_list: WebDriver):
    d = driver_agents_list

    d.find_element(By.XPATH, RATING_LINK).click()
    a.switchToNthTab(d, 2)

    check.is_in('info.cian.ru', d.current_url)

    text = d.find_element(By.XPATH, RATING_HEADINGS).get_attribute('textContent')
    check.is_in('Место',text)
    check.is_in('Риелторы',text)
    check.is_in('Агентства',text)
    check.is_in('Охват',text)
    check.is_in('млн показов',text)

def test_agents_agencies_switch(driver_agents_list: WebDriver):
    d = driver_agents_list

    d.find_element(By.XPATH, AGENCIES_BUTTON).click()
    check.is_in('agentstva', d.current_url)
    text = d.find_element(By.XPATH, LISTING).get_attribute('textContent')
    check.is_in("Этажи Москва", text)

def test_deal_kinds_filter(driver_agents_list: WebDriver):
    d = driver_agents_list
    d.find_element(By.XPATH, DEAL_TYPE_FILTER).click()

    text = d.find_element(
        By.XPATH, DEAL_FILTER_DROPDOWN).get_attribute('textContent')
    check.is_in('Аренда', text)
    check.is_in('Покупка и продажа', text)

def test_estate_kind_filter(driver_agents_list: WebDriver):
    d = driver_agents_list
    d.find_element(By.XPATH, ESTATE_KIND_FILTER).click()

    text = d.find_element(
        By.XPATH, ESTATE_KIND_DROPDOWN).get_attribute('textContent')
    check.is_in('Жилая', text)
    check.is_in('Загородная', text)
    check.is_in('Коммерческая', text)

def test_search_bar_is_present(driver_agents_list: WebDriver):
    d = driver_agents_list

    eh.check_element_is_present(d, SEARCH_BAR, By.XPATH)

def test_agents_list_sorting_filters(driver_agents_list: WebDriver):
    d = driver_agents_list

    eh.check_element_is_not_present(d, SORT_FILTER_DROPDOWN, By.XPATH)

    d.find_element(By.CSS_SELECTOR, SORT_FILTER).click()

    text = d.find_element(
        By.XPATH, SORT_FILTER_DROPDOWN).get_attribute('textContent')

    check.is_in('По времени на Циан', text)
    check.is_in('По алфавиту', text)
    check.is_in('По количеству объявлений', text)

def test_call_us_banner_is_present(driver_agents_list: WebDriver):
    d = driver_agents_list

    text = d.find_element(
        By.XPATH, CALL_US_BANNER).get_attribute('textContent')

    check.is_in('Позвоните нам', text)
    check.is_in('Мы бесплатно подберём риелтора по вашим запросам', text)
    check.is_in('Для звонков по России', text)

    eh.check_element_is_present(d, CALL_US_BANNER + CALL_BUTTON, By.XPATH)

def test_agent_selection_help_banner_is_present(driver_agents_list: WebDriver):
    d = driver_agents_list

    w.wait_for_text(d, 20, By.XPATH,
                    AGENT_SELECTION_BANNER, 'Бесплатно подберем риелтора')
    w.wait_for_text(d, 20, By.XPATH, AGENT_SELECTION_BANNER,
                    'Ответьте на несколько вопросов и вам позвонят подходящие риелторы')
    eh.check_element_is_present(d, SELECT_AGENT_BUTTON, By.XPATH)

def test_rating_estate_kind_switch(driver_no_link: WebDriver):
    d = driver_no_link

    d.get(c.urls["AGENCIES_RATINGS"])

    d.find_element(By.XPATH, RATING_COMMERCIAL_ESTATE_LABEL).click()

    check.is_in('com', d.current_url)

    text = d.find_element(By.XPATH, INTRO_SECTION).get_attribute('textContent')
    check.is_in('Рейтинг профессионалов рынка недвижимости', text)
