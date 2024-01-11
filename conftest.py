import pytest
from selenium import webdriver
from constants import Urls


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(Urls.URL)
    yield driver
    driver.quit()


