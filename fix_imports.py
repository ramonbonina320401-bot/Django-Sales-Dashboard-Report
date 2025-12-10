with open('dashboard/views.py', 'r') as f:
    content = f.read()

# Find where the imports end
import_block = """from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Sum, Count
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Product, SalesData
from .forms import ProductForm, SalesDataForm
from .reports import SalesReport, MarketShareReport, PredictionReport
import numpy as np"""

# Find the old import block
old_import_block = """from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import Product, SalesData
from .reports import SalesReport, MarketShareReport, PredictionReport
import numpy as np"""

if old_import_block in content:
    print("Found old import block")
    content = content.replace(old_import_block, import_block, 1)
    print("Replaced with new import block")
    
    with open('dashboard/views.py', 'w') as f:
        f.write(content)
    
    print("File updated successfully")
else:
    print("Old import block not found - checking what we have:")
    lines = content.split('\n')
    for i in range(min(10, len(lines))):
        print(f"Line {i+1}: {lines[i]}")
