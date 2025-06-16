import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

def test_create_ad_unauthorized(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

    driver.find_element(*BUTTON_CREATE_AD).click()

    # Проверка, что появилось модальное окно с текстом
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MODAL_LOGIN_REQUIRED)
    )
    assert driver.find_element(*MODAL_LOGIN_REQUIRED).is_displayed()
