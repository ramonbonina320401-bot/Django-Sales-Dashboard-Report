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
    path('product/create/', views.product_create, name='product_create'),
    path('product/<int:pk>/update/', views.product_update, name='product_update'),
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),
    
    # Sales Data CRUD
    path('salesdata/create/', views.salesdata_create, name='salesdata_create'),
    path('salesdata/<int:pk>/update/', views.salesdata_update, name='salesdata_update'),
    path('salesdata/<int:pk>/delete/', views.salesdata_delete, name='salesdata_delete'),
]