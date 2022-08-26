from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=16, blank=True, null=True, verbose_name='Телефон')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        default_related_name = 'users'
