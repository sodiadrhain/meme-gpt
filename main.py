# Pass all your imports here for test
# import tg.bot
from services.twitter import get_recent_search
# from services.dexscreener import get_token_asset

# tg.bot.start_bot()

print(get_recent_search({"query": "2ru87k7yAZnDRsnqVpgJYETFgqVApuBcwB2xDb19pump"}))
# print("dex: ", get_token_asset("dhdhdh"))
