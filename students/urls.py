from django.urls import path 
from . import views 

urlpatterns = [ 
path('list/',views.list_view, name='list'),
path('list1/',views.list_view1, name='list1'),
]
