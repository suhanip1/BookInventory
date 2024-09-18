from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    path('', inventory_view, name='inventory'),
    path('inventory/', inventory_list_create, name='inventory_list_create'), 
    path('inventory/<int:pk>/', inventory_delete, name='inventory_delete'), 
    path('inventory/export/csv/', export_books_csv, name='export_books_csv'),
]
