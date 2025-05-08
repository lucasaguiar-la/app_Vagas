from scrapper.selenium_scrapper import run_bot
from dotenv import load_dotenv

import os

load_dotenv()

login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')

run_bot(login=login, password=password)