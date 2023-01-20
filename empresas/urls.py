from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='empresas_index'),
    path('cursos', views.CursoListView.as_view(), name='empresas_cursos'),
    path('aulas', views.AulaListView.as_view(), name='empresas_aulas'),
    path('pagamentos', views.PagamentoListView.as_view(), name='empresas_pagamentos'),
]