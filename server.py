#!/usr/bin/env python3

from flask import Flask
from flask_restful import Api

import config
from block_resource import BlockResource

app = Flask(__name__)
api = Api(app)

@app.route("/")
def hello() :
    return "Hello World!"

api.add_resource(BlockResource, '/ethereum/blocks/latest')

if __name__ == '__main__' :
     app.run(port=5002)
