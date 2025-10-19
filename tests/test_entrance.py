from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import Credentials
from locators import *
from helper import generate_registration_data

class TestEntrance:
    def test_login_from_main_page(self, driver):
        # Открытие главной страницы
        driver.get(URL.main_site) 
       # вход по кнопки войти в аккаунт
        driver.find_element(*Locators.ENTRANCE_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.EMAIL))
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        assert driver.find_element(*Locators.PERSONAL_PAGE).is_displayed()
       
    # вход через личный кабинет
    def test_login_from_perconal_account(self, driver):
         # Открытие главной страницы
        driver.get(URL.main_site) 
        #вход через личный кабинет
        driver.find_element(*Locators.PER_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.EMAIL))
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        assert driver.find_element(*Locators.PERSONAL_PAGE).is_displayed()
    
     # вход через регистрацию
    def test_login_from_registration(self, driver):
         # Открытие главной страницы
        driver.get(URL.main_site) 
        # вход через регистрацию
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.ENT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.EMAIL))
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        assert driver.find_element(*Locators.PERSONAL_PAGE).is_displayed()

    # вход через кнопку восстановления пароля
    def test_login_from_recovery_password(self, driver):
         # Открытие главной страницы
        driver.get(URL.main_site) 
        # вход через восстановление пароля
        driver.find_element(*Locators.RECOVER_PASSWORD_BUTTON).click()
        driver.find_element(*Locators.ENT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.EMAIL))
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        assert driver.find_element(*Locators.PERSONAL_PAGE).is_displayed()
