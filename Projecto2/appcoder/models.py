from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100)
    talle = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.BooleanField(default=True)
    image = models.ImageField(upload_to= "products", null=True)


    def __str__(self):
        return self.name

class ImageProducts(models.Model):
    imagen = models.ImageField(upload_to="products")
    producto = models.ForeignKey(Products, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=50, unique= True)


    def __str__(self):
        return self.name


