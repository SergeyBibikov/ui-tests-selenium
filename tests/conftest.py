import platform
from selenium import webdriver
import pytest
import os
from constants import Urls
import constants

def get_driver():
    options = webdriver.ChromeOptions()
    if os.environ.get("HEADLESS") == "1":
        options.add_argument("--headless")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    d = webdriver.Chrome(options=options)
    d.implicitly_wait(5)
    pform = platform.system()
    if pform == 'Linux':
        d.set_window_size("1366", "768")
    else:
        d.set_window_size("1920", "1080")
    return d

@pytest.fixture
def driver():
    d = get_driver()
    d.get(constants.urls["MAIN_PAGE"])
    yield d
    d.close()

@pytest.fixture
def driver_rent():
    d = get_driver()
    d.get(constants.urls["ROOM_RENT"])
    yield d
    d.close()

@pytest.fixture
def driver_place_ad():
    d = get_driver()
    d.get(constants.urls["PLACE_AD"])
    yield d
    d.close()

@pytest.fixture
def driver_no_link():
    d = get_driver()
    yield d
    d.close()

@pytest.fixture
def driver_agents_list():
    d = get_driver()
    d.get(Urls.AGENTS_LIST)
    yield d
    d.close()

@pytest.fixture
def driver_buy_flat_results():
    d = get_driver()
    d.get(Urls.BUY_FLAT_RESULTS)
    yield d
    d.close()