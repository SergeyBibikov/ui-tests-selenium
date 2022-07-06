import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

import pytest_check as check

from pageobjects.header import Header
import helpers.scripts as s
import helpers.elements as eh

GET_CODE = '//form//button[span[text()="Получить код"]]'
DIFFERENT_METHOD = '//form//button[span[text()="Другим способом"]]'
SIGN_IN_WITH_PHONE = '//form//button[span[text()="Войти по телефону"]]'
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

    driver.implicitly_wait(5)

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
    driver.implicitly_wait(5)

    header = Header(driver)
    header.sign_in_button.click()
    
    driver.find_element(By.XPATH, DIFFERENT_METHOD).click()

    eh.check_element_is_present(driver, SIGN_IN_WITH_PHONE, By.XPATH)
    eh.check_element_is_present(driver, icons['MAIL_RU'], By.XPATH)
    eh.check_element_is_present(driver, icons['VK'], By.XPATH)
    eh.check_element_is_present(driver, icons['APPLE_ID'], By.XPATH)
    eh.check_element_is_present(driver, icons['MORE'], By.XPATH)