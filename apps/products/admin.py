from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from apps.products.models import (
    Category,
    Banner,
    Servises,
    Advertising,
    Brand,
    Color,
    Size,
    Product,
    ProductImage,
    ProductSize,
    AdditionalInfo,
    Review
)
# Register your models here.

class BannerAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Banner
        fields = '__all__'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_at', 'update_at')
    search_fields = ('title',)
    list_filter = ('create_at', 'update_at')
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 10

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    form = BannerAdminForm 
    list_display = ('title', 'create_at', 'update_at')
    search_fields = ('title',)
    list_filter = ('create_at', 'update_at')
    list_per_page = 10

@admin.register(Servises)
class ServisesAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_at', 'update_at')
    search_fields = ('title',)
    list_filter = ('create_at', 'update_at')
    list_per_page = 10

@admin.register(Advertising)
class AdvertisingAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_at', 'update_at')
    search_fields = ('title',)
    list_filter = ('create_at', 'update_at')
    list_per_page = 10

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_at', 'update_at')
    search_fields = ('name',)
    list_filter = ('create_at', 'update_at')

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_at', 'update_at')
    search_fields = ('name',)
    list_filter = ('create_at', 'update_at')

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_at', 'update_at')
    search_fields = ('name',)
    list_filter = ('create_at', 'update_at')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'create_at')
    search_fields = ('product', 'user', 'rating')
    list_filter = ('create_at', 'rating')
    list_per_page = 10

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3

class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 3

class AdditionalInfoInline(admin.TabularInline):
    model = AdditionalInfo
    extra = 3

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'sku')
    search_fields = ('title', 'sku')
    list_filter = ('create_at', 'update_at')
    list_per_page = 10
    inlines = [ProductImageInline, ProductSizeInline, AdditionalInfoInline]