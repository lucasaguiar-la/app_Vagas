from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

from config.scrapper_config import (
    SITE_URL,
    LOGIN_BUTTON,
    ID_USERNAME,
    ID_PASSWORD,
    VALIDATE_LOGIN_BUTTON
)

def run_bot(login, password):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get(url=SITE_URL)

    login_field = driver.find_element(by=By.CLASS_NAME, value=LOGIN_BUTTON)
    login_field.click()
    sleep(2)

    username_field = driver.find_element(by=By.ID, value=ID_USERNAME)
    username_field.send_keys(login)
    sleep(0.5)

    password_field = driver.find_element(by=By.ID, value=ID_PASSWORD)
    password_field.send_keys(password)
    sleep(0.5)

    validate_button = driver.find_element(by=By.CLASS_NAME, value=VALIDATE_LOGIN_BUTTON)
    validate_button.click()
    sleep(3)
