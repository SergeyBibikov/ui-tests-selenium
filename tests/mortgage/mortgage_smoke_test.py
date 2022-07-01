from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

import helpers.elements as eh
import helpers.waits as w
import constants


def test_survey_for_new_users(driver_no_link: WebDriver):
    d = driver_no_link

    d.get(constants.urls["MORTGAGE_MAIN"])

    w.wait_for_text(d, 30, By.CSS_SELECTOR, 'body', "Ответьте на несколько вопросов")
    eh.check_element_is_present(d, '//button[text()="Ок, я готов"]', By.XPATH)
    eh.check_element_is_present(d, '//button[text()="Я уже заполнял анкету"]', By.XPATH)

def test_survey_already_taken(driver_no_link: WebDriver):
    d = driver_no_link

    d.get(constants.urls["MORTGAGE_MAIN"])
    d.find_element(By.XPATH, '//button[text()="Я уже заполнял анкету"]').click()
    w.wait_for_text(d, 30, By.CSS_SELECTOR, 'body', 'Льготная ипотека от 6 банков')
    w.wait_for_text(d, 30, By.CSS_SELECTOR, 'body', 'Укажите номер телефона, чтобы продолжить')

def test_mortgage_with_state_support(driver_no_link: WebDriver):
    d = driver_no_link

    d.get(constants.urls["MORTGAGE"])
    eh.check_element_is_present(d, '//a[text()="Узнать свои ставки"]', By.XPATH);
    w.wait_for_text(d, 30, By.CSS_SELECTOR, 'body', 'Ипотека с')
    w.wait_for_text(d, 30, By.CSS_SELECTOR, 'body', 'господдержкой — все')
    w.wait_for_text(d, 30, By.CSS_SELECTOR, 'body', 'программы')
    w.wait_for_text(d, 30, By.CSS_SELECTOR, 'body', 'Какие есть программы господдержки')
    w.wait_for_text(d, 30, By.CSS_SELECTOR, 'body', 'С какими банками мы работаем')

def test_mortgage_calculator(driver_no_link: WebDriver):
    d = driver_no_link

    d.get(constants.urls["MORTGAGE_CALCULATOR"])
    eh.check_element_is_present(d, '//span[text()="Подать заявку онлайн"]', By.XPATH);
    eh.check_element_is_present(d, '//span[text()="Рассчитать досрочное погашение"]', By.XPATH);
    w.wait_for_text(d, 30, By.CSS_SELECTOR, 'body', 'Ипотечный калькулятор')
    w.wait_for_text(d, 30, By.CSS_SELECTOR, 'body', 'Персональные ставки от крупных банков')
    w.wait_for_text(d, 30, By.CSS_SELECTOR, 'body', 'Такие же условия и ставки, как при обращении в банки напрямую')
    w.wait_for_text(d, 30, By.CSS_SELECTOR, 'body', 'Предложения по ипотеке бесплатно за 10 минут')