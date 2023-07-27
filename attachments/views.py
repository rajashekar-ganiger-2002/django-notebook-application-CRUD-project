from django.shortcuts import render,redirect
from .models import Attachments
from notes.models import Notes
# Create your views here.
def attachments(request):
    if request.method=='POST':
        attach=request.FILES.getlist('attach')
        notebook=request.session.get('notebook')
        note=request.session.get('note')
        email=request.session.get('user')
        
        note_obj=Notes.return_note_obj(note,notebook,email)
        for i in attach:
            object=Attachments(file=i,note=note_obj)
            object.save()
        redirect_to_note='/notes/'+notebook+'/content/'+note
        return redirect(redirect_to_note)
        
