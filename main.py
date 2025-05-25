from time import sleep
from utils.logger_config import setup_logger
from src.extractor import extractor
from src.transformer import transformer
from src.loader import save_data_raw

logger = setup_logger(name='Workflow')

def workflow():
    logger.info('Sessão iniciada!')

    job_objects = extractor()

    if job_objects:
        for job in job_objects:
            try:
                save_data_raw(data=job)
                data_transformed = transformer(data=job)
        
            except Exception as e:
                logger.error(f'Erro ao salvar e tratar o dado: {e}')
                continue

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