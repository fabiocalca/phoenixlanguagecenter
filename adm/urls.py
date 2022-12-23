from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='adm_index'),
    path('presenca/', views.AulaListView.as_view(), name='presenca'),
    path('add_curso/', views.CursoCreateView.as_view(), name='add_curso'),
    path('cursos/', views.CursoListView.as_view(), name='cursos'),
    path('<pk>/update', views.CursoUpdateView.as_view(), name='update'),
    path('<pk>/delete', views.CursoDeleteView.as_view(), name='delete'),
    
    path('add_pagamento', views.PagamentoCreateView.as_view(), name='add_pagamento'),
    path('pagamentos/', views.PagamentoListView.as_view(), name='pagamentos'),
    path('<pk>/delete_pagamento', views.PagamentoDeleteView.as_view(), name='delete_pagamento'),
    path('<pk>/update_pagamento', views.PagamentoUpdateView.as_view(), name='update_pagamento'),
    
    path('add_idioma', views.IdiomaCreateView.as_view(), name='add_idioma'),
    path('idiomas/', views.IdiomaListView.as_view(), name='idiomas'),
    path('<pk>/delete_idioma', views.IdiomaDeleteView.as_view(), name='delete_idioma'),
    path('<pk>/update_idioma', views.IdiomaUpdateView.as_view(), name='update_idioma'),
    
    path('add_usuario',views.UsuarioCreateView.as_view(), name='add_usuario'),
    path('usuarios/', views.UsuarioListView.as_view(), name='usuarios'),
    path('<pk>/delete_usuario', views.UsuarioDeleteView.as_view(), name='delete_usuario'),
    path('<pk>/update_usuario', views.UsuarioUpdateView.as_view(), name='update_usuario'),

    path('add_empresa', views.EmpresaCreateView.as_view(), name='add_empresa'),
    path('empresas/', views.EmpresaListView.as_view(), name='empresas'),
    path('<pk>/delete_empresa', views.EmpresaDeleteView.as_view(), name='delete_empresa'),
    path('<pk>/update_empresa', views.EmpresaUpdateView.as_view(), name='update_empresa'),

    path('add_professor', views.ProfessorCreateView.as_view(), name='add_professor'),
    path('professores/', views.ProfessorListView.as_view(), name='professores'),
    path('<pk>/delete_professor', views.ProfessorDeleteView.as_view(), name='delete_professor'),
    path('<pk>/update_professor', views.ProfessorUpdateView.as_view(), name='update_professor'),
    
    path('add_aluno', views.AlunoCreateView.as_view(), name='add_aluno'),
    path('alunos/', views.AlunoListView.as_view(), name='alunos'),
    path('<pk>/delete_aluno', views.AlunoDeleteView.as_view(), name='delete_aluno'),
    path('<pk>/update_aluno', views.AlunoUpdateView.as_view(), name='update_aluno'),
]
