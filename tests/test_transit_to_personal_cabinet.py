from constants import Constants
from locators import Locators

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestTransitionToPersonalCabinet:
    def test_transit_to_personal_cabinet(self, driver):
        driver.get(Constants.URL_LOGIN)
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.PERSONAL_ACC_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.PROFILE_BUTTON))

        assert Constants.URL_PERSONAL_CABINET in driver.current_url



