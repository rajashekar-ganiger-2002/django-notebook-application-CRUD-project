from django.contrib import admin
from .models import Notebook
from .models import Share_notebook
# Register your models here.

@admin.register(Notebook)
class AdminNotebook(admin.ModelAdmin):
    list_display=['book_name','book_created_on','book_last_modified','notebook_slug','bookmark_notebook','user']
    
    
    
    
@admin.register(Share_notebook)
class AdminShare_notebook(admin.ModelAdmin):
    list_display=['email','shared_by','notebook']
    
    
    
    
    
    
