from django.urls import path, include
from boardApp import views

urlpatterns = [
    path('', views.boardList, name='boardList'),
    path('goHome/', views.goHome),
    path('boardRead/', views.boardRead),

]
