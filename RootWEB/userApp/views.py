from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def login(request):
    print('✅ GET Login 🚀')
    context = {}
    if request.session.get('user_name'):
        context['sessionUserName'] = request.session.get('user_name')
        return render(request, 'user/signedIn.html', context)
    else:
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
    context = {}
    try:
        user = WebUser.objects.get(user_id = id, user_pwd = pwd)
        print('⛔️ User Check', user.user_name)
        request.session['user_id'] = user.user_id
        request.session['user_name'] = user.user_name
        # session 생성
        context['sessionUserId'] = request.session['user_id']
        context['sessionUserName'] = request.session['user_name']
        return render(request, 'user/signedIn.html',context)
    except Exception as e:
        context['error'] = str(e)
        return render(request, 'user/logIn.html', context)

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
    return redirect('userLogin')

def userLogOut(request):
    print('✅ GET User LogOut 🚀')
    # delete session
    request.session['user_id'] = {}
    request.session['user_name'] =  {}
    request.session.modified = True
    return redirect('userLogin')

def userRemove(request):
    print('✅ GET User Remove 🚀')
    return redirect('home')


def userDetail(request):
    print('✅ GET User Detail 🚀')
    return render(request,'user/userDetail.html')