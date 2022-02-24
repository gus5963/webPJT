from django.urls import path, include
from userApp import views

urlpatterns = [
    path('', views.login, name = 'userLogin'),
    path('signedIn/', views.signedIn),
    path('signUp/', views.signUp),
    path('join/', views.join),
    path('goHome/', views.goHome),
    path('userLogOut/', views.userLogOut),
    path('userRemove/', views.userRemove),
    path('userDetail/', views.userDetail),

]
