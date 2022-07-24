import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

import pytest_check as check

from pageobjects.header import Header
from pageobjects.base import Base
import helpers.scripts as s
import helpers.elements as eh
import helpers.waits as w
import helpers.actions as a

import constants as c

GET_CODE = '//form//button[span[text()="Получить код"]]'
DIFFERENT_METHOD = '//form//button[span[text()="Другим способом"]]'
SIGN_IN_WITH_PHONE = '//form//button[span[text()="Войти по телефону"]]'
NEED_HELP_LINK = '//a[div[text()="Нужна помощь?"]]'
EMAIL_ID_INPUT = 'form input[name="username"]'
CONTINUE = '//form//button[span[text()="Продолжить"]]'
CREATE_ACCOUNT = '//form//button[span[text()="Создать аккаунт"]]'
FORGOT_PASSWORD = '//a[text()="Забыли пароль?"]'
AUTH_MODAL = c.common_elements["AUTH_MODAL"]
icons = {
    "MAIL_RU":"//button[@title='Почта Mail.Ru']",
    "VK":"//button[@title='ВКонтакте']",
    "APPLE_ID":"//button[@title='Apple ID']",
    "MORE":"//button[@title='Показать ещё']"
}

def test_phone_field_red_border_on_empty_phone(driver: WebDriver):
    expected_initial_border = '1px solid rgb(206, 209, 215)'
    expected_border_after_validation = '1px solid rgb(255, 31, 52)'
    phone_input = 'form div[class*="--input-wrapper"]'

    header = Header(driver)
    header.sign_in_button.click()
    eh.check_element_is_present(driver, 'form')

    border = s.get_element_style_property(driver, phone_input, 'border')
    check.equal(border, expected_initial_border)

    driver.find_element(By.XPATH, GET_CODE).click()

    time.sleep(1) #Letting the style to change

    border = s.get_element_style_property(driver, phone_input, 'border')
    check.equal(border, expected_border_after_validation)

def test_other_sign_in_methods_icons(driver: WebDriver):

    header = Header(driver)
    header.sign_in_button.click()
    
    driver.find_element(By.XPATH, DIFFERENT_METHOD).click()

    eh.check_element_is_present(driver, SIGN_IN_WITH_PHONE, By.XPATH)
    eh.check_element_is_present(driver, icons['MAIL_RU'], By.XPATH)
    eh.check_element_is_present(driver, icons['VK'], By.XPATH)
    eh.check_element_is_present(driver, icons['APPLE_ID'], By.XPATH)
    eh.check_element_is_present(driver, icons['MORE'], By.XPATH)

def test_need_help_form_lead(driver: WebDriver):

    header = Header(driver)
    header.sign_in_button.click()
    Base.close_cookies_notification(driver)

    driver.find_element(By.XPATH, NEED_HELP_LINK).click()
    a.switchToNthTab(driver, 2)

    check.is_in("contacts", driver.current_url)
    eh.check_element_is_present(driver, '//span[text()="Напишите нам"]', By.XPATH)
    eh.check_element_is_present(driver, '//button[span[text()="Отправить"]]', By.XPATH)
    eh.check_element_is_present(driver, '//a[span[text()="Закрыть"]]', By.XPATH)

def test_forgot_password(driver: WebDriver):
    header = Header(driver)
    header.sign_in_button.click()
    
    driver.find_element(By.XPATH, DIFFERENT_METHOD).click()
    driver.find_element(By.CSS_SELECTOR, EMAIL_ID_INPUT).send_keys("1")
    driver.find_element(By.XPATH, CONTINUE).click()
    driver.find_element(By.XPATH, FORGOT_PASSWORD).click()
    w.wait_for_text(driver, 30, By.CSS_SELECTOR, AUTH_MODAL, 
        'Восстановление пароля')
    w.wait_for_text(driver, 30, By.CSS_SELECTOR, AUTH_MODAL,
        'Введите email, который вы указали при регистрации')
    eh.check_element_is_present(driver, CONTINUE, By.XPATH)
    eh.check_element_is_present(driver, CREATE_ACCOUNT, By.XPATH)