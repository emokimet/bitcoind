from prometheus_client import start_http_server, Gauge
import requests
import json

btc_coindesk_price = Gauge('btc_coindesk_price', 'Current BTC price from Coindesk')
btc_blockchain_price = Gauge('btc_blockchain_price', "Current BTC price from Blockchain.com")

def get_prices():
    # BTC
    btc_coindesk_url = 'https://api.coindesk.com/v1/bpi/currentprice/CNY.json'
    coindesk_r = requests.get(btc_coindesk_url)
    coindesk_response = coindesk_r.json()
    coindesk_value = coindesk_response['bpi']['USD']['rate_float']

    btc_blockchain_url = 'https://api.blockchain.com/v3/exchange/tickers/BTC-USD'
    blockchain_r = requests.get(btc_blockchain_url)
    blockchain_response = blockchain_r.json()
    blockchain_value = blockchain_response['last_trade_price']

    # Set gauges
    btc_coindesk_price.set(coindesk_value)
    btc_blockchain_price.set(blockchain_value)


if __name__ == "__main__":
    start_http_server(8000)
    while True:
        get_prices()
