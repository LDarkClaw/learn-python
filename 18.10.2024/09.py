import requests

url = 'https://date.nager.at/api/v3/PublicHolidays/2024/RU'
res = requests.get(url)
data = res.json()

print("\n".join([f"{item['date']} - {item['localName']}" for item in data]))