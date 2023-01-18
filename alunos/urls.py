from django.contrib import admin
from django.urls import path
from . import views
from usuarios.decorators import aluno_required
urlpatterns = [
    path('', aluno_required(views.index), name='alunos_index'),
    path('meus_pagamentos', aluno_required(views.MeusPagamentosListView.as_view()), name='meus_pagamentos'),
    path('minhas_aulas',aluno_required(views.AulaListView.as_view()), name='minhas_aulas'),
    path('meus_cursos', aluno_required(views.CursoListView.as_view()), name='meus_cursos'),
    path('<pk>/descricao_aula', aluno_required(views.AulaDetailView.as_view()), name='aluno_descricao_aula'),
]
