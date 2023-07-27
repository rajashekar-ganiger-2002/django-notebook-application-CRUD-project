from django.urls import path
from . import views
urlpatterns = [
    path('',views.task,name='task'),
    path('add_task/',views.add_task,name='add_task'),
    path('delete_task/',views.delete_overdue,name='delete_overdue')
    
    
]
