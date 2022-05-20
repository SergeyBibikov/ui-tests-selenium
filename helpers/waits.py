from selenium.webdriver.support.ui import WebDriverWait


def wait_for_text(driver, timeout, by, selector, text):
    WebDriverWait(driver, timeout).until(lambda d: text in d.find_element(
        by, selector).text)
