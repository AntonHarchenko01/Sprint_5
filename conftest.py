import pytest
from selenium import webdriver
from constants import Constants
from locators import Login, MainPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import Data

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(Constants.URL_MAIN_PAGE)
    yield driver
    driver.quit()

# Фикстура для входа в аккаунт
@pytest.fixture
def login(driver):
    driver.get(Constants.URL_LOGIN)
    driver.find_element(*Login.l_email).send_keys(Data.LOGIN_EMAIL)
    driver.find_element(*Login.l_psw).send_keys(Data.LOGIN_PSW)
    driver.find_element(*Login.l_button_entry).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPage.mn_order_button))
    return driver