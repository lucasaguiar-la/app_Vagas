from selenium import webdriver
from selenium.webdriver.common.by import By
from config.scrapper_config import(
    LINKEDIN_URL,
    CSS_CLASS
    )

import json

class Extractor:
    def __init__(self):
        self.vacacy = []
        self.driver = webdriver.Chrome()

    def run_bot(self):
        self.driver.get(url=LINKEDIN_URL)
        vacacys_links = self.driver.find_element(by=By.CSS_SELECTOR, value=CSS_CLASS)

        for vacacy_job in vacacys_links:
            link = vacacys_links.get_attribute('href')
            self.vacacy.append({
                "job_url": link
            })

        with open('result.json', 'w', encoding='utf-8') as file:
            json.dump(self.vacacy, file, indent=2)

        self.driver.quit()
        return 'Arquivo salvo!'