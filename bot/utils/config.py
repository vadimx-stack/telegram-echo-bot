import os
from pathlib import Path
from dotenv import load_dotenv


def load_config() -> str:
    dotenv_path = Path('.') / '.env'
    load_dotenv(dotenv_path=dotenv_path)
    
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    if not token:
        raise ValueError('TELEGRAM_BOT_TOKEN не настроен в файле .env')
    
    return token 