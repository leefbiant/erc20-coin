# -*- coding: UTF-8 -*-
import json
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract
from eth_account.messages import encode_defunct

# web3.py instance
web3 = Web3(HTTPProvider("https://kovan.infura.io/v3/c2f0069b6c5b488395992009425f05dc"))
print(web3.isConnected())

key="b09f37cea7f3da434e0d6c19d31846e4b555b00e6ec423279fc8527008cefbf7"
acct = web3.eth.account.privateKeyToAccount(key)

block = web3.eth.get_block('latest')
#print(block)

print(web3.eth.accounts)
#print(web3.eth.accounts[0], 0)
#print(web3.eth.get_balance(web3.eth.account))
print(web3.eth.get_balance("0x3f9E93988a96a48B451E01CcF776C71Ce238970F"))

#web3.eth.send_transaction({
#  'to': '0x3F171Bd8779f9709DB9F5b1F8aA87267e6b6d1a5',
#  'from': web3.eth.accounts[1],
#  'value': 700000000000000000
#})
#
contract_addr = "0xFC4C60d7621e8fbaBd27674749e7407D0E100779"
print(contract_addr)
#
with open('../build/contracts/Doge.json', 'r') as f:
    conf = json.load(f)
    abi = conf['abi']
    #print(json.dumps(abi))

#print(abi)
c = web3.eth.contract(contract_addr, abi=abi)
print(c.all_functions()) 
print(c.functions.name().call()) 
print(c.functions.symbol().call()) 
print(c.functions.decimals().call()) 

addr="0x3f9E93988a96a48B451E01CcF776C71Ce238970F"

#print(web3.eth.gasPrice())
#
to_addr="0x1c81CEc7323847f5807Bb472f30EC519dbc6B8C0"
#tx = c.functions.getBlockNum().buildTransaction({'gas': 1000000,
#    'gasPrice': web3.toWei('21', 'gwei'), 'from': acct.address,
#    'nonce': web3.eth.getTransactionCount(acct.address)})
#signed = acct.signTransaction(tx)
#tx_id = web3.eth.sendRawTransaction(signed.rawTransaction)
#
#print(tx_id)
#print(c.functions.totalSupply().call())
print(c.functions.balanceOf(addr).call())
#print(c.functions.approve(addr, 10).call())
#print(c.functions.transfer("0x00F766400Edadd70d5944B740b2F321AbF513846", 10).call())

try:
    tx = c.functions.transfer(to_addr, 10000000000000000000000).buildTransaction({'gas': 1000000,
        'gasPrice': web3.toWei('21', 'gwei'), 'from': acct.address,
        'nonce': web3.eth.getTransactionCount(acct.address)})
    signed = acct.signTransaction(tx)
    tx_id = web3.eth.sendRawTransaction(signed.rawTransaction)
    print(tx_id.hex())
except Exception as r:
    print("Exception feed_list failed :%s", r) 


