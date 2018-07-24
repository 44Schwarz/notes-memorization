from django.urls import path
from . import views

# app_name = 'notes'
urlpatterns = [
    path(r'', views.index),
    path(r'add_note/', views.add_note),
]
