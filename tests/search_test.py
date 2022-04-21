import allure
from selenium.webdriver.chrome.webdriver import WebDriver
import pytest_check as check
from pageobjects.searchBlock import SearchBlock


@allure.step
def checkText(textToFind, text, msg=""):
    check.is_in(textToFind, text, msg)


def test_buy_default_filters(driver: WebDriver):
    """ Estate type and room filters must have default values """
    sb = SearchBlock(driver)
    checkText("Квартиру в новостройке и вторичке", sb.offerType.text)
    checkText("1, 2 комн.", sb.roomCount.text)
