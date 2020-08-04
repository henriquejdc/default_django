from django.shortcuts import render
from applications.product.utils import display_featured
from applications.product.models import Department
from ..models import Banner, ShoppingCart, ShoppingTemporaryCart, Site
from importlib import import_module
from django.conf import settings
SessionStore = import_module(settings.SESSION_ENGINE).SessionStore


def home(request, template='index.html'):
    ctx = {}
    ctx['produtos'] = display_featured()
    ctx['dep'] = Department.objects.filter(active=True)
    sum = 0
    try:
        ctx['carrinho'] = request.session['cart']
        for i in ctx['carrinho']:
            sum += i.price.price
        ctx['sum'] = sum
    except KeyError:
        request.session['cart'] = list()
    ctx['departments_all'] = Department.objects.all()
    ctx['banners'] = Banner.objects.filter(ativo=True)
    ctx['logo'] = Site.objects.filter(ativo=True)

    return render(request, template, ctx)