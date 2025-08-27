import requests
import sys

def main():
    btc = get_bitcoin()
    if len(sys.argv) != 2:
        sys.exit("Missing valid argument")
        return
    arg = sys.argv[1]
    try:
        number = float(arg)
        result = float(number * btc)
        print(f"${result:,.4f}")
    except ValueError:
        sys.exit("Argument is not a number!")

def get_bitcoin():
    try:
        r = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=5e1fdd2c62e07806ba7ff99cf03826f1d310fee47225de9a718cf342046638ff')
        content = r.json()
        price = float(content["data"]["priceUsd"])
        return price
    except requests.RequestException:
        print('No api')
main()
