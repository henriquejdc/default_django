from django.db import models
from faicon.fields import FAIconField
from applications.user.models import UserDetail, AddressUser
from applications.payment.models import AffiliationsPayment
from applications.shipping.models import ShippingCompany
from applications.product.models import Sku

class Banner(models.Model):
    name = models.CharField(verbose_name='Texto em destaque do banner', max_length=50)
    banner = models.ImageField(upload_to='media/')
    texto = models.TextField()
    ativo = models.BooleanField(default=False, verbose_name='O banner esta ativo?')

    def __str__(self):
        return "{}".format(self.name)


class Site(models.Model):
    nome_site = models.CharField(verbose_name='Nome do site caso nao tenha logo e para meta tag', max_length=50)
    icone = models.ImageField(verbose_name='Icone para metatag do site', upload_to='media/', blank=True)
    ativo = models.BooleanField(default=False, verbose_name='Essa informacao esta ativa?')
    icon = FAIconField(verbose_name='Icons prontos para uso',blank=True)

    def save(self, *args, **kwargs):
        if not self.icone and self.icon:
            self.icone = self.icon.icon
            super(Site, self).save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.nome_site)


class ItemsCart(models.Model):
    sku = models.ForeignKey(Sku, on_delete=models.CASCADE)
    time = models.TimeField(auto_now=True)


class ShoppingCart(models.Model):
    user = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    address = models.ForeignKey(AddressUser, on_delete=models.CASCADE)
    affiliation = models.ForeignKey(AffiliationsPayment, on_delete=models.CASCADE)
    shipping = models.ForeignKey(ShippingCompany, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    items = models.ForeignKey(ItemsCart, on_delete=models.CASCADE)


class ShoppingTemporaryCart(models.Model):
    time = models.TimeField(auto_now=True)
    session = models.CharField(max_length=200)
    items = models.ForeignKey(ItemsCart, on_delete=models.CASCADE)
