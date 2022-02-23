from django.urls import path, include
from cartApp import views

urlpatterns = [
    path('', views.cartList),

]