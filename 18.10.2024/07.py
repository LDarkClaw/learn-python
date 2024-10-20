import requests

url = 'https://date.nager.at/api/v3/AvailableCountries'

res = requests.get(url)
data = res.json()

print(data)