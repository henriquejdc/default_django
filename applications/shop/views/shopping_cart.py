from django.shortcuts import render
from ..models import ShoppingCart, ShoppingTemporaryCart, ItemsCart
from applications.product.models import Sku


def shopping_cart(request, template='shop/checkout/shopping_cart.html'):
    ctx = {}
    ctx['carrinho'] = request.session['cart']

    return render(request, template, ctx)


def add_to_cart(request):
    cart = ShoppingTemporaryCart.objects.create(session=request.session)
    cart.save()
    items = ItemsCart(shopping_temp=cart)
    sku = Sku.objects.get(id=request.POST.get('produto'))
    items.sku = sku
    items.save()
    lista = request.session['cart']
    for item in lista:
        if item['sku'] == sku:
            item['quantity'] += 1
            item['sum'] += sku.price.price
            request.session['cart'] = lista
            return render(request, template_name='index.html')
    cart_item = {
        'sku': sku,
        'quantity': 1,
        'sum': sku.price.price
    }
    lista.append(cart_item)
    request.session['cart'] = lista
    return render(request, template_name='index.html')