from django.shortcuts import render
from django.views.generic.list import ListView
from adm.models import Curso, Pagamento
from professores.models import Aula
from usuarios.models import Empresa
# Create your views here.
def index(request):
    context = {}
    return render(request, 'empresas/index.html', context)

class CursoListView(ListView):
    model = Curso
    context_object_name = 'curso_list'
    template_name = 'empresas/curso_list.html'
    def get_queryset(self):
        qs = Curso.objects.filter(alunos_do_curso__empresa_vinculada=self.request.user.empresa)
        return qs

class AulaListView(ListView):
    model = Aula
    context_object_name = 'aula_list'
    template_name = 'empresas/aula_list.html'
    def get_queryset(self):
        qs = Aula.objects.filter(curso__alunos_do_curso__empresa_vinculada=self.request.user.empresa)
        return qs

class PagamentoListView(ListView):
    model = Pagamento
    context_object_name = 'pagamento_list'
    template_name = 'empresas/pagamento_list.html'
    def get_queryset(self):
        qs = Pagamento.objects.filter(curso__alunos_do_curso__empresa_vinculada=self.request.user.empresa)
        return qs
