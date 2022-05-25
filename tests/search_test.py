import allure
from selenium.webdriver.chrome.webdriver import WebDriver
import pytest_check as check
from pageobjects.searchblock import SearchBlock


@allure.step
def checkText(textToFind, actualText, msg=""):
    check.is_in(textToFind, actualText, msg)


def test_buy_default_filters(driver: WebDriver):
    """ Estate type and room filters must have default values """
    sb = SearchBlock(driver)
    checkText("Квартиру в новостройке и вторичке", sb.offerType.text)
    checkText("1, 2 комн.", sb.roomCount.text)
