from django.contrib import admin
from .models import Banner, Site


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    pass


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    pass
