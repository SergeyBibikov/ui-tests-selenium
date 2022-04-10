from selenium import webdriver
import pytest


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    d = webdriver.Chrome(options=options)
    d.implicitly_wait(20)
    d.get('https://www.cian.ru/')
    yield d
    d.close()
