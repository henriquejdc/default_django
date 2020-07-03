from django.db import models


class ShippingCompany(models.Model):
    name = models.CharField(verbose_name='Nome da transportadora', max_length=200)