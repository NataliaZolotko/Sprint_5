from selenium.webdriver.common.by import By

class Locators:
    # локаторы для регистрации
    REGISTER_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'password')
    REG_BUTTON = (By.XPATH, "//a[@class='Auth_link__1fOlj']")
    ENTRANCE_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    PER_ACCOUNT_BUTTON = (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2']")
    NAME = (By.ID, 'name')
    ERROR_MESSAGE = (By.XPATH, "//p[@class='input__error text_type_main-default']")
    ENTRANCE_PAGE = (By.XPATH,"//div[@class='Auth_login__3hAey']")
    PERSONAL_PAGE = (By.XPATH, "//@div[@class='Modal_modal_overlay__x2ZCr']")
    ENT_BUTTON = (By.LINK_TEXT, "Войти")
    RECOVER_PASSWORD_BUTTON = (By.LINK_TEXT, "Восстановить пароль")
    CONSTRUCTOR_BUTTON = (By.LINK_TEXT, "Конструктор")
    PAGE_CONSTRUCTOR = (By.XPATH, "//main[@class='App_componentContainer__2JC2W']")
    LOGO = (XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")
    PAGE_PER_CAB = (By.XPATH, "//div[@class='Account_account__vgk_w']")
    EXIT_BUTTON = (By.LINK_TEXT, "Выход")
    BULKI_BUTTON = (By.XPATH, "//span[contains(text(), 'Булки')]")
    SAUSES_BUTTON = (By.XPATH, "//span[contains(text(), 'Соусы')]")
    FILLINGS_BUTTON = (By.XPATH, "//span[contains(text(), 'Начинки')]")
    BULKI_PAGE = (By.XPATH, "//p[contains(text(), 'Флюоресцентная булка R2-D3')]")
    SAUSES_PAGE = (By.XPATH, "//p[contains(text(), 'Соус Spicy-X')]")
    FILLINGS_PAGE = (By.XPATH, "//p[contains(text(), 'Говяжий метеорит (отбивная)')]")

