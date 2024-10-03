from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Product
from django.http import JsonResponse
from django.db.models import Q

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'products/register.html', {'form': form})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def search_products(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(Q(brand__icontains=query) | Q(model__icontains=query))
    return JsonResponse(list(products.values()), safe=False)