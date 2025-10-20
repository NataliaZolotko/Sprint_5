from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from curl import URL

class TestBulki:
    def test_bulki(self, driver):
    # Открытие главной страницы, где есть кнопка «Личный кабинет»
        driver.get(URL.main_site) 
        driver.find_element(*Locators.PER_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.EMAIL))
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.PAGE_CONSTRUCTOR))
    # проверим, что переходит в раздел "булки"
        driver.find_element(*Locators.BULKI_BUTTON).click()
     # Проверка, что открылся раздел "Булки"
        assert driver.find_element(*Locators.BULKI_PAGE).is_displayed()

