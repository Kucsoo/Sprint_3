from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from urls import TestUrls
from data import Data


def test_login_by_button_enter_to_personal_account_success(driver):
    driver.find_element(*TestLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((TestLocators.ENTER_BUTTON)))
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(Data.USER_EMAIL)
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(Data.USER_PASSWORD)
    driver.find_element(*TestLocators.ENTER_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((TestLocators.HEADER_BUNS)))
    assert driver.find_element(*TestLocators.MAKE_ORDER_BUTTON).text == 'Оформить заказ', "Вход в аккаунт не выполнен"



def test_login_by_personal_account_in_header_success(driver):
    driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((TestLocators.ENTER_BUTTON)))
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(Data.USER_EMAIL)
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(Data.USER_PASSWORD)
    driver.find_element(*TestLocators.ENTER_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((TestLocators.HEADER_BUNS)))
    assert driver.find_element(*TestLocators.MAKE_ORDER_BUTTON).text == 'Оформить заказ', "Вход в аккаунт не выполнен"


def test_login_button_in_registration_form_success(driver):
    driver.get(TestUrls.REGISTERATION_PAGE)
    element = driver.find_element(*TestLocators.ENTER_REGISTRATION_PAGE)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    driver.find_element(*TestLocators.ENTER_REGISTRATION_PAGE).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((TestLocators.ENTER_BUTTON)))
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(Data.USER_EMAIL)
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(Data.USER_PASSWORD)
    driver.find_element(*TestLocators.ENTER_BUTTON).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((TestLocators.HEADER_BUNS)))
    assert driver.find_element(*TestLocators.MAKE_ORDER_BUTTON).text == 'Оформить заказ', "Вход в аккаунт не выполнен"
    driver.quit()

def test_login_button_forgot_password_success(driver):
    driver.get(TestUrls.LOGIN_TO_ACCOUNT_PAGE)
    element = driver.find_element(*TestLocators.PASSWORD_REF_FORGOT)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    driver.find_element(*TestLocators.PASSWORD_REF_FORGOT).click()
    driver.find_element(*TestLocators.ENTER_REF).click()
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(Data.USER_EMAIL)
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(Data.USER_PASSWORD)
    driver.find_element(*TestLocators.ENTER_BUTTON).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((TestLocators.HEADER_BUNS)))
    assert driver.find_element(*TestLocators.MAKE_ORDER_BUTTON).text == 'Оформить заказ', "Вход в аккаунт не выполнен"



def test_logout_personal_account_by_button_exit_success(driver):
    driver.get(TestUrls.LOGIN_TO_ACCOUNT_PAGE)
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(Data.USER_EMAIL)
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(Data.USER_PASSWORD)
    driver.find_element(*TestLocators.ENTER_BUTTON).click()
    driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((TestLocators.EXIT_BUTTON)))
    driver.find_element(*TestLocators.EXIT_BUTTON).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((TestLocators.ENTER_BUTTON)))
    assert driver.find_element(*TestLocators.ENTER_BUTTON).text == "Войти", "Выход из аккаунта не выполнен"

