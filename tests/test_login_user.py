import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

EMAIL = "test_group_22_at_12345@test.com"
PASSWORD = "999C1m1k223!"

def test_login_valid_user(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

    # Открытие формы логина
    driver.find_element(*BUTTON_LOGIN_REGISTRATION).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(INPUT_EMAIL)).send_keys(EMAIL)
    driver.find_element(*INPUT_PASSWORD).send_keys(PASSWORD)
    driver.find_element(*BUTTON_LOGIN).click()

    # Ждём появления имени пользователя
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TEXT_USER_NAME))

    # Проверяем, что текст совпадает точно
    actual_username = driver.find_element(*TEXT_USER_NAME).text
    assert actual_username == "User.", f"Expected 'User.', but got '{actual_username}'"
