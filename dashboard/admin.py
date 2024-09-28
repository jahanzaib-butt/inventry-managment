from django.contrib import admin
from .models import Product,Order

class productAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity')  # Corrected spelling of 'category'
    list_filter = ('category',)

# Register your models here.
admin.site.register(Product, productAdmin)
admin.site.register(Order)
