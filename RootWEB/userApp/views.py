from django.shortcuts import render

# Create your views here.

def login(request):
    print('✅ GET Login 🚀')
    return  render(request, 'user/login.html')