from django import forms
from .models import Product, SalesData


class ProductForm(forms.ModelForm):
    """Form for creating and editing products"""
    
    class Meta:
        model = Product
        fields = ['name', 'category', 'price']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-lg text-white focus:outline-none focus:border-teal-500 focus:ring-1 focus:ring-teal-500',
                'placeholder': 'Enter product name'
            }),
            'category': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-lg text-white focus:outline-none focus:border-teal-500 focus:ring-1 focus:ring-teal-500',
                'placeholder': 'Enter category (e.g., Electronics)'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-lg text-white focus:outline-none focus:border-teal-500 focus:ring-1 focus:ring-teal-500',
                'placeholder': 'Enter price',
                'step': '0.01',
                'min': '0'
            }),
        }
        labels = {
            'name': 'Product Name',
            'category': 'Category',
            'price': 'Price (₱)',
        }


class SalesDataForm(forms.ModelForm):
    """Form for creating and editing sales data"""
    
    class Meta:
        model = SalesData
        fields = ['product', 'quantity', 'revenue', 'cost', 'date']
        widgets = {
            'product': forms.Select(attrs={
                'class': 'w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-lg text-white focus:outline-none focus:border-teal-500 focus:ring-1 focus:ring-teal-500'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-lg text-white focus:outline-none focus:border-teal-500 focus:ring-1 focus:ring-teal-500',
                'placeholder': 'Enter quantity',
                'min': '1'
            }),
            'revenue': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-lg text-white focus:outline-none focus:border-teal-500 focus:ring-1 focus:ring-teal-500',
                'placeholder': 'Enter revenue',
                'step': '0.01',
                'min': '0'
            }),
            'cost': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-lg text-white focus:outline-none focus:border-teal-500 focus:ring-1 focus:ring-teal-500',
                'placeholder': 'Enter cost',
                'step': '0.01',
                'min': '0'
            }),
            'date': forms.DateInput(attrs={
                'class': 'w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-lg text-white focus:outline-none focus:border-teal-500 focus:ring-1 focus:ring-teal-500',
                'type': 'date'
            }),
        }
        labels = {
            'product': 'Product',
            'quantity': 'Quantity',
            'revenue': 'Revenue (₱)',
            'cost': 'Cost (₱)',
            'date': 'Sale Date',
        }
