from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    gender=models.CharField(max_length=1)
    address_1=models.TextField()
    address_2=models.TextField()

class admin(models.Model):
    admin_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    role=models.CharField(max_length=255)
    employee_id=models.IntegerField()

class seller(models.Model):
    seller_id=models.AutoField(primary_key=True)
    swller_name=models.CharField(max_length=255)
    legal_name=models.CharField(max_length=255)
    contact_person=models.CharField(max_length=255)
    alter_mobile=models.CharField(max_length=14)

class products(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=255)
    slug=models.TextField()
    description=models.TextField()
    short_description=models.TextField()
    categories=models.TextField()
    brand_name=models.CharField(max_length=255)
    Images=models.ImageField()

class inventory(models.Model):
    price=models.DecimalField(max_digits=7,decimal_places=2)
    original_price=models.DecimalField(max_digits=7,decimal_places=2)
    stock_quantity=models.IntegerField()

class cart(models.Model):
    product_id=models.ForeignKey(products,on_delete=models.CASCADE)
    customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product_quantity=models.IntegerField()

    class meta:
        unique_togethor = ('customer_id','product_id')

class transaction(models.Model):
    transaction_id=models.AutoField(primary_key=True)
    transaction_date=models.DateTimeField()
    payment_method=models.CharField(max_length=10)
    amout=models.IntegerField()
    transaction_status=models.CharField(max_length=10)
    ip_address=models.IntegerField()
    response_code=models.IntegerField()
    response_message=models.CharField(max_length=255)

class order(models.Model):
    order_id=models.AutoField(primary_key=True)
    customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    order_date=models.DateTimeField()
    order_status=models.CharField(max_length=10)
    transaction_id=models.ForeignKey(transaction,on_delete=models.CASCADE)

class order_details(models.Model):
    order_details_id=models.AutoField(primary_key=True)
    order_id=models.ForeignKey(order,on_delete=models.CASCADE)
    product_id=models.ForeignKey(products,on_delete=models.CASCADE)
    product_quantity=models.IntegerField()
    total_amount=models.DecimalField(max_digits=7,decimal_places=2)
