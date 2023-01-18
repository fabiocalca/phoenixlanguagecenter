from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.admin.views.decorators import staff_member_required
urlpatterns = [
    path('', staff_member_required(views.index), name='adm_index'),
    path('presenca/', staff_member_required(views.AulaListView.as_view()), name='presenca'),
    path('<pk>/descricao_aula', staff_member_required(views.AulaDetailView.as_view()), name='adm_descricao_aula'),
    path('add_curso/', staff_member_required(views.CursoCreateView.as_view()), name='add_curso'),
    path('cursos/', staff_member_required(views.CursoListView.as_view()), name='cursos'),
    path('<pk>/update', staff_member_required(views.CursoUpdateView.as_view()), name='update'),
    path('<pk>/delete', staff_member_required(views.CursoDeleteView.as_view()), name='delete'),
    
    path('add_pagamento', staff_member_required(views.PagamentoCreateView.as_view()), name='add_pagamento'),
    path('pagamentos/', staff_member_required(views.PagamentoListView.as_view()), name='pagamentos'),
    path('<pk>/delete_pagamento', staff_member_required(views.PagamentoDeleteView.as_view()), name='delete_pagamento'),
    path('<pk>/update_pagamento', staff_member_required(views.PagamentoUpdateView.as_view()), name='update_pagamento'),
    
    path('add_idioma', staff_member_required(views.IdiomaCreateView.as_view()), name='add_idioma'),
    path('idiomas/', staff_member_required(views.IdiomaListView.as_view()), name='idiomas'),
    path('<pk>/delete_idioma', staff_member_required(views.IdiomaDeleteView.as_view()), name='delete_idioma'),
    path('<pk>/update_idioma', staff_member_required(views.IdiomaUpdateView.as_view()), name='update_idioma'),
    
    path('add_usuario', staff_member_required(views.UsuarioCreateView.as_view()), name='add_usuario'),
    path('usuarios/', staff_member_required(views.UsuarioListView.as_view()), name='usuarios'),
    path('<pk>/delete_usuario', staff_member_required(views.UsuarioDeleteView.as_view()), name='delete_usuario'),
    path('<pk>/update_usuario', staff_member_required(views.UsuarioUpdateView.as_view()), name='update_usuario'),

    path('add_empresa', staff_member_required(views.EmpresaCreateView.as_view()), name='add_empresa'),
    path('empresas/', staff_member_required(views.EmpresaListView.as_view()), name='empresas'),
    path('<pk>/delete_empresa', staff_member_required(views.EmpresaDeleteView.as_view()), name='delete_empresa'),
    path('<pk>/update_empresa', staff_member_required(views.EmpresaUpdateView.as_view()), name='update_empresa'),

    path('add_professor', staff_member_required(views.ProfessorCreateView.as_view()), name='add_professor'),
    path('professores/', staff_member_required(views.ProfessorListView.as_view()), name='professores'),
    path('<pk>/delete_professor', staff_member_required(views.ProfessorDeleteView.as_view()), name='delete_professor'),
    path('<pk>/update_professor', staff_member_required(views.ProfessorUpdateView.as_view()), name='update_professor'),
    
    path('add_aluno', staff_member_required(views.AlunoCreateView.as_view()), name='add_aluno'),
    path('alunos/', staff_member_required(views.AlunoListView.as_view()), name='alunos'),
    path('<pk>/delete_aluno', staff_member_required(views.AlunoDeleteView.as_view()), name='delete_aluno'),
    path('<pk>/update_aluno', staff_member_required(views.AlunoUpdateView.as_view()), name='update_aluno'),
]
