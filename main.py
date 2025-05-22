from time import sleep
from utils.logger_config import setup_logger
from src.extractor import extractor
from src.transformer import transformer
from src.loader import save_data_raw

logger = setup_logger(name='Workflow')

def workflow():
    logger.info('Sessão iniciada!')

    job_vacancy = extractor()
    if job_vacancy:
        save_data_raw(data=job_vacancy)
        data_transformed = transformer(data=job_vacancy)

        if data_transformed:
            logger.info('Dados tratados com sucesso!')


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