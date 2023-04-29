
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Tests.Locators import TestLocators
driver = webdriver.Chrome()
chrome_options = webdriver.ChromeOptions()
driver.maximize_window()

def test_registration_success(email, password):
    driver.get('https://stellarburgers.nomoreparties.site/register')
    driver.find_element(*TestLocators.INPUT_NAME).send_keys("Kiki")
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(email)
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(password)
    driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
    WebDriverWait(
        driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, ".//button[contains(text(),'Войти')]")))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login", "Пользователь не зарегистрирован"
    driver.quit()

def test_registration_failed_without_name(email, password):
    driver.get('https://stellarburgers.nomoreparties.site/register')
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(email)
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(password)
    driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
    assert driver.find_element(*TestLocators.REGISTRATION_BUTTON).text == "Зарегистрироваться", "Пользователь зарегистрирован"
    driver.quit()


def test_registration_failed_wrong_email(password):
    driver.get('https://stellarburgers.nomoreparties.site/register')
    driver.find_element(*TestLocators.INPUT_NAME).send_keys("Kiki")
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys("wsad@")
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(password)
    driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
    assert driver.find_element(
        *TestLocators.REGISTRATION_BUTTON).text == "Зарегистрироваться", "Пользователь зарегистрирован"
    driver.quit()

def test_registration_failed_incorrect_password_shows_error(email, incorrect_password):
    driver.get('https://stellarburgers.nomoreparties.site/register')
    driver.find_element(*TestLocators.INPUT_NAME).send_keys("Kiki")
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(email)
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(incorrect_password)
    driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
    WebDriverWait(
        driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, ".//p[contains(text(), 'Некорректный пароль')]")))
    assert driver.find_element(*TestLocators.HINT_ERROR_PASSWORD).text == "Некорректный пароль", "Сообщение об неверном пароле не отображается"
    driver.quit()

def test_registration_failed_incorrect_user_already_exist(password):
    driver.get('https://stellarburgers.nomoreparties.site/register')
    driver.find_element(*TestLocators.INPUT_NAME).send_keys("Kiki")
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys("kucsoo@ya.ru")
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(password)
    driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
    element = driver.find_element(*TestLocators.ENTER_REGISTRATION_PAGE)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    WebDriverWait(
        driver, 5).until(
        expected_conditions.presence_of_element_located((By.XPATH, ".//p[contains(text(), 'Такой пользователь уже существует')]")))
    assert driver.find_element(*TestLocators.HINT_ERROR_USER_EXIST).text == "Такой пользователь уже существует", "Сообщение об ошибке не отображается"
    driver.quit()

