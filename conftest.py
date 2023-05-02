import pytest
from helpers import Helpers
from urls import TestUrls
from selenium import webdriver


@pytest.fixture
def email():
    email = Helpers.email_generation()
    return email
@pytest.fixture
def password():
    password = Helpers.password_generation()
    return password

@pytest.fixture
def incorrect_password():
    incorrect_password = Helpers.wrong_password_generation()
    return incorrect_password

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    chrome_options = webdriver.ChromeOptions()
    driver.maximize_window()
    driver.get(TestUrls.MAIN_PAGE_URL)

    yield driver
    driver.quit()










