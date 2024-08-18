    
from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    
    path('list_account/', views.list_account, name='list_account'),
    
    path('create_account/', views.create_account, name='create_account'),
    
    path('delete_account/<int:id>/', views.delete_account, name='delete_account'),
    
    path('update_account/<int:id>/', views.update_account, name='update_account'),
    
    path('account_detail/<int:id>/', views.account_detail, name='account_detail'),
]
