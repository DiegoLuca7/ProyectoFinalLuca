from django.db import models

class Providers(models.Model):
    CONDITION_CHOICE = (
        ('monostributista', 'monotributista'),
        ('responsable inscripto', 'responsable inscripto'),
    )


    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    condition = models.CharField(max_length=50, choices = CONDITION_CHOICE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - {self.email}'

