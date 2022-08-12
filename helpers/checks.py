from asyncore import close_all
from gc import collect
import pytest_check as check
import allure


@allure.step('Checking if text is present')
def check_text(textToFind, wholeText):
    check.is_in(textToFind, wholeText)


@allure.step('Checking collection length')
def check_length(collection, expectedLenght):
    check.equal(len(collection), expectedLenght)


@allure.step('Checking two items are not equal')
def check_not_equal(item1, item2):
    check.not_equal(item1, item2)
