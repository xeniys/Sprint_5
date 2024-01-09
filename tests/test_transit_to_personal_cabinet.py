from constants import UserData
from constants import Urls
from locators import Locators

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestTransitionToPersonalCabinet:
    def test_transit_to_personal_cabinet(self, driver):
        driver.get(Urls.URL_LOGIN)
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(UserData.EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(UserData.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.PERSONAL_ACC_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.PROFILE_BUTTON))

        assert Urls.URL_PERSONAL_CABINET in driver.current_url



