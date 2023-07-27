from django.db import models
from notebook.models import Notebook
from autoslug import AutoSlugField
from django.db.models import Q
# Create your models here.
class Notes(models.Model):
    notes_name=models.CharField(max_length=20,blank=False)
    notes_text=models.TextField(default="text here...")
    notes_created_on=models.DateTimeField(auto_now_add=True)
    notes_last_modified=models.DateTimeField(auto_now=True)
    tags=models.TextField(max_length=50,blank=True,default="None")
    notebook=models.ForeignKey(Notebook,on_delete=models.CASCADE,related_name='notes')
    notes_slug=AutoSlugField(populate_from='notes_anme',default=None)
    bookmark_notes=models.BooleanField(default=False)


    
    
    
    def notes_by_notebookslug(email,slug):
        return Notes.objects.all().filter(Q(notebook__notebook_slug=slug) & Q(notebook__user__email=email))

    def return_content(slug,email):
        return Notes.objects.filter(Q(notes_slug=slug) & Q(notebook__user__email=email)).first()

    def save_conetnt(notebook,note,email,content):
        return Notes.objects.filter(Q(notebook__user__email=email) & Q(notebook__notebook_slug=notebook) & Q(notes_slug=note)).update(notes_text=content)
    
    def query(notebook,email,search):
        return Notes.objects.all().filter(Q(notebook__user__email=email) & Q(notebook__book_name=notebook) & Q(notes_name__icontains=search))
    
    def return_note_obj(note,notebook,email):
        return Notes.objects.filter(Q(notebook__user__email=email) & Q(notebook__book_name=notebook) & Q(notes_name=note)).first()
    
    def return_count_by_name(email,slug):
        return Notes.objects.filter(Q(notebook__notebook_slug=slug) & Q(notebook__user__email=email)).count()
    
    def return_tags(email,note):
        return Notes.objects.filter(Q(notebook__user__email=email) & Q(notes_name=note)).first()
    
    def return_all_user_notes(email):
        return Notes.objects.all().filter(Q(notebook__user__email=email)).order_by('-notes_last_modified')
    
    def return_all_notes(email):
        return Notes.objects.all().filter(Q(notebook__user__email=email))
    
    def return_bookmark_notes(email):
        return Notes.objects.all().filter(Q(notebook__user__email=email) & Q(bookmark_notes=True))