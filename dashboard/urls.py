from django.urls import path
from . import views

urlpatterns = [
    path('', views.sales_report, name='sales'),         # Button 1 (Default)
    path('market/', views.market_share, name='market'), # Button 2
    path('data/', views.raw_data, name='data'),         # Button 3
    path('eval/', views.model_eval, name='eval'),       # Button 4
    path('export-csv/', views.export_csv, name='export_csv'), # Export CSV
    path('export-json/', views.export_json, name='export_json'), # Export JSON
]