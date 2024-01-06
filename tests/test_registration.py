import data
from constants import Constants
from locators import Locators

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestRegistration:
    def test_successful_registration(self, driver):
        driver.get(Constants.URL_REGISTRATION)

        driver.find_element(*Locators.REG_NAME_INPUT).send_keys(Constants.REGISTRATION_NAME)
        driver.find_element(*Locators.REG_EMAIL_INPUT).send_keys(data.email_gen())
        driver.find_element(*Locators.REG_PASSWORD_INPUT).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.REG_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))

        assert Constants.URL_LOGIN == driver.current_url

    def test_registration_wrong_password(self, driver):
        driver.get(Constants.URL_REGISTRATION)

        driver.find_element(*Locators.REG_NAME_INPUT).send_keys(Constants.REGISTRATION_NAME)
        driver.find_element(*Locators.REG_EMAIL_INPUT).send_keys(data.email_gen())
        driver.find_element(*Locators.REG_PASSWORD_INPUT).send_keys('aaa')
        driver.find_element(*Locators.REG_BUTTON).click()

        assert driver.find_element(*Locators.WRONG_PASSWORD_ERROR).text == 'Некорректный пароль'

