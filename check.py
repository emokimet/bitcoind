import requests
import json

def get_price():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/CNY.json'
    r = requests.get(url)
    response = r.json()
    value = response['bpi']['USD']['rate_float']

    b_url = 'https://www.buda.com/api/v2/markets/BTC-CLP/ticker'
    b_r = requests.get(b_url)
    b_response = b_r.json()
    b_price = b_response['ticker']['last_price'][0]
    b_var24h = b_response['ticker']['price_variation_24h']
    b_var7d = b_response['ticker']['price_variation_7d']

    print("CLP: ${} | 24h: {}% | 7d: {}% | USD ${}".format(b_price, b_var24h, b_var7d, int(value)))

if __name__ == "__main__":
    get_price()
