from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from urls import TestUrls
from data import Data


def test_goto_personal_account_by_header_button_success(driver):
    driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((TestLocators.ENTER_BUTTON)))
    assert driver.find_element(*TestLocators.ENTER_BUTTON).text == "Войти", "Переход в личный кабинет не выполнен"


def test_goto_profile_by_personal_account_button(driver):
    driver.get(TestUrls.LOGIN_TO_ACCOUNT_PAGE)
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(Data.USER_EMAIL)
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(Data.USER_PASSWORD)
    driver.find_element(*TestLocators.ENTER_BUTTON).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((TestLocators.HEADER_BUNS)))
    driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(
        (TestLocators.SAVE_BUTTON)))
    assert driver.find_element(*TestLocators.EXIT_BUTTON).text == "Выход", "Переход в личный кабинет не выполнен"

def test_goto_constructor_from_personal_account_success(driver):
    driver.get(TestUrls.LOGIN_TO_ACCOUNT_PAGE)
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(Data.USER_EMAIL)
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(Data.USER_PASSWORD)
    driver.find_element(*TestLocators.ENTER_BUTTON).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((TestLocators.HEADER_BUNS)))
    driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.SAVE_BUTTON)))
    driver.find_element(*TestLocators.CONSTRUCTOR).click()
    assert driver.find_element(*TestLocators.HEADER_COLLECT_YOUR_BURGER).text == "Соберите бургер", "Переход в конструктор не выполнен"


def test_goto_from_account_to_main_page_by_logo_success(driver):
    driver.find_element(*TestLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((TestLocators.ENTER_BUTTON)))
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(Data.USER_EMAIL)
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(Data.USER_PASSWORD)
    driver.find_element(*TestLocators.ENTER_BUTTON).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((TestLocators.HEADER_BUNS)))
    driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
    driver.find_element(*TestLocators.LOGO).click()
    assert driver.find_element(*TestLocators.MAKE_ORDER_BUTTON).text == 'Оформить заказ', "Переход на главную страницу не выполнен"

def test_constructor_goto_souces_success(driver):
    driver.find_element(*TestLocators.HEADER_SOUCES).click()
    assert driver.find_element(*TestLocators.HEADER_SOUCES).text == 'Соусы', 'Переход в раздел "Соусы" не выполнен'

def test_constructor_goto_fillings_success(driver):
    driver.find_element(*TestLocators.HEADER_FILLINGS).click()
    assert driver.find_element(*TestLocators.HEADER_FILLINGS).text == 'Начинки', 'Переход в раздел "Начинки" не выполнен'

def test_constructor_goto_buns_success(driver):
    driver.find_element(*TestLocators.HEADER_FILLINGS).click()
    driver.find_element(*TestLocators.HEADER_BUNS).click()
    assert driver.find_element(*TestLocators.HEADER_BUNS).text == 'Булки', 'Переход в раздел "Булки" не выполнен'


