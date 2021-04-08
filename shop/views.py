from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.views.generic import DetailView, ListView
from .forms import ProductCommentForm
from .models import Product



class All_Products(ListView):
    model = Product
    context_object_name = 'product'
    template_name = 'shop/shop.html'
    
    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'
    
    def post(self, *args, **kwargs):
        """Adds review to product using the ProductCommentForm and productComment model)."""
        form = ProductCommentForm(self.request.POST)
        if form.is_valid():
            name_product = self.get_object()
            productcomment = form.instance
            productcomment.user = self.request.user
            productcomment.name_product = name_product
            productcomment.save()
            return redirect("shop:product_detail", pk=name_product.pk)
        return redirect("shop:product_detail", pk=self.get_object().pk)