
from django.urls import path
from . import views
urlpatterns = [

   path('<slug>',views.notes,name='notes'),
   path('newnote/',views.new_note,name='new_note'),
   path('<slug:notebook>/content/<slug:note>',views.select_note,name='select_note'),
   path('content/',views.content,name='content'),
   path('tags/',views.tags,name='tags'),
   path('delete_tag/',views.delete_tag,name='delete_tag'),
   path('delete_file/',views.delete_file,name='delete_file'),
   path('bookmark/<slug:bookmark>/',views.notes_bookmark,name='notes_bookmark'),
   
   
   

    
    
]
