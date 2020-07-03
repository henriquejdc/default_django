from ..models import Product, Department, Category, Sku, Brand
from django.shortcuts import get_object_or_404, render


def department_view(request,slug, classe='', template='shop/product/product_render.html'):
    products = Product.objects.filter(department__slug=slug)
    sku = Sku.objects.filter(product__in=products)
    dep = Department.objects.filter(slug=slug)
    category = Category.objects.filter(id__in=products.values_list('category', flat=True))
    brand = Brand.objects.filter(id__in=products.values_list('brand', flat=True))
    ctx = {
        'departments': dep,
        'produtos': sku,
        'categorys': category,
        'brands': brand,
        'departments_all': Department.objects.all()
    }

    return render(request, template, ctx)


def category_view(request,slug, classe='', template='product_render.html'):
    products = Product.objects.filter(category__slug=slug)
    sku = Sku.objects.filter(product__in=products)
    dep = Department.objects.filter(id__in=products.values_list('department', flat=True))
    category = Category.objects.filter(slug=slug)
    brand = Brand.objects.filter(id__in=products.values_list('brand', flat=True))
    ctx = {
        'departments': dep,
        'produtos': sku,
        'categorys': category,
        'brands': brand,
        'departments_all': Department.objects.all()
    }

    return render(request, template, ctx)

def brand_view(request,slug, classe='', template='product_render.html'):
    brand = Brand.objects.filter(slug=slug)
    products = Product.objects.filter(brand__in=brand)
    sku = Sku.objects.filter(product__in=products)
    dep = Department.objects.filter(id__in=products.values_list('department', flat=True))
    category = Category.objects.filter(id__in=products.values_list('category', flat=True))
    ctx = {
        'departments': dep,
        'produtos': sku,
        'categorys': category,
        'brands': brand,
        'departments_all': Department.objects.all()
    }
    return render(request, template, ctx)