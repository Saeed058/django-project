from django.shortcuts import render
from django.views.generic import ListView,  TemplateView
from django.db.models import Q
from .models import Product



class SearchResultsView(ListView):
    model = Product
    template_name = 'search/search-product.html'
    context_object_name = 'products'


    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
           products=Product.objects.filter(Q(name__icontains=query) | Q(title__icontains=query) | Q(saleprice__icontains=query)).order_by("created_at")
           return products
        
    