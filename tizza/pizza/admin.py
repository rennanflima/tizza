from django.contrib import admin

from tizza.pizza.models import Like, Pizza, Pizzeria

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Pizzeria)
admin.site.register(Like)
