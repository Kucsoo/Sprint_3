from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Tests.Locators import TestLocators
driver = webdriver.Chrome()
chrome_options = webdriver.ChromeOptions()
driver.maximize_window()


def test_login_by_button_enter_to_personal_account_success():
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(*TestLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, ".//button[contains(text(),'Войти')]")))
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys("kucsoo@ya.ru")
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys("1234567")
    driver.find_element(*TestLocators.ENTER_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, ".//h2[contains(text(),'Булки')]")))
    assert driver.find_element(*TestLocators.MAKE_ORDER_BUTTON).text == 'Оформить заказ', "Вход в аккаунт не выполнен"
    driver.quit()


def test_login_by_personal_account_in_header_success():
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.XPATH, ".//button[contains(text(),'Войти')]")))
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys("kucsoo@ya.ru")
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys("1234567")
    driver.find_element(*TestLocators.ENTER_BUTTON).click()
    assert driver.find_element(*TestLocators.MAKE_ORDER_BUTTON).text == 'Оформить заказ', "Вход в аккаунт не выполнен"
    driver.quit()

def test_login_button_in_registration_form_success():
    driver.get('https://stellarburgers.nomoreparties.site/register')
    element = driver.find_element(*TestLocators.ENTER_REGISTRATION_PAGE)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    driver.find_element(*TestLocators.ENTER_REGISTRATION_PAGE).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.XPATH, ".//button[contains(text(),'Войти')]")))
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys("kucsoo@ya.ru")
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys("1234567")
    driver.find_element(*TestLocators.ENTER_BUTTON).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.XPATH, ".//h2[contains(text(),'Булки')]")))
    assert driver.find_element(*TestLocators.MAKE_ORDER_BUTTON).text == 'Оформить заказ', "Вход в аккаунт не выполнен"
    driver.quit()

def test_login_button_forgot_password_success():
    driver.get('https://stellarburgers.nomoreparties.site/login')
    element = driver.find_element(*TestLocators.PASSWORD_REF_FORGOT)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    driver.find_element(*TestLocators.PASSWORD_REF_FORGOT).click()
    driver.find_element(*TestLocators.ENTER_REF).click()
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys("kucsoo@ya.ru")
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys("1234567")
    driver.find_element(*TestLocators.ENTER_BUTTON).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.XPATH, ".//h2[contains(text(),'Булки')]")))
    assert driver.find_element(*TestLocators.MAKE_ORDER_BUTTON).text == 'Оформить заказ', "Вход в аккаунт не выполнен"
    driver.quit()


def test_logout_personal_account_by_button_exit_success():
    driver.get('https://stellarburgers.nomoreparties.site/login')
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys("kucsoo@ya.ru")
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys("1234567")
    driver.find_element(*TestLocators.ENTER_BUTTON).click()
    driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.XPATH, ".//button[contains(text(),'Выход')]")))
    driver.find_element(*TestLocators.EXIT_BUTTON).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.XPATH, ".//button[contains(text(),'Войти')]")))
    current_url = driver.current_url
    assert current_url == 'https://stellarburgers.nomoreparties.site/login', "Выход из аккаунта не выполнен"

