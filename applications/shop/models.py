from django.db import models


class Image(models.Model):
    name = models.CharField(name="Nome da imagem", max_length=200)
    image_url = models.ImageField(name="Caminho da imagem", upload_to="media/")

class Price(models.Model):
    name = models.CharField(name="Descricao do preco", max_length=200)
    price = models.DecimalField(name="Valor do preco", decimal_places=2, max_digits=2, blank=True, null=True)
    discount = models.DecimalField(name="Valor de desconto", decimal_places=2, max_digits=2, blank=True, null=True)


class Product(models.Model):
    name = models.CharField(name=("Nome do produto"), max_length=200)
    url_image = models.ForeignKey(Image, on_delete=models.CASCADE)
    price = models.ForeignKey(Price, on_delete=models.CASCADE)