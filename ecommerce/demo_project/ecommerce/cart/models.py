from django.db import models
from shop.models import Product
from django.contrib.auth.models import User
# Cart model

class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    data_added=models.DateTimeField(auto_now_add=True)

    # def subtotal(self):
    #     return self.quantity*self.product.price

    def __str__(self):
        return self.user.username

    def subtotal(self):
           return self.quantity*self.product.price
class Order_table(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    no_of_items=models.IntegerField()
    phone=models.CharField(max_length=30)
    pin=models.CharField(max_length=30,blank=True)
    address=models.TextField()
    order_id=models.CharField(max_length=12,blank=True)
    ordered_date=models.DateTimeField(auto_now_add=True)
    payment_status=models.CharField(default="pending",max_length=30)
    delivery_status = models.CharField(default="pending",max_length=30)

    def __str__(self):
        return self.user.username

class Account(models.Model):
    acctnum=models.BigIntegerField()
    accttype=models.CharField(max_length=20)
    amount=models.IntegerField()

    def __str__(self):
        return str(self.acctnum)


class payment(models.Model):
    name=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)
    order_id=models.CharField(max_length=30,blank=True)
    razorpay_payment_id=models.CharField(max_length=30,blank=True)
    paid=models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)
