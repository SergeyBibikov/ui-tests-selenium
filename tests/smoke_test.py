from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import helpers.elements as els
from pageobjects.searchBlock import SearchBlock


def test_title_content(driver: WebDriver):
    assert 'Циан - база недвижимости' in driver.title


def test_cookies_notification_hides_on_confirmation(driver: WebDriver):
    elements = driver.find_elements(
        By.CSS_SELECTOR, '[data-name="CookiesNotification"]')
    assert len(elements) == 1

    el: WebElement = elements[0].find_element(
        By.XPATH, '//span[text()="Принять"]')
    el.click()
    els.check_element_is_not_present(
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
