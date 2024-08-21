from django.urls import path
from . import views
# Create your views here.



urlpatterns = [
    
    path('list_track/', views.list_track, name='list_track'),
    
    path('create_track/', views.create_track, name='create_track'),
    
    path('delete_track/<int:id>/', views.delete_track, name='delete_track'),
    
    path('update_track/<int:id>/', views.update_track, name='update_track'),
    
    path('track_detail/<int:id>/', views.track_detail, name='track_detail'),
]