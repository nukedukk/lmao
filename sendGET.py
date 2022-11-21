import requests

url = input("Plz input url you want to request: ")
try:
    getResponse = requests.get("https://" + url)
    print(getResponse)
except requests.exceptions.ConnectionError:
    pass
