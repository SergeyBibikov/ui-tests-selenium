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
    d.implicitly_wait(20)
    d.set_window_size("1920", "1080")
    d.get('https://www.cian.ru/')
    yield d
    d.close()
