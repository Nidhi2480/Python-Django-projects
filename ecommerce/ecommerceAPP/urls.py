from django.urls import path
from . import views
app_name='shop'
urlpatterns=[
    path('',views.allprod,name='allprod'),
    path('<slug:c_slug>/',views.allprod,name='allprodbycat'),
    path('<slug:c_slug>/<slug:product_slug>', views.proddetail, name='allproddetail')
]