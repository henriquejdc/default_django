from django.urls import path
from applications.shop.views.home import *

urlpatterns = [
    path('', home, name='home')
]