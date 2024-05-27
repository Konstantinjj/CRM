from django.db import models

class SortGroup(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    sort_group = models.ForeignKey(SortGroup, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
