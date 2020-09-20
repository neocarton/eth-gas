from functools import reduce
from statistics import mean
import numpy as np
from tabulate import tabulate
from concurrent.futures import ThreadPoolExecutor
from web3 import Web3

GWEI = 1000000000
BLOCK_COUNT = 10

executor = ThreadPoolExecutor(10)
web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/5628222b9a4c49cf8557b1b539bad81e"))
lastBlockNumber = web3.eth.blockNumber
blocks = list(executor.map(web3.eth.getBlock, range(lastBlockNumber, lastBlockNumber - BLOCK_COUNT, -1)))
transactionHashes = list(reduce(lambda transactionHashList1, transactionHashList2: transactionHashList1 + transactionHashList2, map(lambda block: block.transactions, blocks)))
transactions = list(executor.map(web3.eth.getTransaction, transactionHashes))
print(transactions)
gasPrices = np.array(list(map(lambda tx: tx['gasPrice'] / GWEI, transactions)))
print("min %d, max %d, avg. %d Gwei (number of transactions %d)" % (np.min(gasPrices), np.max(gasPrices), np.average(gasPrices), len(gasPrices)))
