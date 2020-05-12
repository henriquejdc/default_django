from django.db import models
from . import config
from django.contrib.sites.models import Site
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
import sys
from django.template.defaultfilters import slugify
import uuid
import os

class ImageProduct(models.Model):
    name = models.CharField(verbose_name="Nome da imagem", max_length=200, blank=True)
    img = models.ImageField(verbose_name="Caminho da imagem", upload_to="image")
    active = models.BooleanField(verbose_name=("Esta ativo?"), default=True)
    principal = models.BooleanField(verbose_name=("Imagem que vai aparecer na home"))

    def __str__(self):
        return "{}".format(self.name)

    def save(self):
        # Opening the uploaded image
        im = Image.open(self.img)

        output = BytesIO()

        # Resize/modify the image
        im = im.resize((260, 260))

        # after modifications, save it to the output
        im.save(output, format='PNG', quality=100)
        output.seek(0)

        # change the imagefield value to be the newley modifed image value
        self.img = InMemoryUploadedFile(output, 'ImageField', "%s.png" % self.img.name.split('.')[0], 'image/png',
                                        sys.getsizeof(output), None)

        self.name = "%s.%s" % (self.img.name, uuid.uuid4())
        super(ImageProduct, self).save()

class Price(models.Model):
    name = models.CharField(verbose_name="Descricao do preco", max_length=200)
    price = models.DecimalField(verbose_name="Valor do preco", decimal_places=2, max_digits=15)
    discount = models.DecimalField(verbose_name="Valor de desconto", decimal_places=2, max_digits=15, blank=True, null=True)
    active = models.BooleanField(verbose_name=("Esta ativo?"), default=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.price)

    def save(self, *args, **kwargs):
        self.name = "%s-%s" % (self.name, uuid.uuid4())
        super(Price, self).save(*args, **kwargs)

class Brand(models.Model):
    name = models.CharField(verbose_name=("Nome da Marca"), max_length=200)
    active = models.BooleanField(verbose_name=("Esta ativo?"), default=True)
    slug = models.SlugField(("Slug"), help_text=("URL"),blank=True)

    def __str__(self):
        return "{}".format(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Brand, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return "/brand/{}".format(self.slug)

class Department(models.Model):
    name = models.CharField(verbose_name=("Nome do departamento"), max_length=200)
    active = models.BooleanField(verbose_name=("Esta ativo?"), default=True)
    slug = models.SlugField(("Slug"), help_text=("URL"),blank=True)

    def __str__(self):
        return "{}".format(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Department, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return "/department/{}".format(self.slug)


class Category(models.Model):
    name = models.CharField(verbose_name=("Nome da categoria"), max_length=200)
    department = models.ForeignKey(Department,verbose_name=("Departamento da categoria"), on_delete=models.CASCADE)
    active = models.BooleanField(verbose_name=("Esta ativo?"), default=True)
    slug = models.SlugField(("Slug"), help_text=("URL"),blank=True)

    def __str__(self):
        return "{}".format(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return "/category/{}".format(self.slug)

class Product(models.Model):
    name = models.CharField(verbose_name=("Nome do produto"), max_length=200)
    category = models.ForeignKey(Category,verbose_name=("Categoria do produto"), on_delete=models.CASCADE)
    department = models.ForeignKey(Department, verbose_name=("Departamento do produto"),on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,verbose_name=("Marca do produto"), on_delete=models.CASCADE)
    active = models.BooleanField(verbose_name=("Esta ativo?"), default=True)
    slug = models.SlugField(("Slug"), help_text=("URL"),blank=True)

    def __str__(self):
        return "{}".format(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return "/product/{}".format(self.slug)

class Stock(models.Model):
    name = models.CharField(verbose_name=("Descricao do estoque"), max_length=200)
    quantity = models.IntegerField(verbose_name=("Quantidade do estoque"))
    active = models.BooleanField(verbose_name=("Esta ativo?"), default=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.quantity)

    def save(self, *args, **kwargs):
        self.name = "%s-%s" % (self.name, uuid.uuid4())
        super(Stock, self).save(*args, **kwargs)


class Sku(models.Model):
    name = models.CharField(verbose_name=("Nome do sku"), max_length=200)
    product = models.ForeignKey(Product,verbose_name=("Produto Pai"), on_delete=models.CASCADE)
    image = models.ForeignKey(ImageProduct, verbose_name=("Caminho da imagem do sku"), on_delete=models.CASCADE)
    price = models.ForeignKey(Price,verbose_name=("Preco do sku"), on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, verbose_name=("Quantidade em estoque"), on_delete=models.CASCADE)
    width = models.DecimalField(verbose_name=("Largura do sku"), decimal_places=4, max_digits=15)
    length = models.DecimalField(verbose_name=("Comprimento do sku"), decimal_places=4, max_digits=15)
    height = models.DecimalField(verbose_name=("Altura do sku"), decimal_places=4, max_digits=15)
    active = models.BooleanField(verbose_name=("Esta ativo?"), default=True)
    slug = models.SlugField(("Slug"), help_text=("URL"),blank=True)

    def __str__(self):
        return "{} - {}".format(self.product, self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Sku, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return "/product/{}".format(self.slug)


class Specification(models.Model):
    name = models.CharField(verbose_name='Nome para especificacao ex: Detalhes', max_length=200)
    text = models.TextField(verbose_name='Texto da especificacao')
    sku = models.ForeignKey(Sku, verbose_name='sku a ser vinculado', on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.name)