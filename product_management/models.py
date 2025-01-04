from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Products(models.Model):
    name= models.CharField(max_length=256)
    is_tech= models.BooleanField(default=False)
    count= models.IntegerField()
    color= models.CharField(max_length=128)
    categories= models.ManyToManyField("Categories")

    def __str__(self):
        return self.name
    
    def is_available(self) -> bool:
        return self.count > 0
    
    def clean(self):
        if self.count < 0:
            raise ValidationError("Products count should not be negative")


class Price(models.Model):
    amount= models.DecimalField(max_digits=5, decimal_places=2)
    region= models.CharField(max_length=64)
    product= models.ForeignKey(Products, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.product.name}: {self.amount}{self.region}"
    
    def clean(self):
        if self.amount < 0:
            raise ValidationError("Price\'s amount should not be negative")
    

class Categories(models.Model):
    name= models.CharField(max_length=256)

    def __str__(self):
        return self.name