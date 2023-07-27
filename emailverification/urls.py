
from django.urls import path
from . import views
urlpatterns = [
    path('',views.verification,name='verification'),
    path('otp_verify/',views.otp_verification,name='otp_verification'),
    
]
