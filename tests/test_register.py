import time
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

def test_register_valid(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    driver.find_element(*BUTTON_LOGIN_REGISTRATION).click()
    driver.find_element(*LINK_NO_ACCOUNT).click()

    email = f"test{random.randint(1000, 9999)}@ya.ru"
    password = "CHita8541"

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(INPUT_EMAIL)).send_keys(email)
    driver.find_element(*INPUT_PASSWORD).send_keys(password)
    driver.find_element(*INPUT_REPEAT_PASSWORD).send_keys(password)
    driver.find_element(*BUTTON_CREATE_ACCOUNT).click()

    # Ждём появления имени пользователя
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TEXT_USER_NAME))

    # Проверяем, что текст совпадает точно
    actual_username = driver.find_element(*TEXT_USER_NAME).text
    assert actual_username == "User.", f"Expected 'User.', but got '{actual_username}'"



