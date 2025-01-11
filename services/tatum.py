import requests
from config.env import TATUM_API_KEY

# HEADERS
TATUM_HEADERS = {
    "accept": "application/json",
    "content-type": "application/json",
    "x-api-key": TATUM_API_KEY
}

TATUM_API_URL = "https://api.tatum.io/v3"

# Generate Solana wallet
# https://docs.tatum.io/reference/solanageneratewallet
def generate_solana_wallet():
    try:
        response = requests.get(TATUM_API_URL + "/solana/wallet", headers=TATUM_HEADERS)
        # Check if the response is successful
        if response.status_code == 200:
            return {"status": "success", "data": response.json(), "message": "Solana wallet generated successfully"}
        else:
            return {"status": "failed", "data": response.json(), "message": "Solana wallet generated failed with " + str(response.status_code) + " error" }
    except requests.exceptions.RequestException as e:
        return {"status": "error", "data": str(e), "message": "An error occured on generating solana wallet" }
    

# Get Solana Account balance
# https://docs.tatum.io/reference/solanagetbalance
def get_solana_account_balance(address: str):
    try:
        response = requests.get(TATUM_API_URL + "/solana/account/balance/" + address, headers=TATUM_HEADERS)
        # Check if the response is successful
        if response.status_code == 200:
            return {"status": "success", "data": response.json(), "message": "Solana account balance fetched successfully"}
        else:
            return {"status": "failed", "data": response.json(), "message": "Failed to fetch solana account balance with " + str(response.status_code) + " error" }
    except requests.exceptions.RequestException as e:
        return {"status": "error", "data": str(e), "message": "An error occured on fetching solana account balance" }
    

# Send SOL from account to account
# https://docs.tatum.io/reference/solanablockchaintransfer
def send_sol_from_acount(from_address: str, to_address: str, amount: float, from_private_key: str):
    body_params = {
        "from": from_address,
        "to": to_address,
        amount: amount,
        "fromPrivateKey": from_private_key
    }

    try:
        response = requests.post(TATUM_API_URL + "/solana/transaction", headers=TATUM_HEADERS, json=body_params)
        # Check if the response is successful
        if response.status_code == 200:
            return {"status": "success", "data": response.json(), "message": "Sent sol to account successfully"}
        else:
            return {"status": "failed", "data": response.json(), "message": "Failed to send sol to accounte with " + str(response.status_code) + " error" }
    except requests.exceptions.RequestException as e:
        return {"status": "error", "data": str(e), "message": "An error occured on sending sol to account" }