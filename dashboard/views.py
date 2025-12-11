from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Sum, Count
from django.contrib.auth.decorators import login_required
from .models import Product, SalesData
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

def sales_report(request):
    """Sales Report with NumPy calculations, statistics, and Matplotlib visualizations"""
    
    filter_product = request.GET.get('filter', 'all')
    
    # Get sales data
    if filter_product != 'all':
        sales_qs = SalesData.objects.filter(product__category=filter_product)
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
    }
    
    return render(request, 'dashboard/sales.html', context)


def market_share(request):
    """Market Share visualization showing product performance"""
    
    # Get sales by product
    product_sales = Product.objects.annotate(
        total_sales=Sum('sales__revenue'),
        units_sold=Sum('sales__quantity')
    ).order_by('-total_sales')
    
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
        'total_revenue': total_revenue,
    }
    
    return render(request, 'dashboard/market.html', context)


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
def product_list(request):
    """List all products with search, filter, and sort"""
    products = Product.objects.all()
    
    # Search functionality
    search = request.GET.get('search', '')
    if search:
        products = products.filter(name__icontains=search)
    
    # Filter by category
    category = request.GET.get('category', '')
    if category:
        products = products.filter(category=category)
    
    # Sort functionality
    sort_by = request.GET.get('sort', 'name')
    products = products.order_by(sort_by)
    
    # Calculate profit margin for each product
    products_with_margin = []
    for product in products:
        margin = ((product.price - product.cost) / product.price * 100) if product.price > 0 else 0
        sales_count = product.sales.count()
        total_revenue = sum(s.revenue for s in product.sales.all())
        products_with_margin.append({
            'product': product,
            'margin': f'{margin:.1f}',
            'sales_count': sales_count,
            'total_revenue': total_revenue,
        })
    
    # Pagination
    paginator = Paginator(products_with_margin, 10)
    page = request.GET.get('page', 1)
    page_obj = paginator.get_page(page)
    
    # Get all categories for filter
    categories = Product.objects.values_list('category', flat=True).distinct()
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'search': search,
        'category': category,
        'sort_by': sort_by,
        'active_page': 'products',
    }
    return render(request, 'dashboard/product_list.html', context)


@login_required(login_url='login')
def product_create(request):
    """Create a new product"""
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'Product "{product.name}" created successfully!')
            return redirect('product_list')
    else:
        form = ProductForm()
    
    return render(request, 'dashboard/product_form.html', {
        'form': form,
        'title': 'Add New Product',
        'button_text': 'Create Product',
        'is_create': True,
    })


@login_required(login_url='login')
def product_edit(request, pk):
    """Edit an existing product"""
    product = Product.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Product "{product.name}" updated successfully!')
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    
    # Show sales history
    sales_history = product.sales.all().order_by('-date')[:10]
    
    return render(request, 'dashboard/product_form.html', {
        'form': form,
        'product': product,
        'sales_history': sales_history,
        'title': f'Edit Product: {product.name}',
        'button_text': 'Update Product',
        'is_create': False,
    })


@login_required(login_url='login')
def product_delete(request, pk):
    """Delete a product"""
    product = Product.objects.get(pk=pk)
    sales_count = product.sales.count()
    
    if request.method == 'POST':
        delete_sales = request.POST.get('delete_sales') == 'on'
        
        if delete_sales and sales_count > 0:
            product.sales.all().delete()
        
        product_name = product.name
        product.delete()
        
        messages.success(request, f'Product "{product_name}" deleted successfully!')
        return redirect('product_list')
    
    return render(request, 'dashboard/product_confirm_delete.html', {
        'product': product,
        'sales_count': sales_count,
    })


# ============================================================================
# SALES DATA CRUD OPERATIONS
# ============================================================================

