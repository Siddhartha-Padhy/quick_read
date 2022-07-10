from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from news_section.util import *

COUNTRY = {
    'in': 'India',
    'us': 'United States',
    'ca': 'Canada',
    'sg': 'Singapore',
    'jp': 'Japan'
}

LANGUAGE = {
    'en': 'English',
    'hi': 'Hindi',
    'ta': 'Tamil',
    'te': 'Telegu',
    'ja': 'Japanese'
}

#Sign-in and log-in page
@csrf_exempt
def index_page(request):
    error = None
    if request.method == "POST":
        username = str(request.POST.get("username"))
        password = str(request.POST.get("password"))
        country = str(request.POST.get("country"))
        lang = str(request.POST.get("lang"))

        #For sign-in
        if request.POST['sign'] == 'sign-in':
            try:
                validate_sign_in(request, username, password)
                return redirect('home')
            except Exception as e:
                print('Error: ',e)
                error = 'Invalid Credentials'
    
        #For sign-up
        elif request.POST['sign'] == 'sign-up':
            try:
                validate_sign_up(request=request, username=username, password=password,country=country, lang = lang)
                return redirect('home')
            except Exception as e:
                error = 'Something went wrong!'
    return render(request, 'index.html', {'error':error})

@login_required
def logout(request):
    auth_logout(request)
    return redirect('index_page')

@csrf_exempt
@login_required
def home(request):
    if(request.method == "POST"):
        query = str(request.POST.get('query'))
        headlines = get_news(keyword=query)
    else:
        headlines = get_headlines()

    return render(request, 'home.html', {'headlines':headlines, 'active':'home', 'username': str(request.user.username)})

@login_required
def profile(request):
    username = str(request.user.username)
    country = str(request.user.first_name)
    lang = str(request.user.last_name)
    
    user_data = {
        'username': username,
        'country': COUNTRY[country],
        'lang': LANGUAGE[lang]
    }

    return render(request, 'profile.html', {'user': user_data, 'active': 'profile', 'username': str(request.user.username)})