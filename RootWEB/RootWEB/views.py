from django.shortcuts import render

def home(request):
    print('✅ GET Home 🚀')
    request.session.get('user_name')
    context ={
        'user_name' : request.session['user_name']
    }
    return render(request, 'home.html', context)