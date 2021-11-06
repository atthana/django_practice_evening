from django.http.response import HttpResponse
from django.shortcuts import render

from django.http import HttpResponse
from .models import Product

def Home(request): # ต้องใส่ request เข้าไปด้วยนะ เพราะ render ต้องการ request เป็นส่วนประกอบ

    allproduct = Product.objects.all()  # SELECT * from product มันคือแบบนี้นะใน SQL
    context = {'allproduct': allproduct}

    return render(request, 'company/home.html', context)

def AboutUs(request):
    return render(request, 'company/aboutus.html')

def ContactUs(request):
    if request.method == 'POST':
        data = request.POST.copy()
        title = data.get('title')
        email = data.get('email')
        detail = data.get('detail')
        print(data)
        print('------------')
        print(title)
        print(email)
        print(detail)
        print('------------')
    return render(request, 'company/contact.html')