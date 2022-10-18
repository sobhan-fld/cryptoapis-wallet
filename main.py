import cryptoapis
print("possible values:\ncoins: bitcoin,ethereum,tron\nnetwork: testnet,goerli,Nile\n")
s1 = input("1-Coins\n2-Tokens\n")
print()
if s1 == '1':
    s2 = input("1-Generate deposit address\n"
               "2-list Depoit addresses\n"
               "3-Wallet transactions\n"
               "4-Withdraw\n")
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
    else:
        print("Error")


elif s1 == '2':
    s2 = input("1-Transaction details\n")

    if s2 == '1':
        coin = input("enter network's coin")



