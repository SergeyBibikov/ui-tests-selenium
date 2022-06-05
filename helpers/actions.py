from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


def hover(driver: WebDriver, element: WebElement):
    ActionChains(driver).move_to_element(element).perform()
