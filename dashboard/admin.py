from django.contrib import admin
from .models import Product, SalesData

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'cost']
    list_filter = ['category']
    search_fields = ['name', 'category']


@admin.register(SalesData)
class SalesDataAdmin(admin.ModelAdmin):
    list_display = ['product', 'date', 'quantity', 'revenue', 'profit']
    list_filter = ['date', 'product__category']
    search_fields = ['product__name']
    date_hierarchy = 'date'
