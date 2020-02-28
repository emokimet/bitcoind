import requests
import json

def get_latest_block():
    url = 'https://blockchain.info/latestblock'
    r = requests.get(url)
    response = r.json()

    print("Latest block: {}".format(response['height']))

if __name__ == "__main__":
    get_latest_block()
