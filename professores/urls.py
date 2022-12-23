from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='professor_index'),
    path('create_aula', views.AulaCreateView.as_view(), name='create_aula'),
    path('aulas',views.AulaListView.as_view(), name='aulas'),
]