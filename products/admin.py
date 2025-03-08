from django.contrib import admin

from .models import Category, Product, Stock, SupplierProduct
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(SupplierProduct)
admin.site.register(Stock)
