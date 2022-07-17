from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from helpers.actions import hover

result_card = '//article[@data-name="CardComponent"]'

class SearchResults():

    @staticmethod
    def click_first_result(driver: WebDriver):
        first_card_ad_link = f"{result_card}//a[contains(@href, 'flat')]/span"
        els = []
        while (len(els) == 0):
            els = driver.find_elements(By.XPATH, first_card_ad_link)
        els[0].click()
    
    @staticmethod
    def toggle_first_result_favs(driver: WebDriver):
        els = []
        while (len(els) == 0):
            els = driver.find_elements(By.XPATH, result_card)
        hover(driver, els[0])
        driver.find_element(By.XPATH, f"{result_card}//button[@data-mark='FavoritesControl']").click()
