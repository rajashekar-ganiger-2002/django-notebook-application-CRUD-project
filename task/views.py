from django.shortcuts import render,redirect
from emailverification.models import User
from .models import Task
from datetime import datetime,timedelta
from pytz import timezone

# Create your views here.
def task(request):
    if request.method=='GET':
        email=request.session.get('user')
        task=Task.return_task(email)
        due_task=Task.due_task(email)
        overdue_task=Task.overdue_task(email)
        count=Task.count_task(email)


    return render(request,'task.html',{'task':task,'due_task':due_task,'overdue_task':overdue_task,'count':count})


def add_task(request):
    if request.method=='POST':
        task=request.POST.get('task')
        task_datetime=request.POST.get('datetime')
        task_datetime=datetime.strptime(task_datetime,"%Y-%m-%dT%H:%M")
        task_datetime=task_datetime.astimezone(timezone('Asia/Kolkata'))
        email=request.session.get('user')
        user=User.user_object(email)
        task_obj=Task(task_name=task,task_date=task_datetime,user=user)
        task_obj.save()
        return redirect('task')
    
    
    
    
def delete_overdue(request):
    if request.method=='GET':
        email=request.session.get('user')
        Task.delete_overdue(email)
        return redirect('task')