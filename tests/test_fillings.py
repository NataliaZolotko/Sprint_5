from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from curl import URL

class TestFillings:
    def test_fillings(self, driver):
    # Открытие главной страницы, где есть кнопка «Личный кабинет»
        driver.get(URL.main_site) 
        driver.find_element(*Locators.PER_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.EMAIL))
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.PAGE_CONSTRUCTOR))
    # проверим, что переходит в раздел "начинки"
        driver.find_element(*Locators.FILLINGS_BUTTON).click()
     # Проверка, что открылся раздел "начинки"
        assert driver.find_element(*Locators.FILLINGS_PAGE).is_displayed()