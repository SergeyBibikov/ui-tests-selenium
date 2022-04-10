from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from pageobjects.header import Header
from pageobjects.kindswitch import KindSwitch


def test_title_content(driver: WebDriver):
    assert 'Циан - база недвижимости' in driver.title


def test_header_links(driver: WebDriver):
    expected_links_list = [
        'Аренда',
        'Продажа',
        'Новостройки',
        'Дома и участки',
        'Коммерческая',
        'Ипотека',
        'Сервисы',
        'Ещё',
        'Ещё',
        'Ещё'
    ]
    header = Header(driver)
    links = [el.get_attribute('textContent') for el in header.root.find_elements(
        By.CSS_SELECTOR, 'ul > li > *')]
    assert links == expected_links_list


def test_operation_kinds(driver: WebDriver):
    expected_links_list = [
        'Купить',
        'Снять',
        'Посуточно',
        'Оценить',
        'Ипотека',
        'Подбор риелтора',
    ]
    kind_switch = KindSwitch(driver)
    links = [el.get_attribute('textContent') for el in kind_switch.root.find_elements(
        By.CSS_SELECTOR, 'ul > li > a')]
    assert links == expected_links_list
