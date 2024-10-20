import requests

def get_lang():
    languages={0:'ru',1:'en'}
    choice=(input("На каком языке вы хотите цитату?: 0 - Русский | 1 - Английский  -- "))

    url = 'http://api.forismatic.com/api/1.0/'
    payload  = {'method': 'getQuote', 'format': 'text', 'lang': languages[int(choice)]}
    res = requests.get(url, params=payload)

    data = res.text

    print(data)

get_lang()