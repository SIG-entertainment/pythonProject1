from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from datetime import datetime

class ProductsList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'products.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = 'Распродажа НИКОГДА!'
        return context
# Create your views here.
class PoductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'
