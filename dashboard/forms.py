from django import forms
from .models import Product,Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'quantity']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order  # Corrected: Use only one model
        fields = ['product', 'order_quantity']
