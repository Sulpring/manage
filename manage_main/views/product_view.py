from django.shortcuts import render, get_object_or_404, redirect
from manage_main.models import User

def product_list_showing_view(request):
    return render(request, 'products/product_list.html')
