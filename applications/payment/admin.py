from django.contrib import admin
from .models import MethodPayment, AffiliationsPayment


@admin.register(MethodPayment)
class MethodPaymentAdmin(admin.ModelAdmin):
    pass


@admin.register(AffiliationsPayment)
class AffiliationsPaymentAdmin(admin.ModelAdmin):
    pass
