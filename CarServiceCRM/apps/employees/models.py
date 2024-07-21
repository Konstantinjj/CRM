from django.db import models

class Employee(models.Model):
    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    middle_name = models.CharField("Отчество", max_length=100, blank=True, null=True)
    salary = models.DecimalField("Зарплата", max_digits=10, decimal_places=2, default=0)
    paid_salary = models.DecimalField("Выплаченная зарплата", max_digits=10, decimal_places=2, default=0)
    bonuses = models.DecimalField("Бонусы", max_digits=10, decimal_places=2, default=0)

    @property
    def remaining_salary(self):
        return (self.salary or 0) + (self.bonuses or 0) - (self.paid_salary or 0)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name if self.middle_name else ''}"

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
