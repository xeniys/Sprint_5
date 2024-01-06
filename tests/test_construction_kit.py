from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators



class TestConstructionKit:
    def test_constructor_buns_transition(self, driver):
        driver.find_element(*Locators.TOPPINGS_BUTTON).click()
        driver.find_element(*Locators.BUNS_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BUNS_H2))

        assert driver.find_element(*Locators.BUNS_H2).is_displayed()
        assert driver.find_element(*Locators.BUN).is_displayed()

    def test_constructor_sauces_transition(self, driver):
        driver.find_element(*Locators.TOPPINGS_BUTTON).click()
        driver.find_element(*Locators.SAUCES_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.SAUCES_H2))

        assert driver.find_element(*Locators.SAUCES_H2).is_displayed()
        assert driver.find_element(*Locators.SAUCE).is_displayed()

    def test_constructor_toppings_transition(self, driver):
        driver.find_element(*Locators.TOPPINGS_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.TOPPING))

        assert driver.find_element(*Locators.TOPPINGS_H2).is_displayed()
        assert driver.find_element(*Locators.TOPPING).is_displayed()
