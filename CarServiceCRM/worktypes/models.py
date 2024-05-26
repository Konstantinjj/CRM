from django.db import models

class WorkType(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование работы")
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")

    def __str__(self):
        return self.name
