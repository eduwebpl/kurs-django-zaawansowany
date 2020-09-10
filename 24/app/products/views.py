from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product


class ProductListView(ListView):
    queryset = Product.objects.all()
