from django.db import models

# Create your models here.


class User(models.Model):
    email=models.EmailField(unique=True,max_length=20,blank=False)
    password=models.TextField(max_length=30,blank=False)
    
    
    def check_user_exist(email):
        try:
            if User.objects.all().filter(email=email):
                return True
        except:
            return False
    
    def user_object(email):
        try:
            return User.objects.filter(email=email).first()
        except:
            pass
    

