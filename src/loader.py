from dotenv import load_dotenv
from pymongo import MongoClient
from utils.logger_config import setup_logger

import os
import psycopg2 #TODO: Conexão com PostgreSQL

load_dotenv()
logger = setup_logger(name='Loader')

def connect_mongodb():
    logger.info('Estabelecendo conexão...')

    try:
        mongo_uri = os.getenv('MONGO_URI')
        mongo_db = os.getenv('MONGO_DB')
        mongo_collection = os.getenv('MONGO_COLLECTION')

        client = MongoClient(mongo_uri)
        db = client[mongo_db]
        collection = db[mongo_collection]

        logger.info('Conexão estabelecida!')
        return client, collection
    except Exception as e:
        logger.error(f'Erro ao conectar com MongoDB: {e}')
        raise

def list_all_data():
    client, collection = connect_mongodb()

    print('Arquivos salvos:')
    for idx, doc in enumerate(collection.find(), start=1):
        print(f'{idx}º Registro: {doc}')
    client.close()

def save_data_raw(data):
    logger.info('Salvando dados brutos...')

    try:
        client, collection = connect_mongodb()
        collection.insert_one(data)
        logger.info('Dados brutos salvos com sucesso!')
        return True
    except Exception as e:
        logger.error(f'Erro ao salvar dados brutos: {e}')
        return False
    finally:
        client.close()
