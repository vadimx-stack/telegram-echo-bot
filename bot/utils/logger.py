import logging
from pathlib import Path


def setup_logger() -> logging.Logger:
    logs_dir = Path('logs')
    logs_dir.mkdir(exist_ok=True)
    
    logger = logging.getLogger('telegram_bot')
    logger.setLevel(logging.INFO)
    
    file_handler = logging.FileHandler(logs_dir / 'bot.log')
    console_handler = logging.StreamHandler()
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger 