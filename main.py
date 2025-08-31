import requests

req = requests.request('GET', 'https://httpbin.org/get')
print(req.json()['origin'])
