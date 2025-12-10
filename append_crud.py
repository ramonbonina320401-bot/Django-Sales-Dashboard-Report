#!/usr/bin/env python
"""
Append CRUD functions to views.py
"""

crud_code = '''

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
'''

# Append to views.py
with open('dashboard/views.py', 'a') as f:
    f.write(crud_code)

print("CRUD code appended successfully")

# Verify
with open('dashboard/views.py', 'r') as f:
    content = f.read()
    if 'def product_list' in content:
        print("Verification: product_list found!")
    else:
        print("Verification: product_list NOT found!")
