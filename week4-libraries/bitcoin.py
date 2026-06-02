import requests
import sys


if len(sys.argv) < 2:
    sys.exit("Not Enough Argument!")
try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Error!")


try:
    url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=8a43ef048557720fccac288f2d9cf136874c4492140c5b6c142c27b70f999f5b"
    response = requests.get(url)
    data = response.json()
    price = float(data["data"]["priceUsd"])
    cost = price * n
    print(f"${cost:,.4f}")
except requests.RequestException:
    sys.exit("Error")

