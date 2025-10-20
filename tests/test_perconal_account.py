from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from curl import URL

class TestPersonalAccount:
    def test_personal_cabinet(self, driver):
    # Открытие главной страницы, где есть кнопка «Личный кабинет»
        driver.get(URL.main_site) 

    # вход в личный кабинет «Личный кабинет»
        driver.find_element(*Locators.PER_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.EMAIL))
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.PAGE_CONSTRUCTOR))
        driver.find_element(*Locators.PER_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.PAGE_PER_CAB))
        # Проверка, что открылась страницы "Личный кабинет"
        assert driver.find_element(*Locators.PAGE_PER_CAB).is_displayed()