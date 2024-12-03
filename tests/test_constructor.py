from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import MainPage
from conftest import driver, login



# Проверял через time.sleep что прокрутка осуществляется, но т.к. сказали их не оставлять убрал
class TestStellarBurgerConstructorForm:
    # Тест на переход к начинкам на главной форме, если переход произошел, тест пройден

    def test_constructor_go_to_fillings_scroll_to_fillings(self, login, driver):
        driver = login
        driver.find_element(*MainPage.mn_fillings_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPage.mn_fillings_text))
        fillings = driver.find_element(*MainPage.mn_fillings_text)
        driver.execute_script("arguments[0].scrollIntoView();", fillings)
        assert fillings.text == 'Начинки'

    # Тест на переход к соусам на главной форме, если переход произошел, тест пройден
    def test_constructor_go_to_sauces_scroll_to_fillings(self, login, driver):
        driver = login
        driver.find_element(*MainPage.mn_sauces_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPage.mn_sauces_text))
        sauces = driver.find_element(*MainPage.mn_sauces_text)
        driver.execute_script("arguments[0].scrollIntoView();", sauces)
        assert sauces.text == 'Соусы'

    # Тест на переход к булкам на главной форме, если переход произошел, тест пройден
    def test_constructor_go_to_buns_scroll_to_buns(self, login, driver):
        driver = login
        driver.find_element(*MainPage.mn_fillings_button).click()                       #Сначала перейдем на вкладку начинки
        driver.find_element(*MainPage.mn_buns_buttons).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPage.mn_buns_text))
        buns = driver.find_element(*MainPage.mn_buns_text)
        driver.execute_script("arguments[0].scrollIntoView();", buns)
        assert buns.text == 'Булки'