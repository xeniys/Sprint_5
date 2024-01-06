В данном проекте реализованы автотесты для сервиса Stellar Burgers - https://stellarburgers.nomoreparties.site/

Тесты: 

- Файл test_registration.py содержит класс class TestRegistration:
  - def test_successful_registration() проверяет успешную регистрацию. Поле «Имя» должно быть не пустым; 
  в поле Email введён email в формате логин@домен: например, 123@ya.ru. Минимальный пароль — шесть символов.
  Email генерируется в файле data.py (кол-во уникальных значений ограничено, иногда тест может флапать).
  - def test_registration_wrong_password() проверяет ошибку для некорректного пароля.
- Файл test_login.py содержит класс TestLogin:
  - def test_authorization_from_main_page() - вход по кнопке «Войти в аккаунт» на главной;
  - def test_authorization_from_header() - вход через кнопку «Личный кабинет»;
  - def test_authorization_from_registration_form() - вход через кнопку в форме регистрации;
  - def test_authorization_from_reset_password_form() - ход через кнопку в форме восстановления пароля.
- Файл test_transit_to_personal_cabinet.py содержит класс TestTransitionToPersonalCabinet:
  - def test_transit_to_personal_cabinet() - переход по клику на «Личный кабинет».
- Файл test_transit_to_construction_kit.py содержит класс TestTransitionToConstructionKit:
  - def test_transit_from_personal_cabinet_to_constructor() - переход по клику на «Конструктор» и на логотип Stellar Burgers.
- Файл test_logout.py содержит класс TestLogout:
  - def test_logout() - выход по кнопке «Выйти» в личном кабинете.
- Файл test_construction_kit.py содержит класс TestConstructionKit:
  - def test_constructor_buns_transition() - переход к разделу "Булки"
  - def test_constructor_sauces_transition() - переход к разделу "Соусы"
  - def test_constructor_toppings_transition() - переход к разделу "Начинки"

В файле constants.py содержатся константы, используемые в тестах, а в файле locators.py - все локаторы с описаниями.

