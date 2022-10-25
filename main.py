import cryptoapis
import contracts

print(contracts.tron_contracts("BTT"))
print("possible values:\ncoins: bitcoin,ethereum,tron\nnetwork: testnet,goerli,Nile\n")
s1 = input("1-Coins\n2-Tokens\n")
print()
if s1 == '1':
    s2 = input("1-Generate deposit address\n"
               "2-list Depoit addresses\n"
               "3-Wallet transactions\n"
               "4-Withdraw\n"
               "5-Wallet assets (admin)\n")
    if s2 == '1':
        coin = input("coin: ")
        coin = coin.lower()
        network = input("network: ")
        print(cryptoapis.generate_deposit(coin, network))

    elif s2 == '2':
        coin = input("coin: ")
        coin = coin.lower()
        network = input("network: ")
        cryptoapis.list_dep_add(coin, network)

    elif s2 == '3':
        coin = input("coin: ")
        coin = coin.lower()
        network = input("network: ")
        cryptoapis.wallet_tx(coin, network)

    elif s2 == '4':
        coin = input("coin: ")
        coin = coin.lower()
        network = input("network: ")
        amount = input("amount: ")
        address = input("address: ")
        cryptoapis.withdrawal(coin, network, amount, address)
    elif s2 == '5':
        cryptoapis.wallet_assets()
    else:
        print("Error")


elif s1 == '2':
    s2 = input("1-withdrawal tron tokens\n"
               "2-withdrawal eth token\n")

    if s2 == '1':
        senderaddress = input("enter the sender address: ")
        symbol = input("enter the symbol: ")
        symbol = symbol.upper()
        rcaddress = input("recipient address: ")
        amount = input("enter the amount: ")
        cryptoapis.token_withdrawal_tron(senderaddress, rcaddress, amount, symbol)

    elif s2 == '2':
        symbol = input("enter the symbol: ")
        symbol = symbol.upper()
        senderaddress = input("enter the sender address: ")
        rcaddress = input("recipient address: ")
        amount = input("enter the amount: ")
        cryptoapis.token_withdrawal_eth(senderaddress, symbol, amount, rcaddress)

