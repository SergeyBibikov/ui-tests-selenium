from pageobjects.header import Header
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

import helpers.elements as eh
import helpers.waits as w
import helpers.actions as a

import pytest_check as check

from constants import CommonElements

COMPARE_OBJECTS_POPUP = '//div[@data-popper-placement][div[text()="Сравнение объектов"]]'
EMPTY_COMPARISON_LIST = '//h1[text()="Список сравнения пуст"]'
EMPTY_RESULTS = 'div[data-name="ResultsEmpty"]'
FAVOURITES_POPUP = '//div[@data-popper-placement][div[text()="Избранное"]]'
FLAT_SEARCH_BUTTON = '//a[span[text()="Искать квартиры"]]'
NOTIFICATIONS_POPUP = '//div[@data-popper-placement][div[text()="Уведомления"]]'
RESIDENTIAL_HOMES = '//li[text()="Жилые комплексы"]'
SAVE_INTERESTING_RES_HOMES = '//span[text()="Сохраняйте интересные жилые комплексы"]'


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
    eh.check_element_is_present(driver, Header.place_ad, By.XPATH)


def test_sign_in_button_is_present(driver: WebDriver):
    header = Header(driver)
    eh.check_element_is_present(
        header.root, '//a[span[text()="Войти"]]', By.XPATH)


def test_popup_compare_objects(driver: WebDriver):
    eh.check_element_is_not_present(driver, COMPARE_OBJECTS_POPUP, By.XPATH)

    header = Header(driver)
    a.hover(driver, header.compare_objects)

    eh.check_element_is_present(driver, COMPARE_OBJECTS_POPUP, By.XPATH)


def test_popup_favourites(driver: WebDriver):

    eh.check_element_is_not_present(driver, FAVOURITES_POPUP, By.XPATH)

    header = Header(driver)
    a.hover(driver, header.favourites)

    eh.check_element_is_present(driver, FAVOURITES_POPUP, By.XPATH)


def test_popup_notifications(driver: WebDriver):
    eh.check_element_is_not_present(driver, NOTIFICATIONS_POPUP, By.XPATH)

    header = Header(driver)
    a.hover(driver, header.notifications)

    eh.check_element_is_present(driver, NOTIFICATIONS_POPUP, By.XPATH)


def test_go_to_compare(driver: WebDriver):
    header = Header(driver)
    header.compare_objects.click()
    a.switchToNthTab(driver, 2)
    eh.check_element_is_present(driver, EMPTY_COMPARISON_LIST, By.XPATH)
    eh.check_element_is_present(driver, FLAT_SEARCH_BUTTON, By.XPATH)


def test_empty_notifications_card(driver: WebDriver):

    n_card = Header.notificationsCard["root"]
    n_card_body = Header.notificationsCard["body"]

    eh.check_element_is_not_present(
        driver, n_card, By.XPATH)

    header = Header(driver)
    header.notifications.click()

    eh.check_element_is_present(driver, n_card, By.XPATH)
    w.wait_for_text(driver, 15, By.XPATH,
                    n_card_body,
                    'Ещё нет уведомлений')
    w.wait_for_text(driver, 15, By.XPATH,
                    n_card_body,
                    'Здесь будут уведомления об изменении цены и новых объявлениях по вашему поиску')


def test_notification_card_more_info_list(driver: WebDriver):

    more_icon = Header.notificationsCard["more"]["icon"]
    more_list = Header.notificationsCard["more"]["list"]

    header = Header(driver)
    header.notifications.click()

    eh.check_element_is_not_present(
        header.driver, more_list, By.XPATH)

    header.driver.find_element(By.XPATH, more_icon).click()

    eh.check_element_is_present(
        header.driver, more_list, By.XPATH)

    list_el_text = header.driver.find_element(
        By.XPATH, more_list).get_attribute('textContent')

    assert 'Отметить как прочитанные' in list_el_text
    assert 'Удалить все' in list_el_text
    assert 'Управление подписками' in list_el_text


def test_place_ad_button_lead(driver: WebDriver):

    header = Header(driver)
    header.place_ad_button.click()

    assert 'razmestit-obyavlenie' in driver.current_url


def test_sign_in_button_should_trigger_sign_in_window(driver: WebDriver):
    header = Header(driver)
    header.sign_in_button.click()
    eh.check_element_is_present(driver, CommonElements.AUTH_MODAL)


""" TESTS OF DROPDOWN CONTENT AFTER HOVER ON A HEADER LINK """


