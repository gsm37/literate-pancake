
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='sales-home'),
    path('about/', views.about, name='sales-about'),
    path('Inventory/', views.inventory, name='sales-inventory'),
]