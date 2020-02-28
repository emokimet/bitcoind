import requests
import json

def get_price():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/CNY.json'
    r = requests.get(url)
    response = r.json()
    value = response['bpi']['USD']['rate'][:5]

    print("BTC ${}".format(value))

if __name__ == "__main__":
    get_price()
