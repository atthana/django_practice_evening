from django.http.response import HttpResponse
from django.shortcuts import render

from django.http import HttpResponse
from .models import ContactList, Product

def Home(request): # ต้องใส่ request เข้าไปด้วยนะ เพราะ render ต้องการ request เป็นส่วนประกอบ

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

        # ContactUs(title=title, email=email, detail=detail).save()  # ทำแบบนี้ก็ save ได้เหมือนกันนะ ลด code ให้เหลือบรรทัดเดียวเลย แต่จะไม่ยืดหยุ่นเหมือนแบบหลายบรรทัดข้างล่างที่มันใส่เงื่อนไขแต่ละ field ได้
        
        newrecord = ContactList()
        newrecord.title = title  # เพราะเราสร้าง model แล้ว เลยใช้ .title ได้เลย เหมือนกับ Flutter ที่สร้าง model นั่นแหละ
        newrecord.email = email  # พวกนี้คือการใส่ค่าเข้าไปใน model น่ั่นแหละ
        newrecord.detail = detail
        newrecord.save()  # พอใช้ .save() ก็จะ save ข้อมูลเข้า db นะ
        context['message'] = 'ตอนนี้คิวได้รับข้อความแล้ว เด่วขออ่านก่อนนะแล้วจะตอบกลับภายใน 5 ปี'

    return render(request, 'company/contact.html', context=context)