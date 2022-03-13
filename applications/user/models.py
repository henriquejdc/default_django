from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UsuarioManager(BaseUserManager):
    use_in_migration = True

    def _create_user(self,email, password, **extra_fields):
        if not email:
            raise ValueError("o e-mail e obrigatorio")
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser = True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff = True')

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    fone = models.CharField('Telefone', max_length=15)
    is_staff = models.BooleanField('Membro da equipe', default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'fone']

    def __str__(self):
        return self.email

    objects = UsuarioManager()


class UserDetail(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    cpf_cnpj = models.CharField(verbose_name='Cnpj ou Cpf do cliente', max_length=18, blank=True, null=True)
    ie_rg = models.CharField(verbose_name='Insc. estadual ou RG', max_length=20, blank=True, null=True)
    celular = models.CharField(verbose_name='Celular principal', max_length=13, blank=True, null=True)
    celular2 = models.CharField(verbose_name='Celular secundario', max_length=13, blank=True, null=True)
    telefone = models.CharField(verbose_name='Telefone residencial', max_length=13, blank=True, null=True)


class AddressUser(models.Model):
    user_detail = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    cep = models.CharField(verbose_name='CEP do cliente', max_length=200, blank=True, null=True)
    street = models.CharField(verbose_name='Rua do cliente', max_length=200, blank=True, null=True)
    number = models.CharField(verbose_name='Numero do cliente', max_length=200, blank=True, null=True)
    neighborhood = models.CharField(verbose_name='Bairro do cliente', max_length=200, blank=True, null=True)
    city = models.CharField(verbose_name='Cidade do cliente', max_length=200, blank=True, null=True)
    complement = models.CharField(verbose_name='Complemento', max_length=200, blank=True, null=True)
    description = models.CharField(verbose_name='Descrição do endereço', max_length=200, blank=True, null=True)
