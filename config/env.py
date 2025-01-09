import os
from dotenv import load_dotenv

load_dotenv()

TATUM_API_KEY: str = os.getenv('TATUM_API_KEY')
HELIUS_API_KEY: str = os.getenv('HELIUS_API_KEY')
TWITTER_API_KEY: str = os.getenv('TWITTER_API_KEY')
TELEGRAM_BOT_TOKEN: str = os.getenv('TELEGRAM_BOT_TOKEN')



