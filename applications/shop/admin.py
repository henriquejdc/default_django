from django.contrib import admin
from .models import Image, Product, Price

class ImageAdmin(admin.ModelAdmin):
    pass


class Productadmin(admin.ModelAdmin):
    pass


class Priceadmin(admin.ModelAdmin):
    pass

admin.site.register(Image, ImageAdmin)
admin.site.register(Product, Productadmin)
admin.site.register(Price, Priceadmin)