from secret_keys import *
import requests

def format_news(data):
    for article in data:
        article['content'] = str(article['content']).split("... [")[0] + "..."
    return data

def get_news(keyword,lang='en',country='in'):
    link = f'https://gnews.io/api/v4/search?q={keyword}&lang={lang}&country={country}&token={API_TOKEN}'
    data = requests.get(link)
    data = data.json()['articles']
    data = format_news(data)
    return data

def get_headlines(lang='en',country='in'):
    link = f"https://gnews.io/api/v4/top-headlines?lang={lang}&country={country}&token={API_TOKEN}"
    data = requests.get(link)
    data = data.json()['articles']
    data = format_news(data)
    return data
