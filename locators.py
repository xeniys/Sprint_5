from selenium.webdriver.common.by import By


class Locators:
    REG_NAME_INPUT = (By.XPATH, './/input[@name = "name"]')  # поле ввода имени на странице регистрации
    REG_EMAIL_INPUT = (By.XPATH, './/fieldset[2]/div/div/input[@name = "name"]')  # поле ввода email на странице
    # регистрации
    REG_PASSWORD_INPUT = (By.XPATH, './/input[@name = "Пароль"]')  # поле ввода пароля на странице регистрации
    REG_BUTTON = (By.XPATH, './/button[text() = "Зарегистрироваться"]')  # кнопка "Зарегистрироваться" на странице
    # регистрации
    WRONG_PASSWORD_ERROR = (By.XPATH, './/p[@class="input__error text_type_main-default"]')  # ошибка при вводе
    # некорректного пароля на странице регистрации

    MAIN_AUTH_BUTTON = (By.XPATH, './/button[text()="Войти в аккаунт"]')  # кнопка "Войти в аккаунт" на главной странице
    PERSONAL_ACC_BUTTON = (By.XPATH, './/p[text()="Личный Кабинет"]')  # кнопка "Личный кабинет" в хедере
    LOGIN_EMAIL = (By.XPATH, './/input[@name = "name"]')  # поле ввода emaila на странице авторизации
    LOGIN_PASSWORD = (By.XPATH, './/input[@name = "Пароль"]') # поле ввода пароля на странице авторизации
    LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти"]')  # кнопка "войти" на странице авторизации
    ORDER_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]') # кнопка "Оформить заказ" на главной странице (
    # авторизованная зона)

    REG_LINK = (By.XPATH, './/a[text() = "Зарегистрироваться"]')  # ссылка "Зарегистрироваться" на странице
    # авторизации
    LOGIN_LINK = (By.XPATH, './/a[text()="Войти"]')  # ссылка "войти" на странице регистрации
    RESET_PASSWORD_LINK = (By.XPATH, './/a[text()="Восстановить пароль"]') # ссылка "Восстановить пароль" на странице
    # авторизации
    RESET_LOGIN_LINK = (By.XPATH, './/a[@class="Auth_link__1fOlj"]') # ссылка "Войти" на странице сброса пароля

    PROFILE_BUTTON = (By.XPATH, './/a[text()="Профиль"]') # кнопка "Профиль" в личном кабинете
    CONSTRUCTOR_BUTTON = (By.XPATH, './/p[text()="Конструктор"]') #к нопка "Конструктор" в хедере
    LOGO_BUTTON = (By.XPATH, './/a[@href="/"]') # кнопка лого в хедере
    LOGOUT_BUTTON = (By.XPATH, './/button[text()="Выход"]') # кнопка "Выход" в личном кабинете

    BUNS_BUTTON = (By.XPATH, './/span[text()="Булки"]') # кнопка "Булки" в конструкторе
    SAUCES_BUTTON = (By.XPATH, './/span[text()="Соусы"]') # кнопка "Соусы" в конструкторе
    TOPPINGS_BUTTON = (By.XPATH, './/span[text()="Начинки"]') # кнопка "Начинки" в конструкторе

    BUNS_H2 = (By.XPATH, './/h2[text()="Булки"]') # раздел "Булки" в ленте конструктора
    SAUCES_H2 = (By.XPATH, './/h2[text()="Соусы"]') # раздел "Соусы" в ленте конструктора
    TOPPINGS_H2 = (By.XPATH, './/h2[text()="Начинки"]') # раздел "Начинки" в ленте конструктора

    BUN = (By.XPATH, './/p[text()="Флюоресцентная булка R2-D3"]') # товар в булках
    SAUCE = (By.XPATH, './/p[text()="Соус Spicy-X"]') # товар в соусах
    TOPPING = (By.XPATH, './/p[text()="Мясо бессмертных моллюсков Protostomia"]') # товар в начинках
