import requests
import json

def get_price():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/CNY.json'
    r = requests.get(url)
    response = r.json()
    value = response['bpi']['USD']['rate_float']

    print("BTC ${}".format(int(value)))

if __name__ == "__main__":
    get_price()
