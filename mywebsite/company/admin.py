from django.contrib import admin

from company.models import ContactList, Product

# Register your models here.

admin.site.register(Product)  # เป็นการ register model เข้าไปเพื่อให้ admin สามารถมองเห็นและแก้ไขได้
admin.site.register(ContactList)