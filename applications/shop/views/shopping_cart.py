from django.shortcuts import render
from ..models import ShoppingCart, ShoppingTemporaryCart, ItemsCart
from applications.product.models import Sku


def shopping_cart(request, template='shop/checkout/shopping_cart.html'):
    ctx = {}
    if ShoppingCart.objects.filter(user__user_id=request.user.id).exists():
        ctx['carrinho'] = ShoppingCart.objects.get(user=request.user)
    elif ShoppingTemporaryCart.objects.filter(session=request.session).exists():
        ctx['carrinho'] = ShoppingCart.objects.get(session=request.session)

    return render(request, template, ctx)


def add_to_cart(request, id):

    cart = ShoppingTemporaryCart.objects.create(session=request.session)
    cart.save()
    items = ItemsCart(shopping_temp=cart)
    sku = Sku.objects.get(id=id)
    items.sku = sku
    items.save()
    product_document = {
        'title': sku.name,
        'price': sku.price.price
    }
    try:
        request.session['cart'][str(sku.id)] = product_document
    except:
        request.session['cart'] = {}

    print(request.session['cart'])
    return render(request, template_name='index.html')