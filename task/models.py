from django.db import models
from emailverification.models import User
from django.db.models import Q
from datetime import datetime,timedelta
import time
import pytz
tz=pytz.timezone('Asia/Kolkata')
# Create your models here.
class Task(models.Model):
    task_name=models.CharField(max_length=20,blank=False)
    task_date=models.DateTimeField()
    time_diff=models.DurationField(blank=True,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    
    def return_task(email):
        return Task.objects.all().filter(user__email=email)
    
    
    def due_task(email):
        task=Task.objects.all().filter(user__email=email)
        for i in task:
            time_diff=i.task_date-datetime.now(tz)
            print(time_diff,i.task_date,datetime.now(tz))
          
            Task.objects.filter(Q(task_name=i.task_name) & Q(user__email=email)).update(time_diff=time_diff)
        zero_duration=timedelta(seconds=0)
        # 0H 0M 0S
        return Task.objects.all().filter(Q(user__email=email) & Q(time_diff__gte=zero_duration)).order_by('task_date')
    
    
    def overdue_task(email):
        zero_duration=timedelta(seconds=0)
        # 0H 0M 0S
        return Task.objects.all().filter(Q(user__email=email) & Q(time_diff__lt=zero_duration)).order_by('-task_date')
    
    
    def count_task(email):
        return Task.objects.all().filter(user__email=email).count()
    
    
    def delete_overdue(email):
        zero_duration=timedelta(seconds=0)
        Task.objects.all().filter(Q(user__email=email) & Q(time_diff__lt=zero_duration)).delete()
        
        
    def return_5_task(email):
        return Task.objects.all().filter(user__email=email)[:5]