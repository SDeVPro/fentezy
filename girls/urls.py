from django.urls import path,include
from girls import views 
urlpatterns = [
  
    path('',views.index,name='index'),
]
