from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name or ''}".strip()