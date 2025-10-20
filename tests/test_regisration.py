from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import Credentials
from locators import *
from helper import generate_registration_data

class TestRegistrationWithNewCredentials:
    def test_sucсess_registration(self, driver):
        email, password, name = generate_registration_data()
        driver.find_element(*Locators.ENTRANCE_BUTTON).click()
        driver.find_element(*Locators.NAME).send_keys(Credentials.name)
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
          # Нажмите кнопку регистрации
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.ENTRANCE_PAGE))
        # Проверьте, что пользователь успешно зарегистрирован
        assert driver.find_element(*Locators.ENTRANCE_PAGE).is_displayed()
   
    # проверка ошибки при некорректном пароле
    def test_incorrect_password_error(self, driver):
        email = generate_registration_data()[0]
        password = "123"  # Пароль меньше шести символов
        name = Credentials()
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        error_message = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.ERROR_MESSAGE))
        # Проверка, что пароль некорректный
        assert error_message.text == "Некорректный пароль"