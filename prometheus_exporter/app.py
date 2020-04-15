from prometheus_client import start_http_server, Gauge
import requests
import json

btc_price = Gauge('btc_coindesk_price', 'Current BTC price from Coindesk')
def get_price():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/CNY.json'
    r = requests.get(url)
    response = r.json()
    value = response['bpi']['USD']['rate_float']

    btc_price.set(value)


if __name__ == "__main__":
    start_http_server(8000)
    while True:
        get_price()
