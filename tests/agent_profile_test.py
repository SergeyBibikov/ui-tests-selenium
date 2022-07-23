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

AGENT_PAGE = 'https://www.cian.ru/agents/6703588/'
CONTACT_FORM = '[data-name="Aside"]'

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