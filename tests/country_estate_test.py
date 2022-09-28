from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

import helpers.elements as eh

from constants import Urls

ADD_VILLAGE_BUTTON = '//button[span[text()="Добавить посёлок"]]'
LAND_SELL_LINK = '//a[text()="Продажа участков"]'
RENT_HOUSE_LINK = '//a[text()="Аренда домов"]'
VILLAGE_LIST_LINK = '//a[text()="в посёлках "]'


def test_housing_community_add_village_button(driver_no_link: WebDriver):
    d = driver_no_link

    d.get(Urls.HOUSING_COMMUNITY)

    eh.check_element_is_present(d, ADD_VILLAGE_BUTTON, By.XPATH)
