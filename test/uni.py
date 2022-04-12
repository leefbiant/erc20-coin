import json
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract
from eth_account.messages import encode_defunct

# web3.py instance
web3 = Web3(HTTPProvider("http://101.32.35.92:8545"))
print(web3.isConnected())

key="0x46c57b3cb855b82a0aa368913077afb6638502e32f46456510ec4dd63eed77b4"
acct = web3.eth.account.privateKeyToAccount(key)

block = web3.eth.get_block('latest')
#print(block)

print(web3.eth.accounts)
print(web3.eth.accounts[0], 0)
print(web3.eth.get_balance(web3.eth.accounts[0]))

#web3.eth.send_transaction({
#  'to': '0x3F171Bd8779f9709DB9F5b1F8aA87267e6b6d1a5',
#  'from': web3.eth.accounts[1],
#  'value': 700000000000000000
#})
#
contract_addr = "0x06E5B6441F5d96c09B6d49aFF40c07c7F83c49a8"
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

addr="0x3F171Bd8779f9709DB9F5b1F8aA87267e6b6d1a5"

#c.functions.getBlocTime().call()
#
#to_addr="0x3F171Bd8779f9709DB9F5b1F8aA87267e6b6d1a5"
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
    tx = c.functions.transfer("0x00F766400Edadd70d5944B740b2F321AbF513846", 1).buildTransaction({'gas': 1000000,
        'gasPrice': web3.toWei('21', 'gwei'), 'from': acct.address,
        'nonce': web3.eth.getTransactionCount(acct.address)})
    signed = acct.signTransaction(tx)
    tx_id = web3.eth.sendRawTransaction(signed.rawTransaction)
    print(tx_id)
except Exception as r:
    print("feed_list failed :%s", r) 


