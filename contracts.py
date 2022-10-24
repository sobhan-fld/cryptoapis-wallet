

def tron_contracts(symbol):
    if symbol == "BTT":
        contract = "TNuoKL1ni8aoshfFL1ASca1Gou9RXwAzfn"
    elif symbol == "USDT":
        contract = "TXLAQ63Xg1NAzckPwKHvzw7CSEmLMEqcdj"
    elif symbol == "JST":
        contract = "TF17BgPaZYbz8oxbjhriubPDsA7ArKoLX3"
    elif symbol == "USDJ":
        contract = "TLBaRhANQoJFTqre9Nf1mjuwNWjCJeYqUL"
    elif symbol == "WIN":
        contract = "TU2T8vpHZhCNY8fXGVaHyeZrKm8s6HEXWe"
    return contract


def eth_contracts(symbol):
    if symbol == "USDC":
        contract = "0x07865c6e87b9f70255377e024ace6630c1eaa37f"
    return contract