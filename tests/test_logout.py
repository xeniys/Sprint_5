from constants import Urls
from constants import UserData
from locators import Locators

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestLogout:
    def test_logout(self, driver):
        driver.get(Urls.URL_LOGIN)
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(UserData.EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(UserData.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.PERSONAL_ACC_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGOUT_BUTTON))

        driver.find_element(*Locators.LOGOUT_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))

        assert Urls.URL_LOGIN == driver.current_url
        assert driver.find_element(*Locators.LOGIN_BUTTON).text == "Войти"