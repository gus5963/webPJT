from django.shortcuts import render

# Create your views here.

def cartList(request):
    print('✅ GET Cart List 🚀')
    return render(request, 'cart/cartList.html')