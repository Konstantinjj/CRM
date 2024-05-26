from django.contrib import admin
from .models import WorkType

@admin.register(WorkType)
class WorkTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost')
    search_fields = ('name',)
