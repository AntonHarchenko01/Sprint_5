
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import MainPage, PersonalAccount, Login
from conftest import driver, login
from urls import Urls

class TestStellarBurgersTransitions:
    # Переход в личный кабинет, авторизуемся, переходим в личный кабинет, если есть кнопка выход, тест пройден
    def test_button_personal_account_open_page(self, login, driver):
        driver = login
        driver.find_element(*MainPage.mn_account_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(PersonalAccount.pa_exit_button))
        exit_button = driver.find_element(*PersonalAccount.pa_exit_button)
        assert exit_button.text == 'Выход'

    # Переход из личного кабинета на главную форму через кнопку конструктор, если есть надпись соберите бургер, тест пройден
    def test_click_button_constructor_in_pa_open_main_form(self, login, driver):
        driver = login
        driver.find_element(*MainPage.mn_account_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(PersonalAccount.pa_exit_button))
        driver.find_element(*PersonalAccount.pa_constructor_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPage.mn_assemble_burger))
        assemble_burger = driver.find_element(*MainPage.mn_assemble_burger)
        assert assemble_burger.text == 'Соберите бургер'

    # Переход из личного кабинет на главную форму через кнопку StellarBurger, если есть надпись соберите бургер, тест пройден
    def test_click_button_stellarburger_in_pa_open_main_form(self, login, driver):
        driver = login
        driver.find_element(*MainPage.mn_account_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(PersonalAccount.pa_exit_button))
        driver.find_element(*PersonalAccount.pa_stellarburger_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPage.mn_assemble_burger))
        assemble_burger = driver.find_element(*MainPage.mn_assemble_burger)
        assert assemble_burger.text == 'Соберите бургер'

    # Выход из личного кабинета, если открылась форма входа, тест пройден
    def test_click_button_exit_open_in_pa_login_form(self, login, driver):
        driver = login
        driver.find_element(*MainPage.mn_account_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(PersonalAccount.pa_exit_button))
        driver.find_element(*PersonalAccount.pa_exit_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Login.l_entry))
        assert driver.current_url == Urls.URL_LOGIN