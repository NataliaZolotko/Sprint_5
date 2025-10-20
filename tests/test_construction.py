from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from curl import URL
from locators import *
from helper import generate_registration_data

class TestConstruction:
    def test_passer_by_constructor(self, driver):
    # Открытие главной страницы
        driver.get(URL.main_site) 
    # Нахождение и нажатие кнопки «Личный кабинет»
        driver.find_element(*Locators.PER_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.EMAIL))
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.PERSONAL_PAGE))
    # переход по клику на «Конструктор» 
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
    # Проверка, что открылась страница конструктора
        assert driver.find_element(*Locators.PAGE_CONSTRUCTOR).is_displayed()

