from django.db import models
from apps.base.models import BaseModel
from mptt.models import TreeForeignKey, MPTTModel
from ckeditor.fields import RichTextField
from datetime import timedelta
from django.utils import timezone
from decimal import Decimal

# Create your models here.

class Category(MPTTModel, BaseModel):
    title = models.CharField(max_length=255, verbose_name='title')
    slug = models.SlugField()
    icon = models.TextField(null=True, blank=True, verbose_name='Icon')
    photo = models.ImageField(upload_to='category_photo/', null=True, blank=True, verbose_name='Category photo')
    parent = TreeForeignKey('self', on_delete = models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self) -> str:
        return self.title
    
    
class Banner(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Title')
    banner = models.ImageField(upload_to='banner/')
    body = RichTextField(verbose_name='Body')
    url = models.URLField(verbose_name='Link')
    

    def __str__(self) -> str:
        return self.title

class Servises(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Title')
    desc = models.CharField(max_length=255, verbose_name='Description')
    icon = models.FileField(upload_to='servises_icon/', verbose_name='Servises_icon')

    def __str__(self) -> str:
        return self.title
    

class Advertising(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Title')
    body = RichTextField(verbose_name='Body')
    link = models.URLField(verbose_name='Link')
    is_active = models.BooleanField(default=False, verbose_name='is_active')
    start_time = models.DateTimeField(null=True, blank=True, verbose_name='Start time')
    duration = models.PositiveIntegerField(help_text='Duration in hours', verbose_name='duration')

    @property
    def time_remaining(self):
        if self.is_active and self.start_time:
            end_time = self.start_time + timedelta(hours=self.duration)
            remaining_time = end_time - timezone.now()
            if remaining_time.total_seconds() > 0:
                return remaining_time
            else:
                self.is_active = False
                self.save
                return timedelta(0)
        return None


class Brand(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Brand name')
    logo = models.ImageField(upload_to='brand/', verbose_name='Brand logo')

    def __str__(self) -> str:
        return self.name
    

class Color(BaseModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    

class Size(BaseModel):
    name = models.CharField(max_length=100, verbose_name='Size')

    def __str__(self) -> str:
        return self.name


class Product(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Product name')
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, related_name='brand')
    category = models.ManyToManyField('Category')
    short_desc = models.TextField(verbose_name='Short description')
    description = models.TextField(verbose_name='Full description')
    sku = models.CharField(max_length=100, unique=True, verbose_name='SKU')
    discount = models.IntegerField(max_length=5, verbose_name='Discount (%)', null=True, blank=True)
    sales_count = models.PositiveIntegerField(default=0, verbose_name='Sales count')

    def __str__(self) -> str:
        return self.title
    
    def is_new(self):
        return (timezone.now() - self.create_at).days <= 5
    
    def is_hot(self):
        return self.discount and self.discount >= 50
    
    def is_best_sell(self):
        return self.sales_count >= 100


class ProductImage(BaseModel):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Product', related_name='images')
    color = models.ForeignKey('Color', on_delete=models.CASCADE, verbose_name='Color')
    image = models.ImageField(upload_to='product/', verbose_name='Product Image')
    hover_image = models.ImageField(upload_to='product/hover_image/', verbose_name='Hover Image')


class ProductSize(BaseModel):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Product', related_name='size')
    size = models.ForeignKey('Size', on_delete=models.CASCADE, verbose_name='Size')
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Price')
    availability = models.IntegerField(verbose_name='Availability')
    color = models.ForeignKey('Color', on_delete=models.CASCADE, verbose_name='Color')
        
    def get_discounted_price(self):
        price = self.price
        if self.product.discount:
            discounted_price = price * (Decimal(1) - Decimal(self.product.discount) / Decimal(100))
            return discounted_price.quantize(Decimal("0.01"), rounding="ROUND_HALF_UP")
        return price




class AdditionalInfo(BaseModel):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    key = models.CharField(max_length=100, verbose_name='Key')
    value = models.CharField(max_length=100, verbose_name='Value')

    def __str__(self) -> str:
        return f"{self.key}, {self.value}"
    

class Review(BaseModel):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    user = models.ForeignKey('accaunts.User', on_delete=models.CASCADE)
    rating = models.IntegerField(verbose_name='Rating')
    review = models.TextField(verbose_name='Review')
