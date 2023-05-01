
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from urls import TestUrls
from data import Data


def test_registration_success(driver, email, password):
    driver.get('https://stellarburgers.nomoreparties.site/register')
    driver.find_element(*TestLocators.INPUT_NAME).send_keys(Data.USER_NAME)
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(email)
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(password)
    driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
    WebDriverWait(
        driver, 5).until(expected_conditions.presence_of_element_located((TestLocators.ENTER_BUTTON)))
    assert driver.find_element(*TestLocators.ENTER_BUTTON).text == "Войти", "Пользователь не зарегистрирован"


def test_registration_failed_without_name(driver, email, password):
    driver.get(TestUrls.REGISTERATION_PAGE)
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(email)
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(password)
    driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
    assert driver.find_element(*TestLocators.REGISTRATION_BUTTON).text == "Зарегистрироваться", "Пользователь зарегистрирован"



def test_registration_failed_wrong_email(driver, password):
    driver.get(TestUrls.REGISTERATION_PAGE)
    driver.find_element(*TestLocators.INPUT_NAME).send_keys(Data.USER_NAME)
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(Data.USER_INCORRECT_EMAIL)
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(password)
    driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
    assert driver.find_element(
        *TestLocators.REGISTRATION_BUTTON).text == "Зарегистрироваться", "Пользователь зарегистрирован"


def test_registration_failed_incorrect_password_shows_error(driver, email, incorrect_password):
    driver.get(TestUrls.REGISTERATION_PAGE)
    driver.find_element(*TestLocators.INPUT_NAME).send_keys(Data.USER_NAME)
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(email)
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(incorrect_password)
    driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
    WebDriverWait(
        driver, 5).until(expected_conditions.presence_of_element_located((TestLocators.HINT_ERROR_PASSWORD)))
    assert driver.find_element(*TestLocators.HINT_ERROR_PASSWORD).text == "Некорректный пароль", "Сообщение об неверном пароле не отображается"


def test_registration_failed_incorrect_user_already_exist(driver, password):
    driver.get(TestUrls.REGISTERATION_PAGE)
    driver.find_element(*TestLocators.INPUT_NAME).send_keys(Data.USER_NAME)
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(Data.USER_EMAIL)
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(password)
    driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
    element = driver.find_element(*TestLocators.ENTER_REGISTRATION_PAGE)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    WebDriverWait(
        driver, 5).until(
        expected_conditions.presence_of_element_located((TestLocators.HINT_ERROR_USER_EXIST)))
    assert driver.find_element(*TestLocators.HINT_ERROR_USER_EXIST).text == "Такой пользователь уже существует", "Сообщение об ошибке не отображается"


