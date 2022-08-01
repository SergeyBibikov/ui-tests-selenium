import enum
import string

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

def _hover_on_first_result(driver):
    els = wait_for_elements(driver, result_card)
    hover(driver, els[0])

# TODO: Refactor toggle funcs to take enum to determine action
class SearchResults():

    @staticmethod
    def click_first_result(driver: WebDriver):
        first_card_ad_link = f"{result_card}//a[contains(@href, 'flat')]/span"
        els = wait_for_elements(driver, first_card_ad_link)
        els[0].click()

    @staticmethod
    def toggle_first_result_icon(driver: WebDriver, icon: str):
        _hover_on_first_result(driver)
        driver.find_element(By.XPATH, f"{result_card}//button[@data-mark='{icon}']").click()

    @staticmethod
    def hover_on_first_result(driver: WebDriver):
        _hover_on_first_result(driver)

    @staticmethod
    def contact_ad_author(driver: WebDriver):
        driver.find_element(By.XPATH, f"{result_card}//button[@data-name='ChatButtonContainer']").click()


class CardIcons():
    DOWNLOAD_PDF = '//a[@data-mark="DownloadPDFControl"]'
    FAVOURITES = 'FavoritesControl'
    COMPARE = 'ComparisonControl'
    HIDE = 'HideOfferControl'
    REPORT = 'ComplainControl'
    SHOW_ON_MAP = 'ShowOfferOnMapControl'