from fastapi import FastAPI, Response
from fastapi_utils.tasks import repeat_every
from prometheus_client import Gauge, generate_latest, CONTENT_TYPE_LATEST
import requests
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

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

    return coindesk_value, blockchain_value

@app.get("/")
def read_root():
    return "See /metrics"


@app.on_event("startup")
@repeat_every(seconds=10)
@app.get("/metrics")
def read_items():
    get_prices()
    logger.info("Updated prices")
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
