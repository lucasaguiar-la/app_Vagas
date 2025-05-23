from time import sleep
from bs4 import BeautifulSoup
from utils.logger_config import setup_logger
import re

logger = setup_logger(name='Transformer')

def transformer(data):
    logger.info('Iniciando tratamento...')
    sleep(0.5)

    try:
        soup = BeautifulSoup(data['Descrição'], 'html.parser')
        clean_text = soup.get_text(separator='\n').strip()

        for br in soup.find_all('br'):
            br.replace_with('\n')
        for ul in soup.find_all(['ul', 'ol']):
            for li in ul.find_all('li'):
                li.insert_before('\n• ')
            ul.unwrap()

        clean_text = soup.get_text(separator=' '.strip())
        clean_text = re.sub(r'\n\s*\n', '\n\n', clean_text)
        clean_text = re.sub(r' +', ' ', clean_text)
        clean_text = '\n'.join(line.strip() for line in clean_text.splitlines())

        formated_data = {
            'titulo': data['Título'],
            'empresa': data['Empresa'],
            'data_postagem': data['Postado'],
            'descricao': clean_text,
            'url': data['Link']
        }

        logger.info(
            f'\nTítulo da vaga: {formated_data['titulo']}\n'
            f'Empresa: {formated_data['empresa']}\n'
            f'Data da postagem: {formated_data['data_postagem']}'
            )

        return formated_data
    except Exception as e:
        logger.error(f'Algo deu errado no tratamento: {e}')
        return False
