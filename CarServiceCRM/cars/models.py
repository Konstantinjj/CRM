from django.db import models
from clients.models import Client

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    gos_num = models.CharField(max_length=10)
    vin_number = models.CharField(max_length=17)
    year_of_production = models.IntegerField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.brand} {self.model}'