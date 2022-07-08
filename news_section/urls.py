from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile')
]