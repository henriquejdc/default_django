from django.urls import path
from applications.shop.views.home import *
from applications.product.urls.urls import urlpatterns

urlpatterns += [
    path('', home, name='home')
]