import requests


apikey = "f96ef2c9cd5a01bed860f03a359dc4e1386a42c4"
baseurl = "https://rest.cryptoapis.io"

def apipost(url,payload):
    x = requests.post(baseurl+url, headers={"X-Api-Key": apikey, "Content-type": "application/json"}, data=payload)
    return x

def apiget(url):
    x = requests.get(baseurl+url,headers={"X-Api-Key": apikey, "Content-type": "application/json"})
    return x

