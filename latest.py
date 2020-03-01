import requests
import json

def get_latest_block():
    url = 'https://blockchain.info/latestblock'
    r = requests.get(url)
    response = r.json()
    curr_block = response['height']

    remaining_blocks = 840000 - curr_block
    print("Latest block: {}. {} Blocks remaining".format(curr_block, remaining_blocks))

if __name__ == "__main__":
    get_latest_block()
