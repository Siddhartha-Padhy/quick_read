from secret_keys import *
import requests
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate

def format_news(data):
    for id, article in enumerate(data):
        article['id'] = id
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

def validate_sign_in(request, username, password):
    user = authenticate(username=username, password=password)
    if user == None:
        raise Exception('No user found')
    else:
        auth_login(request, user)

def validate_sign_up(username, password, lang):
    try:
        user = User.objects.create_user(username=username, password=password)
    except Exception as e:
        print("Exp: " + e)