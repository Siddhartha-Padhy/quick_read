from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from news_section.util import *

@csrf_exempt
def index_page(request):
    error = None
    if request.method == "POST":
        username = str(request.POST.get("username"))
        password = str(request.POST.get("password"))
        lang = str(request.POST.get("lang"))
        if request.POST['sign'] == 'sign-in':
            try:
                validate_sign_in(request, username, password)
                return redirect('home')
            except Exception as e:
                print('Error: ',e)
                error = 'Invalid Credentials'
    
        elif request.POST['sign'] == 'sign-up':
            try:
                validate_sign_up(username=username, password=password, lang = lang)
                return redirect('home')
            except Exception:
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
    return render(request, 'home.html', {'headlines':headlines, 'active':'home'})

@login_required
def profile(request):
    user_data = {
        'name': 'Steven Smith',
        'country': 'India',
        'lang': 'English'
    }
    return render(request, 'profile.html', {'user': user_data, 'active': 'profile'})