from selenium.webdriver.common.by import By

# Локаторы для формы регистрация
class Registration:
    r_name = (By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]")  # Имя на форме регистрация
    r_email = (By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]")  # Email на форме регистрация
    r_psw = (By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/input[1]")    # Пароль на форме регистрация
    r_reg_button = (By.XPATH, ".//button[text()='Зарегистрироваться']")     # Кнопка зарегистрироваться на форме регистрация
    r_incorrect_psw = (By.XPATH, "//p[contains(@class,'input__error')]")    # Надпись Некорректный пароль
    r_entry = (By.XPATH, "//a[contains(text(),'Войти')]")                   # Кнопка войти на форме регистрации

# Локаторы для формы Входа
class Login:
    l_entry = (By.XPATH, "//h2[contains(text(),'Вход')]")   # Надпись Вход
    l_email = (By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]")  # Email на форме Входа
    l_psw = (By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]")    # Пароль на форме Входа
    l_button_entry = (By.XPATH, "//button[contains(text(),'Войти')]")   # Кнопка Войти на форме Входа


# Локаторы для главной формы
class MainPage:
    mn_login_button = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")    # Кнопка Войти в аккаунт на главной форме
    mn_order_button = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")     # Кнопка оформить заказ на главной форме
    mn_account_button = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")        # Кнопка личный кабинет на главной форме
    mn_assemble_burger = (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")     # Надпись соберите бургер на главной форме
    mn_fillings_button = (By.XPATH, ".//span[contains(text(),'Начинки')]")           # Кнопка начинки на главной форме
    mn_fillings_text = (By.XPATH, "//h2[contains(text(),'Начинки')]")               # Надпись начинки в разделе соберите бургер на главной форме
    mn_sauces_button = (By.XPATH, "//span[contains(text(),'Соусы')]")               # Кнопка соусы на главной форме
    mn_sauces_text = (By.XPATH, "//h2[contains(text(),'Соусы')]")                   # Надпись соусы в разделе соберите бургер на главной форме
    mn_buns_buttons = (By.XPATH, "//span[contains(text(),'Булки')]")                # Кнопка булки на главной форме
    mn_buns_text = (By.XPATH, "//h2[contains(text(),'Булки')]")                     # Надпись булки в разделе соберите бургер на главной форме

# Локаторы для формы восстановления пароля
class ForgotPsw:
    fp_login = (By.XPATH, " //a[contains(text(),'Войти')]")     # Кнопка войти на форме восстановления пароля

# Локаторы личного кабинета
class PersonalAccount:
    pa_exit_button = (By.XPATH, "//button[contains(text(),'Выход')]")               # Кнопка выход, на форме личного кабинета
    pa_constructor_button = (By.XPATH, "//p[contains(text(),'Конструктор')]")       # Кнопка конструктор, на форме личного кабинета
    pa_stellarburger_button = (By.XPATH, "//header/nav[1]/div[1]/a[1]/*[1]")        # Кнопка stellarburger, на форме личного кабинета







