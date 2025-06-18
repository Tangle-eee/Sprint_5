import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from test_data.test_user_data import EMAIL, PASSWORD
from test_data.urls import BASE_URL

class TestLogoutUser:

    def test_logout_user(self, driver):
        driver.get(BASE_URL)

        # Вход в систему
        driver.find_element(*BUTTON_LOGIN_REGISTRATION).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(INPUT_EMAIL)
        ).send_keys(EMAIL)
        driver.find_element(*INPUT_PASSWORD).send_keys(PASSWORD)
        driver.find_element(*BUTTON_LOGIN).click()

        # Кликаем по кнопке "Выйти"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(BUTTON_LOGOUT)
        ).click()

        # Проверяем, что снова появилась кнопка "Вход и регистрация"
        login_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(BUTTON_LOGIN_REGISTRATION)
        )
        assert login_button.is_displayed()
