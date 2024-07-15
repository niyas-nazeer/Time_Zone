from django.db import models

# Create your models here.

class customer(models.Model):
    customer_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    gender=models.CharField(max_length=1)
    address_1=models.TextField()
    address_2=models.TextField()

class admin(models.model):
    admin_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    role=models.CharField(max_length=255)
    employee_id=models.IntegerField()

class seller(models.model):
    seller_id=models.AutoField(primary_key=True)
    swller_name=models.CharField(max_length=255)
    legal_name=models.CharField(max_length=255)
    contact_person=models.CharField(max_length=255)
    alter_mobile=models.CharField(max_length=14)

class order(models.model):
    order_id=models.AutoField(primary_key=True)
    customer_id=models.IntegerField()
    order_date=models.DateTimeField()
    order_status=models.CharField(max_length=10)
    transaction_id=models.IntegerField()

class order_details(models.model):
    order_details_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField()
    product_id=models.IntegerField()
    product_quantity=models.IntegerField()
    total_amount=models.DecimalField(7,2)

class cart(models.model):
    product_id=models.IntegerField()
    customer_id=models.IntegerField()
    product_quantity=models.IntegerField()

    class meta:
        unique_togethor = ('customer_id','product_id')

