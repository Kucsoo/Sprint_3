from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Tests.Locators import TestLocators
driver = webdriver.Chrome()
chrome_options = webdriver.ChromeOptions()
driver.maximize_window()

def test_goto_personal_account_by_header_button_success():
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.XPATH, ".//button[contains(text(),'Войти')]")))
    current_url = driver.current_url
    assert current_url == 'https://stellarburgers.nomoreparties.site/login', "Переход в личный кабинет не выполнен"
    driver.quit()

def test_goto_profile_by_personal_account_button():
    driver.get('https://stellarburgers.nomoreparties.site/login')
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys("kucsoo@ya.ru")
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys("1234567")
    driver.find_element(*TestLocators.ENTER_BUTTON).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.XPATH, ".//h2[contains(text(),'Булки')]")))
    driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(
        (By.XPATH, ".//button[contains(test(), 'Сохранить')]")))
    current_url = driver.current_url
    assert current_url == 'https://stellarburgers.nomoreparties.site/account/profile', "Переход в личный кабинет не выполнен"

def test_goto_constructor_from_personal_account_success():
    driver.get('https://stellarburgers.nomoreparties.site/login')
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys("kucsoo@ya.ru")
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys("1234567")
    driver.find_element(*TestLocators.ENTER_BUTTON).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.XPATH, ".//h2[contains(text(),'Булки')]")))
    driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(
        (By.XPATH, ".//button[contains(test(), 'Сохранить')]")))
    driver.find_element(*TestLocators.CONSTRUCTOR).click()
    assert driver.find_element(*TestLocators.HEADER_COLLECT_YOUR_BURGER).text == 'Соберите бургер', "Переход в конструктор не выполнен"


def test_goto_from_account_to_main_page_by_logo_success():
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(*TestLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.XPATH, ".//button[contains(text(),'Войти')]")))
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys("kucsoo@ya.ru")
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys("1234567")
    driver.find_element(*TestLocators.ENTER_BUTTON).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.XPATH, ".//h2[contains(text(),'Булки')]")))
    driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
    driver.find_element(*TestLocators.LOGO).click()
    current_url = driver.current_url
    assert current_url== 'https://stellarburgers.nomoreparties.site/', "Переход на главную страницу не выполнен"

def test_constructor_goto_souces_success():
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(*TestLocators.HEADER_SOUCES).click()
    assert driver.find_element(*TestLocators.HEADER_SOUCES).text == 'Соусы', 'Переход в раздел "Соусы" не выполнен'

def test_constructor_goto_fillings_success():
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(*TestLocators.HEADER_FILLINGS).click()
    assert driver.find_element(*TestLocators.HEADER_FILLINGS).text == 'Начинки', 'Переход в раздел "Начинки" не выполнен'

def test_constructor_goto_buns_success():
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(*TestLocators.HEADER_FILLINGS).click()
    driver.find_element(*TestLocators.HEADER_BUNS).click()
    assert driver.find_element(*TestLocators.HEADER_BUNS).text == 'Булки', 'Переход в раздел "Булки" не выполнен'


