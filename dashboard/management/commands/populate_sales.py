from django.core.management.base import BaseCommand
from dashboard.models import Product, SalesData
from datetime import datetime, timedelta
import random
from decimal import Decimal


class Command(BaseCommand):
    help = 'Populate database with sample sales data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        SalesData.objects.all().delete()
        Product.objects.all().delete()
        
        # Create products
        products_data = [
            {'name': 'Gaming Laptop Pro', 'category': 'laptop', 'price': Decimal('85000'), 'cost': Decimal('60000')},
            {'name': 'Wireless Mouse X', 'category': 'mouse', 'price': Decimal('1500'), 'cost': Decimal('800')},
            {'name': 'Mechanical Keyboard RGB', 'category': 'keyboard', 'price': Decimal('3500'), 'cost': Decimal('2000')},
            {'name': '4K Monitor Ultra', 'category': 'monitor', 'price': Decimal('25000'), 'cost': Decimal('18000')},
            {'name': 'Gaming Headset Pro', 'category': 'headset', 'price': Decimal('5000'), 'cost': Decimal('3000')},
        ]
        
        products = []
        for prod_data in products_data:
            product = Product.objects.create(**prod_data)
            products.append(product)
            self.stdout.write(self.style.SUCCESS(f'Created product: {product.name}'))
        
        # Generate sales data for the past 12 months
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=365)
        
        current_date = start_date
        sales_count = 0
        
        while current_date <= end_date:
            # Create random sales for each product
            for product in products:
                # Random number of sales per day (0-5)
                num_sales = random.randint(0, 5)
                
                for _ in range(num_sales):
                    quantity = random.randint(1, 10)
                    revenue = product.price * quantity
                    cost = product.cost * quantity
                    profit = revenue - cost
                    
                    SalesData.objects.create(
                        product=product,
                        date=current_date,
                        quantity=quantity,
                        revenue=revenue,
                        cost=cost,
                        profit=profit
                    )
                    sales_count += 1
            
            current_date += timedelta(days=1)
        
        self.stdout.write(self.style.SUCCESS(f'Successfully created {sales_count} sales records'))
