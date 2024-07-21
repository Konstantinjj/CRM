from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'salary', 'paid_salary', 'bonuses', 'remaining_salary')
    readonly_fields = ('remaining_salary',)

admin.site.register(Employee, EmployeeAdmin)
