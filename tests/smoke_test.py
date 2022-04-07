from selenium import webdriver

driver = webdriver.Chrome()

def teardown_function():
    driver.close()

def test_opening():
    driver.get('https://www.cian.ru/')
    assert 'Циан - база недвижимости' in driver.title