import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from test_data.test_user_data import INVALOD_PASSWORD, INVALID_EMAIL
from test_data.urls import BASE_URL

class TestRegisterUser:

    def test_register_invalid_email_format(self, driver):
        driver.get(BASE_URL)

        # Открытие формы регистрации
        driver.find_element(*BUTTON_LOGIN_REGISTRATION).click()
        driver.find_element(*LINK_NO_ACCOUNT).click()

        # Ввод данных
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(INPUT_EMAIL)
        ).send_keys(INVALID_EMAIL)
        driver.find_element(*INPUT_PASSWORD).send_keys(INVALOD_PASSWORD)
        driver.find_element(*INPUT_REPEAT_PASSWORD).send_keys(INVALOD_PASSWORD)

        driver.find_element(*BUTTON_CREATE_ACCOUNT).click()

        # Проверка наличия ошибки под полем email
        error_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ERROR_MESSAGE_EMAIL)
        )
        assert error_element.is_displayed()
        assert "Ошибка" in error_element.text
