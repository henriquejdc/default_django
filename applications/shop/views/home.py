from django.shortcuts import render
from applications.product.utils import display_featured
from applications.product.models import Department
from ..models import Banner, ShoppingCart, ShoppingTemporaryCart, Site


def home(request, template='index.html'):
    ctx = {}
    ctx['produtos'] = display_featured()
    ctx['dep'] = Department.objects.filter(active=True)
    if ShoppingCart.objects.filter(user__user_id=request.user.id).exists():
        ctx['carrinho'] = ShoppingCart.objects.get(user=request.user)
    elif ShoppingTemporaryCart.objects.filter(session=request.session).exists():
        ctx['carrinho'] = ShoppingTemporaryCart.objects.get(session=request.session)
    ctx['departments_all'] = Department.objects.all()
    ctx['banners'] = Banner.objects.filter(ativo=True)
    ctx['logo'] = Site.objects.filter(ativo=True)

    return render(request, template, ctx)