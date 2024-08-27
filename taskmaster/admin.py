from django.contrib import admin
from .models import Task


# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'due_date', 'completed')
    search_fields = ('title', 'description')
    list_filter = ('priority', 'completed')
