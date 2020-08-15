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
    b_price = float(b_response['ticker']['last_price'][0])
    b_var24h = float(b_response['ticker']['price_variation_24h']) * 100
    b_var7d = float(b_response['ticker']['price_variation_7d']) * 100

    print("CLP: ${:.0f} | 24h: {:.2f}% | 7d: {:.2f}% | USD ${}".format(b_price, b_var24h, b_var7d, int(value)))

if __name__ == "__main__":
    get_price()
