from django.contrib import admin
from .models import product

class productAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity')  # Corrected spelling of 'category'
    list_filter = ('category',)

# Register your models here.
admin.site.register(product, productAdmin)