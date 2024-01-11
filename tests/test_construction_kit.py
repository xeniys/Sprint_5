from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


class TestConstructionKit:
    def test_constructor_buns_transition(self, driver):
        driver.find_element(*Locators.TOPPINGS_BUTTON).click()
        driver.find_element(*Locators.BUNS_BUTTON).click()

        assert "current" in driver.find_element(*Locators.BUNS_BUTTON).get_attribute("class")

    def test_constructor_sauces_transition(self, driver):
        driver.find_element(*Locators.SAUCES_BUTTON).click()

        assert "current" in driver.find_element(*Locators.SAUCES_BUTTON).get_attribute("class")

    def test_constructor_toppings_transition(self, driver):
        driver.find_element(*Locators.TOPPINGS_BUTTON).click()

        assert "current" in driver.find_element(*Locators.TOPPINGS_BUTTON).get_attribute("class")
