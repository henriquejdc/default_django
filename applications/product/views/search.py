from ..models import *
from django.shortcuts import render, reverse
from django.contrib.postgres.search import TrigramSimilarity



def search(request, template='product_render.html'):
    products = Product.objects.annotate(
        similarity=TrigramSimilarity('name', request.GET.get('search')),
    ).filter(similarity__gt=0.9).order_by('-similarity')
    if not products:
        products = Product.objects.filter(name__icontains=request.GET.get('search'))
    sku = Sku.objects.filter(product__in=products)
    dep = Department.objects.filter(id__in=products.values_list('department', flat=True))
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