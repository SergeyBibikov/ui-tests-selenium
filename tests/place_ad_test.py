from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

import pytest_check as check

import helpers.elements as eh
import helpers.waits as w

DOCUMENTS_LIST = '//ul[@class="modal-rules__list"][2]'
HOMEOWNER_TOOLTIP = '//homeowner-tooltip//div'
OWNER = '//div[text()="Собственник"]'
PLACEMENT_RULES = '//a[text()="Правила размещения"]'
REPORT_A_PROBLEM_LINK = '//a[text()="Сообщить о проблеме"]'
REPORT_A_PROBLEM_MODAL = '.modal-report-error'
RULES_MODAL = '.cui-modal__dialog'
RULES_LIST = '//ul[@class="modal-rules__list"][1]'
SEND_REPORT_BUTTON = '.modal-report-error__button'

def test_tooltip_on_owner_selection(driver_place_ad: WebDriver):
    d = driver_place_ad
    eh.check_element_is_not_present(d, HOMEOWNER_TOOLTIP, By.XPATH)
    d.find_element(By.XPATH, OWNER).click()
    eh.check_element_is_present(d, HOMEOWNER_TOOLTIP, By.XPATH)

def test_regulatory_documents(driver_place_ad: WebDriver):
    d = driver_place_ad
    d.find_element(By.XPATH, PLACEMENT_RULES).click()

    w.wait_for_text(d, 30, By.CSS_SELECTOR,
        RULES_MODAL, 'Документы, регулирующие размещение объявлений:')
    w.wait_for_text(d, 30, By.XPATH,
        DOCUMENTS_LIST, 'Лицензионное соглашение')
    w.wait_for_text(d, 30, By.XPATH,
        DOCUMENTS_LIST, 'Правила пользования сайтами')
    w.wait_for_text(d, 30, By.XPATH,
        DOCUMENTS_LIST, 'Федеральный Закон о Рекламе')
    w.wait_for_text(d, 30, By.XPATH,
        DOCUMENTS_LIST, 'Программа «Работаем честно»')

def test_rules_modal_should_include_a_warning(driver_place_ad: WebDriver):
    d = driver_place_ad
    d.find_element(By.XPATH, PLACEMENT_RULES).click()

    w.wait_for_text(d, 30, By.CSS_SELECTOR,
        RULES_MODAL, (
            "Объявления, нарушающие данные требования, могут быть отклонены"
            " или удалены без каких-либо компенсаций. При многократных нарушениях "
            "вы получите предупреждение, и ваш аккаунт может быть заблокирован!"))

def test_rules_list(driver_place_ad: WebDriver):
    d = driver_place_ad
    d.find_element(By.XPATH, PLACEMENT_RULES).click()

    w.wait_for_text(d, 30, By.CSS_SELECTOR,
        RULES_MODAL, "Подавая объявление, пожалуйста, убедитесь, что:")
    w.wait_for_text(d, 30, By.XPATH,
        RULES_LIST, 'правильно выбран раздел для размещения')
    w.wait_for_text(d, 30, By.XPATH,
        RULES_LIST, 'указаны точные и действительные параметры объекта')
    w.wait_for_text(d, 30, By.XPATH,
        RULES_LIST, 'объект реально существует и предложение по нему актуально')
    w.wait_for_text(d, 30, By.XPATH,
        RULES_LIST, 'указана реальная цена объекта, в которую включены все обязательные дополнительные платежи')
    w.wait_for_text(d, 30, By.XPATH,
        RULES_LIST, 'цена указана в значении «до торга», т.е. не учтены скидки и возможные личные договорённости')
    w.wait_for_text(d, 30, By.XPATH,
        RULES_LIST, 'указаны верные условия оплаты (предоплата, залог) и точный размер комиссии')
    w.wait_for_text(d, 30, By.XPATH,
        RULES_LIST, 'использованы реальные фотографии объекта, и у вас есть права на их использование')

def test_report_a_problem_popup(driver_place_ad: WebDriver):
    d = driver_place_ad

    d.find_element(By.XPATH, REPORT_A_PROBLEM_LINK).click()

    modal = d.find_element(By.CSS_SELECTOR, REPORT_A_PROBLEM_MODAL)

    text = modal.get_attribute('textContent')

    check.is_in('Сообщить о проблеме', text)
    check.is_in('Кратко опишите, что идет не так', text)
    check.is_in('Мы постараемся', text)
    check.is_in('исправить проблему как можно быстрее', text)
    check.is_in('Ваш email', text)

    eh.check_element_is_present(modal, SEND_REPORT_BUTTON)
