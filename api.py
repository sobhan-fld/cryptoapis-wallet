import requests

#put the api key here
apikey = ""
baseurl = "https://rest.cryptoapis.io"

def apipost(url,payload):
    x = requests.post(baseurl+url, headers={"X-Api-Key": apikey, "Content-type": "application/json"}, data=payload)
    return x

def apiget(url):
    x = requests.get(baseurl+url,headers={"X-Api-Key": apikey, "Content-type": "application/json"})
    return x

