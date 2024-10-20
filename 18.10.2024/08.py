import requests

url = 'https://date.nager.at/api/v3/AvailableCountries'

countrys = requests.get(url).json()

for country in countrys:
    if  country['countryCode'] == "RU":
        print(country['name'])

