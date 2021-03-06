from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def login(request):
    print('โ GET Login ๐')
    context = {}
    if request.session.get('user_name'):
        context['sessionUserName'] = request.session.get('user_name')
        return render(request, 'user/signedIn.html', context)
    else:
        return  render(request, 'user/login.html')

def goHome(request):
    print('โ GET Go Home ๐')
    return redirect('home')
    # ํด๋น ํ์ผ์ userApp์ ์์ง๋ง redirect๋ ๋ค๋ฅธ ํด๋์ ์๋ url์ name์ ์ฐพ์ ๋ค์ด๊ฐ ์ ์๋ค.


def signedIn(request):
    print('โ GET Signed In ๐')
    id = request.POST['id']
    pwd = request.POST['pwd']
    print('โ๏ธ request check id:{}/pwd:{}'.format(id,pwd))
    # model - DB(select)
    # select orm : modelName.objects.get() or .all()
    context = {}
    try:
        user = WebUser.objects.get(user_id = id, user_pwd = pwd)
        print('โ๏ธ User Check', user.user_name)
        request.session['user_id'] = user.user_id
        request.session['user_name'] = user.user_name
        # session ์์ฑ
        context['sessionUserId'] = request.session['user_id']
        context['sessionUserName'] = request.session['user_name']
        return render(request, 'user/signedIn.html',context)
    except Exception as e:
        context['error'] = str(e)
        return render(request, 'user/logIn.html', context)

def signUp(request):
    print('โ GET Sign Up ๐')
    return render(request, 'user/signUp.html')

def join(request):
    print('โ GET Join ๐')
    id = request.POST['id']
    pwd = request.POST['pwd']
    name = request.POST['name']
    print('โ๏ธ request check id : {} / pwd : {} / name : {}'.format(id,pwd,name))
    # views -> model (insert)
    # insert orm : modelName(attr = values).save()
    WebUser(user_id = id,user_pwd = pwd, user_name=name).save()
    #redirect ์ฌ์ฉํ์ฌ login page๋ก ๊ฐ๊ธฐ
    return redirect('userLogin')

def userLogOut(request):
    print('โ GET User LogOut ๐')
    # delete session
    request.session['user_id'] = {}
    request.session['user_name'] =  {}
    request.session.modified = True
    return redirect('userLogin')

def userRemove(request):
    print('โ GET User Remove ๐')
    return redirect('home')


def userDetail(request):
    print('โ GET User Detail ๐')
    return render(request,'user/userDetail.html')