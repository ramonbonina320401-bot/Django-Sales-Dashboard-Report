from django.shortcuts import render

# Create your views here.

def sales_report(request):
    return render(request, 'dashboard/sales.html', {'active_page': 'sales'})

def market_share(request):
    return render(request, 'dashboard/market.html', {'active_page': 'market'})

def raw_data(request):
    return render(request, 'dashboard/data.html', {'active_page': 'data'})

def model_eval(request):
    return render(request, 'dashboard/eval.html', {'active_page': 'eval'})