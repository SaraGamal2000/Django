from django.urls import path
from . import views

urlpatterns = [
    
    path('infotrack', views.infotrack, name='infotrack'),
    
]