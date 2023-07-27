
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('notebook/',views.notebook,name='notebook'),
    path('add_notebook/',views.add_notebook,name='add_notebook'),
    path('share_notebook/',views.share_notebook,name='share_notebook'),
    path('sort/<str:sort>/',views.sort,name='sort'),
    path('notebook/bookmark/<slug:bookmark>/',views.bookmark,name='bookmark'),
    path('share/',views.share,name='share'),
    
    
    
]
