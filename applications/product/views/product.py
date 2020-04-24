from ..models import Product, Department, Category, Sku, Brand
from django.shortcuts import get_object_or_404, render


def product_view(request, slug, template='product.html'):
    sku = Sku.objects.filter(slug=slug)
    product = Product.objects.filter(sku__in=sku)
    skus = Sku.objects.filter(product__in=product)
    dep = Department.objects.filter(slug=slug)
    category = Category.objects.filter(id__in=product.values_list('category', flat=True))
    brand = Brand.objects.filter(id__in=product.values_list('brand', flat=True))
    ctx = {
        'departments': dep,
        'product': product,
        'sku': sku,
        'variations': skus,
        'categorys': category,
        'brands': brand,
        'departments_all': Department.objects.all()
    }
    return render(request, template, ctx)