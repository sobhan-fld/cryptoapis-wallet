import json
import requests
import api
import contracts

walletID = "620bb9632b0df000061a180d"

def generate_deposit(coin, network):

    url = "/wallet-as-a-service/wallets/"+walletID+"/"+coin+"/"+network+"/addresses?context=clientdeposit"

    payload = '{"data":{"item":{"label":"examlpe"}}}'
    x = api.apipost(url,payload)
    print(x)
    json_result = json.loads(x.text)
    dep_add = json_result["data"]["item"]["address"]
    return dep_add


def list_dep_add(coin, network):

    url = "/wallet-as-a-service/wallets/"+walletID+"/"+coin+"/"+network+"/addresses?limit=50"

    x = api.apiget(url)
    print(x)
    print(json.dumps(x.json(), indent=4))

def wallet_tx(coin, network):
    url = '/wallet-as-a-service/wallets/'+walletID+'/'+coin+'/'+network+'/transactions'

    x = api.apiget(url)

    print(x)
    print(json.dumps(x.json(), indent=4))

def withdrawal(coin, network, amount, address):
    url= "/wallet-as-a-service/wallets/"+walletID+"/"+coin+"/"+network+"/transaction-requests"

    payload = '{"data":{"item":{"feePriority":"standard","recipients":[{"address":"'+address+'","amount":"'+amount+'"}]}}}'

    x = api.apipost(url, payload)

    print(x)
    print(json.dumps(x.json(), indent=4))


def token_withdrawal(coin, network, senderaddress, rcaddress, amount, symbol):
    url= "/wallet-as-a-service/wallets/"+walletID+"/"+coin+"/"+network+"/addresses/"+senderaddress+"/feeless-token-transaction-requests"

    smartcontract = contracts.tron_contracts(symbol)
    print(smartcontract)

    payload = '{"data":{"item":{"amount":"'+amount+'","feeLimit":"1000000000","recipientAddress":"'+rcaddress+'","tokenIdentifier":"TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t"}}}'

    x = api.apipost(url,payload)

    print(x)
    print(json.dumps(x.json(), indent=4))

def wallet_assets():
    url = "/wallet-as-a-service/wallets/all-assets"

    x = api.apiget(url)
    print(x)
    print(json.dumps(x.json(), indent=4))