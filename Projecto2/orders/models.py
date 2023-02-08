from django.db import models

# Create your models here.



class Order(models.Model):
    CHOICES = (
        ("Card", "Card"),
        ("Cash", "Cash"),

    )

    client = models.CharField(max_length=100)
    product =models.CharField(max_length=100)
    creation_time = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(choices=CHOICES, max_length=4)

    def __str__(self):
        return self.client
