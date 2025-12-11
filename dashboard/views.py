from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.db.models import Sum, Count
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, SalesData
from .forms import ProductForm, SalesDataForm
from .reports import SalesReport, MarketShareReport, PredictionReport
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from datetime import datetime, timedelta
from sklearn.metrics import confusion_matrix
import json

# Create your views here.

@login_required(login_url='login')
def sales_report(request):
    """Sales Report with NumPy calculations, statistics, and Matplotlib visualizations"""
    
    filter_product = request.GET.get('filter', 'all')
    
    # Get sales data
    if filter_product != 'all':
        # Filter by product name (case-insensitive)
        sales_qs = SalesData.objects.filter(product__name__iexact=filter_product)
    else:
        sales_qs = SalesData.objects.all()
    
    # NumPy calculations for total revenue, cost, and profit
    revenues = np.array([float(s.revenue) for s in sales_qs])
    costs = np.array([float(s.cost) for s in sales_qs])
    
    total_revenue = np.sum(revenues) if len(revenues) > 0 else 0
    total_cost = np.sum(costs) if len(costs) > 0 else 0
    gross_profit = total_revenue - total_cost
    profit_margin = (gross_profit / total_revenue * 100) if total_revenue > 0 else 0
    
    # Statistical Analysis (NumPy)
    mean_revenue = np.mean(revenues) if len(revenues) > 0 else 0
    median_revenue = np.median(revenues) if len(revenues) > 0 else 0
    std_revenue = np.std(revenues) if len(revenues) > 0 else 0
    
    # Get monthly data for trend chart and linear regression
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=365)
    
    monthly_data = {}
    month_numbers = []
    for month_offset in range(12):
        month_date = end_date - timedelta(days=30 * month_offset)
        month_start = month_date.replace(day=1)
        if month_offset == 0:
            month_end = end_date
        else:
            month_end = month_start + timedelta(days=30)
        
        month_sales = sales_qs.filter(date__gte=month_start, date__lte=month_end)
        month_revenue = sum([float(s.revenue) for s in month_sales])
        monthly_data[month_start.strftime('%b')] = month_revenue
        month_numbers.append(11 - month_offset)  # 0-11 for regression
    
    # Reverse to get chronological order
    monthly_labels = list(reversed(list(monthly_data.keys())))
    monthly_values = list(reversed(list(monthly_data.values())))
    month_numbers = list(reversed(month_numbers))
    
    # Linear Regression for Sales Prediction (Regression Model)
    from sklearn.linear_model import LinearRegression
    if len(monthly_values) >= 2:
        X = np.array(month_numbers).reshape(-1, 1)
        y = np.array(monthly_values)
        
        model = LinearRegression()
        model.fit(X, y)
        
        # Predict next 3 months
        future_months = np.array([12, 13, 14]).reshape(-1, 1)
        predictions = model.predict(future_months)
        
        predicted_value = float(predictions[0])
        slope = float(model.coef_[0])
        intercept = float(model.intercept_)
    else:
        predicted_value = 0
        slope = 0
        intercept = 0
    
    # Get distribution data (histogram bins)
    if len(revenues) > 0:
        hist, bin_edges = np.histogram(revenues, bins=10)
        distribution_labels = [f'₱{int(bin_edges[i])}-{int(bin_edges[i+1])}' for i in range(len(hist))]
        distribution_values = hist.tolist()
    else:
        distribution_labels = []
        distribution_values = []
    
    # Get all available products for filter buttons
    all_products = Product.objects.all().order_by('name')
    
    context = {
        'active_page': 'sales',
        'total_revenue': f'₱{total_revenue:,.2f}',
        'total_cost': f'₱{total_cost:,.2f}',
        'gross_profit': f'₱{gross_profit:,.2f}',
        'profit_margin': f'{profit_margin:.1f}%',
        'mean_revenue': f'₱{mean_revenue:,.2f}',
        'median_revenue': f'₱{median_revenue:,.2f}',
        'std_revenue': f'₱{std_revenue:,.2f}',
        'monthly_labels': json.dumps(monthly_labels),
        'monthly_values': json.dumps(monthly_values),
        'distribution_labels': json.dumps(distribution_labels),
        'distribution_values': json.dumps(distribution_values),
        'current_filter': filter_product,
        'total_records': f'{len(sales_qs):,}',
        'predicted_next_month': f'₱{predicted_value:,.2f}',
        'regression_slope': f'{slope:,.2f}',
        'regression_intercept': f'{intercept:,.2f}',
        'all_products': all_products,
    }
    
    return render(request, 'dashboard/sales.html', context)


