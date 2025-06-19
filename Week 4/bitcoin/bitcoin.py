import requests
import sys

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
try:
    bitcoin = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=90d31d87e441891a632b9df0944ee26d2d5176541fa41c56a8d8dc0a3bf9c18a")
except requests.RequestException:
    sys.exit()


data = response.json()
price = float(data["data"]["priceUsd"])
cost = round(bitcoin*price, 4)
print(f"${cost:,f}")


