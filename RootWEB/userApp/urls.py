from django.urls import path, include
from userApp import views

urlpatterns = [
    path('', views.login, name = 'login'),
    path('signedIn/', views.signedIn),
    path('signUp/', views.signUp),
    path('join/', views.join),
    path('goHome/', views.goHome),

]
