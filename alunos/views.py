from django.shortcuts import render
from adm.models import Pagamento, Curso 
from professores.models import Aula
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.

def index(request):
    context = {}
    return render(request, 'alunos/index.html', context)

class MeusPagamentosListView(ListView):
    model = Pagamento
    context_object_name = 'pagamento_list'
    template_name = 'alunos/pagamento_list.html'
    def get_queryset(self):
        return super().get_queryset().filter(curso__alunos_do_curso=self.request.user.aluno)

class AulaListView(ListView):
    model = Aula
    context_object_name = 'aula_list'
    template_name = 'alunos/aula_list.html'
    def get_queryset(self):
        return super().get_queryset().filter(curso__alunos_do_curso=self.request.user.aluno)

class AulaDetailView(DetailView):
    model = Aula
    template_name = 'alunos/aula_detail.html'
    def get_queryset(self):
        qs = super(AulaDetailView, self).get_queryset()
        return qs.filter(curso__alunos_do_curso=self.request.user.aluno)

class CursoListView(ListView):
    model = Curso
    context_object_name = 'curso_list'
    template_name = 'alunos/curso_list.html'
    def get_queryset(self):
        return super().get_queryset().filter(alunos_do_curso=self.request.user.aluno)
