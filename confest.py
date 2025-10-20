import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from locators import Locators
from curl import *
from data import Credentials

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.education-services.ru/')
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    # фикстура для авторизации пользователя
    driver.find_element(*Locators.NAME).send_keys(Credentials.name)
    driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
    driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
    driver.find_element(*Locators.REGISTER_BUTTON).click()
    return driver
