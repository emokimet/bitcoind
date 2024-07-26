from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

class BitcoinRPC():
    def __init__(self, rpc_user, rpc_password):
        self.rpc_user = rpc_user
        self.rpc_password = rpc_password
        self.rpc_connection = AuthServiceProxy(f"http://{self.rpc_user}:{self.rpc_password}@192.168.1.30:8332",
                                               timeout=10)


    def getblockcount(self):
        msg = f"Current block count: {self.rpc_connection.getblockcount()}"
        return msg

    def getchaintips(self):
        return self.rpc_connection.getchaintips()


