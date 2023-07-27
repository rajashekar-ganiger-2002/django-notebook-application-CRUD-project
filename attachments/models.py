from django.db import models
from notes.models import Notes
from django.db.models import Q
# Create your models here.

class Attachments(models.Model):
    file=models.FileField(blank='True',upload_to='attachments/uploads')
    note=models.ForeignKey(Notes,on_delete=models.CASCADE)
    
    
    
    
    def return_files(email,note,notebook):
        return Attachments.objects.all().filter(Q(note__notebook__user__email=email) & Q(note__notes_name=note) & Q(note__notebook__book_name=notebook))
    
    
    
    def delete_attach(email,note,delete_file):
        Attachments.objects.filter(Q(note__notebook__user__email=email) & Q(note__notes_name=note) & Q(file=delete_file)).first().delete()
        return