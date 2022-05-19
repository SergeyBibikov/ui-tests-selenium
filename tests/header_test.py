from time import sleep
from pageobjects.header import Header
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import helpers.elements as eh


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
    eh.check_element_is_present(
        header.root, '//a[span[text()="+ Разместить объявление"]]', By.XPATH)


def test_sign_in_button_is_present(driver: WebDriver):
    header = Header(driver)
    eh.check_element_is_present(
        header.root, '//a[span[text()="Войти"]]', By.XPATH)


def test_popup_compare_objects(driver: WebDriver):
    eh.check_element_is_not_present(
        driver, '//div[@data-popper-placement][div[text()="Сравнение объектов"]]', By.XPATH
    )

    header = Header(driver)
    ActionChains(driver).move_to_element(header.compare_objects).perform()

    eh.check_element_is_present(
        driver, '//div[@data-popper-placement][div[text()="Сравнение объектов"]]', By.XPATH)


def test_popup_favourites(driver: WebDriver):

    eh.check_element_is_not_present(
        driver, '//div[@data-popper-placement][div[text()="Избранное"]]', By.XPATH
    )

    header = Header(driver)
    ActionChains(driver).move_to_element(header.favourites).perform()

    eh.check_element_is_present(
        driver, '//div[@data-popper-placement][div[text()="Избранное"]]', By.XPATH)


def test_popup_notifications(driver: WebDriver):
    eh.check_element_is_not_present(
        driver, '//div[@data-popper-placement][div[text()="Уведомления"]]', By.XPATH
    )

    header = Header(driver)
    ActionChains(driver).move_to_element(header.notifications).perform()

    eh.check_element_is_present(
        driver, '//div[@data-popper-placement][div[text()="Уведомления"]]', By.XPATH)


def test_go_to_compare(driver: WebDriver):
    header = Header(driver)
    header.compare_objects.click()
    driver.switch_to.window(driver.window_handles[1])
    eh.check_element_is_present(
        driver, '//h1[text()="Список сравнения пуст"]', By.XPATH)
    eh.check_element_is_present(
        driver, '//a[span[text()="Искать квартиры"]]', By.XPATH)


def test_empty_favourites_card_text(driver: WebDriver):
    driver.implicitly_wait(5)

    eh.check_element_is_not_present(
        driver, Header.favsCard, By.XPATH)

    header = Header(driver)
    header.favourites.click()
    eh.check_element_is_present(driver, Header.favsCard, By.XPATH)

    card = driver.find_element(By.XPATH, Header.favsCardBody)
    assert 'Добавляйте объявления в избранное' in card.get_attribute(
        'textContent')

    driver.find_element(By.XPATH, '//button[text()="ЖК"]').click()
    card = driver.find_element(By.XPATH, Header.favsCardBody)
    assert 'Здесь будут любимые жилые комплексы' in card.get_attribute(
        'textContent')


def test_go_to_favs_page_from_favs_card(driver: WebDriver):
    driver.implicitly_wait(5)

    header = Header(driver)
    header.close_compare_promo()
    header.favourites.click()

    card = driver.find_element(By.XPATH, Header.favsCard)
    card.find_element(
        By.XPATH, '//a[span[text()="Перейти в избранное"]]').click()

    assert len(driver.window_handles) == 2
    driver.switch_to.window(driver.window_handles[1])
    assert '/favorites' in driver.current_url
