
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from constants import Constants
from locators import Registration, Login, MainPage, ForgotPsw
from conftest import driver


class TestStellarBurgersLogin:
    # Тест входа по кнопке войти в аккаунт на главной странице, если после успешной авторизации появилась кнопка оформить заказ на главной форме, тест пройден
    def test_login_sign_in_correct_data_show_order_button(self, driver):
        driver.find_element(*MainPage.mn_login_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Login.l_entry))
        driver.find_element(*Login.l_email).send_keys(Constants.LOGIN_EMAIL)
        driver.find_element(*Login.l_psw).send_keys(Constants.LOGIN_PSW)
        driver.find_element(*Login.l_button_entry).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPage.mn_order_button))
        order_button = driver.find_element(*MainPage.mn_order_button)
        assert order_button.text == 'Оформить заказ'

    # Тест входа через кнопку Личный кабинет на главной странице, если после успешной авторизации появилась кнопка оформить заказ на главной форме, тест пройден
    def test_login_in_personal_account_correct_data_show_order_button(self, driver):
        driver.find_element(*MainPage.mn_account_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Login.l_entry))
        driver.find_element(*Login.l_email).send_keys(Constants.LOGIN_EMAIL)
        driver.find_element(*Login.l_psw).send_keys(Constants.LOGIN_PSW)
        driver.find_element(*Login.l_button_entry).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPage.mn_order_button))
        order_button = driver.find_element(*MainPage.mn_order_button)
        assert order_button.text == 'Оформить заказ'

    # Тест входа через форму регистрации, если после успешной авторизации появилась кнопка оформить заказ на главной форме, тест пройден
    def test_login_in_registration_account_correct_data_show_order_button(self, driver):
        driver.get(Constants.URL_REGISTER)
        driver.find_element(*Registration.r_entry).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Login.l_entry))
        driver.find_element(*Login.l_email).send_keys(Constants.LOGIN_EMAIL)
        driver.find_element(*Login.l_psw).send_keys(Constants.LOGIN_PSW)
        driver.find_element(*Login.l_button_entry).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPage.mn_order_button))
        order_button = driver.find_element(*MainPage.mn_order_button)
        assert order_button.text == 'Оформить заказ'

    # Тест входа через форму восстановления пароля, если после успешной авторизации появилась кнопка оформить заказ на главной форме, тест пройден
    def test_login_in_forgot_password_correct_data_show_order_button(self, driver):
        driver.get(Constants.URL_FORGOT_PSW)
        driver.find_element(*ForgotPsw.fp_login).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Login.l_entry))
        driver.find_element(*Login.l_email).send_keys(Constants.LOGIN_EMAIL)
        driver.find_element(*Login.l_psw).send_keys(Constants.LOGIN_PSW)
        driver.find_element(*Login.l_button_entry).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPage.mn_order_button))
        order_button = driver.find_element(*MainPage.mn_order_button)
        assert order_button.text == 'Оформить заказ'
