import auth
import json

rpc_connection = auth.BitcoinRPC(rpc_user='foo', rpc_password='bar')
print(rpc_connection.getblockcount())

chaintips = json.dumps(rpc_connection.getchaintips(), indent=2)
print(chaintips)
