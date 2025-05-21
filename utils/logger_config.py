from pathlib import Path
from datetime import datetime

import logging
import sys

def setup_logger(name=__name__):
    log_dir = Path('logs')
    log_dir.mkdir(exist_ok=True)
    date = datetime.now().strftime('%Y%m%d')

    log_file = log_dir / f'app_{date}.log'

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_formatter = logging.Formatter(
        '\n%(asctime)s - %(name)s - %(levelname)s\n%(message)s\n'
    )

    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setFormatter(formatter)
    
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(console_formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger