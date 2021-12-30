from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


# Create your models here.
class CustomUser(AbstractUser):

    objects = CustomUserManager()

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
        self.username = self.username.lower()
        if self.email and CustomUser.objects.filter(email__iexact=self.email).exclude(username=self.username).exists():
            raise ValidationError({'email': 'Este e-mail já foi cadastrado.'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        if self.first_name:
            return f"{self.first_name} ({self.username})"
        return self.username
