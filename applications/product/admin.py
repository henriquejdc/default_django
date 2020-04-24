from django.contrib import admin
from .models import ImageProduct, Product, Price, Sku, Category, Department, Brand, Stock


@admin.register(ImageProduct)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    pass


@admin.register(Sku)
class SkuAdmin(admin.ModelAdmin):
    list_display = ('product', 'name', 'stock', 'price')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    pass


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass

