from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # แก้ไขจาก price เป็น cost
    quantity = models.IntegerField(null=True, blank=True, default=1)
    instock = models.BooleanField(default=True)  # True คือ มีในสต๊อกนะ

    def __str__(self):
        return self.title

class ContactList(models.Model):  # Should be ContactList
    title = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    detail = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)  # ถ้า user ไม่ได้ใส่อะไรมา ก็จะเป้น False อยู่แล้ว

    def __str__(self):
        return self.title
    