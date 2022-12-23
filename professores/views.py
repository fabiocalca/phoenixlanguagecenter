from django.shortcuts import render
from .forms import AulaCreateForm
from .models import Aula
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request,'professores/index.html', context={})

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

'''
def create_aula(request):
    professor = Professor.objects.filter(usuario_professor=request.user)
    cursos = Curso.objects.filter(professor_do_curso=professor)
    return render(request, 'professores/aulas.html', context={'professores':professor})
'''