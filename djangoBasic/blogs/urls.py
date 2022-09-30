from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.home, name='dashboard'),
    path('signUp/', views.signUp, name='signUp'),
    path('', views.login, name='login'),

    # System
    path('addUser/', views.signUpForm, name='addUser'),
    path('useUser/', views.loginForm, name='useUser'),
    path('logOut/', views.logOut, name='logOut'),
]