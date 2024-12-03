
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from constants import Constants
from data import Data
from locators import Registration, Login
from conftest import driver


class TestStellarBurgersRegistration:
    # Тест регистрации, если после успешной регистрации попали на форму входа, тест пройден
    def test_registration_correct_data_successful_reg(self, driver):
        driver.get(Constants.URL_REGISTER)
        driver.find_element(*Registration.r_name).send_keys(Data.user_name)
        driver.find_element(*Registration.r_email).send_keys(Data.email)
        driver.find_element(*Registration.r_psw).send_keys(Data.psw)
        driver.find_element(*Registration.r_reg_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Login.l_entry))
        assert driver.current_url == Constants.URL_LOGIN
    # Тест некорректного пароля, если после ввода некорректного пароля появилась надпись Некорректный пароль, тест пройден
    def test_registration_incorrect_password_unsuccessful_reg(self, driver):
        driver.get(Constants.URL_REGISTER)
        driver.find_element(*Registration.r_name).send_keys(Data.user_name)
        driver.find_element(*Registration.r_email).send_keys(Data.email)
        driver.find_element(*Registration.r_psw).send_keys(Data.inccorect_psw)
        driver.find_element(*Registration.r_reg_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Registration.r_incorrect_psw))
        error_message = driver.find_element(*Registration.r_incorrect_psw)
        assert error_message.text == 'Некорректный пароль'
