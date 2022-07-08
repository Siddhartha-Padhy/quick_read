from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('home', views.home, name='home'),
    path('profile', views.profile, name='profile')
]