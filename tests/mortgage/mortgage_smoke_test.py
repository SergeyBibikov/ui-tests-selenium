from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

import helpers.elements as eh
import helpers.waits as w
import constants


def test_survey_for_new_users(driver_no_link: WebDriver):
    d = driver_no_link

    d.get(constants.urls["MORTGAGE"])

    w.wait_for_text(d, 30, By.CSS_SELECTOR, 'body', "Ответьте на несколько вопросов")
    eh.check_element_is_present(d, '//button[text()="Ок, я готов"]', By.XPATH)
    eh.check_element_is_present(d, '//button[text()="Я уже заполнял анкету"]', By.XPATH)

def test_survey_already_taken(driver_no_link: WebDriver):
    d = driver_no_link

    d.get(constants.urls["MORTGAGE"])
    d.find_element(By.XPATH, '//button[text()="Я уже заполнял анкету"]').click()
    w.wait_for_text(d, 30, By.CSS_SELECTOR, 'body', 'Льготная ипотека от 6 банков')
    w.wait_for_text(d, 30, By.CSS_SELECTOR, 'body', 'Укажите номер телефона, чтобы продолжить')