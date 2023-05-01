from selenium.webdriver.common.by import By

class TestLocators:
    INPUT_NAME = By.NAME, "name"
    INPUT_EMAIL = By.XPATH, "//label[text()='Email']/following-sibling::input"
    INPUT_PASSWORD = By.NAME, "Пароль"
    REGISTRATION_BUTTON = By.XPATH, ".//button[contains(text(),'Зарегистрироваться')]"
    ENTER_BUTTON = By.XPATH, ".//button[contains(text(),'Войти')]"
    HINT_ERROR_PASSWORD = By.XPATH, ".//p[contains(text(), 'Некорректный пароль')]"
    HINT_ERROR_USER_EXIST = By.XPATH, ".//p[contains(text(), 'Такой пользователь уже существует')]"
    LOGIN_BUTTON = By.XPATH, ".//button[contains(text(),'Войти в аккаунт')]"
    HEADER_BUNS = By.XPATH, ".//h2[contains(text(),'Булки')]"
    MAKE_ORDER_BUTTON = By.XPATH, ".//button[contains(text(),'Оформить заказ')]"
    PERSONAL_ACCOUNT = By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]"
    ENTER_REGISTRATION_PAGE = By.CLASS_NAME,"Auth_link__1fOlj"
    PASSWORD_REF_FORGOT = By.XPATH,".//a[contains(text(),'Восстановить пароль')]"
    ENTER_REF = By.XPATH, ".//a[contains(text(),'Войти')]"
    EXIT_BUTTON = By.XPATH, ".//button[contains(text(),'Выход')]"
    SAVE_BUTTON = By.XPATH, ".//button[contains(text(), 'Сохранить')]"
    CONSTRUCTOR = By.XPATH, ".//p[contains(text(), 'Конструктор')]"
    HEADER_COLLECT_YOUR_BURGER = ".//h1[contains(text(), 'Соберите бургер')]"
    LOGO = By.CLASS_NAME, "AppHeader_header__logo__2D0X2"
    HEADER_SOUCES = By.XPATH, ".//span[contains(text(),'Соусы')]"
    HEADER_FILLINGS = By.XPATH, ".//span[contains(text(),'Начинки')]"
