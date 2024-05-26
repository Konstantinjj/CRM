from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=100, verbose_name="Отчество")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.middle_name}'