@login_required(login_url='login')
def market_share(request):
    """Market Share visualization showing product performance"""
    
    # Get sales by product (only products with sales)
    product_sales = Product.objects.annotate(
        total_sales=Sum('sales__revenue'),
        units_sold=Sum('sales__quantity')
    ).filter(total_sales__gt=0).order_by('-total_sales')
    
    products = []
    revenues = []
    colors = ['#3b82f6', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6']
    
    # Calculate total revenue for percentage calculation
    total_revenue = 0
    for product in product_sales:
        if product.total_sales:
            total_revenue += float(product.total_sales)
    
    for idx, product in enumerate(product_sales):
        if product.total_sales:
            products.append(product.name)
            revenues.append(float(product.total_sales))
    
    # Calculate percentages
    total = sum(revenues) if revenues else 1
    percentages = [(rev / total * 100) for rev in revenues]
    
    context = {
        'active_page': 'market',
        'products': json.dumps(products),
        'revenues': json.dumps(revenues),
        'percentages': json.dumps(percentages),
        'colors': json.dumps(colors[:len(products)]),
        'product_data': product_sales,
        'total_revenue': total_revenue if total_revenue > 0 else 1,  # Prevent division by zero
    }
    
    return render(request, 'dashboard/market.html', context)


@login_required(login_url='login')
def raw_data(request):
    """Raw Data Preview with SQL database integration"""
    
    # Get all sales data with related product info (SQL JOIN)
    sales_data = SalesData.objects.select_related('product').order_by('-date')[:100]
    
    # Get summary statistics
    total_records = SalesData.objects.count()
    total_products = Product.objects.count()
    
    context = {
        'active_page': 'data',
        'sales_data': sales_data,
        'total_records': total_records,
        'total_products': total_products,
    }
    
    return render(request, 'dashboard/data.html', context)


@login_required(login_url='login')
def export_csv(request):
    """Export sales data to CSV file"""
    import csv
    from django.http import HttpResponse
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="sales_data.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['ID', 'Date', 'Product', 'Category', 'Quantity', 'Revenue', 'Cost', 'Profit'])
    
    sales_data = SalesData.objects.select_related('product').order_by('-date')
    for sale in sales_data:
        writer.writerow([
            sale.id,
            sale.date,
            sale.product.name,
            sale.product.category,
            sale.quantity,
            sale.revenue,
            sale.cost,
            sale.profit,
        ])
    
    return response


@login_required(login_url='login')
def export_json(request):
    """Export sales data to JSON file (JSON Handling Demonstration)"""
    from django.http import HttpResponse
    
    # Fetch sales data
    sales_data = SalesData.objects.select_related('product').order_by('-date')[:100]
    
    # Create Python dictionary structure
    data = {
        'export_date': datetime.now().isoformat(),
        'total_records': SalesData.objects.count(),
        'sales': []
    }
    
    # Serialize data to JSON-compatible format
    for sale in sales_data:
        data['sales'].append({
            'id': sale.id,
            'date': sale.date.isoformat(),
            'product': {
                'name': sale.product.name,
                'category': sale.product.category,
                'price': float(sale.product.price),
            },
            'quantity': sale.quantity,
            'revenue': float(sale.revenue),
            'cost': float(sale.cost),
            'profit': float(sale.profit),
        })
    
    # Use json.dumps() to serialize Python object to JSON string
    json_string = json.dumps(data, indent=2)
    
    response = HttpResponse(json_string, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="sales_data.json"'
    
    return response


@login_required(login_url='login')
def model_eval(request):
    """Model Evaluation with confusion matrix for sales predictions"""
    
    # Get recent sales data
    sales = SalesData.objects.order_by('-date')[:200]
    
    if len(sales) > 1:
        # Create a simple prediction model based on historical average
        revenues = [float(s.revenue) for s in sales]
        avg_revenue = np.mean(revenues)
        
        # Actual: 1 if revenue increased from previous day, 0 otherwise
        actual = []
        # Predicted: 1 if revenue above average, 0 otherwise
        predicted = []
        
        for i in range(1, len(sales)):
            current_rev = float(sales[i-1].revenue)
            previous_rev = float(sales[i].revenue)
            
            # Actual: did revenue increase?
            actual.append(1 if current_rev > previous_rev else 0)
            
            # Predicted: is revenue above average?
            predicted.append(1 if current_rev > avg_revenue else 0)
        
        # Calculate confusion matrix
        cm = confusion_matrix(actual, predicted)
        
        # Extract values
        tn, fp, fn, tp = cm.ravel() if cm.size == 4 else (0, 0, 0, 0)
        
        # Calculate metrics
        accuracy = (tp + tn) / (tp + tn + fp + fn) if (tp + tn + fp + fn) > 0 else 0
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0
        f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
        
    else:
        tn, fp, fn, tp = 0, 0, 0, 0
        accuracy = precision = recall = f1_score = 0
    
    context = {
        'active_page': 'eval',
        'tn': tn,
        'fp': fp,
        'fn': fn,
        'tp': tp,
        'accuracy': f'{accuracy * 100:.1f}',
        'precision': f'{precision * 100:.1f}',
        'recall': f'{recall * 100:.1f}',
        'f1_score': f'{f1_score * 100:.1f}',
    }
    
    return render(request, 'dashboard/eval.html', context)


# ============================================================================
# PRODUCT CRUD OPERATIONS
# ============================================================================

@login_required(login_url='login')
def product_create(request):
    """Create a new product"""
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'Product "{product.name}" created successfully!')
            return redirect('sales')
        else:
            messages.error(request, 'Error creating product. Please check the form.')
    else:
        form = ProductForm()
    
    context = {
        'form': form,
        'action': 'Create',
    }
    return render(request, 'dashboard/product_form.html', context)


@login_required(login_url='login')
def product_update(request, pk):
    """Update an existing product"""
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'Product "{product.name}" updated successfully!')
            return redirect('sales')
        else:
            messages.error(request, 'Error updating product. Please check the form.')
    else:
        form = ProductForm(instance=product)
    
    context = {
        'form': form,
        'product': product,
        'action': 'Update',
    }
    return render(request, 'dashboard/product_form.html', context)


