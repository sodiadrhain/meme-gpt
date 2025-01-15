import requests
from config.env import TWITTER_API_KEY

TWITTER_API_V2_URL = "https://api.twitter.com/2"

# HEADERS
TWITTER_HEADERS = {
    "accept": "application/json",
    "content-type": "application/json",
   'Authorization': 'Bearer ' +  TWITTER_API_KEY
}

# Search Tweets
# https://developer.x.com/en/docs/x-api/tweets/search/introduction

# Recent search
# The recent search endpoint returns Tweets from the last seven days that match a search query
# https://developer.x.com/en/docs/x-api/tweets/search/api-reference/get-tweets-search-recent
def get_recent_search(params: object):
    try:
        response = requests.get(TWITTER_API_V2_URL + "/tweets/search/recent", headers=TWITTER_HEADERS, params=params)
        # Check if the response is successful
        if response.status_code == 200:
            return {"status": "success", "data": response.json(), "message": "Twitter recent search fetched successfully"}
        else:
            return {"status": "failed", "data": response.json(), "message": "Failed to fetch twitter recent search with " + str(response.status_code) + " error" }
    except requests.exceptions.RequestException as e:
        return {"status": "error", "data": str(e), "message": "An error occured on fetching twitter recent search" }


# Full-archive search
# The full-archive search endpoint returns the complete history of public Tweets matching a search query; since the first Tweet was created March 26, 2006.
# https://developer.x.com/en/docs/x-api/tweets/search/api-reference/get-tweets-search-all
def get_search_history(params: object):
    try:
        response = requests.get(TWITTER_API_V2_URL + "/tweets/search/all", headers=TWITTER_HEADERS, params=params)
        # Check if the response is successful
        if response.status_code == 200:
            return {"status": "success", "data": response.json(), "message": "Twitter search history fetched successfully"}
        else:
            return {"status": "failed", "data": response.json(), "message": "Failed to fetch twitter search history with " + str(response.status_code) + " error" }
    except requests.exceptions.RequestException as e:
        return {"status": "error", "data": str(e), "message": "An error occured on fetching twitter search history" }