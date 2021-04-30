import requests
import json
import datetime
from flask import Flask, Response
from flask_apscheduler import APScheduler
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app, Counter, Gauge

app = Flask(__name__)
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
    })

c = Counter('counter', 'Count of requests')
g_block = Gauge('latest_block', 'Bitcoin latest block')
g_price = Gauge('latest_price', 'Bitcoin latest price')

@app.route('/')
def hello_world():
    r = requests.get('https://blockchain.info/latestblock')
    response = r.json()
    current_block = response['height']
    g_block.set(current_block)

    t = requests.get('https://blockchain.info/ticker')
    tresponse = t.json()
    ticker_usd = tresponse['USD']['last']
    g_price.set(ticker_usd)

    c.inc()
    return Response(f"Latest block: {current_block} - Last price: {ticker_usd}", status=200)

if (__name__ == "__main__"):
    scheduler = APScheduler()
    scheduler.add_job(func=hello_world,
            trigger='interval',
            id='job',
            seconds=30,
            )
    scheduler.start()
    app.run(host='0.0.0.0', port=5001)
