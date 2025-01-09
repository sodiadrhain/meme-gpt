import requests
import uuid
import config.env

HELIUS_API_KEY = config.env.HELIUS_API_KEY
HELIUS_RPC_URL = "https://mainnet.helius-rpc.com/"

def generate_request_id():
    return str(uuid.uuid4()) 

def make_helius_json_rpc_request(method: str, params: object):
    try: 
        response = requests.post(
            HELIUS_RPC_URL + "?api-key="+ HELIUS_API_KEY,
            headers={"Content-Type":"application/json"},
            json={"jsonrpc":"2.0","id": generate_request_id,"method":method,"params":params}
        )
        return {"status": "success", "data": response.json(), "message": "Helius "+method+" request successful"}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "data": str(e), "message": "An error occured on "+method+" helius json rpc request" }

# Get an asset by its ID, ID is CA or Token
# https://docs.helius.dev/compression-and-das-api/digital-asset-standard-das-api/get-asset
def get_token_asset(token: str):
    return make_helius_json_rpc_request("getAsset", {"id": token})