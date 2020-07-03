from django.db import models


class MethodPayment(models.Model):
    name = models.CharField(verbose_name='Metodo de pagamento', max_length=200)


class AffiliationsPayment(models.Model):
    method_payment = models.ForeignKey(MethodPayment, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Empresa financeira', max_length=200)