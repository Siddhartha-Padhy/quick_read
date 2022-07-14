from secret_keys import *
import requests
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate

# Function to append id and format content for each article
def format_news(data):
    for id, article in enumerate(data):
        article['id'] = id
        article['content'] = str(article['content']).split("... [")[0] + "..."
    return data

# Get news based on relevense to a keyword
# params:   keyword: string to search the news for
#           lang, country: language and country of user
# return:  data: news articles
def get_news(keyword,lang='en',country='in'):
    link = f'https://gnews.io/api/v4/search?q={keyword}&lang={lang}&country={country}&token={API_TOKEN}'
    data = requests.get(link)
    data = data.json()['articles']
    data = format_news(data)
    return data

# Get the news headlines
# params:  lang, country: language and country of user
# return:  data: news articles
def get_headlines(topic='',lang='en',country='in'):
    if len(topic)>0:
        link = f"https://gnews.io/api/v4/top-headlines?topic={topic}&lang={lang}&country={country}&token={API_TOKEN}"
    else:
        link = f"https://gnews.io/api/v4/top-headlines?lang={lang}&country={country}&token={API_TOKEN}"

    data = requests.get(link)
    data = data.json()['articles']
    data = format_news(data)
    return data

# Validate and sign in the requested user.
# params:   request: request object
#           username, password: username and password of user
def validate_sign_in(request, username, password):
    user = authenticate(username=username, password=password)
    if user == None:
        raise Exception('No user found')
    else:
        auth_login(request, user)

# Validate and sign up the requested user.
# params:   request: request object
#           username, password: username and password of user
#           country, lang: country and language of user
def validate_sign_up(request, username, password, country, lang):
    try:
        user = User.objects.create_user(username=username, password=password, first_name=country, last_name=lang)
        auth_login(request, user)
    except Exception as e:
        print("Exp: " + e)