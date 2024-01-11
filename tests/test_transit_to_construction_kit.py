from constants import Urls
from constants import UserData
from locators import Locators

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestTransitionToConstructionKit:
    def test_transit_from_personal_cabinet_to_constructor(self, driver):
        driver.get(Urls.URL_LOGIN)
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(UserData.EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(UserData.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.PERSONAL_ACC_BUTTON).click()
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))

        assert Urls.URL == driver.current_url

    def test_transit_from_personal_cabinet_to_constructor_via_logo(self, driver):
        driver.get(Urls.URL_LOGIN)
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(UserData.EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(UserData.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.PERSONAL_ACC_BUTTON).click()
        driver.find_element(*Locators.LOGO_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))

        assert Urls.URL == driver.current_url
