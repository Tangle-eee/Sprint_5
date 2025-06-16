import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import *

EMAIL = "test_group_22_at_12345@test.com"
PASSWORD = "999C1m1k223!"

AD_NAME = "Программирование"
AD_DESCRIPTION = "Учебник по Python"
AD_PRICE = "500"

def test_create_ad_authorized_user(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

    # Вход в аккаунт
    driver.find_element(*BUTTON_LOGIN_REGISTRATION).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(INPUT_EMAIL)).send_keys(EMAIL)
    driver.find_element(*INPUT_PASSWORD).send_keys(PASSWORD)
    driver.find_element(*BUTTON_LOGIN).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TEXT_USER_NAME))

    # Нажатие на кнопку "Разместить объявление"
    driver.find_element(*BUTTON_CREATE_AD).click()

    # Заполнение формы объявления
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(AD_TITLE_INPUT_XPATH)).send_keys(AD_NAME)
    driver.find_element(*AD_DESCRIPTION_INPUT_XPATH).send_keys(AD_DESCRIPTION)
    driver.find_element(*AD_PRICE_INPUT_XPATH).send_keys(AD_PRICE)

    driver.find_element(*CATEGORY_DROP_DOWN_XPATH).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(CATEGORY_VALUE_BOOK_XPATH)).click()

    driver.find_element(*SITY_DROP_DOWN_XPATH).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(SITY_VALUE_EKAT_XPATH)).click()

    driver.find_element(*CONDITION_RADIO_BUTTONS_XPATH).click()
    driver.find_element(*PUBLISH_BUTTON_XPATH).click()

    # Переход в профиль
    driver.find_element(*AVATAR_BUTTON).click()

    # Проверка, что объявление отображается
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MY_ADS_DESC_XPATH))
    assert driver.find_element(*MY_AD_XPATH).is_displayed()
