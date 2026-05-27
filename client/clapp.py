import requests

while True:
    r = requests.get("http://web:8000/")
    print(r.text)
