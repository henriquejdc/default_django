from django.shortcuts import render
from applications.product.utils import display_featured
from applications.product.models import Department
from ..models import Banner


def home(request, template='index.html'):

    featured = display_featured()
    dep = Department.objects.filter(active=True)
    ctx = {
        "produtos": featured,
        "departments" : dep,
        'departments_all': Department.objects.all(),
        'banners': Banner.objects.filter(ativo=True)
    }
    return render(request, template, ctx)