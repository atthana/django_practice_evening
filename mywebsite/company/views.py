from django.http.response import HttpResponse
from django.shortcuts import render

from django.http import HttpResponse
from .models import ContactList, Product
from songline import Sendline

def Home(request):
    allproduct = Product.objects.all()  # SELECT * from product มันคือแบบนี้นะใน SQL
    context = {'allproduct': allproduct}
    return render(request, 'company/home.html', context)

def AboutUs(request):
    return render(request, 'company/aboutus.html')

def ContactUs(request):
    context = {} # สิ่งที่จะแนบไป คือเวลาเข้ามาในหน้านี้ปกติ จะทำบรรทัดนี้
    if request.method == 'POST':
        data = request.POST.copy()  # data จะเป็น dictinary นะ
        title = data.get('title')  # ชื่อพวกนี้ควรเหมือนกับ id ใน html นะ
        email = data.get('email')
        detail = data.get('detail')
        print(data)
        print('------------')
        print(title)
        print(email)
        print(detail)
        print('------------')  # ปกติควร print ก่อนนะ พอได้ข้อมูลแล้วค่อยทำการ save
        if title == '' and email == '':
            context['message'] = 'เทอๆ กรอกหัวข้อและอีเมลล์ด้วยจ้า เพราะจะส่งคำตอบไม่ได้'
            return render(request, 'company/contact.html', context=context)  

        newrecord = ContactList()
        newrecord.title = title
        newrecord.email = email
        newrecord.detail = detail
        newrecord.save()
        context['message'] = 'ตอนนี้คิวได้รับข้อความแล้ว เด่วขออ่านก่อนนะแล้วจะตอบกลับภายใน 5 ปี'

        # ส่ง Line
        token = '8hd3NiwuQQd0yELpCf1BjLSlO7ljAXsFfRG1f8tfn4k'
        m = Sendline(token)
        m.sendtext('\nหัวข้อ: {}\nemail: {}\n>>> {}'.format(title, email, detail))

    return render(request, 'company/contact.html', context=context)

from django.contrib.auth import authenticate, login

def Login(request):
    context = {}
    
    if request.method == 'POST':
        data = request.POST.copy()
        username = data.get('username')
        password = data.get('password')
        try:
            user = authenticate(username=username, password=password)  # เป็นการ get password จากตัว form
            print('-----user-----')
            print(user)
            login(request, user)  # มาจาก lib นะ
        except:
            context['message'] = 'อีเมลล์หรือรหัสผ่านไม่ถูกต้อง กรุณาติดต่อ admin'

    return render(request, 'company/login.html', context=context)