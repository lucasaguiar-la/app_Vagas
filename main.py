from time import sleep
from scrapper.selenium_scrapper import extractor
import json 

def workflow():
    print('Sessão iniciada!')
    job_vacancy = extractor()

    if job_vacancy:
        print(f'\nObjeto criado com sucesso:\n{json.dumps(job_vacancy, ensure_ascii=False, indent=4)}')

if __name__ == '__main__':
    try:
        print('\nIniciando sessão...')
        sleep(1)
        workflow()
    except Exception as e:
        print(f'Algo deu errado ao executar o fluxo da operação: {e}')
        raise
    finally:
        print('\nSessão finalizada!')