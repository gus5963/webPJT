from django.shortcuts import render
from .models import *
# Create your views here.

def login(request):
    print('✅ GET Login 🚀')
    return  render(request, 'user/login.html')


def signedIn(request):
    print('✅ GET Signed In 🚀')
    id = request.POST['id']
    pwd = request.POST['pwd']
    print('⛔️ request check',id,pwd)
    # model - DB(select)
    user = WebUser.objects.get(user_id = id, user_pwd = pwd)
    print('⛔️ User Check', user.user_name)
    context = {'userName' : user }
    return render(request, 'user/signedIn.html',context)