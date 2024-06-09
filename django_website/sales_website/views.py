from django.shortcuts import render
from django.http import HttpResponse
from .models import Inventory

inventory_items = Inventory.objects.all()

# Create your views here.
def home(request):
    context = {
        'page_title' : 'Home'
    }
    return render(request, 'sales_website/home.html', context)

def about(request):
    context = {
        'page_title' : 'About' 
    }
    return render(request, 'sales_website/about.html', context)

def inventory(request):
    context = {
        'page_title' : 'Inventory',
        'inventory_items' : inventory_items
    }
    return render(request, 'sales_website/inventory.html',context)