@login_required(login_url='login')
def sales_list(request):
    """List all sales with advanced filtering"""
    sales = SalesData.objects.select_related('product').all()
    
    # Search functionality
    search = request.GET.get('search', '')
    if search:
        sales = sales.filter(product__name__icontains=search)
    
    # Filter by category
    category = request.GET.get('category', '')
    if category:
        sales = sales.filter(product__category=category)
    
    # Filter by date range
    from_date = request.GET.get('from_date', '')
    to_date = request.GET.get('to_date', '')
    if from_date:
        sales = sales.filter(date__gte=from_date)
    if to_date:
        sales = sales.filter(date__lte=to_date)
    
    # Filter by minimum profit
    min_profit = request.GET.get('min_profit', '')
    if min_profit:
        try:
            min_profit_val = float(min_profit)
            sales = sales.filter(profit__gte=min_profit_val)
        except ValueError:
            pass
    
    # Sort
    sales = sales.order_by('-date')
    
    # Calculate totals
    total_revenue = sum(s.revenue for s in sales)
    total_profit = sum(s.profit for s in sales)
    avg_margin = (total_profit / total_revenue * 100) if total_revenue > 0 else 0
    
    # Pagination
    paginator = Paginator(sales, 25)
    page = request.GET.get('page', 1)
    page_obj = paginator.get_page(page)
    
    # Get categories for filter
    categories = Product.objects.values_list('category', flat=True).distinct()
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'search': search,
        'category': category,
        'from_date': from_date,
        'to_date': to_date,
        'min_profit': min_profit,
        'total_revenue': total_revenue,
        'total_profit': total_profit,
        'avg_margin': f'{avg_margin:.1f}',
        'active_page': 'sales',
    }
    return render(request, 'dashboard/sales_list.html', context)


@login_required(login_url='login')
def sales_create(request):
    """Create a new sale"""
    if request.method == 'POST':
        form = SalesDataForm(request.POST)
        if form.is_valid():
            sale = form.save()
            messages.success(request, f'Sale recorded successfully! Profit: ${sale.profit:.2f}')
            return redirect('sales_list')
    else:
        form = SalesDataForm()
    
    # Get products for the form
    products = Product.objects.all()
    
    return render(request, 'dashboard/sales_form.html', {
        'form': form,
        'products': products,
        'title': 'Record New Sale',
        'button_text': 'Record Sale',
        'is_create': True,
    })


@login_required(login_url='login')
def sales_edit(request, pk):
    """Edit an existing sale"""
    sale = SalesData.objects.get(pk=pk)
    old_profit = sale.profit
    
    if request.method == 'POST':
        form = SalesDataForm(request.POST, instance=sale)
        if form.is_valid():
            updated_sale = form.save()
            profit_diff = updated_sale.profit - old_profit
            
            if profit_diff >= 0:
                messages.success(
                    request,
                    f'Sale updated! Profit change: +${profit_diff:.2f} '
                    f'(New profit: ${updated_sale.profit:.2f})'
                )
            else:
                messages.warning(
                    request,
                    f'Sale updated! Profit change: ${profit_diff:.2f} '
                    f'(New profit: ${updated_sale.profit:.2f})'
                )
            return redirect('sales_list')
    else:
        form = SalesDataForm(instance=sale)
    
    # Get products
    products = Product.objects.all()
    
    return render(request, 'dashboard/sales_form.html', {
        'form': form,
        'sale': sale,
        'products': products,
        'title': f'Edit Sale: {sale.product.name}',
        'button_text': 'Update Sale',
        'is_create': False,
    })


@login_required(login_url='login')
def sales_delete(request, pk):
    """Delete a sale"""
    sale = SalesData.objects.get(pk=pk)
    lost_profit = sale.profit
    
    if request.method == 'POST':
        sale.delete()
        
        messages.success(
            request,
            f'Sale deleted. Lost profit: ${lost_profit:.2f}'
        )
        return redirect('sales_list')
    
    return render(request, 'dashboard/sales_confirm_delete.html', {
        'sale': sale,
    })


# ============================================================================
# API ENDPOINTS
# ============================================================================

@login_required(login_url='login')
def api_product_detail(request, pk):
    """API endpoint to fetch product details for AJAX calls"""
    try:
        product = Product.objects.get(pk=pk)
        return JsonResponse({
            'id': product.id,
            'name': product.name,
            'category': product.category,
            'price': float(product.price),
            'cost': float(product.cost),
        })
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)
