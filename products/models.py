from collections.abc import Iterable
from django.db import models
from django.db import models
from django.urls import reverse
from accounts.models import User



class Category(models.Model):
    name = models.CharField(max_length=100)
    # products = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name

class Products(models.Model):
    PRODUCT_STARS = [
        ('1', 'یک ستاره'),
        ('2', 'دو ستاره'),
        ('3', 'سه ستاره'),
        ('4', 'چهار ستاره'),
        ('5', 'پنج ستاره '),
    ]
    
    title = models.CharField(max_length=100)
    content = models.TextField(null=True)
    cover = models.ImageField(upload_to='products/', null=True)
    star = models.CharField(max_length=100 ,null=True, choices=PRODUCT_STARS)
    price = models.PositiveBigIntegerField(default=0)
    second_price = models.PositiveBigIntegerField(default=0)
    inventory = models.IntegerField(default=0, null=True)
    active = models.BooleanField(default=True)
    discouont = models.PositiveIntegerField(default=0, null=True)
    Datetime_create = models.DateTimeField(auto_now_add=True)
    Datetime_modified = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.second_price =  int(self.price - (self.price * (self.discouont/100)))
        return super(Products, self).save(*args, **kwargs)
    


    
    


class Comment(models.Model):
    PRODUCT_STARS = [
        ('1', 'یک ستاره'),
        ('2', 'دو ستاره'),
        ('3', 'سه ستاره'),
        ('4', 'چهار ستاره'),
        ('5', 'پنج ستاره '),
    ]
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    star = models.CharField(max_length=100 ,null=True, choices=PRODUCT_STARS)
    text = models.TextField(null=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
