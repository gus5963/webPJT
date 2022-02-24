from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def goHome(request):
    print('✅ GET Go Home 🚀')
    return redirect('home')

def boardList(request):
    print('✅ GET Board List 🚀')
    request.session.get('user_id')
    request.session.get('user_name')
    context = {}
    context['user_id'] = request.session['user_id']
    context['user_name'] = request.session['user_name']
    boards = WebBoard.objects.all().order_by('-id')
    context['boards'] = boards
    print('context : ', context)
    return render(request,'boards/boardList.html',context)


def boardRead(request):
    print('✅ GET Read Board 🚀')
    id = request.GET['id']
    board = WebBoard.objects.get(id=id)
    request.session.get('user_id')
    context = {
        'board' : board,
        'user_id': request.session['user_id']
    }
    board.viewcnt += 1
    board.save()
    return render(request, 'boards/boardRead.html', context)