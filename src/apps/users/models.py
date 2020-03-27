from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _

from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from apps.core.models import SuperClass
from apps.users.managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin, SuperClass):
    USER_TYPES = (
        ('P', 'Paciente'),
        ('M', 'Médico/Psicólogo'),
    )

    email = models.EmailField(_('Endereço de E-mail'), unique=True)
    name = models.CharField('Nome Completo', max_length=100)
    phone = models.CharField('Telefone', max_length=30, blank=True, null=True)
    type_user = models.CharField('Tipo de usuário', max_length=1, choices=USER_TYPES)
    state = models.CharField('Estado', max_length=100, blank=True, default="PI")
    city = models.CharField('Cidade', max_length=100, blank=True, default="Teresina")
    is_active = models.BooleanField('Está ativo?', blank=True, default=True)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=False)

    objects = CustomUserManager()

    slug = models.SlugField('Atalho')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'type_user']

    def __str__(self):
        return self.name

    def get_short_name(self):
        return self.name

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['name']


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
