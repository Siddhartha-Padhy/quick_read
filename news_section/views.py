from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from news_section.util import *

def home(request):
    headlines = get_headlines()
    return render(request, 'home.html', {'headlines':headlines})