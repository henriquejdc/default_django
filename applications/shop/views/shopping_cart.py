from django.shortcuts import render


def shopping_cart(request, template='shop/checkout/shopping_cart.html'):
    return render(request, template)