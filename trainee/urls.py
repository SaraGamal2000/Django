from django.urls import path

from . import views

urlpatterns = [
    
    path('list_trainee/', views.list_trainee, name='list_trainee'),
    
    path('create_trainee/', views.create_trainee, name='create_trainee'),
    
    path('delete_trainee/<int:id>/', views.delete_trainee, name='delete_trainee'),
    
    path('update_trainee/<int:id>/', views.update_trainee, name='update_trainee'),
    
    path('trainee_detail/<int:id>/', views.trainee_detail, name='trainee_detail'),
]