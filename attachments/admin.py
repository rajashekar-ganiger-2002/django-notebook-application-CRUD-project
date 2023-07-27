from django.contrib import admin
from .models import Attachments
# Register your models here.

@admin.register(Attachments)
class AdminAttachments(admin.ModelAdmin):
    list_display=['file','note']