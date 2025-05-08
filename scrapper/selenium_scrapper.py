from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
from time import sleep

import sys
import os
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from config.scrapper_config import (
    SITE_URL,
    LOGIN_BUTTON
)

load_dotenv()

login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')

def test():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get(url=SITE_URL)

    log_in = driver.find_element(by=By.CLASS_NAME, value=LOGIN_BUTTON)
    log_in.click()
    sleep(3)