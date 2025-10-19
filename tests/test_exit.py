from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from curl import URL
from locators import *
from helper import generate_registration_data

class TetExit:
    def test_exit(self, driver):
    # Открытие главной страницы
        driver.get(URL.main_site) 
    # вход в «Личный кабинет»
        driver.find_element(*Locators.PER_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.EMAIL))
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.PAGE_CONSTRUCTOR))
        driver.find_element(*Locators.PER_ACCOUNT_BUTTON).click()
    # нажали кнопку выход в личном кабинете
        driver.find_element(*Locators.EXIT_BUTTON).click()
    # Проверка, что открылась страница входа
        assert driver.find_element(*Locators.ENTRANCE_PAGE).is_displayed()
