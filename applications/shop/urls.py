from django.urls import path
from applications.shop.views import shopping_cart, home, product

urlpatterns = [
    path('', home.home, name='home'),
    path('shopping_cart/', shopping_cart.shopping_cart, name='shopping_cart'),
    path('add_to_cart/', shopping_cart.add_to_cart, name='add_to_cart')
]