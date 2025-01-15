import os
from dotenv import load_dotenv

load_dotenv()

TATUM_API_KEY: str = os.getenv('TATUM_API_KEY')
HELIUS_API_KEY: str = os.getenv('HELIUS_API_KEY')
TWITTER_API_KEY: str = os.getenv('TWITTER_API_KEY')
TELEGRAM_BOT_TOKEN: str = os.getenv('TELEGRAM_BOT_TOKEN')
DB_HOST: str = os.getenv('DB_HOST')
DB_DRIVER: str = os.getenv('DB_DRIVER')
DB_NAME: str = os.getenv('DB_NAME')
DB_USER: str = os.getenv('DB_USER')
DB_PASSWORD: str = os.getenv('DB_PASSWORD')
DB_PORT: str = os.getenv('DB_PORT')