def test_rent_action_kinds_on_hover(driver: WebDriver):

    header = Header(driver)

    eh.check_element_is_not_present(driver, header.main_dropdown)

    rent_link: WebElement = header.root.find_element(By.LINK_TEXT, 'Аренда')
    a.hover(driver, rent_link)

    drop_text = driver.find_element(
        By.CSS_SELECTOR, header.main_dropdown).get_attribute('textContent')

    check.is_in('Длительная аренда', drop_text)
    check.is_in('Квартиры', drop_text)
    check.is_in('Комнаты', drop_text)
    check.is_in('Дома и коттеджи', drop_text)
    check.is_in('Посуточная аренда', drop_text)
    check.is_in('Циан.Журнал', drop_text)
    check.is_in('Как снять или сдать квартиру', drop_text)
    check.is_in('Как купить или продать квартиру на вторичном рынке', drop_text)


def test_sell_dropdown_content(driver: WebDriver):

    header = Header(driver)

    eh.check_element_is_not_present(driver, header.main_dropdown)

    rent_link: WebElement = header.root.find_element(By.LINK_TEXT, 'Продажа')
    a.hover(driver, rent_link)

    drop_text = driver.find_element(
        By.CSS_SELECTOR, header.main_dropdown).get_attribute('textContent')

    check.is_in('Квартиры', drop_text)
    check.is_in('Квартиры в новостройках', drop_text)
    check.is_in('Квартиры во вторичке', drop_text)
    check.is_in('Комнаты и доли', drop_text)
    check.is_in('Дома и коттеджи', drop_text)
    check.is_in('Участки', drop_text)


def test_new_houses_dropdown_content(driver: WebDriver):

    header = Header(driver)

    eh.check_element_is_not_present(driver, header.main_dropdown)

    rent_link: WebElement = header.root.find_element(
        By.LINK_TEXT, 'Новостройки')
    a.hover(driver, rent_link)

    drop_text = driver.find_element(
        By.CSS_SELECTOR, header.main_dropdown).get_attribute('textContent')

    check.is_in('Квартиры', drop_text)
    check.is_in('Каталог жилых комплексов', drop_text)
    check.is_in('Каталог коттеджных поселков', drop_text)
    check.is_in('Каталог акций и скидок', drop_text)
    check.is_in('Подобрать новостройку', drop_text)


def test_houses_and_land_dropdown_content(driver: WebDriver):

    header = Header(driver)

    eh.check_element_is_not_present(driver, header.main_dropdown)

    rent_link: WebElement = header.root.find_element(
        By.LINK_TEXT, 'Дома и участки')
    a.hover(driver, rent_link)

    drop_text = driver.find_element(
        By.CSS_SELECTOR, header.main_dropdown).get_attribute('textContent')

    check.is_in('Продажа домов и дач', drop_text)
    check.is_in('Продажа участков', drop_text)
    check.is_in('Продажа таунхаусов', drop_text)
    check.is_in('Аренда домов', drop_text)
    check.is_in('Коттеджные посёлки', drop_text)


def test_MORTGAGE_MAIN_dropdown_content(driver: WebDriver):

    header = Header(driver)

    eh.check_element_is_not_present(driver, header.main_dropdown)

    rent_link: WebElement = header.root.find_element(
        By.LINK_TEXT, 'Ипотека')
    a.hover(driver, rent_link)

    drop_text = driver.find_element(
        By.CSS_SELECTOR, header.main_dropdown).get_attribute('textContent')

    check.is_in('Персональные ипотечные предложения', drop_text)
    check.is_in('Господдержка', drop_text)
    check.is_in('Ипотечный калькулятор', drop_text)
    check.is_in('Ипотека на загородную недвижимость', drop_text)


def test_commercial_estate(driver: WebDriver):

    header = Header(driver)

    eh.check_element_is_not_present(driver, header.main_dropdown)

    rent_link: WebElement = header.root.find_element(
        By.LINK_TEXT, 'Коммерческая')
    a.hover(driver, rent_link)

    drop_text = driver.find_element(
        By.CSS_SELECTOR, header.main_dropdown).get_attribute('textContent')

    check.is_in('Аренда', drop_text)
    check.is_in('Аренда офиса', drop_text)
    check.is_in('Аренда коворкинга', drop_text)
    check.is_in('Аренда торговой площади', drop_text)
    check.is_in('Аренда складского помещения', drop_text)
    check.is_in('Продажа', drop_text)
    check.is_in('Продажа офиса', drop_text)
    check.is_in('Продажа торговой площади', drop_text)
    check.is_in('Продажа складского помещения', drop_text)
    check.is_in('Продажа  бизнеса', drop_text)
