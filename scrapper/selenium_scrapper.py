from time import sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger_config import setup_logger
from config.scrapper_config import(
    LINKEDIN_URL,
    LINK_CLASS,
    TITLE_CLASS,
    COMPANY_CLASS,
    DESCRIPTION_CLASS,
    DATETIME_CLASS
    )

logger = setup_logger(name='Scrapper')

def extractor():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--enable-unsafe-swiftshader')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])

    logger.info('Iniciando extração...')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url=LINKEDIN_URL)

    vacacy_link = driver.find_element(by=By.CSS_SELECTOR, value=LINK_CLASS)
    link = vacacy_link.get_attribute('href')

    try:
        driver.get(link)
        sleep(0.5)

        vacacy_title = driver.find_element(by=By.CSS_SELECTOR, value=TITLE_CLASS).text
        vacacy_company = driver.find_element(by=By.CSS_SELECTOR, value=COMPANY_CLASS).text
        vacacy_datetime = driver.find_element(by=By.CSS_SELECTOR, value=DATETIME_CLASS).text
        request_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        vacacy_description = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, DESCRIPTION_CLASS)))
        vacacy_description_html = vacacy_description.get_attribute('innerHTML')

        job_object = {
            'Título': vacacy_title,
            'Empresa': vacacy_company,
            'Postado': vacacy_datetime,
            'Descrição': vacacy_description_html,
            'Link': link,
            'Data da requisição': request_timestamp
        }

        return job_object
    except Exception as e:
        logger.error(f'Algo deu errado na requisição: {e}')
        return False
    finally:
        driver.quit()