@login_required(login_url='login')
def product_delete(request, pk):
    """Delete a product"""
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        product_name = product.name
        product.delete()
        messages.success(request, f'Product "{product_name}" deleted successfully!')
        return redirect('sales')
    
    context = {
        'product': product,
    }
    return render(request, 'dashboard/product_confirm_delete.html', context)


# ============================================================================
# SALES DATA CRUD OPERATIONS
# ============================================================================

@login_required(login_url='login')
def salesdata_create(request):
    """Create a new sales record"""
    if request.method == 'POST':
        form = SalesDataForm(request.POST)
        if form.is_valid():
            sales = form.save()
            messages.success(request, 'Sales record created successfully!')
            return redirect('data')
        else:
            messages.error(request, 'Error creating sales record. Please check the form.')
    else:
        form = SalesDataForm()
    
    context = {
        'form': form,
        'action': 'Create',
    }
    return render(request, 'dashboard/salesdata_form.html', context)


@login_required(login_url='login')
def salesdata_update(request, pk):
    """Update an existing sales record"""
    salesdata = get_object_or_404(SalesData, pk=pk)
    
    if request.method == 'POST':
        form = SalesDataForm(request.POST, instance=salesdata)
        if form.is_valid():
            sales = form.save()
            messages.success(request, 'Sales record updated successfully!')
            return redirect('data')
        else:
            messages.error(request, 'Error updating sales record. Please check the form.')
    else:
        form = SalesDataForm(instance=salesdata)
    
    context = {
        'form': form,
        'salesdata': salesdata,
        'action': 'Update',
    }
    return render(request, 'dashboard/salesdata_form.html', context)


@login_required(login_url='login')
def salesdata_delete(request, pk):
    """Delete a sales record"""
    salesdata = get_object_or_404(SalesData, pk=pk)
    
    if request.method == 'POST':
        salesdata.delete()
        messages.success(request, 'Sales record deleted successfully!')
        return redirect('data')
    
    context = {
        'salesdata': salesdata,
    }
    return render(request, 'dashboard/salesdata_confirm_delete.html', context)