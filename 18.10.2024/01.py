import requests

def get_lang():
    languages={0:'ru',1:'en'}
    choice=int(input("На каком языке вы хотите цитату?: 0 - Русский | 1 - Английский  -- "))
    return languages.get(choice)


url = 'http://api.forismatic.com/api/1.0/'
payload  = {'method': 'getQuote', 'format': 'text', 'lang': get_lang()}
res = requests.get(url, params=payload)

data = res.text

print(data)
