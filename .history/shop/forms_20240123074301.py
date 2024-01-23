from django import forms
from .models import Client, Product, Order

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'image']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class OrderFilterForm(forms.Form):
    TIME_CHOICES = (
        ('week', 'Неделя'),
        ('month', 'Месяц'),
        ('year', 'Год'),
        ('all', 'Все время'),
    )
    time_period = forms.ChoiceField(choices=TIME_CHOICES, required=False)