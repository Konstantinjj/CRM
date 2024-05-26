from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование позиции")
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")
    quantity = models.PositiveIntegerField(verbose_name="Количество", default=1)

    def __str__(self):
        return self.name