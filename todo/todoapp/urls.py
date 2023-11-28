from django.urls import path
from . import views 
urlpatterns=[
    path('',views.index,name='index'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('listview/',views.listview1.as_view(),name='listview'),
    path('submit/',views.submit,name='submit'),
    path('detailview/<int:pk>',views.detailview1.as_view(),name='detailview'),
    path('updateview/<int:pk>/',views.updateview1.as_view(),name='updateview'),
    path('deleteview/<int:pk>',views.deleteview1.as_view(),name='deleteview')
]