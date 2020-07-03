from django.urls import path
from applications.shop.views import shopping_cart, home, product

urlpatterns = [
    path('', home.home, name='home'),
    path('shopping_cart/', shopping_cart.shopping_cart, name='shopping_cart')
]