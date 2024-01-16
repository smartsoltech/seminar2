from django.contrib import admin
from .models import Client, Order, Product
# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'address', 'registration_date')
    search_fields = ('name', 'email')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'quantity', 'added_date')
    list_filter = ('added_date', 'price')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'total_amount', 'order_date')
    list_filter = ('order_date',)
    filter_horizontal = ('products',)
