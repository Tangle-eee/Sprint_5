from selenium.webdriver.common.by import By

# Главная страница
BUTTON_LOGIN_REGISTRATION = (By.XPATH, "//button[text()='Вход и регистрация']")
BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выйти']")
TEXT_USER_NAME = (By.XPATH, "//h3[normalize-space(text())='User.']")
AVATAR_BUTTON = (By.XPATH, "//button[.//svg]")

# Модальное окно логина/регистрации
LINK_NO_ACCOUNT = (By.XPATH, "//button[text()='Нет аккаунта']")
INPUT_EMAIL = (By.NAME, "email")
INPUT_PASSWORD = (By.NAME, "password")
INPUT_REPEAT_PASSWORD = (By.XPATH, "//input[@placeholder='Повторите пароль']")
BUTTON_CREATE_ACCOUNT = (By.XPATH, "//button[text()='Создать аккаунт']")
BUTTON_LOGIN = (By.XPATH, "//button[text()='Войти']")
ERROR_MESSAGE_EMAIL = (By.XPATH, "//form//div[2]/div[1]/span[text()='Ошибка']")

# Создание объявления
MODAL_LOGIN_REQUIRED = (By.XPATH, "//h1[text()='Чтобы разместить объявление, авторизуйтесь']")
BUTTON_CREATE_AD = (By.XPATH, "//button[text()='Разместить объявление']")
AD_TITLE_INPUT_XPATH = (By.XPATH, "//input[@placeholder='Название']")
AD_DESCRIPTION_INPUT_XPATH = (By.XPATH, "//textarea[@placeholder='Описание товара']")
AD_PRICE_INPUT_XPATH = (By.XPATH, "//input[@placeholder='Стоимость']")
CATEGORY_DROP_DOWN_XPATH = (By.XPATH, "//button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP']")
CATEGORY_VALUE_BOOK_XPATH = (By.XPATH, "//span[contains(text(), 'Книги')]") 
SITY_DROP_DOWN_XPATH = (By.XPATH, "//input[@name='city']//following-sibling::button")
SITY_VALUE_EKAT_XPATH = (By.XPATH, "//span[contains(text(), 'Екатеринбург')]") 
CONDITION_RADIO_BUTTONS_XPATH = (By.XPATH,"//div[@class='radioUnput_inputRegular__FbVbr']")
PUBLISH_BUTTON_XPATH = (By.XPATH,"//button[text()='Опубликовать']")
MY_ADS_DESC_XPATH = (By.XPATH, "//div[contains(@class, 'description')]")
MY_AD_XPATH = (By.XPATH, ".//div[@class='about']/h2")

