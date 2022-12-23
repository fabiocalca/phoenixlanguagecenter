from django.contrib import admin
from django.urls import path
from . import views
from usuarios.decorators import aluno_required
urlpatterns = [
    path('', views.index, name='alunos_index'),
    path('meus_pagamentos', views.MeusPagamentosListView.as_view(), name='meus_pagamentos'),
    path('minhas_aulas',aluno_required(views.AulaListView.as_view()), name='minhas_aulas'),
    path('meus_cursos', views.CursoListView.as_view(), name='meus_cursos')
]
