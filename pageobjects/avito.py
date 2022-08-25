from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Locators():
    RADIUS_LIST_ITEMS = '[data-marker="popup-location/radius-list"]>div'
    SHOW_ADS_BUTTON = '[data-marker="popup-location/save-button"]'
    CHANGE_BUTTON = '//button[span[text()="Изменить"]]'
    MORE_OPTION = '//span[text()="ещё"]'
    MORE_POPUP = '[data-marker="more-popup"]'
    PAGE_TITLE = '[data-marker="page-title"]'
    SEARCH_BAR = '[data-marker="search-form/suggest"]'
    SEARCH_BUTTON = '[data-marker="search-form/submit-button"]'
    SEARCH_PARAMETERS = 'div[class*="filters-subscription-additions"]'
    SEARCH_KINDS_LIST = 'div[class*="top-rubricator-root"]'
    SEARCH_RADIUS = '[data-marker="search-form/radius"]'
    SERVICES_LIST = '//h3[text()="Сервисы и услуги Авито"]/..'
    SUGGESTION_LIST = 'ul[data-marker="suggest/list"]'
    YOUR_CITY_CONFIRMATION_POPUP = '//div[contains(., "Это ваш город?") and contains(@class, "tooltip-tooltip")]'
    YES_BUTTON = '//button[span[text()="Да"]]'


def confirm_location(d: WebDriver):
    d.execute_script('window.stop();')
    d.find_element(
        By.XPATH, Locators.YOUR_CITY_CONFIRMATION_POPUP + Locators.YES_BUTTON
    ).click()
