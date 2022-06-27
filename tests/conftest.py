import platform
from selenium import webdriver
import pytest
import os
import constants

def get_driver():
    options = webdriver.ChromeOptions()
    if os.environ.get("HEADLESS") == "1":
        options.add_argument("--headless")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    d = webdriver.Chrome(options=options)
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
def driver_no_link():
    d = get_driver()
    yield d
    d.close()