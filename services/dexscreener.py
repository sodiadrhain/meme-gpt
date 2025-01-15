import requests
import logging

logger = logging.getLogger(__name__)

DEX_API_URL = "https://api.dexscreener.com/latest/dex/"

# HEADERS
DEX_HEADERS = {
    "content-type": "application/json",
}

def get_token_asset(token: str):
    logger.info("get_token_asset")
    try: 
        response = requests.get(
            DEX_API_URL+"tokens/"+token,
            headers=DEX_HEADERS)
        # Check if the response is successful
        if response.status_code == 200:
            return {"status": "success", "data": response.json(), "message": "Dex token asset fetched successfully"}
        else:
            return {"status": "failed", "data": response.json(), "message": "Dex token asset fetch failed with" + str(response.status_code) + " error" }
    except requests.exceptions.RequestException as e:
        return {"status": "error", "data": str(e), "message": "An error occured on dexscreener get_token_asset" }