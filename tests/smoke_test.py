from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pageObjects.header import Header

def test_title_content(driver: WebDriver):
    assert 'Циан - база недвижимости' in driver.title

def test_header_links_are_present(driver: WebDriver):
    header = Header(driver)
    els = header.root.find_elements(By.CSS_SELECTOR, 'ul > li')
    assert len(els) == 10