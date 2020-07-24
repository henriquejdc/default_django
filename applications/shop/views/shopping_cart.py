from django.shortcuts import render
from ..models import ShoppingCart, ShoppingTemporaryCart


def shopping_cart(request, template='shop/checkout/shopping_cart.html'):
    ctx = {}
    if ShoppingCart.objects.filter(user__user_id=request.user.id).exists():
        ctx['carrinho'] = ShoppingCart.objects.get(user=request.user)

    return render(request, template, ctx)


def add_to_cart(request):
    print(request.POST)
    return render(request, template_name='index.html')