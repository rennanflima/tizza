from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Pizzeria(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='pizzerias')
    address = models.CharField(max_length=512)
    phone = models.CharField(max_length=40)


class Pizza(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=240)
    thumbnail_url = models.URLField()
    approved = models.BooleanField(default=False)
    creator = models.ForeignKey('Pizzeria', on_delete=models.CASCADE, related_name='pizzas')


class Like(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='likes')
    pizza = models.ForeignKey('Pizza', on_delete=models.CASCADE, related_name='likes')
