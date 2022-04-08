from selenium import webdriver
import pytest

@pytest.fixture
def driver():
    d = webdriver.Chrome()
    yield d
    d.close()

def test_opening(driver):
    driver.get('https://www.cian.ru/')
    assert 'Циан - база недвижимости' in driver.title