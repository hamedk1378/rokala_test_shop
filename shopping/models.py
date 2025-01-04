from django.db import models
from django.contrib.auth import get_user_model

from product_management.models import Products

# Create your models here.

class ShoppingCart(models.Model):
    products= models.ManyToManyField(Products)
    user= models.OneToOneField(get_user_model(), on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s cart"
