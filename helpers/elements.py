import pytest_check as check
import allure
from selenium.webdriver.common.by import By


@allure.step
def check_element_is_present(driver, locator, by=By.CSS_SELECTOR):
    elements = driver.find_elements(by, locator)
    check.greater(len(elements), 0)


@allure.step
def check_element_is_not_present(driverOrElement, locator, by=By.CSS_SELECTOR):
    elements = driverOrElement.find_elements(by, locator)
    check.equal(len(elements), 0)
