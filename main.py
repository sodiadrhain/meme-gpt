# Pass all your imports here for test
import logging
import tg.bot
from services.twitter import get_recent_search
from services.dexscreener import get_token_asset
from config.db import initialize_database

# listen to logs
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Connect Database
initialize_database()

tg.bot.start_bot()

# print(get_recent_search({"query": "2ru87k7yAZnDRsnqVpgJYETFgqVApuBcwB2xDb19pump"}))
# print("dex: ", get_token_asset("dhdhdh"))
