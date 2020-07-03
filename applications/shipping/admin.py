from django.contrib import admin
from .models import ShippingCompany


@admin.register(ShippingCompany)
class ShippingCompanyAdmin(admin.ModelAdmin):
    pass
