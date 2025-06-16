import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

EXISTING_EMAIL = "kazakovTest@ya.ru"
PASSWORD = "CHita8541"

def test_register_existing_user(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

    # Открытие формы регистрации
    driver.find_element(*BUTTON_LOGIN_REGISTRATION).click()
    driver.find_element(*LINK_NO_ACCOUNT).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(INPUT_EMAIL)).send_keys(EXISTING_EMAIL)
    driver.find_element(*INPUT_PASSWORD).send_keys(PASSWORD)
    driver.find_element(*INPUT_REPEAT_PASSWORD).send_keys(PASSWORD)

    driver.find_element(*BUTTON_CREATE_ACCOUNT).click()

    # Проверка появления текста "Ошибка"
    error_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ERROR_MESSAGE_EMAIL))
    assert error_element.is_displayed()
    assert "Ошибка" in error_element.text
