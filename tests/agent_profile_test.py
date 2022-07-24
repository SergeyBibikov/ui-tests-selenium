import time
import constants

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

import pytest_check as check

from pageobjects.header import Header
from pageobjects.base import Base
from pageobjects.searchresults import SearchResults
import helpers.elements as eh
import helpers.waits as w
import helpers.actions as actions

AGENT_PAGE = 'https://www.cian.ru/agents/6954508/'
ABOUT_AGENT_SECTION = '[data-name="AboutRealtorDesktop"]'

CONTACT_FORM = '[data-name="Aside"]'
PROFILE_CONTENT = '[data-name="ViewDesktop"]'

def test_contact_agent_form(driver_no_link: WebDriver):
    """
        The first time in a session you open an agent card
        you should see the contact form
    """
    d = driver_no_link
    d.get(AGENT_PAGE)
    w.wait_for_text(d, 20, By.CSS_SELECTOR, CONTACT_FORM, 'Свяжитесь с риелтором')
    w.wait_for_text(d, 20, By.CSS_SELECTOR, CONTACT_FORM, 'Что нужно сделать')
    w.wait_for_text(d, 20, By.CSS_SELECTOR, CONTACT_FORM, 'Какую недвижимость')
    w.wait_for_text(d, 20, By.CSS_SELECTOR, CONTACT_FORM, 'В каком городе')
    w.wait_for_text(d, 20, By.CSS_SELECTOR, CONTACT_FORM, 'Ваше имя')
    w.wait_for_text(d, 20, By.CSS_SELECTOR, CONTACT_FORM, 'Номер для связи')
    w.wait_for_text(d, 20, By.CSS_SELECTOR, CONTACT_FORM, 'Комментарий (необязательно)')
    w.wait_for_text(d, 20, By.CSS_SELECTOR, CONTACT_FORM, 'Отправить заявку')

def test_about_agent_section_content(driver_no_link: WebDriver):
    d = driver_no_link

    d.get(AGENT_PAGE)

    w.wait_for_text(d, 20, By.CSS_SELECTOR, ABOUT_AGENT_SECTION, 'Специализация')
    w.wait_for_text(d, 20, By.CSS_SELECTOR, ABOUT_AGENT_SECTION, 'Регион работы')
    w.wait_for_text(d, 20, By.CSS_SELECTOR, ABOUT_AGENT_SECTION, 'Агентство')

def test_agent_profile_sections(driver_no_link: WebDriver):
    d = driver_no_link

    d.get(AGENT_PAGE)

    w.wait_for_text(d, 20, By.CSS_SELECTOR, PROFILE_CONTENT, 'Отзывы')
    w.wait_for_text(d, 20, By.CSS_SELECTOR, PROFILE_CONTENT, 'Контакты')
    w.wait_for_text(d, 20, By.CSS_SELECTOR, PROFILE_CONTENT, 'Аренда квартир и комнат')
    w.wait_for_text(d, 20, By.CSS_SELECTOR, PROFILE_CONTENT, 'Продажа квартир и комнат')
