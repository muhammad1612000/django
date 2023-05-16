from django.urls import path 
from . import views 

urlpatterns = [ 
path('list/',views.list_view, name='list'),
path('list1/',views.list_view1, name='list1'),
path('home/',views.home_view,name='home'),
path('home2/',views.home_view2,name='home2'),
]
