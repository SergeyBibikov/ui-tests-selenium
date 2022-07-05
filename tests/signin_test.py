import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

import pytest_check as check

from pageobjects.header import Header
import helpers.scripts as s
import helpers.elements as eh


def test_phone_field_red_border_on_empty_phone(driver: WebDriver):
    expected_initial_border = '1px solid rgb(206, 209, 215)'
    expected_border_after_validation = '1px solid rgb(255, 31, 52)'
    driver.implicitly_wait(5)
    header = Header(driver)
    header.sign_in_button.click()
    eh.check_element_is_present(driver, 'form')
    border = s.get_element_style_property(driver, 'form div[class*="--input-wrapper"]', 'border')
    check.equal(border, expected_initial_border)
    driver.find_element(By.XPATH, '//form//button[span[text()="Получить код"]]').click()
    time.sleep(1) #Letting the style to change
    border = s.get_element_style_property(driver, 'form div[class*="--input-wrapper"]', 'border')
    check.equal(border, expected_border_after_validation)