import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

EMAIL = "test_group_22_at_12345@test.com"
PASSWORD = "999C1m1k223!"

def test_logout_user(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

    # Вход в систему
    driver.find_element(*BUTTON_LOGIN_REGISTRATION).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(INPUT_EMAIL)).send_keys(EMAIL)
    driver.find_element(*INPUT_PASSWORD).send_keys(PASSWORD)
    driver.find_element(*BUTTON_LOGIN).click()

    # Кликаем по кнопке "Выйти"
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_LOGOUT)).click()

    # Проверяем, что снова появилась кнопка "Вход и регистрация"
    login_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(BUTTON_LOGIN_REGISTRATION))
    assert login_button.is_displayed()
