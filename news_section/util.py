from secret_keys import *
import requests

def get_news(keyword):
    link = f'https://gnews.io/api/v4/search?q={keyword}&token={API_TOKEN}'
    data = requests.get(link)
    print("Data: "+data)
    return data

def get_headlines():
    link = "https://gnews.io/api/v4/top-headlines?lang=en&token=" + API_TOKEN
    data = requests.get(link)
    data = data.json()['articles']
    return data
