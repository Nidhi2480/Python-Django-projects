from django.urls import path
from .import views


app_name='movieadd'
urlpatterns=[
   
   path('update/',views.update,name='update'),
   path('add/',views.add_movie,name='addmovie'),
   path('update/<int:id>/',views.update,name='update'),
   path('delete/<int:id>/',views.delete,name='delete'),
]