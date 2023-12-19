from django.contrib import admin
from .models import *

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'products', 'count']




@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'product',  'order']