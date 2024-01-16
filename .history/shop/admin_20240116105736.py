from django.contrib import admin
from .models import Client, Product, Order, OrderItem

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'address', 'registration_date')
    search_fields = ('name', 'email', 'phone_number')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'added_date')
    list_filter = ('added_date', 'price')
    search_fields = ('name',)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'total_amount', 'order_date')
    list_filter = ('order_date',)
    inlines = [OrderItemInline]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.save()
