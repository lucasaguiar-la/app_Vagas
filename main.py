from scrapper.selenium_scrapper import Extractor
from config.scrapper_config import LINKEDIN_URL


play = Extractor()

req = play.run_bot()
print(req)