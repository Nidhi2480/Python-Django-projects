from django.urls import path
from . import views
app_name='movie'
urlpatterns=[
 path('',views.AllMovie,name='allmovie'),
 path('login/',views.login,name='login'),
 path('logout/',views.logout,name='logout'),
 path('register/',views.register,name='register'),
 path('register/',views.register,name='register'),
 path('<slug:c_slug>/',views.AllMovie,name='allmovbycat'),
 path('<slug:c_slug>/<slug:product_slug>', views.proddetail, name='allproddetail'),
 
 

 ]