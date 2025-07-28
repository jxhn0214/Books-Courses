import requests
import sys


try:
    bitcoin_info = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=")
except requests.RequestException:
    sys.exit()

bitcoin_data = bitcoin_info.json()

#Check if user has entered bitcoin amount
try:
    if len(sys.argv) > 1:
        dollar = float(sys.argv[1]) #retrieve amount
        bitcoin_value = float(bitcoin_data["data"]["priceUsd"])
        bitcoin_to_dollar = (dollar * bitcoin_value) #convert
        print(f"${bitcoin_to_dollar:,.4f}", end="") #format
    else:
        sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")