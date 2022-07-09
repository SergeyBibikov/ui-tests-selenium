import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

import pytest_check as check

from pageobjects.header import Header
from pageobjects.base import Base
import helpers.scripts as s
import helpers.elements as eh
import helpers.waits as w

OWNER = '//div[text()="Собственник"]'
HOMEOWNER_TOOLTIP = '//homeowner-tooltip//div'

def test_tooltip_on_owner_selection(driver_place_ad: WebDriver):
    d = driver_place_ad
    eh.check_element_is_not_present(d, HOMEOWNER_TOOLTIP, By.XPATH)
    d.find_element(By.XPATH, OWNER).click()
    eh.check_element_is_present(d, HOMEOWNER_TOOLTIP, By.XPATH)