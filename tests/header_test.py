from pageobjects.header import Header
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import helpers.elements as els


def test_links_list(driver: WebDriver):
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


def test_place_ad_button_is_present(driver: WebDriver):
    header = Header(driver)
    els.check_element_is_present(
        header.root, '//a[span[text()="+ Разместить объявление"]]', By.XPATH)


def test_sign_in_button_is_present(driver: WebDriver):
    header = Header(driver)
    els.check_element_is_present(
        header.root, '//a[span[text()="Войти"]]', By.XPATH)


def test_popup_compare_objects(driver: WebDriver):
    els.check_element_is_not_present(
        driver, '//div[@data-popper-placement][div[text()="Сравнение объектов"]]', By.XPATH
    )

    header = Header(driver)
    ActionChains(driver).move_to_element(header.compare_objects).perform()

    els.check_element_is_present(
        driver, '//div[@data-popper-placement][div[text()="Сравнение объектов"]]', By.XPATH)


def test_popup_favourites(driver: WebDriver):

    els.check_element_is_not_present(
        driver, '//div[@data-popper-placement][div[text()="Избранное"]]', By.XPATH
    )

    header = Header(driver)
    ActionChains(driver).move_to_element(header.favourites).perform()

    els.check_element_is_present(
        driver, '//div[@data-popper-placement][div[text()="Избранное"]]', By.XPATH)


def test_popup_notifications(driver: WebDriver):
    els.check_element_is_not_present(
        driver, '//div[@data-popper-placement][div[text()="Уведомления"]]', By.XPATH
    )

    header = Header(driver)
    ActionChains(driver).move_to_element(header.notifications).perform()

    els.check_element_is_present(
        driver, '//div[@data-popper-placement][div[text()="Уведомления"]]', By.XPATH)
