from django.contrib import admin
from . import models as shopping_models
# Register your models here.
admin.site.register(shopping_models.ShoppingCart)