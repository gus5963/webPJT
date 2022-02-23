from django.urls import path, include
from userApp import views

urlpatterns = [
    path('', views.login),
    path('signedIn/', views.signedIn),

]
