from django.urls import path, include
from . import views

# app_name = 'notes'
urlpatterns = [
    path(r'', views.index),
    path(r'add_note/', views.add_note, name='addnote'),
]
