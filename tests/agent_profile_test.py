import time
from constants import CommonElements

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

import pytest_check as check

import helpers.elements as eh
import helpers.waits as w

AGENT_PAGE = 'https://www.cian.ru/agents/6954508/'
AGENT_WITH_CONTACT_FORM = 'https://www.cian.ru/agents/21866732/'
ABOUT_AGENT_SECTION = '[data-name="AboutRealtorDesktop"]'

CONTACT_FORM = '[data-name="Aside"]'

LEAVE_A_REVIEW = '//span[text()="Написать отзыв"]'

PROFILE_CONTENT = '[data-name="ViewDesktop"]'
PHONE_CONTAINER = '[class*="phones-container"]'


def test_contact_agent_form(driver_no_link: WebDriver):
    """
        The first time in a session you open an agent card
        you should see the contact form
    """
    d = driver_no_link
    d.get(AGENT_WITH_CONTACT_FORM)
    w.wait_for_text(d, 20, By.CSS_SELECTOR, CONTACT_FORM,
                    'Свяжитесь с риелтором')
    w.wait_for_text(d, 20, By.CSS_SELECTOR, CONTACT_FORM, 'Что нужно сделать')
    w.wait_for_text(d, 20, By.CSS_SELECTOR, CONTACT_FORM, 'Какую недвижимость')
    w.wait_for_text(d, 20, By.CSS_SELECTOR, CONTACT_FORM, 'В каком городе')
    w.wait_for_text(d, 20, By.CSS_SELECTOR, CONTACT_FORM, 'Ваше имя')
    w.wait_for_text(d, 20, By.CSS_SELECTOR, CONTACT_FORM, 'Номер для связи')
    w.wait_for_text(d, 20, By.CSS_SELECTOR, CONTACT_FORM,
                    'Комментарий (необязательно)')
    w.wait_for_text(d, 20, By.CSS_SELECTOR, CONTACT_FORM, 'Отправить заявку')


def test_about_agent_section_content(driver_no_link: WebDriver):
    d = driver_no_link

    d.get(AGENT_PAGE)

    w.wait_for_text(d, 20, By.CSS_SELECTOR,
                    ABOUT_AGENT_SECTION, 'Специализация')
    w.wait_for_text(d, 20, By.CSS_SELECTOR,
                    ABOUT_AGENT_SECTION, 'Регион работы')
    w.wait_for_text(d, 20, By.CSS_SELECTOR, ABOUT_AGENT_SECTION, 'Агентство')


def test_agent_profile_sections(driver_no_link: WebDriver):
    d = driver_no_link

    d.get(AGENT_PAGE)

    w.wait_for_text(d, 20, By.CSS_SELECTOR, PROFILE_CONTENT, 'Отзывы')
    w.wait_for_text(d, 20, By.CSS_SELECTOR, PROFILE_CONTENT, 'Контакты')
    w.wait_for_text(d, 20, By.CSS_SELECTOR, PROFILE_CONTENT,
                    'Продажа квартир и комнат')


def test_agent_phone_reveal(driver_no_link: WebDriver):
    """
    Checks that the phones is masked by default 
    and is displayed on button click
    """
    d = driver_no_link

    d.get(AGENT_PAGE)

    text = d.find_element(
        By.CSS_SELECTOR, PHONE_CONTAINER).get_attribute('textContent')
    check.is_in('XX-XX', text)

    d.find_element(By.CSS_SELECTOR, PHONE_CONTAINER
                   ).find_element(By.XPATH, '//span[contains(., "Показать")]').click()

    text = d.find_element(
        By.CSS_SELECTOR, PHONE_CONTAINER).get_attribute('textContent')
    check.is_not_in('XX-XX', text)


def test_sign_in_on_review_attempt(driver_no_link: WebDriver):
    """
    Checks that an anauthenticated user cannot 
    leave an agent review
    """
    d = driver_no_link

    d.get(AGENT_PAGE)

    d.find_element(By.XPATH, LEAVE_A_REVIEW).click()

    eh.check_element_is_present(d, CommonElements.AUTH_MODAL)