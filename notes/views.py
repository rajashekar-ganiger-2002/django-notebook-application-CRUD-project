from django.shortcuts import render,redirect
from .models import Notes
from notebook.models import Notebook
from django.utils.text import slugify
from attachments.models import Attachments
# Create your views here.

def notes(request,slug):
    if request.method=='GET':
        email=request.session.get('user')
        notes=Notes.notes_by_notebookslug(email,slug)
        request.session['notebook']=slug
        return render(request,'notes.html',{'notes':notes})
    else:
        search=request.POST.get('search')
        query=[]
        notebook=request.session.get('notebook')
        email=request.session.get('user')
        query=Notes.query(notebook,email,search)
        notes=Notes.notes_by_notebookslug(email,slug)
        return render(request,'notes.html',{'notes':notes,'query':query,'search':search})
        
    
    
def new_note(request):
    if request.method=='POST':
        email=request.session.get('user')
        note=request.POST.get('note')

        print(email)
        slug=request.session.get('notebook')
        print(slug)
        notebook=Notebook.return_first_user_notebook(email,slug)
        
        print()
        note=Notes(notes_name=note,notebook=notebook,notes_slug=slugify(note))
        note.save()
        return redirect(request.META['HTTP_REFERER'])
    
    
    

def select_note(request,notebook,note):
    if request.method=='GET':
        email=request.session.get('user')
        content=Notes.return_content(note,email)
        request.session['note']=note
        notes=Notes.notes_by_notebookslug(email,notebook)
        print(notes)
        object=Notes.return_note_obj(note,notebook,email)
        text=object.tags
        text=text.split()
        request.session['tags']=text
        attach=Attachments.return_files(email,note,notebook)
        return render(request,'notes.html',{'notes':notes,'content':content,'attach':attach})
        

        
        
def content(request):
    if request.method == "POST":
        mytextarea=request.POST.get('mytextarea')
        notebook=request.session.get('notebook')
        note=request.session.get('note')
        email=request.session.get('user')
        Notes.save_conetnt(notebook,note,email,mytextarea)
        redirect_to_note='/notes/'+notebook+'/content/'+note
        return redirect(redirect_to_note)
        
        
        
        
def tags(request):
    if request.method=="POST":
        tags=request.POST.get('tags')
        notebook=request.session.get('notebook')
        note=request.session.get('note')
        email=request.session.get('user')
        object=Notes.return_note_obj(note,notebook,email)
        text=object.tags
        object.tags=text+' '+tags+' '
        object.save()
        text=object.tags
        text=text.split()
        request.session['tags']=text
        redirect_to_note='/notes/'+notebook+'/content/'+note
        return redirect(redirect_to_note)
        
        
        
def delete_tag(request):
    if request.method=='GET':
        delete_tag=request.GET.get('delete_tag')
        notebook=request.session.get('notebook')
        note=request.session.get('note')
        email=request.session.get('user')
        object=Notes.return_note_obj(note,notebook,email)
        text=object.tags
        text=text.split()
        flag=False
        for word in text:
            if word==delete_tag:
                text.remove(word)
                flag=True
        if flag==True:
            request.session['tags']=text
            text=' '.join(text)
        object.tags=text
        object.save()
        redirect_to_note='/notes/'+notebook+'/content/'+note
        return redirect(redirect_to_note)
        
        
        

        
        
def delete_file(request):
    if request.method=='GET':
        delete_file=request.GET.get('delete_file')
        note=request.session.get('note')
        notebook=request.session.get('notebook')
        email=request.session.get('user')
        Attachments.delete_attach(email,note,delete_file)
        redirect_to_note='/notes/'+notebook+'/content/'+note
        return redirect(redirect_to_note)
        
        
        
def notes_bookmark(request,bookmark):
    if request.method=='GET':
        email=request.session.get('user')
        object=Notes.return_content(bookmark,email)
        print(object)
        print(bookmark)
        if object.bookmark_notes==True:
            object.bookmark_notes=False
        else:
            object.bookmark_notes=True
        object.save()
        return redirect(request.META['HTTP_REFERER'])