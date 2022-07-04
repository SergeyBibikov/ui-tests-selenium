
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

class Base():
    coookies_notification = '[data-name="CookiesNotification"]'

    @classmethod
    def close_cookies_notification(self, driver: WebDriver):
        elements = driver.find_elements(By.CSS_SELECTOR, self.coookies_notification)
        elements[0].find_element(By.XPATH, '//span[text()="Принять"]').click()
