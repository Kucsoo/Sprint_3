# Sprint_3
Test registration:
1) test_registration_success - проверка успешной регистрации, где все поля заполнены валидными данными
2) test_registration_failed_without_name - проверка, что регистрация не удалась, если инпут Имя оставить пустым
3) test_registration_failed_wrong_email - проверка, чо регистрация не удалась, если в инпут Email ввести некорректную почту
4) test_registration_failed_incorrect_password_shows_error - проверка, что при попытке зарегистрироваться с паролем, короче 6 символов, появляется хинт об ошибке
5) test_registration_failed_incorrect_user_already_exist - проверка, что при попытке зарегистрироваться с почтой, которая уже есть в базе, появляется хинт об ошибке

Test login logout:
1) test_login_by_button_enter_to_personal_account_success - проверка входа по кнопке «Войти в аккаунт» на главной странице
2) test_login_by_personal_account_in_header_success - проверка входа через кнопку «Личный кабинет» в хедере
3) test_login_button_in_registration_form_success - проверка входа через кнопку "Войти" в форме регистрации
4) test_login_button_forgot_password_success - проверка входа через кнопку "Войти" в форме восстановления пароля
5) test_logout_personal_account_by_button_exit_success - проверка выхода по кнопке «Выйти» в личном кабинете

Test goto:
1) test_goto_personal_account_by_header_button_success - проверка перехода по клику на «Личный кабинет»
2) test_goto_profile_by_personal_account_button - по клику на «Личный кабинет», когда пользователь залогинился
3) test_goto_constructor_from_personal_account_success - проверка перехода из личного кабинета в конструктор (пользователь залогинился)
4) test_goto_from_account_to_main_page_by_logo_success - проверка перехода из личного кабинета логотип Stellar Burgers (пользователь залогинился)
5) test_constructor_goto_souces_success - проверка перехода в раздел «Соусы»
6) test_constructor_goto_fillings_success- проверка перехода в раздел «Начинки»
7) test_constructor_goto_buns_success- проверка перехода в раздел «Булки»

Locators - содержит описания всех локаторов, которые использованы в тестах
conftest - фикстуры для тестов