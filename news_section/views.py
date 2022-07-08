from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from news_section.util import *

@csrf_exempt
def index_page(request):
    error = None
    if request.method == "POST":
        username = str(request.POST.get("username"))
        password = str(request.POST.get("password"))
        if request.POST['sign'] == 'sign-in':
            try:
                validate_sign_in(username,password)
                return redirect('home')
            except Exception as e:
                print('Error: ',e)
                error = 'Invalid Credentials'
    
        elif request.POST['sign'] == 'sign-up':
            try:
                validate_sign_up(username,password)
                return redirect('home',user=username)
            except Exception:
                error = 'Something went wrong!'
    return render(request, 'index.html', {'error':error})

@csrf_exempt
def home(request):
    if(request.method == "POST"):
        query = str(request.POST.get('query'))
        headlines = get_news(keyword=query)
    else:
        headlines = get_headlines()
    return render(request, 'home.html', {'headlines':headlines, 'active':'home'})

def profile(request):
    user_data = {
        'name': 'Steven Smith',
        'country': 'India',
        'lang': 'English'
    }
    return render(request, 'profile.html', {'user': user_data, 'active': 'profile'})