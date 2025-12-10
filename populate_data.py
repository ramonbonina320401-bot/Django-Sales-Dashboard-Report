"""
Populate database with realistic sample data for the Sales Dashboard
Run this script with: python populate_data.py
"""

import os
import django
import random
from datetime import datetime, timedelta
from decimal import Decimal

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangowebapp.settings')
django.setup()

from dashboard.models import Product, SalesData

def clear_existing_data():
    """Clear existing products and sales data"""
    print("Clearing existing data...")
    SalesData.objects.all().delete()
    Product.objects.all().delete()
    print("✓ Data cleared")

def create_products():
    """Create sample products across different categories"""
    print("\nCreating products...")
    
    products_data = [
        {'name': 'Laptop', 'category': 'Electronics', 'price': 899.99, 'cost': 549.99},
        {'name': 'Mouse', 'category': 'Electronics', 'price': 29.99, 'cost': 15.99},
        {'name': 'Keyboard', 'category': 'Electronics', 'price': 79.99, 'cost': 45.99},
        {'name': 'Monitor', 'category': 'Electronics', 'price': 249.99, 'cost': 149.99},
        {'name': 'Headset', 'category': 'Electronics', 'price': 89.99, 'cost': 49.99},
    ]
    
    products = []
    for data in products_data:
        # Convert to Decimal
        data['price'] = Decimal(str(data['price']))
        data['cost'] = Decimal(str(data['cost']))
        
        product = Product.objects.create(**data)
        products.append(product)
        print(f"  ✓ Created: {product.name} ({product.category}) - ${product.price}")
    
    print(f"\n✓ Created {len(products)} products")
    return products

def create_sales_data(products):
    """Create realistic sales data over the past year"""
    print("\nCreating sales data...")
    
    # Generate sales for the past 12 months
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=365)
    
    sales_count = 0
    current_date = start_date
    
    # Create 3-8 sales per day on average
    while current_date <= end_date:
        # Random number of sales per day (0-12, weighted toward 3-8)
        num_sales = max(0, int(random.gauss(5, 3)))
        
        for _ in range(num_sales):
            product = random.choice(products)
            
            # Use product's price with some variation (±10%)
            price_variation = random.uniform(0.9, 1.1)
            revenue = Decimal(str(round(float(product.price) * price_variation, 2)))
            
            # Use product's cost with some variation (±10%)
            cost_variation = random.uniform(0.9, 1.1)
            cost = Decimal(str(round(float(product.cost) * cost_variation, 2)))
            
            # Profit is revenue - cost
            profit = revenue - cost
            
            # Quantity sold (1-5, weighted toward 1-2)
            quantity = max(1, int(random.gauss(1.5, 1)))
            
            # Create sale record
            SalesData.objects.create(
                product=product,
                date=current_date,
                revenue=revenue,
                cost=cost,
                profit=profit,
                quantity=quantity
            )
            sales_count += 1
        
        current_date += timedelta(days=1)
    
    print(f"✓ Created {sales_count} sales records over 365 days")
    
    # Print summary statistics
    total_revenue = sum(float(s.revenue) for s in SalesData.objects.all())
    total_profit = sum(float(s.profit) for s in SalesData.objects.all())
    
    print(f"\n📊 Summary Statistics:")
    print(f"  Total Revenue: ${total_revenue:,.2f}")
    print(f"  Total Profit: ${total_profit:,.2f}")
    print(f"  Profit Margin: {(total_profit/total_revenue*100):.1f}%")
    print(f"  Average Sales/Day: {sales_count/365:.1f}")

def main():
    """Main function to populate database"""
    print("=" * 60)
    print("  SALES DASHBOARD - DATA POPULATION SCRIPT")
    print("=" * 60)
    
    # Clear existing data
    clear_existing_data()
    
    # Create products
    products = create_products()
    
    # Create sales data
    create_sales_data(products)
    
    print("\n" + "=" * 60)
    print("  ✓ DATABASE POPULATED SUCCESSFULLY!")
    print("=" * 60)
    print("\nYou can now visit http://127.0.0.1:8000/ to view the dashboard")
    print("Login credentials: admin / admin123")

if __name__ == '__main__':
    main()
