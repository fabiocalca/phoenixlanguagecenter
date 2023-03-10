from django.shortcuts import render
from .forms import AulaCreateForm
from .models import Aula
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
import adm.models
from usuarios.models import Aluno
# Create your views here.
def index(request):
    alunos = adm.models.Curso.objects.filter(professor_do_curso=request.user.professor).values_list('alunos_do_curso').distinct().count()
    cursos = adm.models.Curso.objects.filter(professor_do_curso=request.user.professor).count()
    aulas = Aula.objects.filter(professor=request.user.professor).count()
    context = {'alunos': alunos,
    'cursos': cursos,
    'aulas': aulas}
    return render(request,'professores/index.html', context)

class AulaCreateView(CreateView):
    template_name = 'professores/create_aula.html'
    form_class = AulaCreateForm

    def get_form_kwargs(self):
        kwargs = super(AulaCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    def get_success_url(self):
        return reverse('aulas')

class AulaListView(ListView):
    model = Aula
    context_object_name = 'aula_list'
    def get_queryset(self):
        return super().get_queryset().filter(professor=self.request.user.professor)

class AulaUpdateView(UpdateView):
    model = Aula
    fields = ['titulo', 'curso', 'presente', 'data']
    success_url = "/professores/aulas"

class AulaDeleteView(DeleteView):
    model = Aula
    success_url = "/professores/aulas"
    template_name = "professores/aula_delete_confirm.html"

class AulaDetailView(DetailView):
    model = Aula
    def get_queryset(self):
        qs = super(AulaDetailView, self).get_queryset()
        return qs.filter(professor=self.request.user.professor)

class CursoListView(ListView):
    model = adm.models.Curso
    context_object_name = 'curso_list'
    template_name = 'professores/curso_list.html'
    def get_queryset(self):
        return super().get_queryset().filter(professor_do_curso=self.request.user.professor)
