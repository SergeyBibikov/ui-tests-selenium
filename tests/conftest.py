import platform
from selenium import webdriver
import pytest
import os
from constants import Urls


def get_driver():
    isHeadless = os.environ.get("HEADLESS")
    isLaptop = os.environ.get("LAPTOP")

    options = webdriver.ChromeOptions()
    if isHeadless == "1":
        options.add_argument("--headless")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    d = webdriver.Chrome(options=options)
    d.implicitly_wait(10)
    pform = platform.system()
    if isLaptop:
        d.set_window_size("1366", "768")
    else:
        d.set_window_size("1920", "1080")
    return d


@pytest.fixture
def avito():
    d = get_driver()
    d.get('https://www.avito.ru/')
    yield d
    d.close()


@pytest.fixture
def driver():
    d = get_driver()
    d.get(Urls.MAIN_PAGE)
    yield d
    d.close()


@pytest.fixture
def driver_rent():
    d = get_driver()
    d.get(Urls.ROOM_RENT)
    yield d
    d.close()


@pytest.fixture
def driver_place_ad():
    d = get_driver()
    d.get(Urls.PLACE_AD)
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
