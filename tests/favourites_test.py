import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

import pytest_check as check

from pageobjects.header import Header
from pageobjects.base import Base
import helpers.scripts as s
import helpers.elements as eh
import helpers.waits as w

def test_popup_when_ad_is_added_to_favs(driver: WebDriver):
    """
    Check that the corresponding popup is seen in the
    search results section
    """
    pass

def test_popup_when_ad_is_unfaved(driver: WebDriver):
    """  
    Checks if the popup  shows
    when the ad is unfaved from the search results.
    """
    pass

def test_popup_on_deletion_from_favs(driver: WebDriver):
    pass

def test_sort_order_criteria(driver: WebDriver):
    """  
    Should have two criferia 
    """
    pass

def test_action_buttons_on_the_ad_in_favs(driver: WebDriver):
    """ 
     Checks that there are buttons allowing
     various actions on an item in favs
      """
    pass

