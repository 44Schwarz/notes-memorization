from django.urls import path
from . import views

app_name = 'notes'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_note/', views.add_note),
    path('<int:note_id>/', views.detail, name='detail'),
]
