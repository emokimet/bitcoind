import urllib3
import json

def get_price():
    http = urllib3.PoolManager()
    url = 'https://api.coindesk.com/v1/bpi/currentprice/CNY.json'
    r = http.request('GET', url)
    response = json.loads(r.data.decode('utf-8'))
    value = response['bpi']['USD']['rate'][:5]

    print("BTC ${}".format(value))

if __name__ == "__main__":
    get_price()
