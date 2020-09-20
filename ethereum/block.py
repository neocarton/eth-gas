from attributedict.collections import AttributeDict
import json
from web3 import Web3

import config

# IPCProvider:
# __w3 = Web3(Web3.IPCProvider("./path/to/geth.ipc"))

# HTTPProvider:
# __w3 = Web3(Web3.HTTPProvider(config.ETH_NODE_HTTP_URL))

# WebsocketProvider:
__w3 = Web3(Web3.WebsocketProvider(config.ETH_NODE_WS_URL))

def toDict(w3Object) :
    objectAsJson = Web3.toJSON(w3Object)
    return json.loads(objectAsJson)


def getLastBlockNumber() :
    return __w3.eth.blockNumber

def getLastBlock() :
    lastBlock = __w3.eth.getBlock('latest')
    return toDict(lastBlock)
