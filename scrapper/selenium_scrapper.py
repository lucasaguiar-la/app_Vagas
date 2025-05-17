from time import sleep
from pyautogui import press
from requests import get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from config.scrapper_config import(
    LINKEDIN_URL,
    LINK_CLASS
    )

import json

def extractor():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--enable-unsafe-swiftshader')

    print('Iniciando sessão...')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url=LINKEDIN_URL)
    print(driver)

    sleep(1)
    #press('esc')

    vacacys_link = driver.find_element(by=By.CSS_SELECTOR, value=LINK_CLASS)
    link = vacacys_link.get_attribute('href')
    print(f'Link da vaga: {link}')

    try:
        response = get(url=link)
        print(f'Conteúdo do link: {response.text}')
    except Exception as e:
        return f'Algo deu errado na requisição: {e}'
    finally:
        driver.quit()
