from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponse
from .models import Notebook
from django.utils.text import slugify
from emailverification.models import User
from notes.models import Notes
from attachments.models import Attachments
from .models import Share_notebook 
from .models import Share_notebook
from datetime import datetime,timedelta
from task.models import Task
def signin_required(function):
    def inner(request,*args,**kwargs):
        email=request.session.get('user')
        now=datetime.now()
        now=now.replace(microsecond=0)
        
        if email==None:
            return redirect('signin')
        
        else:
            try:
                last=request.session.get('last_activity')
                last=datetime.strptime(last,"%Y-%m-%d %H:%M:%S")
                request.session['last_activity']=str(now)
                if (now-last)>timedelta(seconds=10):
                    request.session.pop('user',None)
                    return redirect('signin')
            except:
                request.session['last_activity']=str(now)
                
        return function(request,*args,**kwargs)
    return inner
        

# Create your views here.
@signin_required
def home(request):
    email=request.session.get('user')
    if request.method == 'GET':
        variable=Notes.return_all_notes(email)
        notes=Notes.return_all_user_notes(email)
        task=Task.return_5_task(email)
        return render(request,'mainblk.html',{'notes':notes,'task':task,'variable':variable})
    else:
        if request.POST.get('submit_btn')=='all_notes':
            variable=Notes.return_all_notes(email)
        else:
            variable=Notes.return_bookmark_notes(email)
        notes=Notes.return_all_user_notes(email)
        task=Task.return_5_task(email)
        return render(request,'mainblk.html',{'notes':notes,'task':task,'variable':variable})
  
        
    
@signin_required
def notebook(request):
    email=request.session.get('user')
    if request.method=='GET':
        count=Notebook.count_notebook(email)
        notebook=Notebook.return_user_notebook(email)
        return render(request,'notebook.html',{'notebook':notebook,'count':count})
    else:
        search=request.POST.get('search')
        query=[]
        query=Notebook.query(search,email)
        count=Notebook.count_notebook(email)
        notebook=Notebook.return_user_notebook(email)
        return render(request,'notebook.html',{'notebook':notebook,'count':count,'query':query,'search':search})
        

        
            
        


        

    


@signin_required
def add_notebook(request):
    email=request.session.get('user')
    if request.method=='GET':
        notebook=Notebook.return_user_notebook(email)
        return render(request,'notebook.html',{'notebook':notebook})
    if request.method=='POST':
        notebook=Notebook.return_user_notebook(email)
        count=Notebook.count_notebook(email)
        notebook_name=request.POST.get('notebook_name')
        check=Notebook.check_notebook(email,notebook_name)
        if check:
            error="book already exist"
            return render(request,'notebook.html',{'error':error,'notebook':notebook,'count':count})
        else:
            user=User.user_object(email)
            count=Notebook.count_notebook(email)
            slug=slugify(notebook_name)
            notebook=Notebook(book_name=notebook_name,notebook_slug=slug,bookmark_notebook=False,user=user)
            notebook.save()
            notebook=Notebook.return_user_notebook(email)
            sucess="notebook added sucessfully"
            return render(request,'notebook.html',{'sucess':sucess,'notebook':notebook,'count':count})
        
        
@signin_required
def share_notebook(request):
    if request.method=="POST":
        user_email=request.POST.get('email')
        user_notebook=request.POST.get('notebook')
        email=request.session.get('user')

        check=User.check_user_exist(user_email)
        check_notebook=Notebook.check_notebook(user_email,user_notebook)
        if check and not check_notebook:
            user_object=User.user_object(user_email)
            notebook=Notebook(book_name=user_notebook,notebook_slug=slugify(user_notebook),bookmark_notebook=False,user=user_object)
            notebook.save()
            note=Notes.notes_by_notebookslug(email,user_notebook)
            for i in note:
                note_obj=Notes(notes_name=i.notes_name,notes_text=i.notes_text,tags=i.tags,notebook=notebook,notes_slug=slugify(i.notes_name),bookmark_notes=False)
                note_obj.save()
                
                try:
                    attach=Attachments.return_files(email,i.notes_name,user_notebook)
                    
                    for j in attach:
                        attach_obj=Attachments.objects.create(note=note_obj)
                        print(attach_obj)
                        with j.file.open() as f:
                            attach_obj.file.save(j.file.name,f)
                        attach_obj.save()
                        
                except:
                    pass
                
            share_object=Share_notebook(email=user_email,shared_by=email,notebook=user_notebook)
            share_object.save()
            count=Notebook.count_notebook(email)
            notebook=Notebook.return_user_notebook(email)
            return render(request,'notebook.html',{'notebook':notebook,'count':count})
        else:
            share_error="user does not exist or user already has notebook"
            count=Notebook.count_notebook(email)
            notebook=Notebook.return_user_notebook(email)
            return render(request,'notebook.html',{'notebook':notebook,'count':count,'share_error':share_error})
        
            
        
            

@signin_required                
def sort(request,sort):
    if request.method=='GET':
        email=request.session.get('user')
        notebook=Notebook.sort_notebook(sort,email)
        count=Notebook.count_notebook(email)
        return render(request,'notebook.html',{'notebook':notebook,'count':count})
        
@signin_required        
def bookmark(request,bookmark):
    if request.method=='GET':
        email=request.session.get('user')
        notebook=Notebook.return_first_user_notebook(email,bookmark)
        if notebook.bookmark_notebook==True:
            notebook.bookmark_notebook=False
        else:
            notebook.bookmark_notebook=True
        notebook.save()
        count=Notebook.count_notebook(email)
        notebook=Notebook.return_user_notebook(email)
        return render(request,'notebook.html',{'notebook':notebook,'count':count})
        
        

@signin_required           
def share(request):
    if request.method=='GET':
        email=request.session.get('user')
        share=Share_notebook.shared_notebook(email)
        return render(request,'shared_notebook.html',{'share':share})
        
                
            
            
            
            
        
        
        