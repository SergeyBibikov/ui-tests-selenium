from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import helpers.elements as eh
import helpers.waits as w
from pageobjects.geoswitcher import GeoSwitcher
from pageobjects.searchblock import SearchBlock
import time


def test_title_content(driver: WebDriver):
    assert 'Циан - база недвижимости' in driver.title


def test_compare_promo_popup(driver: WebDriver):
    loc = '[data-name="CompareOnboarding"]'
    eh.check_element_is_present(driver, loc)
    onb_text = driver.find_element(
        By.CSS_SELECTOR, loc).get_attribute('textContent')
    assert 'Сравнивайте квартиры по параметрам' in onb_text
    assert 'Пока это работает только с квартирами от' in onb_text
    assert 'застройщиков' in onb_text


def test_cookies_notification_hides_on_confirmation(driver: WebDriver):
    elements = driver.find_elements(
        By.CSS_SELECTOR, '[data-name="CookiesNotification"]')
    assert len(elements) == 1

    el: WebElement = elements[0].find_element(
        By.XPATH, '//span[text()="Принять"]')
    el.click()
    eh.check_element_is_not_present(
        driver, '[data-name="CookiesNotification"]')


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
    driver.implicitly_wait(10)

    geo_sw = GeoSwitcher(driver)
    geo_sw.change_location('Казань')
    w.wait_for_text(driver, 20, By.CSS_SELECTOR,
                    geo_sw.main_page_button, 'Казань')


def test_search_with_default_params(driver: WebDriver):
    driver.implicitly_wait(10)
    results = '[data-name="SummaryHeader"]'

    driver.find_element(
        By.CSS_SELECTOR, '[data-mark="FiltersSearchButton"]').click()
    w.wait_for_text(driver, 20, By.CSS_SELECTOR, results, 'Найдено')
    w.wait_for_text(driver, 20, By.CSS_SELECTOR, results, 'объявлени')
