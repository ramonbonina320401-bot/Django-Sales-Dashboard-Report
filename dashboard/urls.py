from django.urls import path
from . import views

urlpatterns = [
    path('', views.sales_report, name='sales'),         # Button 1 (Default)
    path('market/', views.market_share, name='market'), # Button 2
    path('data/', views.raw_data, name='data'),         # Button 3
    path('eval/', views.model_eval, name='eval'),       # Button 4
    path('export-csv/', views.export_csv, name='export_csv'), # Export CSV
    path('export-json/', views.export_json, name='export_json'), # Export JSON
    
    # Product CRUD
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),
    
    # Sales CRUD
    path('sales/', views.sales_list, name='sales_list'),
    path('sales/create/', views.sales_create, name='sales_create'),
    path('sales/<int:pk>/edit/', views.sales_edit, name='sales_edit'),
    path('sales/<int:pk>/delete/', views.sales_delete, name='sales_delete'),
    
    # API Endpoints
    path('api/product/<int:pk>/', views.api_product_detail, name='api_product_detail'),
]