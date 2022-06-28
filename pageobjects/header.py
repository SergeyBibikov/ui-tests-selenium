from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class Header():

    hamburger = '[data-name="Hamburger"]'

    favsCard = '//a[@data-name="UtilityFavoritesContainer"]/following-sibling::div'
    favsCardHeader = favsCard + '//*[@data-name="FavoritesHeader"]'
    favsCardBody = favsCard + '//*[@data-name="NoFavorites"]'

    nc_root = '//a[@data-name="UtilityNotificationsContainer"]/following-sibling::div'
    notificationsCard = {
        "root": nc_root,
        "header": nc_root + '/div[1]',
        "body": nc_root + '/div[2]',
        "more": {
            "icon": nc_root + '//button[@data-name="ContextMenu"]',
            "list": nc_root + '//ul[contains(@class, "--context-menu--")]'
        }
    }

    main_dropdown = '[data-name="DropdownMainMenu"]'

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.root: WebElement = driver.find_element(
            By.CSS_SELECTOR, 'div[data-name="Header"]')
        self.compare_objects: WebElement = self.root.find_element(
            By.CSS_SELECTOR, '[data-name="UtilityCompareContainer"]')
        self.favourites: WebElement = self.root.find_element(
            By.CSS_SELECTOR, '[data-name="UtilityFavoritesContainer"]')
        self.notifications: WebElement = self.root.find_element(
            By.CSS_SELECTOR, '[data-name="UtilityNotificationsContainer"]')
        self.place_ad_button: WebElement = self.root.find_element(
            By.XPATH, '//a[span[text()="+ Разместить объявление"]]')
        self.sign_in_button: WebElement = self.root.find_element(
            By.XPATH, '//a[span[text()="Войти"]]')

    def close_compare_promo(self):
        """ If not closed, the popup will intercept click events+"""
        popup = self.driver.find_element(
            By.XPATH, '//*[@data-name="CompareOnboarding"]')
        popup.find_element(
            By.XPATH, '//div[contains(@class, "close")]').click()
