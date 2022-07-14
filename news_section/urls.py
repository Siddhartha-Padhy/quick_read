from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home'),
    path('home/<str:topic>/', views.defined_headline, name='defined_headline'),
    path('profile/', views.profile, name='profile')
]