from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class SearchResults():

    @staticmethod
    def click_first_result(driver: WebDriver):
        first_card_ad_link = '//article[@data-name="CardComponent"]//a[contains(@href, "flat")]/span'
        els = []
        while (len(els) == 0):
            els = driver.find_elements(By.XPATH, first_card_ad_link)
        els[0].click()
