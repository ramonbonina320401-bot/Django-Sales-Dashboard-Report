from django import forms
from django.core.exceptions import ValidationError
from .models import Product, SalesData


class ProductForm(forms.ModelForm):
    """Form for creating and editing products"""
    
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'cost']
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
                'placeholder': 'Enter selling price',
                'step': '0.01',
                'min': '0'
            }),
            'cost': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-lg text-white focus:outline-none focus:border-teal-500 focus:ring-1 focus:ring-teal-500',
                'placeholder': 'Enter cost price',
                'step': '0.01',
                'min': '0'
            }),
        }
        labels = {
            'name': 'Product Name',
            'category': 'Category',
            'price': 'Selling Price (₱)',
            'cost': 'Cost Price (₱)',
        }
    
    def clean_name(self):
        """Validate that product name is unique (case-insensitive)"""
        name = self.cleaned_data.get('name', '').strip().title()
        
        # Check for duplicates (excluding current instance if updating)
        qs = Product.objects.filter(name__iexact=name)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        
        if qs.exists():
            raise ValidationError(f'A product named "{name}" already exists. Please use a different name.')
        
        return name


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
