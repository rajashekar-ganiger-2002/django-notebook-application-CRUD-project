from django.contrib import admin
from .models import Task
# Register your models here.
@admin.register(Task)
class AdminTask(admin.ModelAdmin):
    list_display=['task_name','task_date','time_diff','user']
    
    