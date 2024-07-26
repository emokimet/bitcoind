import auth
import json

# Catch the timeout exception
try:
    rpc_connection = auth.BitcoinRPC(rpc_user='satoshi', rpc_password='password')
    print(rpc_connection.getblockcount())

    # Get the blockchain information
    chaintips = json.dumps(rpc_connection.getchaintips(), indent=2)
    print(chaintips)

except Exception as e:
    print(e)

