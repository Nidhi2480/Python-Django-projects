from django.urls import path
from .import views


app_name='movieprofile'
urlpatterns=[
  
   
    path('view/', views.view_profile, name='view_profile'),
    path('edit/', views.edit_profile, name='edit_profile'),

]