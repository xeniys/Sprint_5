from constants import Constants
from locators import Locators

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestLogin:
    def test_authorization_from_main_page(self, driver):
        driver.find_element(*Locators.MAIN_AUTH_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))

        assert driver.find_element(*Locators.ORDER_BUTTON).text == "Оформить заказ"

    def test_authorization_from_header(self, driver):
        driver.find_element(*Locators.PERSONAL_ACC_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))

        assert driver.find_element(*Locators.ORDER_BUTTON).text == "Оформить заказ"

    def test_authorization_from_registration_form(self, driver):
        driver.find_element(*Locators.PERSONAL_ACC_BUTTON).click()
        driver.find_element(*Locators.REG_LINK).click()
        driver.find_element(*Locators.LOGIN_LINK).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))

        assert driver.find_element(*Locators.ORDER_BUTTON).text == "Оформить заказ"

    def test_authorization_from_reset_password_form(self, driver):
        driver.find_element(*Locators.PERSONAL_ACC_BUTTON).click()
        driver.find_element(*Locators.RESET_PASSWORD_LINK).click()
        driver.find_element(*Locators.RESET_LOGIN_LINK).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))

        assert driver.find_element(*Locators.ORDER_BUTTON).text == "Оформить заказ"



