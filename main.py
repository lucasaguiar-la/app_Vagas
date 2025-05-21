from time import sleep
from utils.logger_config import setup_logger
from scrapper.selenium_scrapper import extractor

import json 

logger = setup_logger()

def workflow():
    logger.info('Sessão iniciada!')
    job_vacancy = extractor()

    if job_vacancy:
        logger.info(f'\nObjeto criado com sucesso:\n{json.dumps(job_vacancy, ensure_ascii=False, indent=4)}')

if __name__ == '__main__':
    try:
        logger.info('Iniciando sessão...')
        sleep(1)
        workflow()
    except Exception as e:
        logger.error(f'Algo deu errado ao executar o fluxo da operação: {e}')
        raise
    finally:
        logger.info('Sessão finalizada!')