from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='login'),
path('retrive',views.retrive,name='retrive'),
path('generate',views.GenerateProcess,name='generate'),
path('create',views.create,name='create'),
path('store',views.store,name='store'),
path('delete',views.delete,name='delete'),
]
