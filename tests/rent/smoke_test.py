from operator import gt
import time

import pytest_check as check

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from pageobjects.searchblock import SearchBlock
import helpers.elements as eh
import constants

def test_recommend_block_categories(driver: WebDriver):
    driver.get(constants.urls["ROOM_RENT"])
    
    text = driver.find_element(By.CSS_SELECTOR, '[data-name="QuickLinksList"]').get_attribute('textContent')

    check.is_in('без посредников', text)
    check.is_in('холодильник', text)
    check.is_in('с мебелью', text)
    check.is_in('стиральная машина', text)
    check.is_in('изолированные комнаты', text)
    check.is_in('на длительный срок', text)
    check.is_in('не под реновацию', text)
    check.is_in('рядом с метро', text)