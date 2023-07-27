from django.db import models
from autoslug import  AutoSlugField
from emailverification.models import User
from django.db.models import Q
# Create your models here.
class Notebook(models.Model):
    book_name = models.CharField(max_length=25,null=False)
    book_created_on=models.DateTimeField(auto_now_add=True)
    book_last_modified=models.DateTimeField(auto_now=True)
    notebook_slug=AutoSlugField(populate_from='book_name')
    bookmark_notebook=models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        unique_together=[['book_name','user']]
        
        
    
    

    def return_user_notebook(email):
        return Notebook.objects.all().filter(user__email=email)
    
    def return_first_user_notebook(email,slug):
        return Notebook.objects.filter(Q(notebook_slug=slug) & Q(user__email=email)).first()
    
    def check_notebook(email,notebook_name):
        check=Notebook.objects.all().filter(Q(user__email=email) & Q(book_name=notebook_name))
        if check:
            return True
        return False
    
    def count_notebook(email):
        return Notebook.objects.all().filter(user__email=email).count()
    


    def query(search,email):
        return Notebook.objects.all().filter(Q(user__email=email) & Q(book_name__icontains=search))
    
    
    def sort_notebook(sort,email):
        if sort=='A-Z':
            return Notebook.objects.all().filter(user__email=email).order_by('book_name')
        if sort=='Z-A':
            return Notebook.objects.all().filter(user__email=email).order_by('-book_name')
        if sort=='recentused':
            return Notebook.objects.all().filter(user__email=email).order_by('-book_last_modified')
        if sort=='createdon':
            return Notebook.objects.all().filter(user__email=email).order_by('book_created_on')
    
    



class Share_notebook(models.Model):
    email=models.EmailField(max_length=20,blank=False)
    shared_by=models.EmailField(max_length=20,blank=False)
    notebook=models.CharField(max_length=20,blank=False)
    
    
    
    def shared_notebook(email):
        return Share_notebook.objects.all().filter(email=email)