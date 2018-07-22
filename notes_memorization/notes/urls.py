from django.urls import path, include
from django.conf.urls import url
from . import views

# app_name = 'notes'
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_note/$', views.add_note, name='addnote'),
]
