from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Locators():
    CHANGE_BUTTON = '//button[span[text()="Изменить"]]'
    SEARCH_KINDS_LIST = 'div[class*="top-rubricator-root"]'
    SERVICES_LIST = '//h3[text()="Сервисы и услуги Авито"]/..'
    YOUR_CITY_CONFIRMATION_POPUP = '//div[contains(., "Это ваш город?") and contains(@class, "tooltip-tooltip")]'
    YES_BUTTON = '//button[span[text()="Да"]]'


def confirm_location(d: WebDriver):
    d.execute_script('window.stop();')
    d.find_element(
        By.XPATH, Locators.YOUR_CITY_CONFIRMATION_POPUP + Locators.YES_BUTTON
    ).click()
