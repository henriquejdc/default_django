from django.shortcuts import render
from ..models import ShoppingCart, ShoppingTemporaryCart, ItemsCart
from applications.product.models import Sku


def shopping_cart(request, template='shop/checkout/shopping_cart.html'):
    ctx = {}
    ctx['carrinho'] = request.session['cart']

    return render(request, template, ctx)


def add_to_cart(request, id):

    cart = ShoppingTemporaryCart.objects.create(session=request.session)
    cart.save()
    items = ItemsCart(shopping_temp=cart)
    sku = Sku.objects.get(id=id)
    items.sku = sku
    items.save()
    product = {
        'sku': sku,
        'quantity': 0
    }
    lista = request.session['cart']
    lista.append(sku)
    request.session['cart'] = lista
    return render(request, template_name='index.html')