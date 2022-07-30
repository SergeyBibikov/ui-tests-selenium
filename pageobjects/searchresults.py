from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from helpers.actions import hover

result_card = '//article[@data-name="CardComponent"]'

    
def wait_for_elements(driver, element):
    # No timeout as we know that the element(s)
    # will be present at some point
    els = []
    while (len(els) == 0):
        els = driver.find_elements(By.XPATH, element)
    return els

# TODO: Refactor toggle funcs to take enum to determine action
class SearchResults():

    @staticmethod
    def click_first_result(driver: WebDriver):
        first_card_ad_link = f"{result_card}//a[contains(@href, 'flat')]/span"
        els = wait_for_elements(driver, first_card_ad_link)
        els[0].click()
    
    @staticmethod
    def toggle_first_result_favs(driver: WebDriver):
        els = wait_for_elements(driver, result_card)
        hover(driver, els[0])
        driver.find_element(By.XPATH, f"{result_card}//button[@data-mark='FavoritesControl']").click()

    @staticmethod
    def toggle_first_result_comparison(driver: WebDriver):
        els = wait_for_elements(driver, result_card)
        hover(driver, els[0])
        driver.find_element(By.XPATH, f"{result_card}//button[@data-mark='ComparisonControl']").click()
    
    @staticmethod
    def hide_ad(driver: WebDriver):
        els = wait_for_elements(driver, result_card)
        hover(driver, els[0])
        driver.find_element(By.XPATH, f"{result_card}//button[@data-mark='HideOfferControl']").click()