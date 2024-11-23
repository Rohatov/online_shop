from django.urls import path
from apps.products.views import HomePageView, ProductsView, quick_view
app_name = 'products'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('product/<int:id>/', ProductsView.as_view(), name='product_detail'),
    path('quick-view/<int:id>/', quick_view, name='quick_view'),
]