from django.urls import *
from ..views.departments import department_view, category_view, brand_view
from ..views.search import search
from ..views.product import product_view

urlpatterns = [
    re_path(r'^department/(?P<slug>[-\w]+)/$', department_view, {}, 'department'),
    re_path(r'^category/(?P<slug>[-\w]+)/$', category_view, {}, 'category'),
    re_path(r'^product/(?P<slug>[-\w]+)/$', product_view, {}, 'product'),
    re_path(r'^brand/(?P<slug>[-\w]+)/$', brand_view, {}, 'brand'),
    path('search/', search, {}, 'search'),
]