import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from test_data.test_user_data import RAMDOM_EMAIL, RANDOM_PASSWORD
from test_data.urls import BASE_URL

class TestRegisterUser:

    def test_register_valid(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*BUTTON_LOGIN_REGISTRATION).click()
        driver.find_element(*LINK_NO_ACCOUNT).click()

        # Ввод данных
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(INPUT_EMAIL)
        ).send_keys(RAMDOM_EMAIL)
        driver.find_element(*INPUT_PASSWORD).send_keys(RANDOM_PASSWORD)
        driver.find_element(*INPUT_REPEAT_PASSWORD).send_keys(RANDOM_PASSWORD)
        driver.find_element(*BUTTON_CREATE_ACCOUNT).click()

        # Ждём появления имени пользователя
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TEXT_USER_NAME)
        )

        # Проверяем, что текст совпадает точно
        actual_username = driver.find_element(*TEXT_USER_NAME).text
        assert actual_username == "User.", f"Expected 'User.', but got '{actual_username}'"
