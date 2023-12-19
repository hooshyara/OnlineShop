from django.db import models
from accounts.models import User
from products.models import Products
import random
import string



def generate_unic_code():
    cod_length = 6
    characters = string.ascii_letters + string.digits

    while(True):
        code = ''.join(random.choice(characters) for _ in range(cod_length)) 
        
        if not Order.objects.filter(code=code).exists():
            return code
            


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    end_price = models.CharField(max_length=100, null=True, default=0)

    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    post_id = models.CharField(max_length=10, null=True)
    description = models.CharField(max_length=100, blank=True)
    totla_price = models.CharField(max_length=100, default=0)
    code = models.CharField(max_length=6, unique=True, default=generate_unic_code, null=True)


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    product_price = models.DecimalField(max_digits=10, decimal_places=0)
    product_count = models.PositiveIntegerField()
    product_cost = models.DecimalField(max_digits=10, decimal_places=0)



    