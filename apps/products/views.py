from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView, DetailView
from .models import (
    Category, Banner, Servises, Advertising, Brand, 
    Product, Review, Color, Size
)
# Create your views here.

class HomePageView(View):
    def get(self, request):
        categorys = Category.objects.all()
        banners = Banner.objects.all()
        servises = Servises.objects.all()
        advertising = Advertising.objects.all()
        brands = Brand.objects.all()
        products = Product.objects.all()
        reviews = Review.objects.all()
        colors = Color.objects.all()
        size = Size.objects.all()
        context = {
            'category': categorys,
            'banners': banners,
            'servises': servises[:4],
            'advertising': advertising,
            'brand': brands,
            'products': products,
            'review': reviews,
            'color': colors,
            'size': size
        }
        return render(request, 'index-4.html', context)


class ProductsView(DetailView):
    model = Product
    template_name = 'detail.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        product_id = self.kwargs.get('id')
        return get_object_or_404(Product, id=product_id)
    
    
def quick_view(request, id):
    category = get_object_or_404(Category, id=id)
    products = category.objects.all()
    context = {
        'category':category,
        'products':products
    }
    return render(request, 'quick_view.html', context)
