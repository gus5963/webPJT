from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def login(request):
    print('✅ GET Login 🚀')
    return  render(request, 'user/login.html')

def goHome(request):
    print('✅ GET Go Home 🚀')
    return redirect('home')
    # 해당 파일은 userApp에 있지만 redirect는 다른 폴더에 있는 url의 name을 찾아 들어갈 수 있다.


def signedIn(request):
    print('✅ GET Signed In 🚀')
    id = request.POST['id']
    pwd = request.POST['pwd']
    print('⛔️ request check id:{}/pwd:{}'.format(id,pwd))
    # model - DB(select)
    # select orm : modelName.objects.get() or .all()
    user = WebUser.objects.get(user_id = id, user_pwd = pwd)
    print('⛔️ User Check', user.user_name)
    context = {'userName' : user }
    return render(request, 'user/signedIn.html',context)

def signUp(request):
    print('✅ GET Sign Up 🚀')
    return render(request, 'user/signUp.html')

def join(request):
    print('✅ GET Join 🚀')
    id = request.POST['id']
    pwd = request.POST['pwd']
    name = request.POST['name']
    print('⛔️ request check id : {} / pwd : {} / name : {}'.format(id,pwd,name))
    # views -> model (insert)
    # insert orm : modelName(attr = values).save()
    WebUser(user_id = id,user_pwd = pwd, user_name=name).save()
    #redirect 사용하여 login page로 가기
    return redirect('login')