from flask_restful import Resource
from flask_jsonpify import jsonify

import config
from ethereum import block

class BlockNumberResource(Resource) :

    def get(self) :
        return block.getLastBlockNumber()

class BlockResource(Resource) :

    def get(self) :
        lastBlock = block.getLastBlock()
        return jsonify(dict(lastBlock))
