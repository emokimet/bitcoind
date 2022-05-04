from prometheus_client import start_http_server, Gauge
import requests
import json

btc_price = Gauge('btc_coindesk_price', 'Current BTC price from Coindesk')
usd_clp = Gauge('usd_clp_price', 'Current USD/CLP convertion')

def get_prices():
    # BTC
    btc_url = 'https://api.coindesk.com/v1/bpi/currentprice/CNY.json'
    r = requests.get(btc_url)
    response = r.json()
    value = response['bpi']['USD']['rate_float']

    # USD
    usd_url = "https://api.apilayer.com/fixer/latest?base=USD&symbols=CLP"
    usd_headers = {'apikey': 'API KEY'}
    u = requests.get(usd_url, headers=usd_headers)
    u_response = u.json()
    u_value = u_response['rates']['CLP']

    btc_price.set(value)
    usd_clp.set(u_value)


if __name__ == "__main__":
    start_http_server(8000)
    while True:
        get_prices()
