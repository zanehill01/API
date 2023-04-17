
import requests
import json

url = 'https://api.fbi.gov/wanted/v1/list'
r = requests.get(url)

response = r.json()

for row in response:
    print(row)