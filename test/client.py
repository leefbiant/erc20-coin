import json
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract
from eth_account.messages import encode_defunct

# web3.py instance
web3 = Web3(HTTPProvider("http://127.0.0.1:7545"))
print(web3.isConnected())

key="95e10fd65eb0558c07df37f611b221d472b7b054d35367f190c91c3abeeeedd9"
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
contract_addr = "0xace088ef93a8abDDEb887b0bFf7253d0B1948F23"
print(contract_addr)
#
with open('../build/contracts/Doge.json', 'r') as f:
    conf = json.load(f)
    abi = conf['abi']
    #print(json.dumps(abi))

#print(abi)
c = web3.eth.contract(contract_addr, abi=abi)
print(c.all_functions()) 

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

tx = c.functions.transfer("0x00F766400Edadd70d5944B740b2F321AbF513846", 100).buildTransaction({'gas': 1000000,
    'gasPrice': web3.toWei('21', 'gwei'), 'from': acct.address,
    'nonce': web3.eth.getTransactionCount(acct.address)})
signed = acct.signTransaction(tx)
tx_id = web3.eth.sendRawTransaction(signed.rawTransaction)
print(tx_id)


