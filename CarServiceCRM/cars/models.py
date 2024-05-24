from django.db import models
from clients.models import Client


class Car(models.Model):
    gos_num = models.CharField(max_length=20)
    vin_number = models.CharField(max_length=17)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year_of_production = models.IntegerField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='cars')

    def __str__(self):
        return f"{self.brand} {self.model} ({self.gos_num})"
