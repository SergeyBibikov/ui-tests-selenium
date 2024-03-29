from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import helpers.elements as eh
import helpers.waits as w
import helpers.actions as a

import pytest_check as check

from pageobjects.geoswitcher import GeoSwitcher
from pageobjects.searchblock import SearchBlock
from pageobjects.base import Base

import pytest_check as check

""" MAIN PAGE BASIC FUNCTIONALITY AND CONTENT TESTS """


def test_title_content(driver: WebDriver):
    assert 'Циан - база недвижимости' in driver.title


def test_main_page_sections(driver: WebDriver):
    eh.check_element_is_present(
        driver, '//*[text()="Акции и скидки на новостройки"]', By.XPATH)
    eh.check_element_is_present(
        driver, '//*[text()="Полезные ссылки"]', By.XPATH)
    eh.check_element_is_present(
        driver, '//*[text()="Специалисты"]', By.XPATH)
    eh.check_element_is_present(driver, '//*[text()="Журнал"]', By.XPATH)


def test_popular_ads_sell_tabs(driver: WebDriver):
    pop_text = driver.find_elements(
        By.CSS_SELECTOR, '[data-name="PopularHeader"]')[0].get_attribute('textContent')

    check.is_in('Жилая', pop_text)
    check.is_in('Загородная', pop_text)
    check.is_in('Коммерческая', pop_text)


def test_popular_ads_rent_tabs(driver: WebDriver):
    pop_text = driver.find_elements(
        By.CSS_SELECTOR, '[data-name="PopularHeader"]')[1].get_attribute('textContent')

    check.is_in('Жилая', pop_text)
    check.is_in('Загородная', pop_text)
    check.is_in('Коммерческая', pop_text)
    check.is_in('Посуточно', pop_text)


def test_cookies_notification_hides_on_confirmation(driver: WebDriver):
    elements = driver.find_elements(
        By.CSS_SELECTOR, Base.coookies_notification)
    assert len(elements) == 1

    Base.close_cookies_notification(driver)
    eh.check_element_is_not_present(
        driver, Base.coookies_notification)


def test_operation_kinds(driver: WebDriver):
    expected_links_list = [
        'Купить',
        'Снять',
        'Посуточно',
        'Оценить',
        'Ипотека',
        'Подбор риелтора',
    ]
    kind_switch = SearchBlock(driver)
    links = [el.get_attribute('textContent') for el in kind_switch.root.find_elements(
        By.CSS_SELECTOR, 'ul > li > a')]
    assert links == expected_links_list


def test_location_change(driver: WebDriver):
    geo_sw = GeoSwitcher(driver)
    geo_sw.change_location('Казань')

    w.wait_for_text(driver, 20, By.CSS_SELECTOR,
                    geo_sw.main_page_button, 'Казань')


def test_search_with_default_params(driver: WebDriver):
    results = '[data-name="SummaryHeader"]'

    driver.find_element(
        By.CSS_SELECTOR, '[data-mark="FiltersSearchButton"]').click()
    w.wait_for_text(driver, 20, By.CSS_SELECTOR, results, 'Найдено')
    w.wait_for_text(driver, 20, By.CSS_SELECTOR, results, 'объявлени')


def test_map_opening(driver: WebDriver):

    search = SearchBlock(driver)
    search.show_on_map()

    eh.check_element_is_not_present(driver, SearchBlock.root_loc)
    eh.check_element_is_present(driver, '[data-name="Map"]')


def test_specialist_lists_content(driver: WebDriver):
    spec_list = driver.find_elements(
        By.CSS_SELECTOR, '[data-name="SpecialistList"]')
    assert len(spec_list) == 3

    check.is_in('Риелторы', spec_list[0].get_attribute('textContent'))
    check.is_in('Агентства', spec_list[1].get_attribute('textContent'))
    check.is_in('Застройщики', spec_list[2].get_attribute('textContent'))


def test_footer_sections(driver: WebDriver):
    footer_loc = '//main/following-sibling::div[1]'
    text = driver.find_element(
        By.XPATH, footer_loc).get_attribute('textContent')

    check.is_in('Квартиры у метро', text)
    check.is_in('Квартиры в районе', text)
    check.is_in('Недвижимость в Подмосковье', text)
    check.is_in('Объявления по всей России', text)
