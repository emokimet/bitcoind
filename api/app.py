import requests
import json
import datetime
from flask import Flask, Response, jsonify
from flask_apscheduler import APScheduler
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app, Counter, Gauge

app = Flask(__name__)
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
    })

count = Counter('counter', 'Count of requests')
block = Gauge('latest_block', 'Bitcoin latest block')
price = Gauge('latest_price', 'Bitcoin latest price')
volume = Gauge('trade_volume', 'Estimated transaction volume (BTC)')

@app.route('/')
def hello_world():
    r = requests.get('https://api.blockchain.info/stats')
    response = r.json()

    latest_block = response['n_blocks_total']
    block.set(latest_block)

    latest_price = response['market_price_usd']
    price.set(latest_price)

    trade_volume = Response['trade_volume_btc']
    volume.set(trade_volume)

    count.inc()

    with app.app_context():
        return jsonify(latest_block=f"{latest_block}",
            latest_price=f"{latest_price}",
            trade_volume_btc=f"{trade_volume}"
            )

if (__name__ == "__main__"):
    scheduler = APScheduler()
    scheduler.add_job(func=hello_world,
            trigger='interval',
            id='job',
            seconds=30,
            )
    scheduler.start()
    app.run(host='0.0.0.0', port=5001)
