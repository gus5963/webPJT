from django.shortcuts import render

def home(request):
    print('✅ GET Home 🚀')
    context ={'title' : 'PHS'}
    return render(request, 'home.html', context)