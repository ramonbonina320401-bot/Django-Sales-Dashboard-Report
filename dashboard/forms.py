from django import forms
from django.core.exceptions import ValidationError
from .models import Product, SalesData
from datetime import datetime, timedelta


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'cost']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:border-teal-500',
                'placeholder': 'Product Name',
                'required': True
            }),
            'category': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:border-teal-500',
                'placeholder': 'Category (e.g., Electronics, Clothing)',
                'required': True
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:border-teal-500',
                'placeholder': 'Unit Price',
                'step': '0.01',
                'min': '0.01',
                'required': True
            }),
            'cost': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:border-teal-500',
                'placeholder': 'Unit Cost',
                'step': '0.01',
                'min': '0.01',
                'required': True
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        price = cleaned_data.get('price')
        cost = cleaned_data.get('cost')

        if price and cost:
            if cost >= price:
                raise ValidationError(
                    'Unit Cost must be less than Unit Price.'
                )

        return cleaned_data


class SalesDataForm(forms.ModelForm):
    class Meta:
        model = SalesData
        fields = ['product', 'date', 'quantity']
        widgets = {
            'product': forms.Select(attrs={
                'class': 'w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-lg text-white focus:outline-none focus:border-teal-500',
                'required': True
            }),
            'date': forms.DateInput(attrs={
                'class': 'w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-lg text-white focus:outline-none focus:border-teal-500',
                'type': 'date',
                'required': True
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-lg text-white focus:outline-none focus:border-teal-500',
                'placeholder': 'Quantity Sold',
                'min': '1',
                'step': '1',
                'required': True
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        product = cleaned_data.get('product')
        date = cleaned_data.get('date')
        quantity = cleaned_data.get('quantity')

        if quantity and quantity <= 0:
            raise ValidationError('Quantity must be greater than 0.')

        if date and date > datetime.now().date():
            raise ValidationError('Sale date cannot be in the future.')

        if product and date:
            # Check for duplicate entry (same product + date)
            existing = SalesData.objects.filter(product=product, date=date)
            if self.instance.pk:
                existing = existing.exclude(pk=self.instance.pk)
            if existing.exists():
                raise ValidationError(
                    f'A sales record for {product.name} on {date} already exists. '
                    'Edit the existing record instead.'
                )

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        product = instance.product
        
        # Auto-calculate revenue, cost, and profit
        instance.revenue = instance.quantity * product.price
        instance.cost = instance.quantity * product.cost
        instance.profit = instance.revenue - instance.cost
        
        if commit:
            instance.save()
        return instance
