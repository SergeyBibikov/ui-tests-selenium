from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


def hover(driver: WebDriver, element: WebElement):
    ActionChains(driver).move_to_element(element).perform()

def switchToNthTab(driver: WebDriver, tab_count: int):
    """
        Switches to nth-tab, starting with 1.
        To switch to the second tab:
        actions.switchTonNthTab(driver, 2)
    """
    driver.switch_to.window(driver.window_handles[tab_count-1])
