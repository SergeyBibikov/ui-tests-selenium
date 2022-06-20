import platform
from selenium import webdriver
import pytest
import os


@pytest.fixture
def driver():
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
    d.get('https://www.cian.ru/')
    yield d
    d.close()
